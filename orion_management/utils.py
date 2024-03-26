from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from phonenumber_field.phonenumber import to_python
from phonenumber_field.validators import validate_international_phonenumber

# Custom validator for phone number
def validate_phone_number(value):
    phone_number = to_python(value)
    if phone_number and not validate_international_phonenumber(phone_number):
        raise ValidationError("Invalid phone number format")

# Custom validator for email
def validate_email_format(value):
    try:
        validate_email(value)
    except ValidationError:
        raise ValidationError("Invalid email format")
    
class BaseUrlMixin:
    def get_url(self, obj):
        request = self.context.get('request')
        if request is not None:
            return request.build_absolute_uri(obj.get_absolute_url())
        return ''