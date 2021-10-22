from django.db import models
from .PostLog import PostLog


class FileUpload(models.Model):

    post = models.ForeignKey(PostLog,
                             on_delete=models.CASCADE,
                             related_name='files')
    file = models.FileField(upload_to='files')
    url = models.URLField(null=True)
    date_uploaded = models.DateTimeField(auto_now_add=True)

    def save(self , *args , **kwargs):

        self.url = self.file.url
        return super(FileUpload,self).save(*args , **kwargs)

