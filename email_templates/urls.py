from django.urls import path
from email_ s import views

urlpatterns = [
   
    path('basic_action_email',views.BasicActionEmailView.as_view(),name='email_ s-basic_action_email'),
    path('alert_email',views.AlertEmailView.as_view(),name='email_ s-alert_email'),
    path('billing_email',views.BillingEmailView.as_view(),name='email_ s-billing_email'),


]