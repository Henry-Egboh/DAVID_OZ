from django.urls import path
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView
from .import views

# from .views import home
app_name = "shirling"

urlpatterns=[
    path('',views.home, name='home'),
    path('about/',views.about, name='about'),
    path('blog/',views.blog, name='blog'),
    path('cart/',views.cart, name='cart'),
    path('checkout/',views.checkout, name='checkout'),
    path('contact',views.contact, name='contact'),
    path('product/',views.product, name='product'),
]