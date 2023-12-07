from rest_framework.views import APIView, Response, Request, status
from users.serializers import UserSerializer
from users.models import User
from django.shortcuts import get_object_or_404
from users.permissions import IsAdminOrUser, IsEmployeeOrReadOnly
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.


class UserView(APIView):
    def post(self, request: Request) -> Response:
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status.HTTP_201_CREATED)


class UserIdView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminOrUser, IsAuthenticated]

    def get(self, request: Request, user_id: int) -> Response:
        User.objects.order_by("id")
        user = get_object_or_404(User, pk=user_id)
        self.check_object_permissions(request, user)

        serializer = UserSerializer(user)

        return Response(serializer.data, status.HTTP_200_OK)

    def patch(self, request: Request, user_id: int) -> Response:
        user = get_object_or_404(User, pk=user_id)
        self.check_object_permissions(request, user)

        serializer = UserSerializer(
            instance=user,
            data=request.data,
            partial=True,
        )

        serializer.is_valid(raise_exception=True)

        serializer.save()

        return Response(serializer.data, status.HTTP_200_OK)


# class LoginView(APIView):
#     def post(self, request: Request) -> Response:
#         serializer = TokenObtainPairSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)

#         return Response(serializer.validated_data, status.HTTP_200_OK)
