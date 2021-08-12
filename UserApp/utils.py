from django.contrib.auth.tokens import PasswordResetTokenGenerator
from six import text_type

class AppTokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, form, timestamp):
        return (text_type(form.email_verified) + text_type(form.pk) + text_type(timestamp) )

token_generator = AppTokenGenerator()