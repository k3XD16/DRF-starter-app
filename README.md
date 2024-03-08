# Django REST Framework - QuickStart 

![image](https://github.com/k3XD16/DRF-starter-app/assets/47003551/842c822a-10da-4974-abed-9146b5c0e010)


## Installation and setup instructions for Django and the Django REST Framework (DRF):

### Prerequisites


- **Python:** Python 3.7 or newer is recommended. Check if you have it installed by running `python --version` in your terminal. If not, download the appropriate installer from https://www.python.org/downloads/

- **pip:** The package installer for Python. Usually comes bundled with Python. Verify with `pip --version.`


## Steps

### Create a Virtual Environment (Highly Recommended):

Why? Isolates your project's dependencies from other Python projects, avoiding conflicts.

**How:**

```
Linux/macOS: python3 -m venv .venv
Windows: python -m venv .venv
```

**Activate:**

```
Linux/macOS:  source env/bin/activate
Windows:  .venv\Scripts\activate
```

Install Django:

- Inside your activated environment, use pip: `pip install django`

**Start a Django Project:**

- Navigate to where you want your project: cd myprojectdir
- Create a project: `django-admin startproject drf_project`
  
### Install Django REST Framework:

- Inside the same environment: `pip install djangorestframework`

Add DRF to Your Django Project:

Open `drf_project/settings.py`
Find **INSTALLED_APPS** and add: ` 'rest_framework' `


```
INSTALLED_APPS = [
  'django.contrib.admin',
  'django.contrib.auth',
  'django.contrib.contenttypes',
  'django.contrib.sessions',
  'django.contrib.messages',
  'django.contrib.staticfiles',
  'rest_framework',
]
```

## Example Usage

Create a views: (in `drf_project/models.py`)

```
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

class TestView(APIView) :
    def get(self, request, *args, **kwargs) :
        data = {
            'brand': 'Samsung' ,
            'model': 'S23 FE',
            'price': 54999
        }
        return Response(data)
```

Map URL to View (in `drf_project/urls.py`)

```
from django.contrib import admin
from django.urls import path
from .views import TestView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('' , TestView.as_view() , name='test'),
]
```

## Run the Development Server:


`python manage.py runserver`

Now you can access your API at `http://127.0.0.1:8000/`

![image](https://github.com/k3XD16/DRF-starter-app/assets/47003551/1d6f98a6-ebcc-4fec-b842-5f72e186ee07)


Select the `json` to view as a JSON Format

![image](https://github.com/k3XD16/DRF-starter-app/assets/47003551/be10aa92-5419-48d5-8ed1-36f4a939278a)

![image](https://github.com/k3XD16/DRF-starter-app/assets/47003551/3112bcd8-8974-4373-9aac-e834027d2411)


### Remember:

- Virtual environments keep your project's dependencies organized.
- DRF provides powerful tools for building APIs.
- This is a basic example. The Django REST Framework offers extensive features for customization as your API grows more complex.


### For more, refer to the excellent official documentation:

-  [Django](https://www.djangoproject.com/)

-  [Django REST Framework](https://www.django-rest-framework.org/)



## Happy CODING! 🥳
