from django.shortcuts import render
from mydata.models import File


# Create your views here.
def index(request):
    files = File.objects.all()
    return render(request,  "index.html", {"files": files})