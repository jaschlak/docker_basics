

## Project #2 Jupyter Notebooks

    # run docker, interactive, local name, <host port>:<cont port>, map local dir to cont /home/jobyan/work dir, enable lab mode for jupyter (instead of notebook), 
    #    official jupyter image to download see: https://jupyter-docker-stacks.readthedocs.io/en/latest/using/selecting.html
    docker run -it --name jupyter-data1 -p 8888:8888 -v %cd%:/home/jovyan/work -e JUPYTER_ENABLE_LAB=yes jupyter/datascience-notebook