install_env:
	poetry -C fastapi_app/app/ install
	poetry -C frontend/app/ install

run_backend:
	uvicorn fastapi_app.app.main:app --port 8000

run_frontend:
	streamlit run frontend/app/main.py --server.port=8501

docker_build_app:
	docker compose build

docker_app_up:
	docker compose up


docker_run_app: docker_build_app docker_app_up