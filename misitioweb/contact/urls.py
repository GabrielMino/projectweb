from contact import views as contact_view 
from django.urls import path

urlpatterns = [
    path('contact/', contact_view.contact, name="contact")
]