from accounts.views.utils.Imports import *



class FirstPhaseC(BaseUserSerializer):

    def post(self , request):

        last_url_name = None
        last_url = request.META.get('HTTP_REFERER')
        if last_url is not None:
            last_url_name = resolve(last_url).url_name

        help_text = None

        #In the first phase the user enters email address

        first_phase_serialized = self.serializer_class(data=request.data)

        if first_phase_serialized.is_valid(raise_exception=True):

            email = first_phase_serialized.initial_data['email']

            try:
                user = User.objects.get(email=email)

                if user.step == User.STEP_ONE:
                    help_text = 'redirect to second_phase_c'
                else:
                    help_text = 'redirect to login'
                    raise serializers.ValidationError('User already exists.Log in to your account.')

            except User.DoesNotExist:
                help_text = 'redirect to second_phase_c'
            user_first_p = first_phase_serialized.save(user_type=User.CUSTOMER,
                                                       step=User.STEP_ONE)

            response = Response()
            response.data = first_phase_serialized.data
            response.data['id'] = user_first_p.id
            response.data['last_url_name'] = last_url_name
            response.data['help'] = help_text
            response.status_code = status.HTTP_201_CREATED
            return response

        else:

            return Response(first_phase_serialized.errors,
                            status=status.HTTP_400_BAD_REQUEST)



