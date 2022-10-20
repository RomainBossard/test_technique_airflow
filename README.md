# test_technique_airflow

## upload data files
files must be uploaded in ./dags/data folder
## launch project
docker-compose up -d

## access to airflow UI
localhost:8080

user: airflow

password: airflow

## access to metabase
localhost:3000

connexion db:

host:
    
    docker ps

    docker inspect *id_of_postgres_container*
    
    host value in IPAddress

user: airflow

password: airflow

port: 5432

db: airflow

*Unfortunately, the IP is always changing while laucunhing the docker container. With more time, I would have fix this to have a metabase on launch without configuration*

## Analysis average basket value:
From July 1st to september 30 , average basket is 51.73€, growing up in september.
*seems like metabase do not save questions from one session to another, maybe due to the fact that the database is hanging with each container launch*


## Analysis  average tome between orders
Unfortunately, there was not enough time left for this analysis



