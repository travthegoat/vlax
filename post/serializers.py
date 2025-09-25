from rest_framework import serializers

from post.models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'caption', 'image', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']