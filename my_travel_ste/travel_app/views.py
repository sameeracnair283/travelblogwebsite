from django.shortcuts import render, redirect, get_object_or_404
from .models import Destination
from .forms import DestinationForm


def index(request):
    dests = Destination.objects.all()
    return render(request, 'index.html', {'destinations': dests})


def add_blog(request):
    if request.method == "POST":
        form = DestinationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = DestinationForm()

    return render(request, 'add_blog.html', {'form': form})


def edit_blog(request, id):
    post = get_object_or_404(Destination, id=id)

    if request.method == "POST":
        form = DestinationForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = DestinationForm(instance=post)

    return render(request, 'add_blog.html', {'form': form})


def delete_blog(request, id):
    post = get_object_or_404(Destination, id=id)
    post.delete()
    return redirect('/')


def post_detail(request, id):
    post = get_object_or_404(Destination, id=id)
    return render(request, 'blog/post_detail.html', {'post': post})