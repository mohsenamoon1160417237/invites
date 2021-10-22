from django.db import models
from .KeycloakUserEntity import KeycloakUserEntity



class KeycloakRealm(models.Model):

    id = models.CharField(primary_key=True,
                          max_length=36)

    access_code_lifespan = models.IntegerField(blank=True,
                                               null=True)

    user_action_lifespan = models.IntegerField(blank=True, 
                                               null=True)

    access_token_lifespan = models.IntegerField(blank=True, 
                                                null=True)

    account_theme = models.CharField(max_length=255, 
                                     blank=True, 
                                     null=True)

    admin_theme = models.CharField(max_length=255, 
                                   blank=True, 
                                   null=True)

    email_theme = models.CharField(max_length=255, 
                                   blank=True, 
                                   null=True)

    enabled = models.BooleanField()
    events_enabled = models.BooleanField()
    events_expiration = models.BigIntegerField(blank=True, 
                                               null=True)

    login_theme = models.CharField(max_length=255, 
                                   blank=True, 
                                   null=True)

    name = models.CharField(unique=True, 
                            max_length=255, 
                            blank=True, 
                            null=True)

    not_before = models.IntegerField(blank=True, 
                                     null=True)

    password_policy = models.CharField(max_length=2550, 
                                       blank=True, 
                                       null=True)

    registration_allowed = models.BooleanField()
    remember_me = models.BooleanField()
    reset_password_allowed = models.BooleanField()
    social = models.BooleanField()
    ssl_required = models.CharField(max_length=255, 
                                    blank=True, 
                                    null=True)

    sso_idle_timeout = models.IntegerField(blank=True, 
                                           null=True)

    sso_max_lifespan = models.IntegerField(blank=True, 
                                           null=True)

    update_profile_on_soc_login = models.BooleanField()
    verify_email = models.BooleanField()
    master_admin_client = models.CharField(max_length=36, 
                                           blank=True, 
                                           null=True)

    login_lifespan = models.IntegerField(blank=True, 
                                         null=True)

    internationalization_enabled = models.BooleanField()
    default_locale = models.CharField(max_length=255, 
                                      blank=True, 
                                      null=True)

    reg_email_as_username = models.BooleanField()
    admin_events_enabled = models.BooleanField()
    admin_events_details_enabled = models.BooleanField()
    edit_username_allowed = models.BooleanField()
    otp_policy_counter = models.IntegerField(blank=True, 
                                             null=True)

    otp_policy_window = models.IntegerField(blank=True, 
                                            null=True)

    otp_policy_period = models.IntegerField(blank=True, 
                                            null=True)

    otp_policy_digits = models.IntegerField(blank=True, 
                                            null=True)

    otp_policy_alg = models.CharField(max_length=36, 
                                      blank=True, 
                                      null=True)

    otp_policy_type = models.CharField(max_length=36, 
                                       blank=True, 
                                       null=True)

    browser_flow = models.CharField(max_length=36, 
                                    blank=True, 
                                    null=True)

    registration_flow = models.CharField(max_length=36, 
                                         blank=True, 
                                         null=True)

    direct_grant_flow = models.CharField(max_length=36, 
                                         blank=True, 
                                         null=True)

    reset_credentials_flow = models.CharField(max_length=36, 
                                              blank=True, 
                                              null=True)

    client_auth_flow = models.CharField(max_length=36, 
                                        blank=True, 
                                        null=True)

    offline_session_idle_timeout = models.IntegerField(blank=True, 
                                                       null=True)

    revoke_refresh_token = models.BooleanField()
    access_token_life_implicit = models.IntegerField(blank=True, 
                                                     null=True)

    login_with_email_allowed = models.BooleanField()
    duplicate_emails_allowed = models.BooleanField()
    docker_auth_flow = models.CharField(max_length=36, 
                                        blank=True, 
                                        null=True)

    refresh_token_max_reuse = models.IntegerField(blank=True, 
                                                  null=True)

    allow_user_managed_access = models.BooleanField()
    sso_max_lifespan_remember_me = models.IntegerField()
    sso_idle_timeout_remember_me = models.IntegerField()
    users = models.ManyToManyField(KeycloakUserEntity , 
                                   blank=True , 
                                   related_name='realms')
