# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-x(awp=uv)c&2_k%wtazknn56sj_l5-oro%mp@9ss+x!p!3+zwq'

DATABASES = {
    'default': {
        'ENGINE': 'mysql.connector.django',
        'NAME': 'youtubeclone',
        'USER': 'root',
        'PASSWORD': 'Programming!@34',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'OPTIONS': {
            'autocommit': True
        }
    }
}