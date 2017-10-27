from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _


from utils.constants import USER_ROLES, POOL_CUSTOMER


class UserRoles(models.Model):
    """
    Data model for user roles
    """

    name = models.CharField(_('Name'), max_length=255)

    class Meta:
        verbose_name_plural = _('User Roles')

    def __unicode__(self):
        return self.name


class User(AbstractUser):

    """ Custom user model for every pool user. """

    GENDER_CHOICES = (
        ('male', 'Male'),
        ('female', 'Female')
    )

    mobile = models.CharField(_('Mobile Number'),max_length=25, null=True, blank=True)
    gender = models.CharField(_('Gender'), choices=GENDER_CHOICES, max_length=25, null=True, blank=True)
    role = models.CharField(_('Role'), choices=USER_ROLES, max_length=25, default=POOL_CUSTOMER)
    profile_image_url = models.CharField(verbose_name=_('Profile Image URL'), max_length=255, null=True, blank=True)
    dob = models.DateField(verbose_name=_('DOB'), null=True, blank=True)
    roles = models.ManyToManyField(UserRoles, verbose_name=_('User Roles'), blank=True)
    is_owner = models.BooleanField(verbose_name='Is a Car owner ?', default=False)

    class Meta:
        verbose_name_plural = _('Users')

    def __unicode__(self):
        return self.get_username()

