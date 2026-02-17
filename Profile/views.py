from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import profile
from Product.models import product
from django.contrib.auth.models import User


# Create your views here.
@login_required
def Profile(request):
    user_profile =request.user.profile 
    if request.method =='POST':
        num_t=request.POST.get('phone')
        ville=request.POST.get('city')
        image=request.FILES.get('image')
        user_profile.phone=num_t
        user_profile.city=ville
        if image:
          user_profile.image=image
        user_profile.save()
        return redirect('Profile')
    my_products = product.objects.filter(seller=request.user)
    context = {
        'products': my_products
    }

    return render(request, 'profile.html',context)


