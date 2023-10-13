from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions

class UserAction(APIView):
  permission_classes = [permissions.IsAuthenticated]

  # logout the user
  def post(self, request, *args, **kwargs):
    request.user.auth_token.delete()

    return Response(
      {
        "Message": "Your are logged out",
      },
      status = status.HTTP_200_OK
    )