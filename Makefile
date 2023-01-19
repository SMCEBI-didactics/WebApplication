SHELL := /bin/bash

test:
	source tests/start_tests

update-db:
	source tests/update_db

update-db-docker:
	source tests/update_db_docker

clear:
	rm -rf venv/
