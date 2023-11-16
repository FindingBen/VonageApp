# myapp/views.py
from django.shortcuts import get_object_or_404, render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from .models import Sms
from rest_framework.decorators import api_view
from .serializers import SmsSerializer
import vonage
import uuid

def get_sms_list(request):
    sms_objects = Sms.objects.all()
    serializer = SmsSerializer(sms_objects, many=True)
    return render(request, 'smsList.html', {'sms_list': serializer.data})

def get_sms_detail(request, id):
    sms_object = get_object_or_404(Sms, id=id)
    serializer = SmsSerializer(sms_object)
    return render(request, 'sms.html', {'sms_object': serializer.data})


def send_sms(request):
    #Rest of the code here..
    return render(request, 'index.html', {})