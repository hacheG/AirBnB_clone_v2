#!/usr/bin/env bash
#a bash script bla bla bla

sudo apt-get update
sudo apt-get -y install nginx
ufw allow 'Nginx HTTP'
sudo mkdir /data/
sudo mkdir /data/web_static/
sudo mkdir /data/web_static/releases/
sudo mkdir /data/web_static/releases/test/
sudo touch /data/web_static/releases/test/index.html
echo "<html>
	<head>
	</head>
	<body>
		Holberton School
	</body>
	</html>" | sudo tee /data/web_static/releases/test/index.html

sudo mkdir /data/web_static/shared/
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data
sed -i '/listen 80 default_server/a location /hbng_static/ {\n\t alias /data/web_static/current/;}' /etc/nginx/sites-available/default
sudo service nginx restart
exit 0
