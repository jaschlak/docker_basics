
## Project 4: Flask Micro Service

    pull section#3 from https://github.com/d4py/d4py

    update requirements.txt with "Flask==2.2.2"

    docker run -it --rm -p 5000:5000 -v %cd%:/app python:3 bash
    
    cd /app
    
    pip install -r requirements.txt
    
    # run gunicorn webserver on host ip, port 5000, 1 instance(worker), picking app color-boxes
    gunicorn --bind=0.0.0.0:5000 --workers=1 color-boxes:app
    
    http://localhost:5000/
    
    