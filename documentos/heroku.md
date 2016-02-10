###HEROKU###

Siguiendo el [tutorial de Python y Django de Heroku](https://devcenter.heroku.com/articles/getting-started-with-python-o):

Lo primero es instalar [Heroku toolbelt](https://toolbelt.heroku.com) junto con *gunicorn* (Python Web Server Gateway Interface HTTP Server) previamente:
	
	pip install gunicorn

- Una vez estamos registrados en Heroku y con el repositorio subido a GitHub, hacer *login* desde terminal:

	``` heroku login ```
	
- Definir el archivo [Procfile](https://github.com/nachobit/IV_PR_OpenOrder/blob/master/Procfile) para *decirle a Heroku que debe ejecutar*:
	
	```
	web: gunicorn myproject.wsgi --log-file -
	```

- Definir el archivo [requirements](https://github.com/nachobit/IV_PR_OpenOrder/blob/master/requirements.txt) para que Heroku *reconozca la existencia de una aplicación*:

	```
	pip freeze > requirements.txt
	```
Del fichero *requirements.txt* nos quedaremos solamente con las dependencias realmente necesarias con el fin de evitar problemas al lanzar Heroku.

	```
	alembic==0.8.4
	Django==1.9
	django-appconf==1.0.1
	django-classy-tags==0.6.2
	django-easy-maps==0.9.2
	geopy==1.11.0
	gunicorn==19.4.1
	Jinja2==2.8
	Mako==1.0.3
	MarkupSafe==0.23
	python-editor==0.5
	six==1.10.0
	SQLAlchemy==1.0.9
	whitenoise==2.0.6
	Werkzeug==0.11.2
	wheel==0.26.0
	WTForms==2.0.2
	dj-static==0.0.6	
	```

Y por último:

	 wget -O- https://toolbelt.heroku.com/install.sh | sh 

Que automatiza los pasos:

	1.  heroku create
		1.1 git add .
		1.2 git commit -m "Demo"
	2.	git push heroku master
	3.	heroku ps:scale web=1
	4.	heroku open
	
Para cualquier cambio que realicemos a partir de este punto en nuestra aplicación, bastará con realizar el *git push heroku master*.

Una vez realizados los pasos anteriores ya tendremos la aplicación perfectamente funcionando y corriendo sobre Heroku. Pero para conseguir que los cambios realizados se desplieguen al hacer ```git push ``` y continuar con la integración continua de la aplicación, enlazamos el repositorio con **Snap CI** y configuramos Heroku para trabajar con el Deploy Automático de Snap.
	
Comprobamos nuestra aplicación funcionando correctamente en Heroku:

[Aplicación](https://baresdai.herokuapp.com/rango)
