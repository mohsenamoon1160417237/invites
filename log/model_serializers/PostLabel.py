from rest_framework import serializers
from log.models.PostLabel import PostLabel


class PostLabelSerializer(serializers.ModelSerializer):

    class Meta:
        model = PostLabel
        fields = '__all__'

    def create(self, validated_data):

        return PostLabel.objects.create(**validated_data)