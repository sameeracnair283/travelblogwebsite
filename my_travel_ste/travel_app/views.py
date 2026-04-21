from django.shortcuts import render
from .models import Destination
from .forms import DestinationForm
from django.shortcuts import redirect


def index(request):
    dests = Destination.objects.all()
    return render(request, 'index.html', {'destinations': dests})

def add_post(request):
    if request.method == "POST":
        form = DestinationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
        # If form is NOT valid, it falls through to the render below
    else:
        # This handles the initial GET request
        form = DestinationForm()
    
    # This return is OUTSIDE the 'if' block, so it always runs 
    # unless the redirect above is triggered.
    return render(request, 'add_blog.html', {'form': form})