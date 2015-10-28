from django.contrib.auth.models import User
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.timezone import now

@python_2_unicode_compatible
class UserProfile(models.Model):  
    user = models.OneToOneField(User)  
    name = models.CharField(default = 'user', max_length = 25, null = False, blank = False)
    id_internal = models.CharField(max_length = 25, null = True, blank = True)
    verified = models.BooleanField(default = False, null = False, blank = False)
    date_approval = models.DateTimeField('date_approved', null = True, blank = True)

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'
        ordering = ['date_approval']

    def __str__(self):
        return "%s's profile" % self.user  

    def create_user_profile(sender, instance, created, **kwargs):  
        if created:
            profile, created = UserProfile.objects.get_or_create(user=instance)  

        post_save.connect(create_user_profile, sender=User) 

@python_2_unicode_compatible
class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    class Meta:
        verbose_name = 'tag'
        verbose_name_plural = 'tags'
        ordering = ['name']

    def __str__(self):
        return self.name


class PublicManager(models.Manager):
    def get_queryset(self):
        qs = super(PublicManager, self).get_queryset()
        return qs.filter(is_public=True)


@python_2_unicode_compatible
class Link(models.Model):
    name = models.CharField('name', max_length = 50, null = False, blank = False)
    url = models.URLField(null = False, blank = False)
    date_created = models.DateTimeField('date_created')
    date_modified = models.DateTimeField('date_modified')

    description = models.TextField('description', blank=True)
    is_public = models.BooleanField('public', default=True)
    owner = models.ForeignKey(User, verbose_name='owner',
        related_name='links')
    tags = models.ManyToManyField(Tag, blank=True)


    objects = models.Manager()
    public = PublicManager()

    class Meta:
        verbose_name = 'link'
        verbose_name_plural = 'links'
        ordering = ['-date_created']

    def __str__(self):
        return '%s (%s)' % (self.name, self.url)

    def save(self, *args, **kwargs):
        if not self.id:
            self.date_created = now()
        self.date_modified = now()
        super(Link, self).save(*args, **kwargs)

@python_2_unicode_compatible
class List(models.Model):
    name = models.CharField(max_length = 50)
    links = models.ManyToManyField(Link)
    date_created = models.DateTimeField('date_created')
    date_modified = models.DateTimeField('date_modified')
    owner = models.ForeignKey(User, verbose_name='owner', related_name = 'lists')

    objects = models.Manager()
    public = PublicManager()

    class Meta:
        verbose_name = 'list'
        verbose_name_plural = 'lists'
        ordering = ['date_modified']

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.id:
            self.date_created = now()
        self.date_modified = now()
        super(List, self).save(*args, **kwargs)

