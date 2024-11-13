from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import ValidationError, NotFound, PermissionDenied

from rooms.models import Room
from django.contrib.auth import get_user_model
User = get_user_model()

def catch_exceptions(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except PermissionDenied as e:
            print(e)
            return Response(str(e), status.HTTP_403_FORBIDDEN)
        except (Room.DoesNotExist, NotFound) as e:
            print(e)
            return Response(str(e), status.HTTP_404_NOT_FOUND)
        except ValidationError as e:
            print(e)
            return Response(e.detail, status.HTTP_400_BAD_REQUEST)
        except User.DoesNotExist as e:
            print(e)
            return Response('One or more credentials incorrect', status.HTTP_403_FORBIDDEN)
        except Exception as e:
            print(e)
            print(e.__class__.__name__)
            return Response('An unknown error occurred', status.HTTP_500_INTERNAL_SERVER_ERROR)
    return wrapper