from user_invite.views.utils.Imports import *
from user_invite.model_serializers.UserInvite import UserInviteSerializer
import datetime



class MailInviteLink(View):


    @staticmethod
    def post(request , user_id , room_id , invite_method):

        user = KeycloakUserEntity.objects.raw('SELECT * FROM user_invite_keycloakuserentity'
                                              ' WHERE id = %s' , [user_id])[0]


        invite = get_object_or_404(UserInvite , user__id=user_id,
                                                room_id=room_id)
        

        token = RefreshToken.for_user(user).access_token

        domain = get_current_site(request).domain
    
        relativeLink = reverse('accept_or_reject_btns' , kwargs={'user_id' : user.id ,
                                                                 'room_id' : room_id ,
                                                                 'invite_method' : invite_method})
    
        absurl = 'http://' + domain + relativeLink + "?token=" + str(token)

        subject =  "Invitation to our room"

        from_email = settings.EMAIL_HOST_USER

        recipient_list = [user.email]
        send_mail(subject , absurl , from_email , recipient_list , fail_silently=False)

        invite_serialize = UserInviteSerializer(data=invite)

        if invite_serialize.is_valid():

            return JsonResponse(invite_serialize.data,
                                safe=True)
