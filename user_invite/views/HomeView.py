from user_invite.views.utils.Imports import *



class HomeView(View):


    def get(self , request , user_id , room_id , *args , **kwargs):

        user = KeycloakUserEntity.objects.raw('SELECT * FROM user_invite_keycloakuserentity '
                                              'WHERE id = %s' , 
                                               [user_id])[0]

    
        room = KeycloakRealm.objects.raw('SELECT * FROM user_invite_keycloakrealm '
                                         'WHERE id = %s' , 
                                         [room_id])[0]


        return render(request , 'home.html' , {'user' : user,
                                               'room' : room})


    def post(self , request , user_id , room_id , *args , **kwargs):


        user_invite = get_object_or_404(UserInvite,
                                        user__id=user_id,
                                        room_id=room_id)

        user_invite_serialize = UserInviteSerializer(user_invite)

        return JsonResponse(user_invite_serialize.data,
                            safe=False)

