from django.db import models

# Create your models here. Use 'migrate' and 'makemigrations' to build DB

class Tag(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.name

class Person(models.Model):
    name = models.CharField(max_length=255)
    complete_name = models.CharField(max_length=255, blank='', null=True)
    description = models.CharField(max_length=255)
    birth_date = models.DateField()
    position = models.CharField(max_length=255)
    img_url = models.CharField(max_length=255)
    # Relashionship
    persons_tags = models.ManyToManyField(Tag, blank=True)
    
    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.name

class News(models.Model):
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)
    comment = models.TextField(blank=True, null = True)
    source = models.CharField(max_length=255)
    description = models.TextField(blank=True, null = True)
    url = models.CharField(max_length=255)
    date = models.DateField()
    # Relashioships
    persons_news = models.ManyToManyField(Person, blank=True)
    news_tags = models.ManyToManyField(Tag, blank=True)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.title
