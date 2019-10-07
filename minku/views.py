from django.shortcuts import render

# Create your views here.
def portfolio(request):
    res=render(request,"index.html")
    return res
