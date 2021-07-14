# Blogging-site-Django
This is the blogging site made using Django framework . 

## Features :
* Authentication : User can Log in and sign up .
* User can Post their blog using images and varoius fonts .
* Used TinyMCE, the most advanced  HTML editor designed to simplify website content creation.
* User can post comment on others blog.



# To Run this project follow the following instructions :

### **Note** : Python 3.8 is needed to run this project


#### First Clone the project

```
git clone https://github.com/gauravsewatkar/Blogging-site-Django.git
cd Blogging-site-Django
```
#### After running commands as per OS run:
```
cd Blogging-site-Django
python manage.py migrate
python manage.py makemigrations
python manage.py migrate
```

#### Once done with that create a superuser account:
```
python manage.py createsuperuser
```

#### Once superuser account is created we can run the website
```
python manage.py runserver
```

#### If there are no errors website will be running on [http://127.0.0.1:8000/](http://127.0.0.1:8000/) (default)

