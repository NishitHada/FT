from django.core.management.base import BaseCommand
from myapp.models import *


class Command(BaseCommand):
    def _create_user(self):
        t1 = User(id='W012A3CDE', real_name='Egon Spengler', tz='America/Los_Angeles')
        t1.save()

        t2 = User(id='W07QCRPA4', real_name='Glinda Southgood', tz='Asia/Kolkata')
        t2.save()

    def _create_activity(self):
        # u1 = User(id='W012A3CDE', real_name='Egon Spengler', tz='America/Los_Angeles')
        t1 = ActivityPeriod(user=User.objects.get(id='W012A3CDE'), start_time='2020-02-01 13:33', end_time='2020-02-01 13:54')
        t1.save()

        t2 = ActivityPeriod(user=User.objects.get(id='W012A3CDE'), start_time='2020-03-01 11:11', end_time='2020-02-01 14:00')
        t2.save()

        t3 = ActivityPeriod(user=User.objects.get(id='W012A3CDE'), start_time='2020-03-16 17:33', end_time='2020-02-01 20:02')
        t3.save()


        # u2 = User(id='W07QCRPA4', real_name='Glinda Southgood', tz='Asia/Kolkata')
        t4 = ActivityPeriod(user=User.objects.get(id='W07QCRPA4'), start_time='2020-02-01 13:33', end_time='2020-02-01 13:54')
        t4.save()

        t5 = ActivityPeriod(user=User.objects.get(id='W07QCRPA4'), start_time='2020-03-01 11:11', end_time='2020-02-01 14:00')
        t5.save()

        t6 = ActivityPeriod(user=User.objects.get(id='W07QCRPA4'), start_time='2020-03-16 17:33', end_time='2020-02-01 20:02')
        t6.save()


    def handle(self, *args, **options):
        self._create_user()
        self._create_activity()