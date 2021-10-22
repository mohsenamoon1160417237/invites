import datetime

from user_invite.views.utils.Imports import *
from user_invite.views.utils.get_or_create_notification import get_or_create_notification
from .MailInviteLink import MailInviteLink
from .SMSInviteLink import SMSInviteLink




class CheckInviteLink(View):

    
    def post(self , request , user_id , room_id , invite_method , *args , **kwargs):

        previous_invite = None
        
        user = get_object_or_404(KeycloakUserEntity , 
                                 id=user_id)

        room = get_object_or_404(KeycloakRealm , 
                                 id=room_id)
    
        try:

            previous_invite = UserInvite.objects.get(user_id=user_id,
                                                     room_id=room_id)

            if previous_invite.url_clicked == False:

                if invite_method == 'email':

                    MailInviteLink.post(request , user_id , room_id , invite_method)
                                                          
                else:

                    SMSInviteLink.get(request , user.phone_number , room_id , invite_method)

                
                get_or_create_notification(user , room , previous_invite , invite_method , 'sent')
        
            else:

                if previous_invite.accepted_invite == False:

                    if invite_method == 'email':

                        MailInviteLink.post(request , user_id , room_id , invite_method)

                    else:

                        SMSInviteLink.get(request , user.phone_number , room_id , invite_method)
                    
                    get_or_create_notification(user , room , previous_invite , invite_method , 'sent')
            

        except UserInvite.DoesNotExist:
            
            user_invite = UserInvite.objects.create(user=user,
                                                    room_id=room_id)
            

            if invite_method == 'email':

                MailInviteLink.post(request , user_id , room_id , invite_method)

            else:

                SMSInviteLink.get(request , user.phone_number , room_id , invite_method)


            get_or_create_notification(user , room , user_invite , invite_method , 'sent')


        return redirect('home' , user_id=user_id , 
                                 room_id=room_id)
