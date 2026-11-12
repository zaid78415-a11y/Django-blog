from django.shortcuts import render
from sympy.integrals.meijerint_doc import about

from assignment.models import About
from blog.models import Category,Blog

def home(request):
    featured_post = Blog.objects.filter(is_featured=True,status='Published').order_by('-updated_at')
    posts = Blog.objects.filter(is_featured=False,status='Published')

    # fetch about
    try:
        about = About.objects.get()
    except:
        about = None

    context = {
        'featured_post':featured_post,
        'posts':posts,
        'about':about

    }
    return render(request,'home.html',context)
