from urllib import response
from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm

def home(request):
    new_posts = Post.objects.filter().order_by('date')[:5]
    if request.session.get('email', False):
        email = request.session['email']
        return render(request, 'index.html', {'posts':new_posts, 'email':email})
    return render(request, 'index.html', {'posts': new_posts})

def gallery(request):
    all_posts = Post.objects.filter().order_by('date')
    if request.session.get('email', False):
        email = request.session['email']
        return render(request, 'gallery.html', {'all_posts':all_posts, 'email':email})
    return render(request, 'gallery.html', {'all_posts': all_posts})

def postcreate(request):
    if request.method == 'POST' or request.method == "FILES":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            unfinished = form.save(commit=False)
            unfinished.nickname = request.session['email']
            unfinished.save()
            return redirect("gallery")
        else:
            return redirect("gallery")
    else:
        form = PostForm()
        return render(request, "upload_form.html", {'form': form}) 


