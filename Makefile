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
