from django.shortcuts import render
from django.http.response import HttpResponse, Http404
from django.template.loader import get_template     # get_template - отвечает за получение шаблона
from django.template import Context                 # отвечает за хранение переменных которые будут отправлены в шаблон
from django.shortcuts import render_to_response, redirect
from article.models import Article, Comments
from django.core.exceptions import ObjectDoesNotExist
from .forms import CommentForm
from django.core.context_processors import csrf
from django.core.paginator import  Paginator
from django.contrib import auth



def basic_one(request):                # єта функция получает запрос пользователя после чего перенаправляется на хтмл код
    view = "basic_one"
    html = "<html><body> This is %s view </body></html>" % view
    return HttpResponse(html)

def template_two(request):
    view = "template_two"
    t = get_template('my_views.html')                             # указываем имя файла где находится хтмл код
    html = t.render(Context({'name': view}))
    return HttpResponse(html)

def template_three_simple(request):
    view = "template_three_simple"
    return render_to_response('my_views.html', {'name': view})

def articles(request, page_number=1):
    all_articles = Article.objects.all()
    current_page = Paginator(all_articles, 5)
    return render_to_response('articles.html', {'articles': current_page.page(page_number), 'username': auth.get_user(request).username})

#def article(request, article_id=1):
    #return render_to_response('article.html', {'article': Article.objects.get(id=article_id), 'comments': Comments.objects.filter(comments_article_id=article_id)})

def article(request, article_id=1):
    comment_form = CommentForm
    args = {}
    args.update(csrf(request))
    args['article'] = Article.objects.get(id=article_id)
    args['comments'] = Comments.objects.filter(comments_article=article_id)
    args['form'] = comment_form
    args['username'] = auth.get_user(request).username
    return render_to_response('article.html', args)

def addlike(request, article_id):
    try:
        if article_id in request.COOKIES:
           return redirect(request.META.get('HTTP_REFERER', '/'))
            #redirect('/')
        else:
            article = Article.objects.get(id=article_id)
            article.article_likes += 1                      # увеличиваем количество лайков
            article.save()
            #render_to_response = redirect('/')
            render_to_response = redirect(request.META.get('HTTP_REFERER', '/'))
            render_to_response.set_cookie(article_id, 'test')
            return render_to_response
    except ObjectDoesNotExist:
        raise Http404

def addcomment(request, article_id):
    if request.POST:          #and ("pause" not in request.session):
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)                               # получаем данные с формы
            comment.comments_article = Article.objects.get(id=article_id)   # с асоциировался со статьей
            form.save()
            request.session.set_expiry(0)
            request.session["pause"] = True
        return redirect('/articles/get/%s' % article_id)
