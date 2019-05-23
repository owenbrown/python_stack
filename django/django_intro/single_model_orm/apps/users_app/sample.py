from .models import User
User.objects.create(first_name='bob', last_name='smith', email_address='a@b.c', age=77)
User.objects.create(first_name='charlie', last_name='smith', email_address='a@b.c', age=77)
User.objects.create(first_name='david', last_name='smith', email_address='a@b.c', age=77)
User.objects.all()
User.objects.last()
User.objects.first()

User.objects.get(id=3)

u = User.objects.get(id=3)
u.last_name = 'Pancakes'
u.save()

User.objects.get(id=2).delete()
User.objects.order_by('first_name')
User.objects.order_by('-first_name')
