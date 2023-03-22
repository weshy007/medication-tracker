from djoser.serializers import UserCreateSerializer, UserSerializer


class CreateUserSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer):
        fields = ['username', 'first_name', 'last_name', 'email', 'password']


class UserProfileSerializer(UserSerializer):
    class Meta(UserSerializer):
        fields = ['id', 'username', 'first_name', 'last_name', 'email']
