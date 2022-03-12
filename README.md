[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

# Django login template

> Describes a simple project template to build basic login & registering functionality using django framework.
> 
> ⚠️ This application is created for the demo references only.

## Tools

### Production

- python 3.7+
- [sqlite3](https://www.sqlite.org/index.html) database
- [django](https://www.djangoproject.com/) framework
- html & css

### Development

- [black](https://black.readthedocs.io/en/stable/) code formatter

## Usage

Please check deployed app at [http://djangobasics.pythonanywhere.com](http://djangobasics.pythonanywhere.com) web site.

### Quick start

```
git clone git@github.com:vyahello/django-login-template.git
cd django-login-template
pip install -r requirements.txt
python app/manage.py runserver
```

Then please open `http://127.0.0.1:8000` endpoint in the browser.

## Deployment

[PythonAnywhere](https://www.pythonanywhere.com) platform is used for deployment.

- Open https://www.pythonanywhere.com
- Go to bash console
- Execute `mkvirtualenv --python=python3.7 dj`
  ```bash
  mkvirtualenv --python=python3.7 dj
  git clone https://github.com/vyahello/django-login-template.git
  cd django-login-template
  pip install -r requirements.txt
  python app/manage.py migrate
  python app/manage.py makemigrations app
  python app/manage.py createsuperuser
  ```
- Go to dashboard -> web -> add new app 
- Go to manual configuration 
- Configure `Virtualenv` -> `/home/djangoBasics/.virtualenvs/dj`
- Configure `Source code` -> `/home/djangoBasics/django-template/app`
- Edit wsgi file as described in [wsgi.py](wsgi.py)
- Add 'djangoBasics.pythonanywhere.com' to `ALLOWED_HOSTS` in [settings.py](app/server/settings.py) and set DEBUG = True 
- Add '/static/admin' and '/home/djangoBasics/.virtualenvs/dj/lib/python3.7/site-packages/django/contrib/admin/static/admin' dir to Static files section
- Add '/static' and '/home/djangoBasics/django-template/app/static' dir to Static files section

## Development notes

### Startup 

Please follow the next instructions to create fresh app:
```bash
django-admin startproject project_name
cd project_name 
django-admin startapp project_app
python app/manage.py createsuperuser
```

### DB migration

DB migration is performed in case of table changes (e.g new field or column added):

Please follow the next instructions to migrate DB:
```bash
python manage.py migrate
python manage.py makemigrations app
python manage.py migrate  # (one more time)
```

### Meta

Author – _Volodymyr Yahello_. 

Distributed under the `MIT` license. See [LICENSE](LICENSE.md) for more information.

You can reach out me at:
* [vyahello@gmail.com](vyahello@gmail.com)
* [https://twitter.com/vyahello](https://twitter.com/vyahello)
* [https://www.linkedin.com/in/volodymyr-yahello-821746127](https://www.linkedin.com/in/volodymyr-yahello-821746127)

### Contributing
If you are interested to add your ideas into project please follow next simple steps:

1. Clone the repository
2. Configure `git` for the first time after cloning with your `name` and `email`
3. `pip install -r requirements.txt` to install all project dependencies
4. `pip install -r requirements-dev.txt` to install all project dev dependencies
5. Create your feature branch (`git checkout -b feature/fooBar`)
6. Commit your changes (`git commit -am 'Add some fooBar'`)
7. Push to the branch (`git push origin feature/fooBar`)
8. Create a new Pull Request
