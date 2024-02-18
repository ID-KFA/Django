from django.shortcuts import render, get_object_or_404
from django.http import HttpRequest
from .models import ArticleModel, Comment
from .forms import NewAuthor, NewArticle


def all_articles(request: HttpRequest, author_id):
    articles = ArticleModel.objects.filter(author=author_id)
    return render(request, "author/blog.html", {"articles": articles})

def full_articles(request, article_id):
    full = ArticleModel.objects.get(id=article_id)
    comment = Comment.object.filter(article=full)
    return render(request, "author/blog.html", {"articles": full})



def article_page(request: HttpRequest, article_id):
    articles = get_object_or_404(ArticleModel, pk=article_id)
    articles.views_count += 1
    articles.save()
    return render(request, "author/article.html", {"articles": articles})





def newauthor(request):
    if request.method == "POST":
        form = NewAuthor(request.POST)
        if form.is_valid():
            author = form.save()
            return all_articles(request, author.pk)
        else:
            return render(request, "author/newauthor.html", {"form": form})
    return render(request, "author/newauthor.html", {"form": NewAuthor()})


def newarticle(request):
    if request.method == "POST":
        form = NewArticle(request.POST)
        if form.is_valid():
            post = form.save()
            return all_articles(request, post.pk)
        else:
            return render(request, "author/newpost.html", {"form": form})
    return render(request, "author/newpost.html", {"form": NewArticle()})