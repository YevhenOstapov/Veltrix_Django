from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin

############UI-ELEMENTS####################
class AlertsView(View,LoginRequiredMixin):
    def get(self , request):
        greeting = {}       
        greeting['title'] = "Alerts"
        greeting['heading'] = "Veltrix"
        greeting['subheading'] = "UI Elements"
        return render (request,'components/ui-elements/ui_elements-alerts.html',greeting)

class ButtonsView(View,LoginRequiredMixin):
    def get(self , request):
        greeting = {}
        greeting['title'] = "Buttons"
        greeting['heading'] = "Veltrix"
        greeting['subheading'] = "UI Elements"
        return render (request,'components/ui-elements/ui_elements-buttons.html',greeting)

class CardsView(View,LoginRequiredMixin):
    def get(self , request):
        greeting = {}
        greeting['title'] = "Cards"
        greeting['heading'] = "Veltrix"
        greeting['subheading'] = "UI Elements"
        return render (request,'components/ui-elements/ui_elements-cards.html',greeting)          

class CarouselView(View,LoginRequiredMixin):
    def get(self , request):
        greeting = {}
        greeting['title'] = "Carousel"
        greeting['heading'] = "Veltrix"
        greeting['subheading'] = "UI Elements"
        return render (request,'components/ui-elements/ui_elements-carousel.html',greeting)          

class DropDownsView(View,LoginRequiredMixin):
    def get(self , request):
        greeting = {}
        greeting['title'] = "Dropdowns"
        greeting['heading'] = "Veltrix"
        greeting['subheading'] = "UI Elements"
        return render (request,'components/ui-elements/ui_elements-dropdowns.html',greeting)       

class GridView(View,LoginRequiredMixin):
    def get(self , request):
        greeting = {}
        greeting['title'] = "Grid"
        greeting['heading'] = "Veltrix"
        greeting['subheading'] = "UI Elements"
        return render (request,'components/ui-elements/ui_elements-grid.html',greeting)              

class ImagesView(View,LoginRequiredMixin):
    def get(self , request):
        greeting = {}
        greeting['title'] = "Images"
        greeting['heading'] = "Veltrix"
        greeting['subheading'] = "UI Elements"
        return render (request,'components/ui-elements/ui_elements-images.html',greeting)           

class LightBoxView(View,LoginRequiredMixin):
    def get(self , request):
        greeting = {}
        greeting['title'] = "Lightbox"
        greeting['heading'] = "Veltrix"
        greeting['subheading'] = "UI Elements"
        return render (request,'components/ui-elements/ui_elements-lightbox.html',greeting)          

class ModalsView(View,LoginRequiredMixin):
    def get(self , request):
        greeting = {}
        greeting['title'] = "Modals"
        greeting['heading'] = "Veltrix"
        greeting['subheading'] = "UI Elements"
        return render (request,'components/ui-elements/ui_elements-modals.html',greeting)          

class RangeSliderView(View,LoginRequiredMixin):
    def get(self , request):
        greeting = {}
        greeting['title'] = "Range Slider"
        greeting['heading'] = "Veltrix"
        greeting['subheading'] = "UI Elements"
        return render (request,'components/ui-elements/ui_elements-rangeslidebar.html',greeting)       

class SessionTimeoutView(View,LoginRequiredMixin):
    def get(self , request):
        greeting = {}
        greeting['title'] = "Session Timeout"
        greeting['heading'] = "Veltrix"
        greeting['subheading'] = "UI Elements"
        return render (request,'components/ui-elements/ui_elements-sessiontimeout.html',greeting)               

class ProgressBarsView(View,LoginRequiredMixin):
    def get(self , request):
        greeting = {}
        greeting['title'] = "Progress Bars"
        greeting['heading'] = "Veltrix"
        greeting['subheading'] = "UI Elements"
        return render (request,'components/ui-elements/ui_elements-progressbars.html',greeting)   

class SweetAlertView(View,LoginRequiredMixin):
    def get(self , request):
        greeting = {}
        greeting['title'] = " Sweet Alert 2"
        greeting['heading'] = "Veltrix"
        greeting['subheading'] = "UI Elements"
        return render (request,'components/ui-elements/ui_elements-sweetalert.html',greeting)                  

class TabsView(View,LoginRequiredMixin):
    def get(self , request):
        greeting = {}
        greeting['title'] = "Tabs & Accordions"
        greeting['heading'] = "Veltrix"
        greeting['subheading'] = "UI Elements"
        return render (request,'components/ui-elements/ui_elements-tabs.html',greeting)   

class TypoGraphyView(View,LoginRequiredMixin):
    def get(self , request):
        greeting = {}
        greeting['title'] = "Typography"
        greeting['heading'] = "Veltrix"
        greeting['subheading'] = "UI Elements"
        return render (request,'components/ui-elements/ui_elements-typography.html',greeting)  

class VideoView(View,LoginRequiredMixin):
    def get(self , request):
        greeting = {}
        greeting['title'] = "Video"
        greeting['heading'] = "Veltrix"
        greeting['subheading'] = "UI Elements"
        return render (request,'components/ui-elements/ui_elements-video.html',greeting)     

