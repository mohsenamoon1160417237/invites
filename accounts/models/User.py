from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    CUSTOMER = 'c'
    BUISINESSMAN = 'b'

    USER_TYPES = (
        (CUSTOMER , 'customer'),
        (BUISINESSMAN , 'buisiness_man'),
    )

    STEP_ONE = 'one'
    STEP_TWO = 'two'
    STEP_THREE = 'three'

    STEPS = [
        (STEP_ONE , 'one'),
        (STEP_TWO , 'two'),
        (STEP_THREE , 'three')
    ]

    phone_number = models.CharField(max_length=11,
                                    null=True)
    user_type = models.CharField(choices=USER_TYPES,
                                 max_length=15)
    email = models.EmailField()
    first_name = models.CharField(max_length=30,
                                  null=True)
    last_name = models.CharField(max_length=30,
                                 null=True)
    password = models.TextField(null=True)
    step = models.CharField(choices=STEPS,
                            max_length=5,
                            null=True)

    #This field in required only for buisiness man account
    company_name = models.CharField(null=True,
                                    max_length=50)

    username = models.CharField(max_length=20,
                                null=True,
                                unique=True)
    def __str__(self):

        return self.email