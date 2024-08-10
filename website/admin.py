from django.contrib import admin

# Register your models here.

from website.models import Feature
admin.site.register(Feature)

from website.models import News
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'main')
    list_editable = ('main',)
admin.site.register(News, NewsAdmin)

from website.models import Opinion
class OpinionAdmin(admin.ModelAdmin):
    list_display = ('title', 'main')
    list_editable = ('main',)
admin.site.register(Opinion, OpinionAdmin)

from website.models import Sport
class SportAdmin(admin.ModelAdmin):
    list_display = ('title', 'main')
    list_editable = ('main',)
admin.site.register(Sport, SportAdmin)

from website.models import Science
class ScienceAdmin(admin.ModelAdmin):
    list_display = ('title', 'main')
    list_editable = ('main',)
admin.site.register(Science, ScienceAdmin)

from website.models import Life_culture
class Life_cultureAdmin(admin.ModelAdmin):
    list_display = ('title', 'main')
    list_editable = ('main',)
admin.site.register(Life_culture, Life_cultureAdmin)

from website.models import Art
class ArtAdmin(admin.ModelAdmin):
    list_display = ('title', 'main')
    list_editable = ('main',)
admin.site.register(Art, ArtAdmin)

from website.models import Comment
admin.site.register(Comment)
