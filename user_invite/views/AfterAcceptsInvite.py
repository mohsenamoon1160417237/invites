from user_invite.views.utils.Imports import *
from user_invite.views.utils.get_or_create_notification import get_or_create_notification




class AfterAcceptsInvite(View):

    def post(self , request , user_id , room_id , invite_method , *args , **kwargs):

        room = KeycloakRealm.objects.raw('SELECT * FROM user_invite_keycloakrealm WHERE id = %s' , 
                                      [room_id])[0]

        user = KeycloakUserEntity.objects.raw('SELECT * FROM user_invite_keycloakuserentity WHERE id = %s' , 
                                              [user_id])[0]


        user.realms.add(room)
        user.save()

        invite = UserInvite.objects.raw('SELECT * FROM user_invite_userinvite'
                                        ' WHERE user_id = %s AND room_id = %s' , 
                                         [user_id , room_id])[0]
        invite.accepted_invite = True
        invite.save()
    
        cursor = connections['default'].cursor()
        cursor.execute('INSERT INTO user_invite_userjoinroom'
                       '(user_id , date_time_joined , invite_method , room_id)'
                       'VALUES (%s , %s , %s , %s)' , 
                       [user_id , datetime.now() , invite_method , room_id])
        
        
        get_or_create_notification(user ,
                                   room ,
                                   invite ,
                                   invite_method ,
                                   'joint')
        

        return redirect('home' , user_id=user_id , room_id=room_id)
