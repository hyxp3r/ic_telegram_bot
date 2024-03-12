makemigrations:
	alembic revision --autogenerate

migrate:
	alembic upgrade head

run_bot:
	poetry run python -m bot.run_bot

run_bot_prod:
	poetry run gunicorn bot.run_bot:app --workers 4 --preload --worker-class uvicorn.workers.UvicornWorker --bind=0.0.0.0:7000