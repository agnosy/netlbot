help:
	@echo "Usage: make deploy"
	@echo "       make migrate"
	@echo "       make rollback"
	@echo "       make run"

harvest:
	python -m netl.netlbot harvest

deploy:
	pip install --editable .

migrate:
	alembic upgrade head

rollback:
	alembic downgrade base

