from django.shortcuts import render

# Create your views here.

def all_views(request):
    return render(request,"chaiapp/all_chai.html")
