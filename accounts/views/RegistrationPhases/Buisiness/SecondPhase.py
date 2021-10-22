from accounts.views.utils.Imports import *


class SecondPhaseB(BaseUserSerializer):

    def post(self , request , id , url_name):

        user = get_object_or_404(User, id=id)
        password = request.data['password']
        confirm_password = request.data['confirm_password']

        if password != confirm_password:
            raise serializers.ValidationError('Passwords dont match')

        data = {
            'email' : user.email,
            'first_name' : request.data['first_name'],
            'last_name' : request.data['last_name'],
        }
        second_phase_serialize = self.serializer_class(data=data)
        user_id = None

        if second_phase_serialize.is_valid(raise_exception=True):

            user.step = User.STEP_TWO
            user.first_name = data['first_name']
            user.last_name = data['last_name']
            user.set_password(password)
            user.save()
            user_id = id

            response = Response()
            response.data = second_phase_serialize.data
            response.data['id'] = user_id
            response.data['last_url_name'] = url_name
            response.data['help'] = 'redirect to third_phase_b'
            response.status_code = status.HTTP_201_CREATED
            return response

        else:

            return Response(second_phase_serialize.errors,
                            status=status.HTTP_400_BAD_REQUEST)


