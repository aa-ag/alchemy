## Alchemy

Checking out some ORM concepts using Python. 

### env

- `conda create -n alchemy`
- `conda activate alchemy`
- `conda install python`
- `conda install sqlalchemy`
- `conda install psycopg2`

created a PostgreSQL instance

```
docker run --name sqlalchemy-orm-psql \
    -e POSTGRES_PASSWORD=pass \
    -e POSTGRES_USER=usr \
    -e POSTGRES_DB=sqlalchemy \
    -p 5432:5432 \
    -d postgres
```