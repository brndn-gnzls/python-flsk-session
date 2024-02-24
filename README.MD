# Flask HTTPS with Gunicorn
### This is a template for serving a flask API over HTTPS using gunicorn.
Generate your ```cert.pem``` and ```key.pem``` files in the project root
```
$ mkcert -key-file key.pem -cert-file cert.pem 127.0.0.1 localhost ::1
```
Ensure you have gunicorn installed
```
$ pip3 install gunicorn
```
Adjust the ```gunicorn_config.py``` to include your cerfile, keyfile, and url:port binding.
```
$ gunicorn -c gunicorn_config.py app:app
```