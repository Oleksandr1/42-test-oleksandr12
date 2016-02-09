from django.db import models

# Create your models here.


class MyData(models.Model):
    first_name = models.CharField(
                                  max_length=256,
                                  blank=False,
                                  verbose_name="Name")

    last_name = models.CharField(
                                 max_length=256,
                                 blank=False,
                                 verbose_name="Surname")

    birthday = models.DateField(
                                 blank=False,
                                 verbose_name='Data of Birth',
                                 null=True)

    email = models.CharField(
                             max_length=256, blank=False,
                             verbose_name='E-mail')

    skype = models.CharField(
                             max_length=256,
                             blank=False,
                             verbose_name='skype')

    jabber = models.CharField(
                              max_length=256,
                              blank=False,
                              verbose_name='Jabber/xmpp')

    biography = models.TextField(
                                 blank=True,
                                 verbose_name='Biography')

    other_contacts = models.TextField(
                                      blank=True,
                                      verbose_name='other contacts')
