from django.urls import path, include
from . import views

urlpatterns = [
	path('', views.home, name='home'),
	path('digipets/', views.digipets_index, name='index'),
	path('landing/', views.landing, name='landing'),
	path('digipets/<int:digipet_id>/', views.digipets_detail, name='detail'),
	path('digipets/<int:pk>/update/', views.DigipetUpdate.as_view(), name='digipets_update'),
	path('digipets/<int:pk>/feed/', views.digipets_feed, name='digipets_feed'),
  path('accounts/', include('django.contrib.auth.urls')),
  path('accounts/signup/', views.signup, name='signup'),
  path('digipets/create/', views.DigipetCreate.as_view(), name='digipets_create'),
]