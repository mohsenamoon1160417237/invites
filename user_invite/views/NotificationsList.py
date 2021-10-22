from .utils.Imports import *



class NotificationsList(generics.GenericAPIView):

    def get(self , request , user_id , *args , **kwargs):

        notifications = Notification.objects.filter(user__id=user_id)

        for notifi in notifications:

            notifi.status = Notification.SEEN
            notifi.save()

        notifications_serialize = NotificationSerializer(notifications,
                                                         many=True,
                                                         context={'request':request})

        return Response(notifications_serialize.data)

