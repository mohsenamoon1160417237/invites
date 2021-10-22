from user_invite.views.utils.Imports import *
from user_invite.views.utils.get_or_create_notification import get_or_create_notification




class AfterRejectsInvite(View):


    def post(self , request , user_id , room_id , invite_method , *args , **kwargs):

        user = get_object_or_404(KeycloakUserEntity ,
                                 id=user_id)
        
        room = get_object_or_404(KeycloakRealm , 
                                 id=room_id)
        
        invite = get_object_or_404(UserInvite,
                                   user=user,
                                   room_id=room_id)

        get_or_create_notification(user ,
                                   room ,
                                   invite ,
                                   invite_method ,
                                   'rejected')

        
        return redirect('home' , user_id=user_id ,
                                 room_id=room_id)