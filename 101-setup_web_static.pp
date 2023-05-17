# Install nginx
package { 'nginx':
  ensure => installed,
}

# Create necessary directories
file { '/data/web_static/releases/':
  ensure => directory,
}

file { '/data/web_static/shared/':
  ensure => directory,
}

file { '/data/web_static/releases/test/':
  ensure => directory,
}

file { '/data/web_static/releases/test/index.html':
  ensure  => present,
  content => 'Your nginx is working correctly',
}

# Create symbolic link
$target_path = '/data/web_static/releases/test'
$link_path   = '/data/web_static/current'

file { $link_path:
  ensure => link,
  target => $target_path,
  force  => true,
}

# Change folder user and group to ubuntu
exec { 'change-folder-owner':
  command => 'chown -R ubuntu /data/ && chgrp -R ubuntu /data/',
}

# Configure nginx to serve hbnb static
file { '/etc/nginx/sites-available/default':
  ensure  => present,
  content => "
server {
    listen 80;
    listen [::]:80;
    root /etc/nginx/html;
    index index.html index.htm index.nginx-debian.html;
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
}
",
}

# Restart nginx
service { 'nginx':
  ensure  => running,
  enable  => true,
  require => File['/etc/nginx/sites-available/default'],
}
