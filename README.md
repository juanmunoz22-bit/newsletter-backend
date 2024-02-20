# Stori Newsletter Frontend

Backend for the Stori newsletter web application using API REST principles and HTTP communication standard.

## Dependencies

- [Docker](https://www.docker.com/)

## Environment Variables

1. Create a `.env` file in the root of the project with the following environment variables for local development and testing:

```env
POSTGRES_HOST=db
POSTGRES_USER=admin
POSTGRES_PASSWORD=admin
POSTGRES_DB=stori
POSTGRES_PORT=5432
DB_URI="postgresql://$POSTGRES_USER:$POSTGRES_PASSWORD@$POSTGRES_HOST:$POSTGRES_PORT/$POSTGRES_DB"
```

## Running the Application

To run the application, execute the following command:

```bash
docker-compose up --build
```

This will create a container for the application and others for the database, the Redis broker and Celery workers for async tasks. The application will be available at `http://localhost:8080`.
