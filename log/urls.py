from .url_imports import *



urlpatterns = [

    path('post/' , Post.as_view() , name='new_post'),
    path('post/<int:post_id>/' , Post.as_view() , name='edit_post'),
]