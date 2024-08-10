from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Feature(models.Model):
    title = models.CharField(max_length=300)
    date_added = models.DateTimeField(auto_now_add=True)
    content = RichTextField()
    image = models.ImageField(upload_to='media/', blank=True, null=True)
    main = models.BooleanField(default=False)
    
    class Meta: 
        verbose_name_plural = 'features'

    def save(self, *args, **kwargs):
        if self.main:
            Feature.objects.filter(main=True).update(main=False)
        super(Feature, self).save(*args, **kwargs)
          
    def __str__(self):
        return self.title

class News(models.Model):
    title = models.CharField(max_length=300)
    date_added = models.DateTimeField(auto_now_add=True)
    content = RichTextField()
    image = models.ImageField(upload_to='media/', blank=True, null=True)
    main = models.BooleanField(default=False)
    
    class Meta: 
        verbose_name_plural = 'news'

    def save(self, *args, **kwargs):
        if self.main:
            News.objects.filter(main=True).update(main=False)
        super(News, self).save(*args, **kwargs)
          
    def __str__(self):
        return self.title
    
class Opinion(models.Model):
    title = models.CharField(max_length=300)
    date_added = models.DateTimeField(auto_now_add=True)
    content = RichTextField()
    image = models.ImageField(upload_to='media/', blank=True, null=True)
    main = models.BooleanField(default=False)
    
    class Meta: 
        verbose_name_plural = 'opinions'

    def save(self, *args, **kwargs):
        if self.main:
            Opinion.objects.filter(main=True).update(main=False)
        super(Opinion, self).save(*args, **kwargs)
          
    def __str__(self):
        return self.title
    
class Sport(models.Model):
    title = models.CharField(max_length=300)
    date_added = models.DateTimeField(auto_now_add=True)
    content = RichTextField()
    image = models.ImageField(upload_to='media/', blank=True, null=True)
    main = models.BooleanField(default=False)
    
    class Meta: 
        verbose_name_plural = 'sports'

    def save(self, *args, **kwargs):
        if self.main:
            Sport.objects.filter(main=True).update(main=False)
        super(Sport, self).save(*args, **kwargs)
          
    def __str__(self):
        return self.title
    
class Science(models.Model):
    title = models.CharField(max_length=300)
    date_added = models.DateTimeField(auto_now_add=True)
    content = RichTextField()
    image = models.ImageField(upload_to='media/', blank=True, null=True)
    main = models.BooleanField(default=False)
    
    class Meta: 
        verbose_name_plural = 'science'

    def save(self, *args, **kwargs):
        if self.main:
            Science.objects.filter(main=True).update(main=False)
        super(Science, self).save(*args, **kwargs)
          
    def __str__(self):
        return self.title


class Life_culture(models.Model):
    title = models.CharField(max_length=300)
    date_added = models.DateTimeField(auto_now_add=True)
    content = RichTextField()
    image = models.ImageField(upload_to='media/', blank=True, null=True)
    main = models.BooleanField(default=False)
    
    class Meta: 
        verbose_name_plural = 'Life'

    def save(self, *args, **kwargs):
        if self.main:
            Life_culture.objects.filter(main=True).update(main=False)
        super(Life_culture, self).save(*args, **kwargs)
          
    def __str__(self):
        return self.title
    

class Art(models.Model):
    title = models.CharField(max_length=300)
    date_added = models.DateTimeField(auto_now_add=True)
    content = RichTextField()
    image = models.ImageField(upload_to='media/', blank=True, null=True)
    main = models.BooleanField(default=False)
    
    class Meta: 
        verbose_name_plural = 'arts'

    def save(self, *args, **kwargs):
        if self.main:
            Art.objects.filter(main=True).update(main=False)
        super(Art, self).save(*args, **kwargs)
          
    def __str__(self):
        return self.title


class Comment(models.Model):
    name = models.CharField(max_length=50)
    date_added = models.DateTimeField(auto_now_add=True)
    commentary = models.TextField(max_length=4000)

    def __str__(self):
        return self.name
    