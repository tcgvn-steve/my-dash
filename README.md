
# Dash Framework Project

### Structure
```sh
https://dash.plotly.com/urls
```

### Create Virtual
```sh
virtualenv -p python3.8 env
source env/bin/activate
```

### Install requirements
```sh
sudo apt install python3-pip
pip install -r requirements.txt 
```

### Run app (DEV)
```sh
python main.py
gunicorn main:server --bind=0.0.0.0:8000

```

### Library

https://docs-dash-admin-components.herokuapp.com/l/components

https://dash-bootstrap-components.opensource.faculty.ai/docs/components/alert/


### Run docker
```sh
sudo docker build -t my-dash:0.0.6 .
sudo docker run -d -p 8050:8050 --name=my-dash my-dash:0.0.6
sudo docker build -t my-dash:0.0.6 .
sudo docker build -t huyhoang1996ha/my-dash:0.0.5 .
sudo docker push huyhoang1996ha/my-dash:0.0.5
sudo docker run -d -p 8050:8050 --name=my-dash huyhoang1996ha/my-dash:0.0.5

```










