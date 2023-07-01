backup:
	python3 ./scripts/backup.py

upload:
	python3 ./scripts/upload.py

create:
	python3 ./api/create.py

delete:
	python3 ./api/delete.py

clean:
	cd backups && rm -r -f hooks info objects refs config description HEAD

install:
	pip3 install GitPython
	pip3 install python-dotenv
	pip3 install requests

uninstall:
	pip3 uninstall GitPython
	pip3 uninstall python-dotenv
	pip3 uninstall requests