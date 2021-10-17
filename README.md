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

<a href="https://github.com/gurnitha/django-torang-bisa/commit/ba06979cf35628726f0f1feca15a95811755ad05" target="_blank" rel="noopener noreferrer">Github repositori</a>


### 4. DJANGO APP
### -------------------------------------------------


#### 4.1 Membuat django app dengan nama 'proyek'

        Steps:

        1. Membuat folder baru dgn nama 'app'
           > dari terminal: mkdir app
        2. Membuat foder baru di dalam folder app dgn nama 'proyek'
           > dari terminal: mkdir app\proyek
        3. Memembuat django app dgn nama 'proyek'
           > dari terminal: python manage.py startapp app\proyek
        4. Hasilnya spt di bawah ini:

        modified:   README.md
        new file:   app/proyek/__init__.py
        new file:   app/proyek/admin.py
        new file:   app/proyek/apps.py
        new file:   app/proyek/migrations/__init__.py
        new file:   app/proyek/models.py
        new file:   app/proyek/tests.py
        new file:   app/proyek/views.py       

<a href="https://github.com/gurnitha/django-torang-bisa/commit/134ee3940b5dc1375525df4cc318326c4d462c6e" target="_blank" rel="noopener noreferrer">Github repositori</a>


#### 4.2 Mengistal proyek pada settings.py

        modified:   README.md
        modified:   app/proyek/apps.py
        modified:   core/settings.py

<a href="https://github.com/gurnitha/django-torang-bisa/commit/5d99f6cb698d4dc6b2e220f604c50119b4254e0b" target="_blank" rel="noopener noreferrer">Github repositori</a>


### 5. DJANGO MODEL ATAU TABEL
### -------------------------------------------------


#### 5.1 Membuat model dgn nama 'Project' dan menjalankan perintah migrasi

        Steps:
        1. Membuat model
        2. Menjalankan perintah migrasi dari terminal
           > python manage.py makemigrations
           > python manage.py migrate
        3. Memerikasa hasil perintah

        λ python manage.py sqlmigrate proyek 0001
        --
        -- Create model Project
        --
        CREATE TABLE 
        `proyek_project` (
                `title` varchar(200) NOT NULL, 
                `description` longtext NULL, 
                `demo_link` varchar(2000) NULL, 
                `source_link` varchar(2000) NULL, 
                `created` datetime(6) NOT NULL, 
                `id` char(32) NOT NULL PRIMARY KEY
        ); 

        4. Memerikasa hasil perintah dalam format sql        
           > python manage.py dbshell 

        mysql> SHOW tables;
        +------------------------------+
        | Tables_in_django_torang_bisa |
        +------------------------------+
        | auth_group                   |
        | auth_group_permissions       |
        | auth_permission              |
        | auth_user                    |
        | auth_user_groups             |
        | auth_user_user_permissions   |
        | django_admin_log             |
        | django_content_type          |
        | django_migrations            |
        | django_session               |
        | proyek_project               |
        +------------------------------+
        11 rows in set (0.00 sec)

        5. Memerikasa model/tabel Project

        mysql> DESC proyek_project;
        +-------------+---------------+------+-----+---------+-------+
        | Field       | Type          | Null | Key | Default | Extra |
        +-------------+---------------+------+-----+---------+-------+
        | title       | varchar(200)  | NO   |     | NULL    |       |
        | description | longtext      | YES  |     | NULL    |       |
        | demo_link   | varchar(2000) | YES  |     | NULL    |       |
        | source_link | varchar(2000) | YES  |     | NULL    |       |
        | created     | datetime(6)   | NO   |     | NULL    |       |
        | id          | char(32)      | NO   | PRI | NULL    |       |
        +-------------+---------------+------+-----+---------+-------+
        6 rows in set (0.00 sec)        

        modified:   README.md
        new file:   app/proyek/migrations/0001_initial.py
        modified:   app/proyek/models.py

<a href="https://github.com/gurnitha/django-torang-bisa/commit/145523945e2981d089ee2370c82029a223befabf" target="_blank" rel="noopener noreferrer">Github repositori</a>


#### 5.2 Mencatatkan model 'Project' pada admin

        modified:   README.md
        modified:   app/proyek/admin.py




















































































































































































































































































