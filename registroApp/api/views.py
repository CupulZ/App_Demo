from django.shortcuts import render
from rest_framework import generics
from .models import Persona
from .serializers import PersonaSerializer

from django.urls import reverse_lazy
from  django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.generic.edit import FormView
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated

#----------------- NUEVAS IMPORTACIONES
from api import config
from django.views.generic.base import View
from api.forms import RegistrationForm
from django.urls import reverse
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
#----------------

class PersonaList(generics.ListCreateAPIView):
    queryset= Persona.objects.all()
    serializer_class= PersonaSerializer
    permission_classes= (IsAuthenticated,)

class Login(FormView):
    template_name= "login.html"
    form_class = AuthenticationForm
    success_url = reverse_lazy('api:persona_list')

    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    def dispatch(self,request,*args,**kwargs):

        if request.user.is_authenticated:
            return HttpResponseRedirect(self.get_success_url())
        else:
            return super(Login, self).dispatch(request,*args,*kwargs)

    def form_valid(self, form):
        user= authenticate(username= form.cleaned_data['username'],password= form.cleaned_data['password'])
        token,_ = Token.objects.get_or_create(user= user)
        if token:
            login(self.request, form.get_user())
            return super(Login,self).form_valid(form)

#------------------------------------- NUEVO
class LogoutView(View):

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(LogoutView, self).dispatch(*args, **kwargs)

    def get(self, request):
        logout(request)
        return HttpResponseRedirect(config.LOGOUT_REDIRECT_URL)

class RegisterView(FormView):
    template_name = 'register.html'
    form_class = RegistrationForm

    @method_decorator(csrf_protect)
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(config.INDEX_REDIRECT_URL)
        else:
            return super(RegisterView, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):

        user = User.objects.create_user(
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password1'],
            email=form.cleaned_data['email']
        )

        return super(RegisterView, self).form_valid(form)

    def get_success_url(self):
        return reverse('register-success')


class RegisterSuccessView(TemplateView):
    template_name = 'success.html'