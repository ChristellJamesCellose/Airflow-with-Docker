# Airflow-with-Docker

Download the Docker
https://www.docker.com/products/docker-desktop/

After the Docker downloaded, we wil start download the airflow with docker

## Link How to run airflow in Docker
https://airflow.apache.org/docs/apache-airflow/stable/start/docker.html
*Using Ubuntu(WSL) Terminal

1. make a folder
-> mkdir airflow-docker

2. move to the folder
-> cd airflow-docker

3. fetch docker-compose.yaml.
-> (curl -LfO 'https://airflow.apache.org/docs/apache-airflow/2.3.3/docker-compose.yaml')

*before that -> run Remove-item alias:curl

4. open the .yaml file

5. create folder (dags, logs, plugins) use mkdir

6. echo -e "AIRFLOW_UID=$(id -u)\nAIRFLOW_GID=0" > .env

7. docker-compose up airflow-init

8. docker-compose up
