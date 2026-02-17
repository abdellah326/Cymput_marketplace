from django.shortcuts import render
from Product.models import product
# Create your views here.
def home(request):
    latest_products = product.objects.all().order_by('-created_at')[:10]
    return render(request, 'home.html', {'latest_products': latest_products})
