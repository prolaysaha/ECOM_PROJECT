from django.shortcuts import render,redirect # type: ignore
from django.views import View # type: ignore
from django.http import HttpResponse # type: ignore
from .models import Customer,Product,Cart,OrderPlaced
from .forms import CustomerRegistrationForm,CustomerProfile
from django.contrib import messages     # type: ignore


#def home(request):
# return render(request, 'app/home.html')

#Class View
class ProductView(View):
    def get(self,request):
        #DOING FILTER HERE
        mobiles=Product.objects.filter(category='M')
        loptops=Product.objects.filter(category='L')
        topwears=Product.objects.filter(category='TW')
        bottomwears=Product.objects.filter(category='BT')
        return render(request,'app/home.html',{'mobiles':mobiles,'loptops':loptops,'topwears':topwears,'bottomwears':bottomwears})

class ProductDetail(View):
    def get(self,request,pk):
        product=Product.objects.get(id=pk)
        return render(request,'app/productdetail.html',{'product':product})
        
#Function View
#def product_detail(request):
 #return render(request, 'app/productdetail.html')

def add_to_cart(request):
 return render(request, 'app/addtocart.html')

def buy_now(request):
 return render(request, 'app/buynow.html')

def address(request):
 return render(request, 'app/address.html')

def orders(request):
 return render(request, 'app/orders.html')

#class view
#class view
class Laptop(View):
    def get(self,request,data=None):
        if data == None:
            laptops=Product.objects.filter(category='L')
        elif data == 'Dell' or data == 'HP':
            laptops=Product.objects.filter(category='L').filter(brand=data)
        elif data == 'below':
            laptops=Product.objects.filter(category='L').filter(discounted_price__lt=50000)
        elif data == 'above':
            laptops=Product.objects.filter(category='L').filter(discounted_price__gt=50000)
        return render(request,'app/laptop.html',{'laptops':laptops})
#function view
def mobile(request, data = None):
    if data == None:
        mobiles=Product.objects.filter(category='M')
    elif data == 'iphone' or data == 'sumsung':
        mobiles=Product.objects.filter(category='M').filter(brand=data)
    elif data == 'below':
        mobiles=Product.objects.filter(category='M').filter(discounted_price__lt=52000)
    elif data == 'above':
        mobiles=Product.objects.filter(category='M').filter(discounted_price__gt=52000)    
    return render(request, 'app/mobile.html',{'mobiles':mobiles})

def topwear(request, data = None):
    if data == None:
        topwears=Product.objects.filter(category='TW')
    elif data == 'T-Shirt' or data == 'Shirt':
        topwears=Product.objects.filter(category='TW').filter(brand=data)
    elif data == 'below':
        topwears=Product.objects.filter(category='TW').filter(discounted_price__lt=1100)
    elif data == 'above':
        topwears=Product.objects.filter(category='TW').filter(discounted_price__gt=1100)    
    return render(request, 'app/topwear.html',{'topwears':topwears})
"""
def login(request):
     return render(request, 'app/login.html')"""

class CustomerRegistrationView(View):
    def get(self, request):
        form=CustomerRegistrationForm()
        return render(request, 'app/customerregistration.html',{'form':form})
    def post(self, request):
        form=CustomerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registration Successful')
            form=CustomerRegistrationForm()
            return render(request, 'app/customerregistration.html', {'form': form})
            #return redirect('http://127.0.0.1:8000/registration/')
        else:
            # If form is invalid, re-render the form with errors
            
            return render(request, 'app/customerregistration.html', {'form': form})
        
        

def checkout(request):
 return render(request, 'app/checkout.html')

class ProfileView(View):
    def get(self, request):
        form=CustomerProfile()
        return render(request, 'app/profile.html',{'form':form})
    def post(self,request):
        form=CustomerProfile(request.POST)
        if form.is_valid():
            uer=request.user
            nm=form.cleaned_data['name']
            loc=form.cleaned_data['location']
            ct=form.cleaned_data['city']
            zp=form.cleaned_data['zipcode']
            state=form.cleaned_data['state']
            obj=Customer(user=uer,name=nm,location=loc,city=ct,zipcode=zp,state=state)
            obj.save()
            messages.success(request, 'Profile Updated!!')
            form=CustomerProfile()
            return render(request, 'app/profile.html', {'form': form})
        
        
        