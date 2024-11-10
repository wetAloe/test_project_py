PHONY: build
build:
	docker-compose build --no-cache
	docker image prune -f

PHONY: up
up:
	docker-compose up

PHONY: down
down:
	docker-compose down

PHONY: upload_data
upload_data:
	python scripts/upload_data.py
