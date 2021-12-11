from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Articles
from django.core.paginator import Paginator
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
    page = request.GET.get('page')
    if page:
        page = int(page)
    else:
        page = 1
    all_article = Articles.objects.all()
    top2_article_list = Articles.objects.order_by('-publish_date')[:2]
    paginator = Paginator(all_article,2)
    page_num = paginator.num_pages
    page_article_list = paginator.page(page)
    if page_article_list.has_next():
        next_page = page+1
    else:
        next_page = page
    if page_article_list.has_previous():
        previous_page = page - 1
    else:
        previous_page = page
    return render(request,'blog/index.html',{'article_list':page_article_list,
                                             'page_num':range(1,page_num+1),
                                             'cur_page':page,
                                             'next_page':next_page,
                                             'previous_page':previous_page,
                                             'top2_article_list':top2_article_list
                                             })

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
