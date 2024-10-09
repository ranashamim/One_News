from django.shortcuts import render
import numpy as np

# Create your views here.
from django.contrib.auth import get_user_model
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView, RetrieveAPIView, ListAPIView, UpdateAPIView

from .serializers import NewsSerializer
from .models import News

#User = get_user_model()

class ShowAllNewsAPIView(ListAPIView):
    serializer_class = NewsSerializer
    queryset = News.objects.all()


class AddNewsAPIView(CreateAPIView):
    serializer_class = NewsSerializer
    queryset = News.objects.all()
    


class ShowFilerTagsAPIView(ListAPIView):
    serializer_class = NewsSerializer
    queryset = News.objects.all() 
    
    name = 'Filtering'
      
    def get_queryset(self):
        
        filter_tag = self.kwargs['tags']
        tags_array = filter_tag.split("-")
        queryset = News.objects.all() 
        qset = [p.tags for p in queryset]
        tags_split = np.array([p.split() for p in qset])

        common_news = []
        for i in range(0,len(tags_split)):
            if(len(np.intersect1d(tags_split[i], tags_array)) > 0):
                common_news.append(i + 1)

        #filter_tags = tags_split.flatten()
        #final_tags = np.unique(filter_tags)
        print('#####################')
        print(common_news)
        print('#####################')



        #return News.objects.filter(tags=filter_tag)
        return News.objects.filter(id__in = common_news)



class ShowFilerTextAPIView(ListAPIView):

    serializer_class = NewsSerializer
    queryset = News.objects.all() 
    
    name = 'Text_Filtering'
      
    def get_queryset(self):
        filter_text = self.kwargs['text']
        text_array = filter_text.split("-")
        queryset = News.objects.all() 
        qset = [p.news_text for p in queryset]

        text_split = []
        for i in range(0, len(qset)):
            text_split.append(np.array(qset[i].split()))


        common_news = []
        for i in range(0,len(text_split)):
             if(len(np.intersect1d(text_split[i], text_array)) > 0):
                common_news.append(i + 1)

        
        return News.objects.filter(id__in = common_news)
