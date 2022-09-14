from django.shortcuts import render
from django.views.generic import ListView
from .models import HomeSlider, HomeSliderActive, HomeInfo, HomeProduct, Inf, HomeSlider1, HomeSlider1Active
# Create your views here.

class HomeListView(ListView):
    template_name = 'index.html'

    def get(self, request):
        homeslider = HomeSlider.objects.all()
        homeslideractive = HomeSliderActive.objects.all()
        homeinfo = HomeInfo.objects.all()
        inf = Inf.objects.all()
        homeproduct = HomeProduct.objects.all()
        homeslider1 = HomeSlider1.objects.all()
        homeslider1active = HomeSlider1Active.objects.all()
        return render(request, self.template_name, {'homeslideractive':homeslideractive, 'homeslider':homeslider, 'homeinfo':homeinfo, 'homeproduct':homeproduct, 
        'inf':inf, 'homeslider1active':homeslider1active, 'homeslider1':homeslider1})


class AboutListView(ListView):
    template_name = 'about.html'

    def get(self, request):
        return render(request, self.template_name)



class ComputerListView(ListView):
    template_name = 'computer.html'

    def get(self, request):
        return render(request, self.template_name)



class ContactListView(ListView):
    template_name = 'contact.html'

    def get(self, request):
        return render(request, self.template_name)



class LaptopListView(ListView):
    template_name = 'laptop.html'

    def get(self, request):
        return render(request, self.template_name)



class ProductListView(ListView):
    template_name = 'product.html'

    def get(self, request):
        return render(request, self.template_name)
