from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin

class BasicActionEmailView(View,LoginRequiredMixin):
    def get(self , request):
        greeting = {}
        greeting['title'] = "Basic Action Email"
        greeting['heading'] = "Veltrix"
        greeting['subheading'] = "Email  s"
        return render (request,'email_ s/email_ s-basicactionemail.html',greeting)

class AlertEmailView(View,LoginRequiredMixin):
    def get(self , request):
        greeting = {}
        greeting['title'] = "Alert Email"
        greeting['heading'] = "Veltrix"
        greeting['subheading'] = "Email  s"
        return render (request,'email_ s/email_ s-alert_email.html',greeting)        

class BillingEmailView(View,LoginRequiredMixin):
    def get(self , request):
        greeting = {}
        greeting['title'] = "Billing Email"
        greeting['heading'] = "Veltrix"
        greeting['subheading'] = "Email  s"
        return render (request,'email_ s/email_ s-billing_email.html',greeting)         