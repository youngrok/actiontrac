import hashlib
import logging
from annoying.fields import AutoOneToOneField, JSONField
from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = AutoOneToOneField(User)
    name = models.CharField(max_length=200, blank=True)
    profile_image = models.URLField(blank=True)
    data = JSONField(default={})

    def update_social_auth_data(self, backend, data):
        try:
            if 'social_auth_data' not in self.data:
                self.data['social_auth_data'] = {}

            if isinstance(data, dict):
                self.data['social_auth_data'][backend.name] = data

            if backend.name == 'twitter':
                self.profile_image = data['profile_image_url']
                self.name = data['name']
            elif backend.name == 'facebook':
                self.name = data['name']
                self.profile_image = 'http://graph.facebook.com/%s/picture' % data['id']
            elif self.user.email and not self.profile_image:
                self.profile_image = 'http://www.gravatar.com/avatar/' + hashlib.md5(self.user.email).hexdigest()

            self.save()
        except Exception as e:
            logging.exception(e)

    def __unicode__(self):
        return self.name
