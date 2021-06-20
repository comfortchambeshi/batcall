from django.http import HttpResponse
from django.shortcuts import render
from .models import Article 

def blog_home(request):
    articles = Article.objects.all().order_by('published_date')
    
    return render(request, 'blog/blog_home.html', {'articles': articles})


def blog_detail(request, blog_id):
    
    article = Article.objects.get(id=blog_id)
    return render(request, 'blog/blog_view.html', {'article':article})
    
    