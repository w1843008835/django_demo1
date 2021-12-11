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

def get_detail_page(request,article_id):
    all_article = Articles.objects.all()
    cur_article = None
    pre_article = None
    next_article = None
    pre_index = 0
    next_index = 0
    for index,articles in enumerate(all_article):
        if int(article_id) == int(articles.article_id):
            if index == 0:
                pre_index = 0
                next_index = int(index) + 1
            elif index == len(all_article) - 1:
                next_index = int(index)
                pre_index = int(index) - 1
            else:
                pre_index = int(index) - 1
                next_index = int(index) + 1

            cur_article = articles
            pre_article = all_article[pre_index]
            next_article = all_article[next_index]
            break
    section_list = cur_article.content.split("\n")
    return render(request,'blog/detail.html',{'cur_article':cur_article,
                                              'section_list':section_list,
                                              'pre_article':pre_article,
                                              'next_article':next_article
                                              })
