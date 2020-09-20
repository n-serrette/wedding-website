from django.urls import path

from . import views

urlpatterns = [
    path('', views.InvitationResponse.as_view(), name='index'),
    path('gate/', views.GateView.as_view(), name='gate'),
    path('dashboard/', views.DashboardView.as_view(), name='dashboard'),
]
