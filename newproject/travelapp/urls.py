from . import views
from django.urls import path

urlpatterns = [

    path('',views.demo,name='demo'),
    # path('demo1/',views.demo1,name='demo1'),
    #path('add/',views.addition,name='addition')
    #path('add/',views.addition,name='addition')
    #path('contact/',views.contact,name='contact')
]