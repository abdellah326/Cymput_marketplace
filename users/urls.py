from django.urls import path
from users.views import login_view,creatAcc


urlpatterns = [
    path('',login_view,name='login'),
    path('creatAcc',creatAcc,name='creatAcc'),
]
