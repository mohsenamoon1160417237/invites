from .url_imports import *



urlpatterns = [

    path('post/<int:post_id>/' , Post.as_view() , name='edit_post'),
    path('upload_files/' , FileUpload.as_view() , name='upload_files_new_post'),
    path('upload_files/<int:post_id>/' , FileUpload.as_view() , name='upload_files_edit_post'),
]