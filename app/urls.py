from django.urls import path
from app import views

app_name="app"

urlpatterns=[
path('',views.index,name='home'),
path('internals/',views.internals,name='internals'),
path('iamarks/<slug:topic_id>',views.iamarks,name='iamarks'),
# path('chooseSem/',views.chooseSem,name='choosesem'),
path('newEntry/', views.newEntry, name='newentry'),
path('subjects/', views.subjects, name='subjects'),


    path('newEntry1/<slug:topic_id>', views.newEntry1, name='newentry1'),

]
