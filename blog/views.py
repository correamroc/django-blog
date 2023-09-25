from django.shortcuts import render, get_object_or_404
# from django.http import HttpResponse
from .models import Post

def home(request):
    posts= Post.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def post_detail(request, post_id):
    post = Post.objects.get(pk=post_id)
#    except Post.DoesNotExist:
#        return HttpResponse(f"Post com id {post_id} não existe.")
    context = {
        'post': post
    }
    return render(request, 'blog/post_detail.html', context)
    