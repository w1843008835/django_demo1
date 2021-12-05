from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Articles

def hello_world(request):
    return HttpResponse("hello world")

def article_content(request):
    article = Articles.objects.all()[0]
    title = article.title
    breif_content = article.brief_content
    content = article.content
    returnStr = "title:%s, breif_content:%s, content:%s"%(title,breif_content,content)
    return HttpResponse(returnStr)

def get_index_page(request):
    all_article = Articles.objects.all()
    return render(request,'blog/index.html',{'article_list':all_article})

def get_detail_page(request):
    cur_article = Articles.objects.all()[0]
    section_list = cur_article.content.split("\n")
    return render(request,'blog/detail.html',{'cur_article':cur_article,'section_list':section_list})
