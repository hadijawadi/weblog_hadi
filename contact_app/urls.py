from django.urls import path
from .views import contact_view

app_name ='contact_app'

urlpatterns  = [
    path('',contact_view,name ='contact')
]