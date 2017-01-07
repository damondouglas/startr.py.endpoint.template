# [START imports]
import endpoints
from protorpc import message_types
from protorpc import messages
from protorpc import remote

from secret import secret
# [END imports]


# [START messages]
class __apiclass__Request(messages.Message):
    content = messages.StringField(1)


class __apiclass__Response(messages.Message):
    """A proto Message that contains a simple string field."""
    content = messages.StringField(1)


API_RESOURCE = endpoints.ResourceContainer(
    __apiclass__Request,
    n=messages.IntegerField(2, default=1))
# [END messages]


# [START __apiname___api]
@endpoints.api(name='__apiname__', version='v1')
class __apiclass__Api(remote.Service):

    @endpoints.method(
        # This method takes a ResourceContainer defined above.
        API_RESOURCE,
        # This method returns an __apiclass__ message.
        __apiclass__Response,
        path='__apipath__',
        http_method='POST',
        name='echo')
    def echo(self, request):
        output_content = ' '.join([request.content] * request.n)
        return __apiclass__Response(content=output_content)

    @endpoints.method(
        # This method takes an empty request body.
        message_types.VoidMessage,
        # This method returns an __apiclass__ message.
        __apiclass__Response,
        path='__apipath__/getUserEmail',
        http_method='GET',
        allowed_client_ids = [secret.web_client_id],
        # Require auth tokens to have the following scopes to access this API.
        scopes=[endpoints.EMAIL_SCOPE],
        # OAuth2 audiences allowed in incoming tokens.
        audiences=[secret.web_client_id])

    def get_user_email(self, request):
        user = endpoints.get_current_user()
        # If there's no user defined, the request was unauthenticated, so we
        # raise 401 Unauthorized.
        if not user:
            raise endpoints.UnauthorizedException
        return __apiclass__Response(content=user.email())
# [END __apiname___api]


# [START api_server]
api = endpoints.api_server([__apiclass__Api])
# [END api_server]
