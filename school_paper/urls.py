"""
URL configuration for school_paper project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from website.views import (
    home_view, 
    news_view, 
    news_articles_view,
    sport_view, 
    sport_articles_view,
    opinion_view, 
    opinion_articles_view,
    feature_view, 
    feature_articles_view,
    about_view, 
    art_view,
    art_articles_view,
    life_culture_view,
    life_culture_articles_view,
    science_view,
    science_articles_view,
    comment_create_view,
)



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),
    path('news/',news_view, name="news_page"),
    path('news/<int:article_id>/', news_articles_view),
    path('sports/',sport_view, name="sports_page"),
    path('sports/<int:article_id>/', sport_articles_view),
    path('opinion/',opinion_view, name="opinions_page"),
    path('opinion/<int:article_id>/', opinion_articles_view),
    path('feature/',feature_view, name="features_page"),
    path('feature/<int:article_id>/', feature_articles_view),
    path('about/',about_view, name="about_page"),
    path('art/',art_view, name="arts_page"),
    path('art/<int:article_id>/', art_articles_view),
    path('science/',science_view, name="science_page"),
    path('science/<int:article_id>/', science_articles_view),
    path('life_culture/',life_culture_view, name="life_culture_page"),
    path('life_culture/<int:article_id>/', life_culture_articles_view),
    path('comment/',comment_create_view),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)