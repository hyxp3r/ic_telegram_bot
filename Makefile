makemigrations:
	alembic revision --autogenerate

migrate:
	alembic upgrade head

run_bot:
	poetry run python -m bot.run_bot