"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from Home import views
from Product.views import Product
from Product.views import search_view
from contact.views import contact
from Profile.views import Profile
from Product.views import publier
from Product.views import delete_product
from Product.views import product_detail


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home',views.home,name='home'),
    path('Product',Product,name='Product'),
    path('search',search_view,name='search_Product'),
    path('Product-detail/<int:id>/',product_detail,name='product_detail'),
    path('contact',contact,name='contact'),
    path('Profile',Profile,name='Profile'),
    path('', include('users.urls')),
    path('add_post',publier,name='publier'),
    path('delete-product/<int:id>/', delete_product, name='delete_product'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)