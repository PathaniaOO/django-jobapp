from django.urls import path
#from app.views import hello_world
#from app.views import details
from app import views

urlpatterns = [
    path('', views.job_list,name='job_list'),
    path('',views.hello, name='home'),
    #path('job/1',views.details),
    path('job/<int:id>',views.details,name='job_details'),
    #path('job/<str:id>',views.details),
]
