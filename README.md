# uManage
A user management web application developed using - python3.7, django, html, css, bootstrap, sqlite3.


## Requirements - 
> Python3

> Pip

> virtualenv

## Steps to Run the application

 ```python -m pip install --user virtualenv```

 ```py -m venv env```
 
 Activate the virtual env - 
 - Windows
  ``` .\env\Scripts\activate ``` 
 - Linux
  ``` source env/bin/activate ```
  
  Install requirements from requirements file -
  
  ``` pip install -r requirements.txt ```
  
Create a SuperUser -

``` python manage.py createsuperuser ```

You can run server -

``` python manage.py runserver ```
