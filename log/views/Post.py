from .utils.Imports import *


class Post(GenericAPIView):

    def post(self , request , post_id):

        tags = []
        labels = []
        files = []

        post_time = datetime.datetime.now()
        if request.data['status'] == PostLog.SCHEDULE:
            post_time = request.data['post_time']

        post_data = {
            'user' : request.data['user'],
            'title' : request.data['title'] ,
            'content' : request.data['content'],
            'status' : request.data['status'],
            'post_time' : post_time,
            'tags' : request.data['tags'],
            'labels' : request.data['labels']
        }

        post_serialized = PostLogSerializer(data=post_data)

        if post_serialized.is_valid(raise_exception=True):

            post = get_object_or_404(PostLog , id=post_id)
            post.title = post_data['title']
            post.content = post_data['content']
            post.status = post_data['status']
            post.post_time = post_time
            for file in post.files.all():
                files.append({
                    'post_time' : file.date_uploaded,
                    'url' : file.url
                    })

            if request.data['status'] == PostLog.SCHEDULE:
                post_schedule.apply_async(args=[post.id] ,
                                         eta=post_time)
            else:
                post.save()


            for tag in request.data['tags']:

                tag_data = {
                    'type' : tag['type']
                }

                tag_serialized = PostTagSerializer(data=tag_data)

                if tag_serialized.is_valid(raise_exception=True):

                    tag = tag_serialized.save()
                    tag.posts.add(post)
                    tag.save()
                    tags.append(tag_data)

            for label in request.data['labels']:
                label_data = {
                    'name' : label['name'],
                    'user' : request.data['user_id'],
                    'post' : post.id
                }

                label_serialized = PostLabelSerializer(data=label_data)

                if label_serialized.is_valid(raise_exception=True):
                    label = label_serialized.save()
                    label.save()
                    labels.append(label_data)


            response = Response()
            post_data['id'] = post.id
            post_data['files'] = files
            post_data['tags'] = tags
            post_data['labels'] = labels
            response.data = {
                'post_data' : post_data,
            }

            response.status_code = status.HTTP_201_CREATED
            return response

        else:

            return Response(post_serialized.errors,
                            status=status.HTTP_400_BAD_REQUEST)



