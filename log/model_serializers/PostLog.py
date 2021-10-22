from log.models.PostLog import PostLog
from rest_framework import serializers



class PostLogSerializer(serializers.ModelSerializer):

    class Meta:

        model = PostLog
        fields = '__all__'
        extra_fields = ['labels',
                        'tags',
                        'files']

    def create(self, validated_data):

        return PostLog.objects.create(**validated_data)

