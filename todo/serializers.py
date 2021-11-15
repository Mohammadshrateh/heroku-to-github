# serializers.py
from rest_framework import serializers

from todo.models import Category, Todo, Tag


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = '__all__'

    def create(self, validated_data):
        tags_data = validated_data.pop('tags')
        todo = Todo.objects.update_or_create(**validated_data)
        Tag.objects.update_or_create(todo=todo, **tags_data)
        return todo


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'
