# DAI_Django_tango_rango

[Repositorio Github](https://github.com/nachobit/DAI_bares.git)

[![Build Status](https://snap-ci.com/nachobit/DAI_bares/branch/master/build_image)](https://snap-ci.com/nachobit/DAI_bares/branch/master)

[![Heroku](https://www.herokucdn.com/deploy/button.png)](https://baresdai.herokuapp.com/rango)

###RESUMEN###

Práctica de la asignatura DAI para la creación de una aplicación Django basada en la presentación de los bares y las tapas. La aplicación está desplegada en el PaaS Heroku siguiendo el siguiente [tutorial](http://www.tangowithdjango.com/book17/index.html).

###DESPLIEGUE###

Para el despliegue en Heroku de una aplicación Django se deben realizar los siguientes pasos a fin de mostrar todo el contenido estático de la página de forma correcta, ya que Heroku bloquea este contenido al realizar el despliegue:

- Instalar **Whitenoise** y añadirlo al archivo [requirements.txt](https://github.com/nachobit/DAI_bares/blob/master/requirements.txt):

	```pip install whitenoise ```
	
	```pip freeze > requirements.txt```

- En el archivo [settings.py]() añadir las líneas:

```
# Static files (CSS, JavaScript, Images)
STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'
STATIC_ROOT = 'staticfiles'
STATIC_URL = '/static/'
```

- En el archivo [wsgi.py](https://github.com/nachobit/DAI_bares/blob/master/myproject/wsgi.py) del proyecto añadir las líneas:

```
import os

from django.core.wsgi import get_wsgi_application
from whitenoise.django import DjangoWhiteNoise

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myproject.settings")

application = get_wsgi_application()
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
	la herramienta *collectstatic* de Heroku configurará de forma automática el contenido estático.


*Referencias:*

[Heroku Django](https://devcenter.heroku.com/articles/django-assets)

[Using Whitenoise](http://whitenoise.evans.io/en/latest/django.html)