class GeneralView(View,LoginRequiredMixin):
    def get(self , request):
        greeting = {}
        greeting['title'] = "General"
        greeting['heading'] = "Veltrix"
        greeting['subheading'] = "UI Elements"
        return render (request,'components/ui-elements/ui_elements-general.html',greeting) 

class ColorsView(View,LoginRequiredMixin):
    def get(self , request):
        greeting = {}
        greeting['title'] = "Colors"
        greeting['heading'] = "Veltrix"
        greeting['subheading'] = "UI Elements"
        return render (request,'components/ui-elements/ui_elements-colors.html',greeting)  

class RatingView(View,LoginRequiredMixin):
    def get(self , request):
        greeting = {}
        greeting['title'] = "Rating"
        greeting['heading'] = "Veltrix"
        greeting['subheading'] = "UI Elements"
        return render (request,'components/ui-elements/ui_elements-rating.html',greeting) 

class UtilitiesView(View,LoginRequiredMixin):
    def get(self , request):
        greeting = {}
        greeting['title'] = "Utilities"
        greeting['heading'] = "Veltrix"
        greeting['subheading'] = "UI Elements"
        return render (request,'components/ui-elements/ui_elements-utilities.html',greeting)
    
    
class OffcanvasView(View,LoginRequiredMixin):
    def get(self , request):
        greeting = {}
        greeting['title'] = "Offcanvas"
        greeting['heading'] = "Veltrix"
        greeting['subheading'] = "UI Elements"
        return render (request,'components/ui-elements/ui_elements-offcanvas.html',greeting)

############FORMS###########################                 

class FormelementsView(View,LoginRequiredMixin):
    def get(self , request):
        greeting = {}
        greeting['title'] = "Form Elements"
        greeting['heading'] = "Veltrix"
        greeting['subheading'] = "Forms"
        return render (request,'components/forms/forms-formelements.html',greeting)   

class FormValidationView(View,LoginRequiredMixin):
    def get(self , request):
        greeting = {}
        greeting['title'] = "Form Validation"
        greeting['heading'] = "Veltrix"
        greeting['subheading'] = "Forms"
        return render (request,'components/forms/forms-formvalidation.html',greeting)      

class FormAdvancedView(View,LoginRequiredMixin):
    def get(self , request):
        greeting = {}
        greeting['title'] = "Form Advanced"
        greeting['heading'] = "Veltrix"
        greeting['subheading'] = "Forms"
        return render (request,'components/forms/forms-formadvanced.html',greeting) 

class FormEditorsView(View,LoginRequiredMixin):
    def get(self , request):
        greeting = {}
        greeting['title'] = "Form Editors"
        greeting['heading'] = "Veltrix"
        greeting['subheading'] = "Forms"
        return render (request,'components/forms/forms-formeditors.html',greeting)  

class FormFileuploadView(View,LoginRequiredMixin):
    def get(self , request):
        greeting = {}
        greeting['title'] = "Form File Upload"
        greeting['heading'] = "Veltrix"
        greeting['subheading'] = "Forms"
        return render (request,'components/forms/forms-formfileupload.html',greeting) 

class FormXeditableView(View,LoginRequiredMixin):
    def get(self , request):
        greeting = {}
        greeting['title'] = "Form Xeditable"
        greeting['heading'] = "Veltrix"
        greeting['subheading'] = "Forms"
        return render (request,'components/forms/forms-formxeditable.html',greeting)           

class FormRepeaterView(View,LoginRequiredMixin):
    def get(self , request):
        greeting = {}
        greeting['title'] = "Form Repeater"
        greeting['heading'] = "Veltrix"
        greeting['subheading'] = "Forms"
        return render (request,'components/forms/forms-formrepeater.html',greeting)         

class FormWizardView(View,LoginRequiredMixin):
    def get(self , request):
        greeting = {}
        greeting['title'] = "Form Wizard"
        greeting['heading'] = "Veltrix"
        greeting['subheading'] = "Forms"
        return render (request,'components/forms/forms-formrwizard.html',greeting)                  
        
class FormMaskView(View,LoginRequiredMixin):
    def get(self , request):
        greeting = {}
        greeting['title'] = "Form Mask"
        greeting['heading'] = "Veltrix"
        greeting['subheading'] = "Forms"
        return render (request,'components/forms/forms-formrmask.html',greeting) 

############Charts######################                 

class MorrisChartsView(View,LoginRequiredMixin):
    def get(self , request):
        greeting = {}
        greeting['title'] = "Morris Charts"
        greeting['heading'] = "Veltrix"
        greeting['subheading'] = "Charts"
        return render (request,'components/charts/charts-morrischarts.html',greeting)     

class ChartistChartsView(View,LoginRequiredMixin):
    def get(self , request):
        greeting = {}
        greeting['title'] = "Chartist Charts"
        greeting['heading'] = "Veltrix"
        greeting['subheading'] = "Charts"
        return render (request,'components/charts/charts-chartistcharts.html',greeting)     

