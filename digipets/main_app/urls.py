from django.urls import path, include
from . import views

urlpatterns = [
	path('', views.home, name='home'),
	path('landing/', views.landing, name='landing'),
  path('accounts/', include('django.contrib.auth.urls')),
  path('accounts/signup/', views.signup, name='signup'),
  path('digipets/create/', views.DigipetCreate.as_view(), name='digipets_create'),
]