# from django.db import bk
from djongo import models


class Profile(models.Model):
    user_id = models.IntegerField()
    has_kyc = models.BooleanField(default=False)
    military_service_status = models.CharField(max_length=35)

    class Meta:
        db_table = "profiles"
    # meta = {'collection': 'cmsPage'}
    # options = {
    #               'collection': 'profiles',
    #               'managed': True,
    #           },
