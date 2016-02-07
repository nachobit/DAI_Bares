install:
	sudo apt-get update
	sudo apt-get install -y python-dev
	sudo apt-get install -y python-pip
	sudo pip install --upgrade pip
	sudo pip install -r requirements.txt

test:
	python manage.py test

#run:
#	gunicorn myproject.wsgi:application -b 0.0.0.0:80
	
#Install Docker:
#	./install_docker.sh

#Run Docker: 
#	./docker.sh

runserver:
	nohup sudo python manage.py runserver 0.0.0.0:8000
