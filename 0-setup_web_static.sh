#!/usr/bin/env bash
# script that sets up your web servers for the deployment of web_staticscript that sets up your web servers for the deployment of web_staticscript that sets up your web servers for the deployment of web_staticscript that sets up your web servers for the deployment of web_staticscript that sets up your web servers for the deployment of web_staticscript that sets up your web servers for the deployment of web_staticscript that sets up your web servers for the deployment of web_staticscript that sets up your web servers for the deployment of web_staticscript that sets up your web servers for the deployment of web_staticscript that sets up your web servers for the deployment of web_staticscript that sets up your web servers for the deployment of web_static

# install nginx
apt-get update
apt-get install nginx

# create necessary directories
mkdir -p /data/
mkdir -p /data/web_static/releases/
mkdir -p /data/web_static/shared/
mkdir -p /data/web_static/releases/test/
touch /data/web_static/releases/test/index.html

# create a test html file to confirm nginx configuration
printf %s "
Your nginx is workin correctly
" | tee -a /data/web_static/releases/test/index.html > /dev/null

# create symbolic link
link_path="/data/web_static/current"
target_path="/data/web_static/releases/test"

if [ -L "$link_path" ]; then
    rm "$link_path"
fi
ln -s "$target_path" "$link_path"

# change folder user and groub to ubuntu
chown -R 1000:1000 /data/

# configure nginx to serve hbnb static

printf %s "server {
    listen 80;
    listen [::]:80;
    root /etc/nginx/html;
    index index.html index.htm index.nginx-debian.html
    server_name _;

    location /hbnb_static {
        alias /data/web_static/current/;
        }

    location /redirect_me {
        return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;
    }

    error_page 404 /404.html;
    location = /etc/nginx/html/404.html {
      internal;
    }
}" | tee -a /etc/nginx/sites-available/default > /dev/null

# restart nginx
service nginx restart
