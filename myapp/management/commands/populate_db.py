from django.core.management.base import BaseCommand
from myapp.models import *


class Command(BaseCommand):
    def _create_user(self):
        t1 = User(id='W012A3CDE', real_name='Egon Spengler', tz='America/Los_Angeles')
        t1.save()

        t2 = User(id='W07QCRPA4', real_name='Glinda Southgood', tz='Asia/Kolkata')
        t2.save()

    def handle(self, *args, **options):
        self._create_user()