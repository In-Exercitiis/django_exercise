from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.core.urlresolvers import reverse
from random import choice
from datetime import datetime
from dateutil.relativedelta import relativedelta


class User(AbstractBaseUser):

    # Adding Birthday and random_number_fields per spec
    birthday = models.DateField(('Birthday'), auto_now_add=False)
    random_number_field = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        # Random number 1-100, 0 indicates not set
        if self.random_number_field == 0:
            self.random_number_field = choice(xrange(1, 101))
        super(User, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('br_users:index')

    def get_username(self):
        return 'user%s' % self.id

    def is_thirteen(self):
        return self.birthday < datetime.date((datetime.now() - relativedelta(years=13)))

    def bizz_fuzz(self):
        if self.random_number_field % 3 and self.random_number_field % 5:
            return 'BizzFuzz'
        if self.random_number_field % 3:
            return 'Bizz'
        if self.random_number_field % 5:
            return 'Fuzz'
        return self.random_number_field
