#!/usr/bin/env bash
# script that sets up your web servers for the deployment of web_staticscript that sets up your web servers for the deployment of web_staticscript that sets up your web servers for the deployment of web_staticscript that sets up your web servers for the deployment of web_staticscript that sets up your web servers for the deployment of web_staticscript that sets up your web servers for the deployment of web_staticscript that sets up your web servers for the deployment of web_staticscript that sets up your web servers for the deployment of web_staticscript that sets up your web servers for the deployment of web_staticscript that sets up your web servers for the deployment of web_staticscript that sets up your web servers for the deployment of web_static

# install nginx
sudo apt-get update
sudo apt-get install nginx

# create nexessary directories
mkdir -p /data/
mkdir -p /data/web_static/releases/
mkdir -p /data/web_static/shared/
mkdir -p /data/web_static/releases/test/
touch /data/web_static/releases/test/index.html

# create a test html file to confirm nginx configuration
printf %s "
Your nginx is workin correctly
" > /data/web_static/releases/test/index.html

# create symbolic link
link_path="/data/web_static/current"
target_path="/data/web_static/releases/test"

if [ -L "$link_path" ]; then
    rm "$link_path"
fi
ln -s "$target_path" "$link_path"

# change folder user and groub to ubuntu
sudo chown -R ubuntu: ubuntu /data/

# configure nginx to serve hbnb static
printf %s "
location /hbnb_static {
        alias /data/web_static/current/;
}" > /etc/nginx/sites-available/default

# restart nginx
sudo service nginx restart

