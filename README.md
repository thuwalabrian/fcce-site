# FC Consulting Engineers website


## Container deployment

Build and run locally with PostgreSQL:

```bash
docker compose up --build
```

The website is available at `http://localhost:8000`. PostgreSQL data persists in the `fcce-postgres` Docker volume.

For hosted containers, set:

- `DATABASE_URL` to the provider PostgreSQL connection string
- `FCCE_SITE_URL` to the final public HTTPS domain, including no trailing slash
- `PORT` only if the platform does not provide it automatically

The contact-store implementation automatically uses PostgreSQL whenever `DATABASE_URL` or `POSTGRES_URL` is present. Without either variable, it uses SQLite for local-only development.
