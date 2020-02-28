vulnerable-flask-pages

python3 -m virtualenv venv
. venv/bin/activate
pip3 install -r requirements.txt



TO START THE VULNBOX USE THIS:

docker run --rm  -v /var/run/docker.sock:/var/run/docker.sock --name host fenchelfen/vulnerable_flask_pages
