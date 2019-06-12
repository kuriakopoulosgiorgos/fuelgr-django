from collections import OrderedDict

from django.contrib.auth.hashers import BasePasswordHasher

from accounts.models import User


class PlainTextPassword():
    algorithm = "plain"

    def salt(self):
        return ''

    def encode(self, password, salt):
        assert salt == ''
        return password

    def authenticate(self, username, password):
        try:
            user = User.objects.get(username=username)

            if user.password == password:
                return user

        except User.DoesNotExist:
            return None

    def verify(self, password, encoded):
        return password == encoded

    def safe_summary(self, encoded):
        return OrderedDict([
            (('algorithm'), self.algorithm),
            (('hash'), encoded),
        ])