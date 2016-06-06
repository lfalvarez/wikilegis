from django.contrib.auth.middleware import RemoteUserMiddleware
import json


class WikilegisRemoteUser(RemoteUserMiddleware):
    header = "HTTP_AUTH_USER"

    def process_request(self, request):
        super(WikilegisRemoteUser, self).process_request(request)
        if request.user.is_authenticated():
            user = request.user
            user_data = json.loads(request.META.get('HTTP_REMOTE_USER_DATA'))
            user.email = user_data['email']
            user.first_name = user_data['name']
