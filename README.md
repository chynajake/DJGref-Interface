# Clone Project

git clone https://chynaJake@bitbucket.org/chynaJake/news.git
cd news

# Setup Virtual Enviroment (myvenv - default name, pick one you prefer)

python3 -m venv myvenv

if you have only python 3 type:
    python -m venv myvenv

source myvenv/bin/activate

# Install Django

pip install django~=1.10.0

# Add some libs & tools if you are missing some
# (below are the ones you most probably don't have)

pip install django-material
sudo apt-get install memcached
pip install python-memcached

# Inform your db of changes

python manage.py makemigrations app
python manage.py migrate app

# Finally create superUser and run server

python manage.py createsuperuser
    Username: admin
    Email address: admin@admin.com
    Password:
    Password (again):
python manage.py runserver