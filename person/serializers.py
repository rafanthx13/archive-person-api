from rest_framework import serializers
from .models import Person, News, Tag
# Necessario para fazer POST/UPDATE em nested ManyToMany
from drf_writable_nested.serializers import WritableNestedModelSerializer

class TagSerializer(serializers.ModelSerializer):   

    class Meta:
        model = Tag
        fields = (
            'id',
            'name',
        )

class PersonSerializer(WritableNestedModelSerializer):

    persons_tags = TagSerializer(many=True)

    class Meta:
        model = Person
        fields = (
            'id',
            'name',
            'complete_name',
            'description',
            'birth_date',
            'position',
            'img_url',
            'persons_tags',
        )
        extra_kwargs = {'persons_tags': {'required': False}}

class NewsSerializer(WritableNestedModelSerializer):

    persons_news = PersonSerializer(many=True)
    news_tags = TagSerializer(many=True)

    class Meta:
        model = News
        fields = (
            'id',
            'title',
            'subtitle',
            'comment',
            'description',
            'url',
            'source',
            'date',
            'persons_news',
            'news_tags',
        )

        extra_kwargs = {'persons_news': {'required': False},
        'news_tags': {'required': False}
        }    
