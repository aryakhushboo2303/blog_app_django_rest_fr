from rest_framework import serializers
from .models import Blog

class BlogSerializer(serializers.ModelSerializers):
    class Meta:
        model = Blog
        exclude = ['created_at','updated_at']