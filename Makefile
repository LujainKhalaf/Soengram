db_seed:
	sudo -u postgres psql -f ./seed/seed.sql
	python3 ./seed/seed.py
