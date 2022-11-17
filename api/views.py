from django.shortcuts import render

from api.models import User,Saloon,Service,Booking

# Create your views here.
from rest_framework.decorators import action,api_view
from rest_framework.response import Response
from datetime import datetime, timedelta,date,time
from pytz import timezone

def get_daily_slots(start, end, slot,chairs,booking):
    date = datetime.now().date()
    dt = datetime.combine(date, start)
    slots = []
    #dt_in = '{}:{}'.format(dt.hour,dt.minute)
    booking_count = booking.filter(time__lte = dt,endtime__gt = dt)      
    if booking_count.count() < chairs:
        slots.append('{}:{}'.format(dt.hour,dt.minute))
    else:
        pass
    
    while (dt.time() < end):
        dt = dt + timedelta(minutes=slot)
        booking_count = booking.filter(time__lte = dt,endtime__gt = dt)      
        if booking_count.count() < chairs:
            if end > dt.time():
                slots.append('{}:{}'.format(dt.hour,dt.minute))
        else:
            pass
    return slots


# Create your models here.
@api_view(['post'])
def get_slot(request, *args, **kwargs):
    """
    API To Get slt
    """
    
    service_id = request.data.get('service_id',None)
    saloon_id = request.data.get('saloon_id',None)
    if service_id and saloon_id:
        #print('Yup')
        service = Service.objects.get(id =service_id )
        saloon = Saloon.objects.get(id = saloon_id)
        start_time = saloon.working_starttime
        end_time = saloon.working_endtime
        slot_time = 30
        chairs = saloon.no_of_chairs
        #for i in range(days):
        booking = Booking.objects.filter(saloon = saloon,time__date = datetime.now())
        #print(booking)
            
        data = get_daily_slots(start=start_time, end=end_time, slot=slot_time,chairs = chairs,booking = booking)

    return Response({"message": "Available slots.","status": 1,"data":data}, status=200)