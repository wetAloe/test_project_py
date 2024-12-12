PHONY: build
build:
	docker-compose build --no-cache
	docker image prune -f

PHONY: down
down:
	docker-compose down

PHONY: up
up:
	make down
	docker-compose up

PHONY: upload_data
upload_data:
	python scripts/upload_data.py

PHONY: test
test:
	pytest .
