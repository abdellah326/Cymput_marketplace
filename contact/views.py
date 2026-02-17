from django.shortcuts import render,redirect
from .models import Contact
from django.contrib import messages
# Create your views here.
def contact(request):

    if request.method == 'POST':
        fullName=request.POST.get('full_name')
        mail=request.POST.get('email')
        Subject=request.POST.get('subject')
        msg=request.POST.get('message')

        Contact.objects.create(
            full_name=fullName,
            email=mail,
            subject=Subject,
            message=msg
        )
        messages.success(request, 'lah irdi eliik')
        return redirect('contact')
    return render(request , 'contact.html')