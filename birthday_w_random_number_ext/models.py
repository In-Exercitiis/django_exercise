from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from random import choice
from datetime import datetime
from dateutil.relativedelta import relativedelta


class BirthdayWRandomNumberExt(User):
    # Adding Birthday and random_number_fields per spec
    birthday = models.DateField(('Birthday'), auto_now_add=False, blank=True, null=True)
    random_number_field = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        self.username = 'username%s' % len(BirthdayWRandomNumberExt.objects.all())
        # Random number 1-100, 0 indicates not set
        if self.random_number_field == 0:
            self.random_number_field = choice(xrange(1, 101))
        super(BirthdayWRandomNumberExt, self).save(*args, **kwargs)

    def is_thirteen(self):
        if self.birthday:
            return self.birthday < datetime.date((datetime.now() - relativedelta(years=13)))
        else:
            return False

    def bizz_fuzz(self):
        if self.random_number_field % 3 and self.random_number_field % 5:
            return 'BizzFuzz'
        if self.random_number_field % 3:
            return 'Bizz'
        if self.random_number_field % 5:
            return 'Fuzz'
        return self.random_number_field
