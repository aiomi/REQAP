# REQAP

A Multilevel request/approval system for institutions

## Installation

- clone the repo

``git clone https://github.com/aiomi/REQAP.git``

- Install requirements file

``pip3 install -r requirements.txt``

- Create a local_settings.py and update it accordingly

``cp main/settings/default_settings.py main/settings/local_settings.py``

- run migrations and start the server

``python manage.py migrate``

``python manage.py runserver``

## Create Postgres User

`sudo su postgres -c "psql -c \"CREATE USER reqap WITH PASSWORD 'reqap';\""`

`sudo su postgres -c "psql -c \"CREATE DATABASE reqap_db OWNER reqap;\""`

`sudo su postgres -c "psql -d reqap_db -c \"CREATE EXTENSION IF NOT EXISTS postgis;\""`

`sudo su postgres -c "psql -d reqap_db -c \"CREATE EXTENSION IF NOT EXISTS postgis_topology;\""`
