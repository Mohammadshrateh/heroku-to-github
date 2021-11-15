# serializers.py
from rest_framework import serializers
from rest_framework.authtoken.admin import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class UserSerializer(serializers.ModelSerializer):
    # password2 = serializers.CharField(max_length=200)

    class Meta:
        model = User
        fields = ['email', 'username', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def save(self, **kwargs):
        user = User()
        user.email = self.validated_data['email']
        user.username = self.validated_data['username']
        user.set_password(self.validated_data['password'])
        user.save()


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super(MyTokenObtainPairSerializer, cls).get_token(user)

        # Add custom claims
        token['username'] = user.username
        return token