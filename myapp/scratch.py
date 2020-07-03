from .models import *

# if __name__ == '__main__':
for obj in ActivityPeriod.objects.select_related('user').all():
    print(obj)

