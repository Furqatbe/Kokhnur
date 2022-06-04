from msilib.schema import AdminExecuteSequence
from django.urls import path 
from .views import Index, AddContact
urlpatterns = [
    path('', Index, name='index'),
    path('add-contact/', AddContact, name="add-contact"),
    ]