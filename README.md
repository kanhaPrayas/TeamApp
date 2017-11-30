# TeamApp

This is a dummy team management application, which supports CRUD apis for the team members


INSTALLATION:

1: mkdir project

2:virtualenv TeamAppEnv

3:source TeamAppEnv/bin/activate

4:git clone https://github.com/kanhaPrayas/TeamApp.git

5:pip install -r requirements.txt

6: Rename TeamAppApi/TeamAppApi/config.py.txt to TeamAppApi/TeamAppApi/config.py
	config.py is in gitignore file. This file contains DB configuration 

7: Update your db details as per your db configurations

8: Run : python manage.py migrate

9: Run python manage.py runserver


RUNNING THE APPLICATION

Test the apis as follows:

	POST:
		curl -X POST -H "Content-Type:application/json" http://127.0.0.1:8000/core/v1/member/ -d '{"phone":"8884599393","email":"kanha.prayas@gmail.com","role":"admin","first_name":"Arunima","last_name":"Nayak"}'


	GET:
		curl -X GET -H "Content-Type:application/json" http://127.0.0.1:8000/core/v1/member/

	PUT:
		curl -X PUT -H "Content-Type:application/json" http://127.0.0.1:8000/core/v1/member/ -d '{"phone":"8884599393","email":"kanha.prayas@gmail.com","role":"admin","first_name":"Arunima","last_name":"Nayak","id":"3323323"}'

	DELETE:
		curl -X DELETE -H "Content-Type:application/json" http://127.0.0.1:8000/core/v1/member/ -d '{"id":"3323323"}'



Test the DRF apis as follows:

	POST:
		curl -X POST -H "Content-Type:application/json" http://127.0.0.1:8000/core/v1/drf/member/ -d '{"phone":"8884599393","email":"kanha.prayas@gmail.com","role":"admin","first_name":"Arunima","last_name":"Nayak"}'


	GET:
		curl -X GET -H "Content-Type:application/json" http://127.0.0.1:8000/core/v1/drf/member/

	PUT:
		curl -X PUT -H "Content-Type:application/json" http://127.0.0.1:8000/core/v1/drf/member/ -d '{"phone":"8884599393","email":"kanha.prayas@gmail.com","role":"admin","first_name":"Arunima","last_name":"Nayak","id":"3323323"}'

	DELETE:
		curl -X DELETE -H "Content-Type:application/json" http://127.0.0.1:8000/core/v1/drf/member/ -d '{"id":"3323323"}'






