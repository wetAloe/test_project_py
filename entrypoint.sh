#!/bin/sh

# Run migrations
alembic upgrade head

# Start the application
exec python src/run.py
