#!/bin/bash
# sudo ufw allow 22
# sudo ufw allow 8000
# sudo ufw enable

python_interpreter=""
domain_name=""
current_folder_name=${PWD##*/}
echo "$result"

read -p "Python Interpreter: " python_interpreter
read -p "Your domain without protocol: " domain_name

source ../venv/bin/activate
pip install -U pip
pip install -r deps.txt
python manage.py collectstatic

sed -i "s/project1/$current_folder_name/g" confs/nginx/toys.conf /etc/systemd/gunicorn.service
sed -i "s/templatedomain/$domain_name/g" confs/nginx/toys.conf darianatoys/settings.py

sudo ln -s /home/django/dartoys/$current_folder_name/nginx/toys.conf /etc/nginx/sites-enabled/
sudo ln -s /home/django/dartoys/$current_folder_name/systemd/gunicorn.service /etc/systemd/system/

sudo systemctl daemon-reload
sudo systemctl start gunicorn
sudo systemctl enable gunicorn
sudo service nginx restart