from rest_framework import viewsets
from django.contrib.auth.models import User
from rest_framework.permissions import IsAdminUser
from rest_framework.serializers import ModelSerializer


# Serializer for User
class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

# Viewset for User
# Only GET endpoints
class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    # Only admins can access
    permission_classes = [IsAdminUser]

