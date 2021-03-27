from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

UserModel = get_user_model()

class EmailBackend(object):
    def authenticate(username=None,password=None):
        try:
            user = UserModel.objects.get(email=username)
            if user.check_password(password):
                return user
            else:
                return None
        except UserModel.DoesNotExist:
            raise ValidationError('Invalid Credentials')


    def get_user(self,user_id):
        try:
            return UserModel.objects.get(pk=user_id)
        except UserModel.DoesNotExist:
            return None



