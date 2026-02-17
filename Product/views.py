from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import product
from django.db.models import Q
# Create your views here.
@login_required
def publier(request):

    if request.method =='POST':
        title_p=request.POST.get('title')
        descript_p=request.POST.get('description')
        price_p=request.POST.get('price')
        img_p=request.FILES.get('image')

        product.objects.create(
                title=title_p,
                description=descript_p,
                price=price_p,
                image=img_p,
                seller=request.user 
            )
        return redirect('home')
    return render(request, 'publier.html')



def Product(request):
    items = product.objects.all().order_by('-created_at')
    
    return render(request, 'Product.html', {'items': items})




@login_required
def delete_product(request, id):
    item = get_object_or_404(product, id=id)

    if item.seller == request.user:
        item.delete()
    
    return redirect('Profile')

def product_detail(request, id):
    item = get_object_or_404(product, id=id)
    
    return render(request, 'product_detaille.html', {'item': item})


def search_view(request):
    if 'search_name' in request.GET:
        query = request.GET.get('search_name', '').strip()
        
        if query:
            results = product.objects.filter(
                Q(title__icontains=query) | Q(description__icontains=query)
            ).order_by('-created_at')
        else:
            results = []
            return redirect('search_Product')
    else:
        query = None
        results = None 
    return render(request, 'search.html', {
        'results': results, 
        'query': query
    })