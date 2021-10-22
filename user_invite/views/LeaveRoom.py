from user_invite.views.utils.Imports import *



class LeaveRoom(View):

    def post(self , request , user_id , room_id , *args , **kwargs):


        realm = KeycloakRealm.objects.raw('SELECT * FROM user_invite_keycloakrealm WHERE id = %s' , 
                                      [room_id])[0]

        user = KeycloakUserEntity.objects.raw('SELECT * FROM user_invite_keycloakuserentity WHERE id = %s' , 
                                              [user_id])[0]

        user.realms.remove(realm)

        user.save()

        invite = UserInvite.objects.raw('SELECT * FROM user_invite_userinvite'
                                        ' WHERE user_id = %s AND room_id = %s' , 
                                        [user_id , room_id])[0]
        invite.accepted_invite = False

        cursor = connections['default'].cursor()
        cursor.execute('UPDATE user_invite_userjoinroom SET date_time_left = %s'
                       ' WHERE user_id = %s AND room_id = %s' , 
                       [datetime.now() , user_id , room_id])
    
        invite.save()
