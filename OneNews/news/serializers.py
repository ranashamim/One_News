from rest_framework import serializers
from django.contrib.auth import get_user_model

from .models import News

User = get_user_model()


class NewsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = News
        fields = ['title', 'tags', 'news_text', 'source']
    

    #qset = [p.title for p in queryset]
    
  
    
