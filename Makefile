# Top level targets
up:
	@echo "⬆️ Starting application"
	docker compose up --build

dup:
	@echo "⬆️ Starting application in daemon mode"
	docker compose up --build -d

down:
	@echo "🔻 Shutting application down"
	docker compose down

bootstrap: tf-bootstrap
	@echo "✅ 🥾 Bootstrapping complete"

init: tf-init
	@echo "✅ ⚙️ Initialization complete"

format: tf-format python-format
	@echo "✅ 📝 Formatting complete"

lint: tf-lint shell-lint python-lint
	@echo "✅ 🔬 Linting complete"

deploy: tf-init tf-plan-and-apply
	@echo "✅ 🚀 Deployment complete"

undeploy: tf-destroy
	@echo "✅ 🔻 Undeploy complete"

test: python-test
	@echo "✅ 🧪 Test suite complete"

## Terraform targets
tf-init:
	@echo "⚙️Initializing Terraform"
	bash terraform/scripts/init.sh

tf-bootstrap:
	@echo "🥾 Bootstrapping Terraform environment"
	bash terraform/scripts/bootstrap.sh

tf-plan-and-apply:
	@echo "⚙️ Running Terraform plan and apply"
	bash terraform/scripts/plan-and-apply.sh

tf-destroy:
	@echo "🔻 Running Terraform destroy"
	bash terraform/scripts/destroy.sh

tf-partial-destroy:
	@echo "🔻 Running Terraform destroy for the main module"
	bash terraform/scripts/partial-destroy.sh

tf-lint:
	@echo "🔬 Linting Terraform scripts"
	bash terraform/scripts/lint.sh

tf-format:
	@echo "📝 Formatting Terraform scripts"
	bash terraform/scripts/format.sh

## Python targets
python-lint:
	@echo "🔬 Linting Python code"
	docker compose exec app black --check .
	docker compose exec app flake8 .

python-format:
	@echo "📝 Formatting Python code"
	docker compose exec app black .

python-test:
	@echo "🧪 Running Python tests"
	docker compose exec app pytest

## Miscellaneous targets
shell-lint:
	@echo "🔬 Linting shell scripts"
	docker run --rm -v $(CURDIR):/mnt koalaman/shellcheck-alpine sh -c "find /mnt -name '*.sh' | xargs shellcheck"

# Maps the target to a Django management command.
# ex: make migrate -> python manage.py migrate
%:
	docker compose exec app python manage.py $*
