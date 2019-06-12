from rest_framework_jwt.serializers import JSONWebTokenSerializer

from django.contrib.auth import authenticate, get_user_model
from django.utils.translation import ugettext as _
from rest_framework import serializers

from rest_framework_jwt.settings import api_settings


User = get_user_model()
jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
jwt_decode_handler = api_settings.JWT_DECODE_HANDLER
jwt_get_username_from_payload = api_settings.JWT_PAYLOAD_GET_USERNAME_HANDLER


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', )


class CustomJWTSerializer(JSONWebTokenSerializer):
    username_field = 'username'

    def validate(self, attrs):

        password = attrs.get("password")
        user_obj = User.objects.filter(username=attrs.get("username"))
        if len(user_obj) > 0:
            user_obj = user_obj.first()
        else:
            msg = 'Wrong credentials!.'
            raise serializers.ValidationError(msg)

        if user_obj is not None:
            credentials = {
                'username':user_obj.username,
                'password': password
            }
            if all(credentials.values()):
                if user_obj.password != password:
                    user = None
                else:
                    user = user_obj


                if not user:
                    msg = 'Wrong credentials!.'
                    raise serializers.ValidationError(msg)
                else:
                    payload = jwt_payload_handler(user)

                    return {
                        'token': jwt_encode_handler(payload),
                        'user': user
                    }

