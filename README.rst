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
* navigate to 127.0.0.1:8000/birthday_users/
  * add user `birthday_users/add`
  * edit user `birthday_users/<user_id>/edit`
  * delete user `birthday_users/<user_id>/delete`
  * view specific user details `birthday_users/<user_id>`
  * download csv `birthday_users/csv


Notes
======

::

  from dateutil.relativedelta import relativedelta
  from datetime import datetime
  threshold = datetime.now() - relativedelta(years=13)
  datetime.datetime(2002,3,3,15,43,50,237178) < threshold # True
  datetime.datetime(2005, 3, 3, 15, 43, 50, 237178) < threshold # False
