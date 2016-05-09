from django.contrib.auth.middleware import RemoteUserMiddleware
from Cookie import SimpleCookie, Morsel
import copy



class WikilegisRemoteUser(RemoteUserMiddleware):
    header = "HTTP_AUTH_USER"
