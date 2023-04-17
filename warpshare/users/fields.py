from rest_framework import fields

class UsernameField(fields.CharField):
    
    default_error_messages = {
        'invalid': 'Enter a valid string.',
        'max_length': 'Ensure username has no more than {max_length} characters.',
        'min_length': 'Ensure username has at least {min_length} characters.',
    }

class PasswordField(fields.CharField):

    default_error_messages = {
        'invalid': 'Enter a valid string.',
        'max_length': 'Ensure password has no more than {max_length} characters.',
        'min_length': 'Ensure password has at least {min_length} characters.',
    }