


build:
	docker build -t hiking-api .
run:
	docker run --rm -p 8000:8000 hiking-api
up:
	docker compose up --build