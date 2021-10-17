### TORANG BIAS-JEMBATAN DEVELOPER INDONESIA, DIBANGUN MENGGUNAKAN DJANGO V3.2


<a href="https://github.com/gurnitha/django-torang-bisa" target="_blank">Github repositori</a>


### 1. INISIAL COMMIT
### -------------------------------------------------


#### 1.1 Membuat remote repositori di Gihub, README.md dan .gitignore file

        new file:   .gitignore
        new file:   README.md

<a href="https://github.com/gurnitha/django-torang-bisa/commits/main" target="_blank">Github repositori</a>


### 2. INISIAL SETUP
### -------------------------------------------------


#### 2.1 Membuat Django proyek

        > λ django-admin startproject core .

        modified:   README.md
        new file:   core/__init__.py
        new file:   core/asgi.py
        new file:   core/settings.py
        new file:   core/urls.py
        new file:   core/wsgi.py
        new file:   manage.py

<a href="https://github.com/gurnitha/django-torang-bisa/commits/main" target="_blank" rel="noopener noreferrer">Github repositori</a>


### 3. MYSQL DATABASE
### -------------------------------------------------


### 3.1 Membuat and menseting database

        Steps:
        1. Menginstall django-environ
        2. Inisiasi environ pada settings.py 
        3. Membuat .env file di dalam proyek (core), seperti di bawah ini:
                SECRET_KEY=
                DATABASE_NAME=
                DATABASE_USER=
                DATABASE_PASSWORD=
        4. Mencantumkan environment variables pada .env seperti di bawah ini:
                SECRET_KEY=abc-secret-key-imagiantif
                DATABASE_NAME=nama_database
                DATABASE_USER=nama_database_user
                DATABASE_PASSWORD=password
        5. Tambahkan secret_key pada settings.py seperti tibawah ini:
                SECRET_KEY = env('SECRET_KEY');
        6. Non-aktifkan default database (sqlite) pada settings.py seperti tibawah ini:
                # DATABASES = {
                #     'default': {
                #         'ENGINE': 'django.db.backends.sqlite3',
                #         'NAME': BASE_DIR / 'db.sqlite3',
                #     }
                # }

        7. Tambahkan referensi database baru pada settings.py seperti tibawah ini:
                DATABASES = {
                    'default': {
                        'ENGINE': 'django.db.backends.mysql',
                        'NAME': env('DATABASE_NAME'),
                        'USER': env('DATABASE_USER'),
                        'PASSWORD': env('DATABASE_PASSWORD'),
                        'HOST': 'localhost',
                        'PORT': 3306
                    }
                }
        8. Menguji koneksi proyek dan database

        > λ python manage.py check
        System check identified no issues (0 silenced).
        > λ python manage.py runserver
        ...
        Starting development server at http://127.0.0.1:8000/

        modified:   README.md
        modified:   core/settings.py
























































































































































































































































































