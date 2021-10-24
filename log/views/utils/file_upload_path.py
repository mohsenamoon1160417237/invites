def file_upload_path(instance , filename):

    return 'files/user_{}/{}'.format(str(instance.post.user.id) , filename)