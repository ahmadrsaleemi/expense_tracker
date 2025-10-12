APP_NAME = expense_tracker_backend
CONTAINER_NAME = expense_tracker_backend_container
PORT = 5000

build:
	docker build -t $(APP_NAME) .


start:
	docker run -d -p $(PORT):5000 --name $(CONTAINER_NAME) $(APP_NAME)


stop:
	docker stop $(CONTAINER_NAME) || true


clean:
	docker rm -f $(CONTAINER_NAME) || true