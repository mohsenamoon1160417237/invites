from log.model_serializers.FileUpload import FileUploadSerializer
from django.core.files.storage import FileSystemStorage


class FileModule:

    def __init__(self , file_s , post , status , folder_name , user_id):

        self.status = status
        self.folder_name = folder_name
        self.file_s = file_s
        self.post = post
        self.user_id = user_id

    def saveFile(self , file):

        file_data = {
            'file': file,
            'post': self.post.id
        }

        file_serialized = FileUploadSerializer(data=file_data)
        if file_serialized.is_valid(raise_exception=True):
            new_file = file_serialized.save()
            fs = FileSystemStorage(location='files/user_{}/{}'.format(self.user_id,
                                                                      self.folder_name))
            name = fs.save(file.name, file)
            new_file.url = fs.url(name)
            new_file.post = self.post
            new_file.save()

            file_data['url'] = new_file.url
            file_data.pop('file')
            return file_data

    def doUpload(self):

        if self.status == 'single':

            return self.saveFile(self.file_s)

        elif self.status == 'multi':

            files_data = []
            for file in self.file_s:
                files_data.append(self.saveFile(file))

            return files_data


