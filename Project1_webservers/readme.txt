# Docker Basic Runtime

    This example follows the guide at https://gale.udemy.com/course/docker-essentials-for-python-developers/learn/lecture/17229856#overview
    
## Project #1 Web Servers: Instructions after docker installed for web servers flask and django

    # run flask docker container
    docker run -it --name myflask1 -p 5000:5000 -v %cd%:/app python:3.7 bash
    
    # install flask (in container)
    pip3 install flask==2.2.2
    
    # export environmental variables for flask (in container)
    export FLASK_APP=flask_example.py
    export FLASK_DEBUG=1
    
    # run flask (in container)
    flask run --host=0.0.0.0
    
    # check it works (on host browser)
    localhost:5000
    
    # add new flask route (on host)
        @app.route('/version')
        def version() -> str:
            return "Flask Version is {}".format(fv)
            
    # check that new site exists (without rerunning flask) (on host browser)
    localhost:5000/version
    
    # run django docker container
    docker run -it --name mydjango1 -p 8000:8000 -v %cd%:/app python:3.8 bash
    
    # install django
    pip3 install django==2.2.6
    
    # move to /app (host current directory) and install django page with django admin utility
    cd /app
    django-admin startproject testsite
    
    # run django web server for all addresses on port 8000
    cd testsite
    python manage.py runserver 0:8000
    
    


    