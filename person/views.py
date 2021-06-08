from rest_framework import status
from rest_framework import viewsets
from .models import Person, News, Tag
from .serializers import PersonSerializer, NewsSerializer, TagSerializer
from rest_framework.decorators import action
from rest_framework.response import Response

class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

    @action(detail=True, methods=['get'])
    def news(self, request, pk=None):
        avaliacoes = News.objects.filter(persons_news=pk)
        serializer = NewsSerializer(avaliacoes, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['get'])
    def less(self, request, pk=None):
        avaliacoes = News.objects.exclude(persons_news=pk)
        serializer = NewsSerializer(avaliacoes, many=True)
        return Response(serializer.data)

class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer

    @action(detail=True, methods=['post'])
    def removeperson(self, request, pk=None):
        listofnews = request.data
        aperson = Person.objects.get(pk=pk)
        for id_news in listofnews:
            anews = News.objects.get(pk=id_news)
            anews.persons_news.remove(aperson)
        return Response([], status=status.HTTP_200_OK)

    @action(detail=True, methods=['post'])
    def addperson(self, request, pk=None):
        listofnews = request.data
        aperson = Person.objects.get(pk=pk)
        for id_news in listofnews:
            anews = News.objects.get(pk=id_news)
            anews.persons_news.add(aperson)
        return Response([], status=status.HTTP_200_OK)

class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

