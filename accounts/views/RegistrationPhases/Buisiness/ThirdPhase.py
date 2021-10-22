from accounts.views.utils.Imports import *


class ThirdPhaseB(BaseUserSerializer):

    def post(self , request , id , url_name):

        user = get_object_or_404(User , id=id)
        data = {
            'email' : user.email,
            'first_name' : user.first_name,
            'last_name' : user.last_name,
            'company_name' : request.data['company_name']
        }
        third_phase_serialize = self.serializer_class(data=data)

        if third_phase_serialize.is_valid(raise_exception=True):

            user.step = User.STEP_THREE
            user.company_name = data['company_name']
            user.save()

            response = login(user)
            token = response[1]
            response = response[0]
            response.data = third_phase_serialize.data
            response.data['id'] = id
            response.data['last_url_name'] = url_name
            response.data['help'] = 'redirect to last_url'
            response.data['jwt'] = token
            response.status_code = status.HTTP_201_CREATED
            return response

        else:

            return Response(third_phase_serialize.errors,
                            status=status.HTTP_400_BAD_REQUEST)
