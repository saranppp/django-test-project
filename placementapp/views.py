from django.shortcuts import render

# Create your views here.
def hello(request):
    return render(request, 'placementapp/home.html')
def java(request):
    n1="system"
    n2="hp"
    n3="Dell"
    mydict={'news':n1,'news1':n2,'news2':n3}
    return render(request, 'placementapp/java.html', mydict)