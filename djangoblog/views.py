from django.shortcuts import render
from django.http import HttpResponse




def about(request):
    #return HttpResponse('hi there!')
    return render(request,'about.html')


def home(request):
    #return HttpResponse('hey you? you,re wonderful !!!')
    return render(request,'home.html')
