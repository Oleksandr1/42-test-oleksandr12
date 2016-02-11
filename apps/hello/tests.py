from django.test import TestCase

# Create your tests here.


class SomeTests(TestCase):
    def test_math(self):
        """
        put docstrings in your tests
        """
        assert(2 + 2 == 4)

        user = User(
                        username='sanya',
                        is_active=True,
                        is_superuser=True,
                        is_staff=True,
                        email='sanya071186@gmail.com')
        user.set_password('11')
        user.save()
