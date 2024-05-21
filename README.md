# Django-Medium-API
Basic functionality of medium blogs like auth and reviews backend made in Django and PostgreSQL for database.


## Generate secret key for django production
- python -c "import secrets; print(secrets.token_urlsafe(38))"

### Command to create virtual environment
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