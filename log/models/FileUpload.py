from django.db import models
from .PostLog import PostLog
from log.views.utils.file_upload_path import file_upload_path


class FileUpload(models.Model):

    post = models.ForeignKey(PostLog,
                             on_delete=models.CASCADE,
                             related_name='files')
    file = models.FileField(upload_to=file_upload_path)
    url = models.URLField(null=True)
    date_uploaded = models.DateTimeField(auto_now_add=True)
