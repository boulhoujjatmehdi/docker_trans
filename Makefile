

all: 
	docker-compose up --build
down: 
	docker-compose down 
re:  down all

volclean: down
	rm -rf /Users/eboulhou/Desktop/django/django/volume/*
	docker volume prune -f
	# docker volume rm $(docker volume ls -qf dangling=true)



db:
	docker exec -it db sh
dj:
	docker exec -it django sh
user_api_sh:
	docker exec -it userapi sh

PHONY: all down re db dj user_api