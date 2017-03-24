from __future__ import unicode_literals

from datetime import datetime
from dateutil.relativedelta import relativedelta
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.db import models
from random import choice


class BirthdayWRandomNumberExt(User):
    # Adding Birthday and random_number_fields per spec
    birthday = models.DateField(('Birthday'), auto_now_add=False)
    random_number_field = models.IntegerField(default=0)

    def bizz_fuzz(self):
        if self.random_number_field % 3 == 0 and self.random_number_field % 5 == 0:
            return 'BizzFuzz'
        if self.random_number_field % 3 == 0:
            return 'Bizz'
        if self.random_number_field % 5 == 0:
            return 'Fuzz'
        return self.random_number_field

    def get_absolute_url(self):
        return reverse('br_users:index')

    def is_thirteen(self):
        if self.birthday:
            return self.birthday < datetime.date((datetime.now() - relativedelta(years=13)))
        else:
            return False

    def save(self, *args, **kwargs):
        self.username = 'username%s' % len(BirthdayWRandomNumberExt.objects.all())
        # Random number 1-100, 0 indicates not set
        if self.random_number_field == 0:
            self.random_number_field = choice(xrange(1, 101))
        super(BirthdayWRandomNumberExt, self).save(*args, **kwargs)
