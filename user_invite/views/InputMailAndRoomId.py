from user_invite.views.utils.Imports import *




class InputMailAndRoomId(View):


    def get(self , request , *args , **kwargs):


        form = UserRoomForm()
        return render(request , 'input_mail_and_room_id.html' , {'form' : form})

    
    def post(self , request , *args , **kwargs):


        form = UserRoomForm(data=request.POST)
        if form.is_valid():

            cd = form.cleaned_data
            user_email = cd['user_email']
            room_id = cd['room_id']
            user = KeycloakUserEntity.objects.raw('SELECT * FROM user_invite_keycloakuserentity'
                                                  ' WHERE email = %s' , 
                                                  [user_email])[0]

            user_id = user.id

        return redirect('home' , user_id=user_id , room_id=room_id)