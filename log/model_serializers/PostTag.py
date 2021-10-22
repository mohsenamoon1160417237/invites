from rest_framework import serializers
from log.models.PostTag import PostTag


class PostTagSerializer(serializers.ModelSerializer):

    class Meta:

        model = PostTag
        exclude = ['posts']

    def create(self, validated_data):

        return PostTag.objects.create(**validated_data)
