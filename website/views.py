from django.http import HttpResponse
from django.shortcuts import render

from .models import News, Sport, Opinion, Feature, Art, Life_culture, Science
from .forms import CommentForm

# Create your views here.
def home_view(request):
    main_news = News.objects.filter(main=True).first()
    latest_news = News.objects.filter(main=False).order_by('-date_added')[:3]
    main_opinion = Opinion.objects.filter(main=True).first()
    main_art = Art.objects.filter(main=True).first()
    main_life_culture = Life_culture.objects.filter(main=True).first()
    main_science = Science.objects.filter(main=True).first()
    latest_features = Feature.objects.order_by('-date_added')[:3]
    main_sport = Sport.objects.filter(main=True).first()
    latest_sport = Sport.objects.filter(main=False).order_by('-date_added')[:3]
    
    context = {
        'main_news':main_news,
        'latest_news':latest_news,
        'main_opinion':main_opinion,
        'main_art':main_art,
        'main_life_culture':main_life_culture,
        'main_science':main_science,
        'latest_features':latest_features,
        'main_sport':main_sport,
        'latest_sport':latest_sport,

    }
    return render(request, 'home.html', context)


def news_view(request):
    news = News.objects.order_by(('-date_added'))
    context = {
        'news':news,
    }
    return render(request, 'news.html', context)

def news_articles_view(request, article_id):
    news_articles = News.objects.get(id=article_id)
    context = {
        'news_articles': news_articles,
    }
    return render(request, "articles/news_article.html", context)

def sport_view(request):
    sport = Sport.objects.order_by(('-date_added'))
    context = {
        'sport':sport
    }
    return render(request, 'sport.html', context)

def sport_articles_view(request, article_id):
    sport_articles = Sport.objects.get(id=article_id)
    context = {
        'sport_articles': sport_articles,
    }
    return render(request, "articles/sport_article.html", context)

def opinion_view(request):
    opinion = Opinion.objects.order_by(('-date_added'))
    context = {
        'opinion':opinion
    }
    return render(request, 'opinion.html', context)

def opinion_articles_view(request, article_id):
    opinion_articles = Opinion.objects.get(id=article_id)
    context = {
        'opinion_articles': opinion_articles,
    }
    return render(request, "articles/opinion_article.html", context)

def art_view(request):
    art = Art.objects.order_by(('-date_added'))
    context = {
        'art':art
    }
    return render(request, 'art.html', context)

def art_articles_view(request, article_id):
    art_articles = Art.objects.get(id=article_id)
    context = {
        'art_articles': art_articles,
    }
    return render(request, "articles/art_article.html", context)

def life_culture_view(request):
    life_culture = Life_culture.objects.order_by(('-date_added'))
    context = {
        'life_culture':life_culture
    }
    return render(request, 'life_culture.html', context)

def life_culture_articles_view(request, article_id):
    life_culture_articles = Life_culture.objects.get(id=article_id)
    context = {
        'life_culture_articles': life_culture_articles,
    }
    return render(request, "articles/life_culture_article.html", context)

def science_view(request):
    science = Science.objects.order_by(('-date_added'))
    context = {
        'science':science
    }
    return render(request, 'science.html', context)

def science_articles_view(request, article_id):
    science_articles = Science.objects.get(id=article_id)
    context = {
        'science_articles': science_articles,
    }
    return render(request, "articles/science_article.html", context)

def feature_view(request):
    feature = Feature.objects.order_by(('-date_added'))
    context = {
        'feature':feature
    }
    return render(request, 'feature.html', context)

def feature_articles_view(request, article_id):
    feature_articles = Feature.objects.get(id=article_id)
    context = {
        'feature_articles': feature_articles,
    }
    return render(request, "articles/feature_article.html", context)


def about_view(request):
    return render(request, 'about.html', {})


def comment_create_view(request):
    comment = CommentForm(request.POST or None)
    if comment.is_valid():
        comment.save()
    
    context = {
        'comment':comment
    }
    return render(request, "comment.html", context)