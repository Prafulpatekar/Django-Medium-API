# Django-Medium-API
Basic functionality of medium blogs like auth and reviews backend made in Django and PostgreSQL for database.

## For M1 machine MACBOOK
`export DOCKER_DEFAULT_PLATFORM=linux/amd64`

## Generate secret key for django production
- python -c "import secrets; print(secrets.token_urlsafe(38))"

## For makemigration and migrate issue follow below link
- "https://stackoverflow.com/questions/44651760/django-db-migrations-exceptions-inconsistentmigrationhistory"

### Command to create virtual environment (Prefered python version=3.11)
- `py -0p`
- `py -V:3.11 -m venv venv` 

### Command for docker compose
1. Check Docker compose config 
    `docker compose -f local.yml config`
2. To up docker compose
    `docker compose -f local.yml up --build -d --remove-orphans`
3. To check docker compose logs
    `docker compose -f local.yml logs`
4. To check docker compose logs service logs
    `docker compose -f local.yml logs <service name>`
5. To down the docker compose
    `docker compose -f local.yml down`
6. To inspect volume
    `docker volume inspect <volume name>`
7. To execute backup script on postgres service to take backup
    `docker compose -f local.yml exec postgres backup`
8. To execute backups script on postgres service to list backups
    `docker compose -f local.yml exec postgres backups`
9. To execute restore script on postgres service
    `docker compose -f local.yml exec postgres restore <backup file name>`