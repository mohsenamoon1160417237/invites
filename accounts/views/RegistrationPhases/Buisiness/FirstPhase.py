from accounts.views.utils.Imports import *


class FirstPhaseB(BaseUserSerializer):

    def post(self , request):

        last_url_name = None
        last_url = request.META.get('HTTP_REFERER')
        if last_url is not None:
            last_url_name = resolve(last_url).url_name

        first_phase_serialized = self.serializer_class(data=request.data)
        user_id = None
        response = Response()

        if first_phase_serialized.is_valid(raise_exception=True):

            email = first_phase_serialized.initial_data['email']

            try:

                first_phase = User.objects.get(user_type=User.BUISINESSMAN,
                                               email=email,
                                               step=User.STEP_ONE)
                user_id = first_phase.id

                try:

                    second_phase = User.objects.get(email=email,
                                                    user_type=User.BUISINESSMAN,
                                                    step=User.STEP_TWO)

                    second_phase_serialize = self.serializer_class(instance=second_phase)

                    response.data = second_phase_serialize.data
                    response.data['id'] = user_id
                    response.data['last_url_name'] = last_url_name
                    response.data['help'] = 'redirect to third_phase_b'
                    response.status_code = status.HTTP_201_CREATED
                    return response

                except User.DoesNotExist:

                    response.data = first_phase_serialized.data
                    response.data['id'] = user_id
                    response.data['last_url_name'] = last_url_name
                    response.data['help'] = 'redirect to second_phase_b'
                    response.status_code = status.HTTP_201_CREATED
                    return response

            except User.DoesNotExist:

                first_phase = first_phase_serialized.save(user_type=User.BUISINESSMAN,
                                                          step=User.STEP_ONE)
                first_phase_id = first_phase.id

            response.data = first_phase_serialized.data
            response.data['id'] = first_phase_id
            response.data['last_url_name'] = last_url_name
            response.data['help'] = 'redirect to second_phase_b'
            response.status_code = status.HTTP_201_CREATED
            return response

        else:

            return Response(first_phase_serialized.errors,
                            status=status.HTTP_400_BAD_REQUEST)



