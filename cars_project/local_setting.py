# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-ijbue9ssg9f$w0d)=)lycv6#q^-trolxe((xg15(f*9$j7=@9)'

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'cars_database',
        'HOST': 'localhost',
        'USER': 'root',
        'PASSWORD': 'Juraquille7!'
    }
}