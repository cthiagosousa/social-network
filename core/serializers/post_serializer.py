from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from ..models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'description', 'image', 'author', 'created_at', 'updated_at']

    def update(self, instance: Post, validated_data: dict) -> Post:
        self.instance.title = self.validated_data['title']
        self.instance.description = self.validated_data['description']
        self.instance.image = self.validated_data['image']
        author = self.validated_data['author']

        if self.instance.author != author:
            raise ValidationError({'error': 'Você não pode alterar o autor da postagem.'})
        
        self.instance.author = author
        self.instance.save()
        
        return self.instance
