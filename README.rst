==============
 Requirements
==============

Requires dateutil

::

   sudo pip install python-dateutil

=========
 Install
=========

* python manage.py migrate
* python manage.py runserver
* navigate to 127.0.0.1:8000/birthday_w_random_number/

Or use as an api

* add user `birthday_w_random_number/add`
* edit user `birthday_w_random_number/<user_id>/edit`
* delete user `birthday_w_random_number/<user_id>/delete`
* view specific user details `birthday_w_random_number/<user_id>`
* download csv `birthday_w_random_number/csv`

Live Example
============

http://lukepowers.pythonanywhere.com/birthday_w_random_number/

Notes
======

::

  from dateutil.relativedelta import relativedelta
  from datetime import datetime
  threshold = datetime.now() - relativedelta(years=13)
  datetime.datetime(2002,3,3,15,43,50,237178) < threshold # True
  datetime.datetime(2005, 3, 3, 15, 43, 50, 237178) < threshold # False

  http://scottbarnham.com/blog/2008/08/21/extending-the-django-user-model-with-inheritance.1.html
  https://docs.djangoproject.com/en/1.9/topics/class-based-views/
  https://docs.djangoproject.com/en/1.9/topics/http/urls/#url-namespaces
