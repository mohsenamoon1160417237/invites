from accounts.views.utils.Imports import *


class Logout(GenericAPIView):

    def post(self , request):

        response = Response()
        response.delete_cookie('jwt')
        response.data = {
            'message' : 'success'
        }
        return response
