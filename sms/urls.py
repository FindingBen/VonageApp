# myapp/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('sms/', views.get_sms_list, name='sms-list'),
    path('sms/<int:id>/', views.get_sms_detail, name='sms-detail'),
    path('send-sms/', views.send_sms, name='send-sms'),
]
