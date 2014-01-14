Installation Webshop
====================
(Tested on Ubuntu)

* Install Python 2.7 and Django 1.5
https://docs.djangoproject.com/en/1.5/intro/install/

* Checkout Project 
https://github.com/barta3/ch.bfh.bti7054.w2013.p.FashionShop

* Setup DB Connection
Shop/settings.py Line17: edit path

* Start Server
./Shop/manage.py runserver

* Start local smtp server (for sending mails on checkout)
python -m smtpd -n -c DebuggingServer localhost:1025

Webshop backend:  http://127.0.0.1:8000/admin/
Webshop frontend: http://127.0.0.1:8000/home/

user: admin
pw:   admin
