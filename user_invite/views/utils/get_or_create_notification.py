from .Imports import *
from django.contrib.contenttypes.models import ContentType


def get_or_create_notification(user , room , target , invite_method , notification_type):

    try:

        target_ct = ContentType.objects.get_for_model(target)

        notification = Notification.objects.get(user=user,
                                                room=room,
                                                notification_type=notification_type,
                                                target_ct=target_ct,
                                                target_id=target.id)

        notification.date_time = datetime.now()
        notification.status = Notification.NOT_SEEN
        notification.save()

        return notification

    except Notification.DoesNotExist:

        title = None
        body = None

        try:

            target_type = ContentType.objects.get(app_label='user_invite',
                                                  model='userinvite')



            if notification_type == 'sent':

                title = 'Invite sent'
                body = 'Invite sent for {} to join room {} by {}'.format(user.email ,
                                                                         room.id ,
                                                                         invite_method)

            elif notification_type == 'seen':

                title = 'Invite seen'
                body = 'Invite to join room {} seen by {}. {} has clicked on the invite url.If {} clicks on accept or reject button you will get the related notification'.format(room.id,
                                                                                                                                                                                  user.email,
                                                                                                                                                                                  user.email,
                                                                                                                                                                                  user.email)
            elif notification_type == 'joint':

                title = '{} joint room {}'.format(user.email ,
                                                  room.id)
                body = title

            else:

                title = '{} rejected join room {}'.format(user.email ,
                                                          room.id)
                body = title

            notification = Notification.objects.create(user=user,
                                                       room=room,
                                                       invite_method=invite_method,
                                                       target=target,
                                                       notification_type=notification_type,
                                                       status=Notification.NOT_SEEN,
                                                       title=title,
                                                       body=body)

            return notification

        except ContentType.DoesNotExist:

            pass



