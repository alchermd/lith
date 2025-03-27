up:
	docker compose up --build

lint:
	docker compose exec app black .
	docker compose exec app flake8 .

# Maps the target to a Django management command.
# ex: make migrate -> python manage.py migrate
%:
	docker compose exec app python manage.py $*
