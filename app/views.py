from django.shortcuts import render

# Create your views here.

def conditions(request):
    d={'a':1907,'b':2030,'c':2000}
    return render(request ,'conditions.html',context=d)

def loop(request):
    d={'name':'ASHU'}
    return render(request,'loop.html',d)
  