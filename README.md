# ozimiz-hackathon
Ozimiz dev Hackathon

## For run this project you will need install _Python 3.10_:
### and run next commands
```
pip install poetry

poetry install

python3 manage.py runserver
```
*In host 127.0.0.1:8000 will be opened site!*

## Routes

```
http://127.0.0.1:8000/  -  homepage
http://127.0.0.1:8000/courses  -  your courses
http://127.0.0.1:8000/courses/{id}  -  concrete course
http://127.0.0.1:8000/courses/{id}/edit  -  edit concrete course
http://127.0.0.1:8000/courses/{id}/complete  -  complete concrete course
```

### To create admin use next command:
```
python3 manage.py createsuperuser
```
