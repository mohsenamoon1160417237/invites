from accounts.views.utils.Imports import *



class Home(GenericAPIView):

    #authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self , request):

        response = Response()
        response.data = {
            'message' : 'success'
        }
        return response
