from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin

#########Vertical View#################
class LightSidebarView(View,LoginRequiredMixin):
    def get(self , request):
        greeting = {}
        greeting['title'] = "Light Sidebar"
        greeting['heading'] = "Veltrix"
        greeting['subheading'] = "Vertical"
        return render (request,'layouts/vertical/layouts-light_sidebar.html',greeting)

class CompactSidebarView(View,LoginRequiredMixin):
    def get(self , request):
        greeting = {}
        greeting['title'] = "Compact Sidebar"
        greeting['heading'] = "Veltrix"
        greeting['subheading'] = "Vertical"
        return render (request,'layouts/vertical/layouts-compact_sidebar.html',greeting) 

class IconSidebarView(View,LoginRequiredMixin):
    def get(self , request):
        greeting = {}
        greeting['title'] = "Icon Sidebar"
        greeting['heading'] = "Veltrix"
        greeting['subheading'] = "Vertical"
        return render (request,'layouts/vertical/layouts-icon_sidebar.html',greeting)        

class BoxLayoutView(View,LoginRequiredMixin):
    def get(self , request):
        greeting = {}
        greeting['title'] = "Boxed Layout"
        greeting['heading'] = "Veltrix"
        greeting['subheading'] = "Vertical"
        return render (request,'layouts/vertical/layouts-boxlayout.html',greeting)  

class ColoredSidebarView(View,LoginRequiredMixin):
    def get(self , request):
        greeting = {}
        greeting['title'] = "Colored Sidebar"
        greeting['heading'] = "Veltrix"
        greeting['subheading'] = "Vertical"
        return render (request,'layouts/vertical/layouts-coloredsidebar.html',greeting)  

####Horizontal View#########
class HorizontalView(View,LoginRequiredMixin):
    def get(self , request):
        greeting = {}
        greeting['title'] = "Horizontal"
        greeting['heading'] = "Veltrix"
        greeting['subheading'] = "Horizontal"
        return render (request,'layouts/horizontal/layouts-horizontal.html',greeting)  

class TopbarLightHoriView(View,LoginRequiredMixin):
    def get(self , request):
        greeting = {}
        greeting['title'] = "Light Topbar"
        greeting['heading'] = "Veltrix"
        greeting['subheading'] = "Horizontal"
        return render (request,'layouts/horizontal/layouts-topbarlighthori.html',greeting)    

class BoxedWidthHoriView(View,LoginRequiredMixin):
    def get(self , request):
        greeting = {}
        greeting['title'] = "Boxed Layout"
        greeting['heading'] = "Veltrix"
        greeting['subheading'] = "Horizontal"
        return render (request,'layouts/horizontal/layouts-boxwidthhori.html',greeting)                                          