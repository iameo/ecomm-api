from django.db import models
import random
import string


class TimeStampMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


def generate_id(n, is_alphanum=True):
    """
    generate a random id of length n
    is_alphanum (True: random string of alphanumerals; False: random string of numbers)
    """
    id_ = ''.join(["{}".format(random.randint(0, 9)) for num in range(0, n)])
    if is_alphanum:
        letters_and_digits = string.ascii_letters + string.digits
        id_ = ''.join(random.choice(letters_and_digits) for i in range(0, n))
    return id_


def generate_random_product_code(kind, n):
    return f'{kind}-{generate_id(n)}'
