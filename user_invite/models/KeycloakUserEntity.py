from django.db import models




class KeycloakUserEntity(models.Model):

    id = models.CharField(primary_key=True, 
                          max_length=36)

    email = models.CharField(max_length=255, 
                             blank=True, 
                             null=True)

    email_constraint = models.CharField(max_length=255, 
                                        blank=True, 
                                        null=True)

    email_verified = models.BooleanField()
    enabled = models.BooleanField()
    federation_link = models.CharField(max_length=255, 
                                       blank=True, 
                                       null=True)

    first_name = models.CharField(max_length=255, 
                                  blank=True, 
                                  null=True)
                                  
    last_name = models.CharField(max_length=255, 
                                 blank=True, 
                                 null=True)

    realm_id = models.CharField(max_length=255,
                                blank=True, 
                                null=True)

    username = models.CharField(max_length=255, 
                                blank=True, 
                                null=True)

    created_timestamp = models.BigIntegerField(blank=True,
                                               null=True)

    service_account_client_link = models.CharField(max_length=255, 
                                                   blank=True, 
                                                   null=True)
                                                   
    not_before = models.IntegerField()
    phone_number = models.CharField(max_length=10 ,
                                    unique=True)