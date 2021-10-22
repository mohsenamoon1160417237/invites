from user_invite.views.utils.Imports import *
from user_invite.views.utils.get_or_create_notification import get_or_create_notification



class AcceptOrRejectBtns(View):

    def get(self , request , user_id , room_id , invite_method , *args , **kwargs):

        user = KeycloakUserEntity.objects.raw('SELECT * FROM user_invite_keycloakuserentity'
                                              ' WHERE id = %s' , 
                                              [user_id])[0]

        room = get_object_or_404(KeycloakRealm , 
                                 id=room_id)


        invite = UserInvite.objects.raw('SELECT * FROM user_invite_userinvite'
                                        ' WHERE user_id = %s AND room_id = %s',
                                        [user_id, room_id])[0]

        invite.url_clicked = True

        invite.save()


        notification = get_or_create_notification(user ,
                                                  room ,
                                                  invite,
                                                  invite_method ,
                                                  'seen')



        return render(request , 'options.html' , {'invite' : invite , 
                                                  'user' : user , 
                                                  'invite_method' : invite_method})