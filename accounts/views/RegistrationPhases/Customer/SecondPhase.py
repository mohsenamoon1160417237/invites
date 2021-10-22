from accounts.views.utils.Imports import *



class SecondPhaseC(BaseUserSerializer):


    def post(self , request , id , url_name):

        user = get_object_or_404(User , id=id)
        password = request.data['password']
        confirm_password = request.data['confirm_password']

        if password != confirm_password:
            raise serializers.ValidationError('Passwords dont match.')

        data = {
            'email' : user.email,
            'first_name': request.data['first_name'],
            'last_name' : request.data['last_name'],
        }

        second_phase_serialized = self.serializer_class(data=data)

        if second_phase_serialized.is_valid(raise_exception=True):

            user.step = User.STEP_TWO
            user.first_name = data['first_name']
            user.last_name = data['last_name']
            user.set_password(password)
            user.save()

            response = login(user)
            token = response[1]
            response = response[0]
            response.data = second_phase_serialized.data
            response.data['id'] = id
            response.data['last_url_name'] = url_name
            response.data['help'] = 'redirect to last_url'
            response.data['jwt'] = token
            response.status_code = status.HTTP_201_CREATED
            return response

        else:

            return Response(second_phase_serialized.errors,
                            status=status.HTTP_400_BAD_REQUEST)