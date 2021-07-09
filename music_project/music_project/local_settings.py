
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '1u9u)hzx0jd%i)1bbetsibec0bgilif3*+_1$46q0=@=ca75p&'

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'mysql.connector.django',
        'NAME': 'music_library_database',
        'USER': 'root',
        'PASSWORD': '2017Wrangler',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'OPTIONS': {
            'autocommit': True
        }
    }
}
