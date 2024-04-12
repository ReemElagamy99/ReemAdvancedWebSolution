from django.shortcuts import render
from django.http import HttpResponse

# View functions
def index(request):
    # Renders the index page template
    return render(request, 'vendor/productmanagment.html')

def vendorlogin(request):
    # Placeholder for vendor login view
    #return HttpResponse('Login Page for Vendor')
  return render(request, 'vendor/vendorlogin.html')

def vendordashboard(request):
      return render(request, 'vendor/vendordashboard.html')

def productmanagment(request):
      return render(request, 'vendor/productmanagment.html')

def vendorsignup(request):
      return render(request, 'vendor/vendorsignup.html')

def vendoruserprofile(request):
      return render(request, 'vendor/vendoruserprofile.html')


def productsOne(request):
      return render(request, 'vendor/productsOne.html')


def reports(request):
      return render(request, 'vendor/reports.html')
    # Placeholder for vendor dashboard view
    #return HttpResponse('Vendor Dashboard')
    
