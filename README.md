Конфиг Nginx 
 
	server {
		listen 443 ssl;
		server_name *******;
		ssl_certificate /etc/letsencrypt/live/******/fullchain.pem;
		ssl_certificate_key /etc/letsencrypt/live/****/privkey.pem;
		location / {
			proxy_pass http://0.0.0.0:9500;
			proxy_set_header Host $host;
			proxy_set_header X-Real-IP $remote_addr;
			proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
			proxy_set_header X-Forwarded-Proto $scheme;
		}
	}
