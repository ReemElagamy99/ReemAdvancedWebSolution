from django.shortcuts import render
from django.http import HttpResponse
from .models import Login
from .models import Product
from django.template.loader import get_template
from django.template.loader import get_template
from .forms import ProductForm

def add_product(request):
       return render(request, 'vendor/add_product.html')


# View functions
def sales(request):
    # Renders the index page template
    username = request.session.get('username', 'Guest')  # Default to 'Guest' if not found
    context = {'username': username}
    return render(request, 'vendor/sales.html')

# View functions
def index(request):
    # Renders the index page template
    return render(request, 'vendor/productmanagment.html')

def products_view(request):
    # Retrieve data from the Product model
    products = Product.objects.all()
    return render(request, 'vendor/products.html', {'products': products})

def vendorlogin(request):
    # Placeholder for vendor login view
    #return HttpResponse('Login Page for Vendor')
  return render(request, 'vendor/vendorlogin.html')

# views.py
def vendordashboard(request):
    username = request.session.get('username', 'Guest')  # Default to 'Guest' if not found
    context = {'username': username}
    return render(request, 'vendor/vendordashboard.html', context)


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

# views.py
from django.shortcuts import render, redirect

# views.py
from django.shortcuts import render, redirect

# views.py
from django.shortcuts import render, redirect

def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        # Assuming you are saving this data to a model called Login
        data = Login(username=username, password=password)
        data.save()
        # Store username in session
        request.session['username'] = username
        return redirect('vendordashboard')
    return render(request, 'vendor/signup.html')




    # Placeholder for vendor dashboard view
    #return HttpResponse('Vendor Dashboard')
    