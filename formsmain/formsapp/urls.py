from django.urls import path
from .views import submit_form

urlpatterns = [
    path('api/submit-form/', submit_form, name='submit-form'),

]
