up:
	docker compose up --build

# Maps the target to a Django management command.
# ex: make migrate -> python manage.py migrate
%:
	docker compose exec app python manage.py $*
