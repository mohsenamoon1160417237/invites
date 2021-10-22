from rest_framework import serializers
from log.models.FileUpload import FileUpload


class FileUploadSerializer(serializers.ModelSerializer):

    file = serializers.FileField(max_length=None,
                                 allow_empty_file=True,
                                 use_url=True)
    class Meta:

        model = FileUpload
        exclude = ['url']

    def create(self, validated_data):

        return FileUpload.objects.create(**validated_data)