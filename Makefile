up:
	docker compose up --build

dup:
	docker compose up --build -d

down:
	docker compose down

format:
	docker compose exec app black .

lint:
	docker compose exec app black --check .
	docker compose exec app flake8 .
	docker run --rm -v $(CURDIR):/mnt koalaman/shellcheck-alpine sh -c "find /mnt -name '*.sh' | xargs shellcheck"

test:
	docker compose exec app pytest

# Maps the target to a Django management command.
# ex: make migrate -> python manage.py migrate
%:
	docker compose exec app python manage.py $*
