from django.contrib.auth.models import User
import random


def check_if_username_exists(username):
    return User.objects.filter(username=username).exists()


def create_dummy_user():
    while True:
        random_digits = "".join([str(random.randint(0, 9)) for i in range(random.randint(1, 10))])
        username = "hatim" + random_digits
        if not check_if_username_exists(username):
            break

    user_obj = User.objects.create(
        username=username,
        first_name='Hatim',
    )

    user_obj.set_password("helloworld123")
    user_obj.save()
    return user_obj
