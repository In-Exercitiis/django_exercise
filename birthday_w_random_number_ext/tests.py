from django.test import TestCase
from datetime import datetime
from django.core.urlresolvers import reverse
from .models import BirthdayWRandomNumberExt

#
# Model Tests
#


class BirthdayWRandomNumberExtTests(TestCase):

    def test_must_have_birthday(self):
        '''Test that the birthday cannot be null.

        '''
        from django.db import IntegrityError
        usr = BirthdayWRandomNumberExt()
        self.assertRaises(IntegrityError, usr.save)

    def test_is_thirteen(self):
        '''Make sure is_thirteen returns True if thirteen.

        '''
        # Should be coded such that the values for 13 change over
        # time, but overkill for this.
        usr = BirthdayWRandomNumberExt(birthday=datetime.date(datetime(*(2000, 01, 01))))
        usr.save()
        self.assertTrue(usr.is_thirteen())
        usr = BirthdayWRandomNumberExt(birthday=datetime.date(datetime(*(2020, 01, 01))))
        usr.save()
        self.assertFalse(usr.is_thirteen())

    def test_random_number_is_generated(self):
        '''Test that the random generator is working and not leaving
        random_number_field as 0.

        '''
        usr = BirthdayWRandomNumberExt(birthday='2000-01-01')
        usr.save()
        self.failIfEqual(usr.random_number_field, 0)


#
# View Tests
#

class ViewTests(TestCase):

    def test_404(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 404)

    def test_endpoint_200s(self):
        for endpoint in ['index', 'add_user', 'csv_data']:
            print '\n\n'+reverse('br_users:%s' % endpoint)
            response = self.client.get(reverse('br_users:%s' % endpoint))
            self.assertEqual(response.status_code, 200, 'For %s' % endpoint)

        usr = BirthdayWRandomNumberExt(birthday='2014-10-12')
        usr.save()
        for endpoint in ['user_info', 'edit_user', 'delete_user']:
            print '\n\n'+reverse('br_users:%s' % endpoint, kwargs={'pk': 1})
            response = self.client.get(reverse('br_users:%s' % endpoint, args=('1')))
            print endpoint
            self.assertEqual(response.status_code, 200)
