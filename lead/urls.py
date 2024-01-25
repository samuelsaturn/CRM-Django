from django.urls import path
from . import views
urlpatterns = [
    path('add_lead/', views.add_lead, name='add_lead')
]
