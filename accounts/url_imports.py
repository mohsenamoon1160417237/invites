from django.urls import path

#customer views registration
from accounts.views.RegistrationPhases.Customer.FirstPhase import FirstPhaseC
from accounts.views.RegistrationPhases.Customer.SecondPhase import SecondPhaseC

#Buisiness man views registration
from accounts.views.RegistrationPhases.Buisiness.FirstPhase import FirstPhaseB
from accounts.views.RegistrationPhases.Buisiness.SecondPhase import SecondPhaseB
from accounts.views.RegistrationPhases.Buisiness.ThirdPhase import ThirdPhaseB

#Authentication views
from accounts.views.Authentication.Login import LoginView
from accounts.views.Authentication.Logout import Logout

#Home view
from accounts.views.Home import Home