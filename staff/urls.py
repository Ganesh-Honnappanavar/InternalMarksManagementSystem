from django.urls import path
from staff import views

app_name="staff"

urlpatterns=[
path('',views.staff,name='staffHome'),
]
