from django.urls import path    # type: ignore
from app import views
from django.conf import settings    # type: ignore
from django.conf.urls.static import static  # type: ignore
from django.contrib.auth import views as auth_views #type: ignore
from .forms import LoginForm,Password_Change_Form
urlpatterns = [
    #path('', views.home),
    
    #CLASS VIEW URL
    path('', views.ProductView.as_view(),name='home'),
    path('product-detail/<int:pk>', views.ProductDetail.as_view(),name='product-detail'),
    #Function View URL
    #path('product-detail/', views.product_detail, name='product-detail'),
    path('cart/', views.add_to_cart, name='add-to-cart'),
    path('buy/', views.buy_now, name='buy-now'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('address/', views.address, name='address'),
    path('orders/', views.orders, name='orders'),
   
    
    path('topwear/', views.topwear, name='topwear'),
    path('topwear/<slug:data>', views.topwear, name='topweardata'),
    
    path('mobile/', views.mobile, name='mobile'),
    path('mobile/<slug:data>', views.mobile, name='mobiledata'),
    
    path('laptop/', views.Laptop.as_view(), name='laptop'),
    path('laptop/<slug:data>', views.Laptop.as_view(), name='laptopdata'),
    
    # for login,logout we are using default authentication form
    #from here we, login is controled. no need to write view function in views.py for login
    path('accounts/login/',auth_views.LoginView.as_view(template_name='app/login.html',authentication_form=LoginForm), name='login'),
    
    #from here we, logout is controled. no need to write view function in views.py for logout
    path('logout/',auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    
    #for change password we used default view PasswordChangeView
    path('changepassword/',auth_views.PasswordChangeView.as_view(template_name='app/changepassword.html',form_class=Password_Change_Form,success_url='/passwordchangedone/'),name='changepassword'),
    # this is mandatory after change password PasswordChangeDoneView
    path('passwordchangedone/',auth_views.PasswordChangeDoneView.as_view(template_name='app/passwordchangedone.html'),name='passwordchangedone'),
    
    
    
    
    path('registration/', views.CustomerRegistrationView.as_view(), name='customerregistration'),
    path('checkout/', views.checkout, name='checkout'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  #image related configaretion , in setting.py also have to changed
