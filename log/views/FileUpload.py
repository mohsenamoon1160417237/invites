import datetime

from log.views.utils.Imports import *


class FileUpload(GenericAPIView):
    
    serializer_class = FileUploadSerializer
    queryset = FileUpload.objects.all()
    
    def post(self , request , post_id=None):

        post_time = datetime.datetime.utcnow()
        if post_id:
            post = get_object_or_404(PostLog , id=post_id)
            post_data = {
                'id'  :post_id,
                'title' : post.title,
                'content' : post.content,
                'status' : post.status,
                'post_time' : datetime.datetime.utcnow()
            }
        else:
            post_data = {
                'user' : request.data['user'],
                'title' : request.data['title'],
                'content' : request.data['content']
            }
            post_data['status'] = 'draft'
            post_data['post_time'] = post_time
            post_serialized = PostLogSerializer(data=post_data)
            if post_serialized.is_valid(raise_exception=True):
                post = post_serialized.save()
                post_data['id'] = post.id

        response = Response()
        response.data = post_data

        file = FileModule(request.data['files'] ,
                          post ,
                          request.data['status'] ,
                          request.data['folder_name'],
                          request.data['user'])

        response.data['files'] = file.doUpload()
        return response