class ChartjsChartsView(View,LoginRequiredMixin):
    def get(self , request):
        greeting = {}
        greeting['title'] = "Chartjs Charts"
        greeting['heading'] = "Veltrix"
        greeting['subheading'] = "Charts"
        return render (request,'components/charts/charts-chartjscharts.html',greeting) 

class FlotChartsView(View,LoginRequiredMixin):
    def get(self , request):
        greeting = {}
        greeting['title'] = "Flot Charts"
        greeting['heading'] = "Veltrix"
        greeting['subheading'] = "Charts"
        return render (request,'components/charts/charts-flotcharts.html',greeting)    

class JqueryKnobChartsView(View,LoginRequiredMixin):
    def get(self , request):
        greeting = {}
        greeting['title'] = "Jquery Knob Charts"
        greeting['heading'] = "Veltrix"
        greeting['subheading'] = "Charts"
        return render (request,'components/charts/charts-jqueryknobcharts.html',greeting)                                       

class SparklineChartsView(View,LoginRequiredMixin):
    def get(self , request):
        greeting = {}
        greeting['title'] = "Sparkline Charts"
        greeting['heading'] = "Veltrix"
        greeting['subheading'] = "Charts"
        return render (request,'components/charts/charts-sparklinecharts.html',greeting)   

######Tables##########
class BasicTablesView(View,LoginRequiredMixin):
    def get(self , request):
        greeting = {}
        greeting['title'] = "Basic Tables"
        greeting['heading'] = "Veltrix"
        greeting['subheading'] = "Tables"
        return render (request,'components/tables/tables-basictables.html',greeting)         

class DataTablesView(View,LoginRequiredMixin):
    def get(self , request):
        greeting = {}
        greeting['title'] = "Data Tables"
        greeting['heading'] = "Veltrix"
        greeting['subheading'] = "Tables"
        return render (request,'components/tables/tables-datatables.html',greeting) 

class ResponsiveTablesView(View,LoginRequiredMixin):
    def get(self , request):
        greeting = {}
        greeting['title'] = "Responsive Table"
        greeting['heading'] = "Veltrix"
        greeting['subheading'] = "Tables"
        return render (request,'components/tables/tables-responsivetables.html',greeting)  

class EditableTablesView(View,LoginRequiredMixin):
    def get(self , request):
        greeting = {}
        greeting['title'] = "Editable Table"
        greeting['heading'] = "Veltrix"
        greeting['subheading'] = "Tables"
        return render (request,'components/tables/tables-editabletables.html',greeting)   

###########Icons################  
class MaterialDesignView(View,LoginRequiredMixin):
    def get(self , request):
        greeting = {}
        greeting['title'] = "Material Design"
        greeting['heading'] = "Veltrix"
        greeting['subheading'] = "Icons"
        return render (request,'components/icons/icons-materialdesign.html',greeting)  

class FontAwesomeView(View,LoginRequiredMixin):
    def get(self , request):
        greeting = {}
        greeting['title'] = "Font Awesome"
        greeting['heading'] = "Veltrix"
        greeting['subheading'] = "Icons"
        return render (request,'components/icons/icons-fontawesome.html',greeting)     

class IonIconsView(View,LoginRequiredMixin):
    def get(self , request):
        greeting = {}
        greeting['title'] = "Ion Icons"
        greeting['heading'] = "Veltrix"
        greeting['subheading'] = "Icons"
        return render (request,'components/icons/icons-ionicons.html',greeting)  

class ThemifyIconsView(View,LoginRequiredMixin):
    def get(self , request):
        greeting = {}
        greeting['title'] = "Themify Icons"
        greeting['heading'] = "Veltrix"
        greeting['subheading'] = "Icons"
        return render (request,'components/icons/icons-themifyicons.html',greeting)   

class DripIconsView(View,LoginRequiredMixin):
    def get(self , request):
        greeting = {}
        greeting['title'] = "Dripicons"
        greeting['heading'] = "Veltrix"
        greeting['subheading'] = "Icons"
        return render (request,'components/icons/icons-dripicons.html',greeting)          

class TypIconsView(View,LoginRequiredMixin):
    def get(self , request):
        greeting = {}
        greeting['title'] = "Typicons Icons"
        greeting['heading'] = "Veltrix"
        greeting['subheading'] = "Icons"
        return render (request,'components/icons/icons-typicons.html',greeting)    

###########Maps###############
class GoogleMapsView(View,LoginRequiredMixin):
    def get(self , request):
        greeting = {}
        greeting['title'] = "Google Maps"
        greeting['heading'] = "Veltrix"
        greeting['subheading'] = "Maps"
        return render (request,'components/maps/maps-googlemaps.html',greeting)                                            

class VectorMapsView(View,LoginRequiredMixin):
    def get(self , request):
        greeting = {}
        greeting['title'] = "Vector Maps"
        greeting['heading'] = "Veltrix"
        greeting['subheading'] = "Maps"
        return render (request,'components/maps/maps-vectormaps.html',greeting)

               