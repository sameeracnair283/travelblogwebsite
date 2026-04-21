from django.shortcuts import render
from .models import Destination
from .forms import DestinationForm
from django.shortcuts import redirect


def index(request):
    dests = Destination.objects.all()
    return render(request, 'index.html', {'dests': dests})

def add_post(request):
    if request.method=="POST":
        form = DestinationForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            form = DestinationForm()
            return render(request,'add_blog.html',{'form':form})