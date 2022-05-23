from django.urls import path, include
from . import views

urlpatterns = [
	path('', views.home, name='home'),
	path('digipets/', views.digipets_index, name='index'),
	path('landing/', views.landing, name='landing'),
	path('digipets/<int:digipet_id>/', views.digipets_detail, name='detail'),
  path('accounts/', include('django.contrib.auth.urls')),
  path('accounts/signup/', views.signup, name='signup'),
]