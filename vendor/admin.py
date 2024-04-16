from django.contrib import admin

#Important for admin 5asa b mas2oleen l mawke3 btt7akem fel mawke3 bta3ak meno
# Register your models here.
#mn 5lal admin 7at3ml register lel model bta3tak

from .models import Product
admin.site.register(Product)

#from .models import Vendor
#admin.site.register(Vendor)

from .models import Login
admin.site.register(Login)