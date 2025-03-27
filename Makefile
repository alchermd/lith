up:
	docker compose up --build

dup:
	docker compose up --build -d

down:
	docker compose down

lint:
	docker compose exec app black --check .
	docker compose exec app flake8 .

test:
	docker compose exec app pytest

# Maps the target to a Django management command.
# ex: make migrate -> python manage.py migrate
%:
	docker compose exec app python manage.py $*
