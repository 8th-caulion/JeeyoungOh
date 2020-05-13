from django.shortcuts import render, get_object_or_404, redirect
from .models import Blog
from django.utils import timezone
from django.core.paginator import Paginator

# Create your views here.
def home(request):
    blogs = Blog.objects.all()
    paginator = Paginator(blogs, 5)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'home.html', {'posts':posts})

def detail(request, blog_id):
    details = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'detail.html', {'details':details})

def new(request):
    return render(request, 'new.html')

def create(request):
    blog = Blog()
    blog.title = request.POST["title"]
    blog.content = request.POST["content"]
    blog.pub_date = request.POST["pub_date"]
    blog.save()
    return redirect('home')

def edit(request,blog_id):
    blog = get_object_or_404(Blog, pk = blog_id)
    return render(request, 'edit.html', {'blog':blog})

def update(request, blog_id):
    blog =  get_object_or_404(Blog, pk = blog_id)
    blog.title = request.GET['title']
    blog.body =   request.GET['body']
    blog.pub_date = timezone.datetime.now()
    blog.save()
    return redirect('home')
    
def delete(request, blog_id):
    blog =  get_object_or_404(Blog, pk = blog_id)
    blog.delete()
    return redirect('home')
    