from django.urls import path
from . import views

urlpatterns = [
    path('persona/', views.PersonaList.as_view(), name= 'persona_list'),
]