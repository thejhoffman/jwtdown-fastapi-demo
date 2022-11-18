# JWTdown for FastAPI Demo
This repo is meant to be used as a guide for following along side the video for Hack Reactor's Week 14 lesson titled "D4: Backend Authentication with JWTdown"

The database used in this repo is a PostgreSQL database. MongoDB is also an option, but not configured here.

This repo contains two branches: `main` and `final`
* `main` is blank starting point for following along with the video
* `final` is an implementation that I ended up with upon finishing the video and can be used as reference

Structuring the database and queries is not covered in the video and intentionally left bank on the `main` branch

---
Note for SIGNING_KEY:
* Key needs to be created manually can be anything
* Ideally should 20-40 characters long
* This should also be its own environment variable using `.env`
---
## Steps to run the docker containers
```
docker volume create jwtdow-db-data
docker compose build
docker compose up
```

## Useful commands for viewing data in the database

```powershell
<# To connect to docker container shell #>
docker exec -it <container_id> /bin/bash

<# While in container shell: connect to database#>
psql -d jwt_db -U jwt_user

<# While connected to db: view definition of users table #>
\d users

<# While connected to db: show all rows for users table #>
SELECT * FROM users;
```
