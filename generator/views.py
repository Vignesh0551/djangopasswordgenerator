from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.
def home(request):
    return render(request,'generator\home.html')

def password(request):
    Charecters=list('abcdefghijklmnopqrstuvwxyz')
    if request.GET.get('Uppercase'):
        Charecters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    if request.GET.get('Number'):
        Charecters.extend(list('1234567890'))

    if request.GET.get('Special'):
        Charecters.extend(list('!@#$%^&*()_+?/><'))

    length=int(request.GET.get('length'))
    password=''
    for i in range(length):
        password +=random.choice(Charecters)
    return render(request,'generator\password.html',{'password':password})
