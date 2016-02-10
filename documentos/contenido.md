##Configuración de contenido estático##



Lo recomendable es NO tener los css de bootstrap en el repositorio, por limpieza, evitar posibles problemas y tener archivos innecesarios. 

Lo correcto es usar [CDN](https://www.bootstrapcdn.com) y "linkar" los *css/js* directamente.

A continuación se detallan las 2 formas de habilitar el contenido estático en la aplicación Django:

####FORMA 1 (MÁS CORRECTA):####

- Instalar [*Cling*](https://pypi.python.org/pypi/dj-static) y añadirlo al archivo [requirements.txt](https://github.com/nachobit/DAI_bares/blob/master/requirements.txt):

	```pip install Cling ```
	
	```pip freeze > requirements.txt```
	
		 dj-static==0.0.6


- Editar el archivo [wsgi.py](https://github.com/nachobit/DAI_bares/blob/master/myproject/wsgi.py) y añadir *Cling*:

	```
	from dj_static import Cling

	(...)

	application = Cling(get_wsgi_application())

	```

- En el archivo [settings.py](https://github.com/nachobit/DAI_bares/blob/master/myproject/settings.py) añadir (si no están) las líneas:

	```
	STATIC_ROOT = os.path.join(BASE_DIR,'staticfiles')
	STATIC_ROOT = 'staticfiles'
	STATIC_URL = '/static/'

	STATICFILES_DIRS = (
 	   os.path.join(BASE_DIR, 'static'),
	)

	```

- Modificar el *html* con el contenido web,

	- Añadiendo al principio del documento:

		```{% load staticfiles %}```

	- Cambiar las referencias a contenido estático (css,js...) con el *CDN*:

	```
	<link href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css" rel="stylesheet"
	
	<script type="text/javascript" src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/js/bootstrap.min.js" ></script>
	
	```

####FORMA 2 (MENOS CORRECTA):####

- Instalar **Whitenoise** y añadirlo al archivo [requirements.txt](https://github.com/nachobit/DAI_bares/blob/master/requirements.txt):

	```pip install whitenoise ```
	
	```pip freeze > requirements.txt```


- En el archivo [settings.py]() añadir (si no están) las líneas:

	```
	# Static files (CSS, JavaScript, Images)
	STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'
	STATIC_ROOT = 'staticfiles'
	STATIC_URL = '/static/'
	```

- En el archivo [wsgi.py](https://github.com/nachobit/DAI_bares/blob/master/myproject/wsgi.py) del proyecto añadir las líneas:

	```

	from whitenoise.django import DjangoWhiteNoise

	(...)

	application = DjangoWhiteNoise(application)

	```

- Modificar el *html* con el contenido web añadiendo al principio del documento:

	```{% load staticfiles %}```

	Y cambiar las referencias a contenido estático (css,js...) a la forma:

	```
	<link href="{% static 'css/bootstrap.min.css' %}" rel="stylesheet">
	```

- Finalmente al realizar el despligue de la aplicación en Heroku mediante:

	```git push heroku master```

	la herramienta *collectstatic* de Heroku configurará de forma automática el contenido estático al realizar el push.


*Referencias:*

[Heroku Django](https://devcenter.heroku.com/articles/django-assets)

[Using Whitenoise](http://whitenoise.evans.io/en/latest/django.html)
