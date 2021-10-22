from accounts.views.utils.Imports import *


class LoginView(GenericAPIView):

    def post(self , request):

        last_url_name = None
        last_url = request.META.get('HTTP_REFERER')
        if last_url is not None:
            last_url_name = resolve(last_url).url_name

        email = request.data['email']
        password = request.data['password']

        try:

            user = User.objects.get(email=email)

            if not user.check_password(password):
                raise AuthenticationFailed('Wrong password')

            response = login(user)
            token = response[1]
            response = response[0]
            response.data = {
                'jwt' : token,
                'last_url_name' : last_url_name
            }
            return response

        except User.DoesNotExist:

            raise AuthenticationFailed('user does not exist')