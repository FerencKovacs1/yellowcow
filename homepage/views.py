from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'home/home.html')

def seo(request):
    return render(request, 'home/seo.html')
