from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin


class TimelineView(View,LoginRequiredMixin):
    def get(self, request):
        greeting = {}
        greeting['title'] = "Timeline"
        greeting['heading'] = "Veltrix"
        greeting['subheading'] = "Extra Pages"
        return render (request,'extra_pages/extra_pages-timeline.html',greeting)    

class InvoiceView(View,LoginRequiredMixin):
    def get(self, request):
        greeting = {}
        greeting['title'] = "Invoice"
        greeting['heading'] = "Veltrix"
        greeting['subheading'] = "Extra Pages"
        return render (request,'extra_pages/extra_pages-invoice.html',greeting)     

class DirectoryView(View,LoginRequiredMixin):
    def get(self, request):
        greeting = {}
        greeting['title'] = "Directory"
        greeting['heading'] = "Veltrix"
        greeting['subheading'] = "Extra Pages"
        return render (request,'extra_pages/extra_pages-directory.html',greeting)   

class StarterPageView(View,LoginRequiredMixin):
    def get(self, request):
        greeting = {}
        greeting['title'] = "Starter Page"
        greeting['heading'] = "Veltrix"
        greeting['subheading'] = "Extra Pages"
        return render (request,'extra_pages/extra_pages-starterpage.html',greeting)  

class ErrorView(View,LoginRequiredMixin):
    def get(self, request):
        return render (request,'extra_pages/extra_pages-404error.html')  

class ErrorsView(View,LoginRequiredMixin):
    def get(self, request):
        return render (request,'extra_pages/extra_pages-500error.html')                                      

class PricingView(View,LoginRequiredMixin):
    def get(self, request):
        greeting = {}
        greeting['title'] = "Pricing"
        greeting['heading'] = "Veltrix"
        greeting['subheading'] = "Extra Pages"
        return render (request,'extra_pages/extra_pages-pricing.html',greeting)  

class GalleryView(View,LoginRequiredMixin):
    def get(self, request):
        greeting = {}
        greeting['title'] = "Gallery"
        greeting['heading'] = "Veltrix"
        greeting['subheading'] = "Extra Pages"
        return render (request,'extra_pages/extra_pages-gallery.html',greeting) 

class MaintenanceView(View,LoginRequiredMixin):
    def get(self, request):
        greeting = {}
        greeting['title'] = "Maintenance"
        greeting['heading'] = "Veltrix"
        greeting['subheading'] = "Extra Pages"
        return render (request,'extra_pages/extra_pages-maintenance.html',greeting)   

class ComingSoonView(View,LoginRequiredMixin):
    def get(self, request):
        greeting = {}
        greeting['title'] = "Coming Soon"
        greeting['heading'] = "Veltrix"
        greeting['subheading'] = "Extra Pages"
        return render (request,'extra_pages/extra_pages-comingsoon.html',greeting)                  


class FaqsView(View,LoginRequiredMixin):
    def get(self, request):
        greeting = {}
        greeting['title'] = "FAQs"
        greeting['heading'] = "Veltrix"
        greeting['subheading'] = "Extra Pages"
        return render (request,'extra_pages/extra_pages-faqs.html',greeting)    
    


class ProfileView(View,LoginRequiredMixin):
    def get(self, request):
        greeting = {}
        greeting['title'] = "Profile"
        greeting['heading'] = "Veltrix"
        greeting['subheading'] = "Extra Pages"
        return render (request,'extra_pages/extra_pages-profile.html',greeting)           