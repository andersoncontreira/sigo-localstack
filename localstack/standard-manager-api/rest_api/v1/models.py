from django.db import models


class Currencies(models.TextChoices):
    BRL = "Real"
    USD = "Dollar"
    EUR = "Euro"


class Status(models.TextChoices):
    EM_VIGOR = "Em Vigor"
    ARQUIVADO = "Arquivado"


class Languages(models.TextChoices):
    PORTUGUES = "Português"
    ENGLISH = "English"


# Create your models here.
class StandardManager(models.Manager):
    """
        The manager for the auth's Group model.
        """
    use_in_migrations = True

    def get_by_natural_key(self, title):
        return self.get(name=title)


class Standard(models.Model):
    # created = models.DateTimeField(auto_now_add=True)
    # linenos = models.BooleanField(default=False)
    # language = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100)
    # style = models.CharField(choices=STYLE_CHOICES, default='friendly', max_length=100)

    uuid = models.UUIDField()
    identification = models.CharField(max_length=100, blank=False)
    publication_date = models.DateField()
    validity_start = models.DateField()
    title = models.CharField(max_length=100, blank=False, default='')
    title_global_language = models.CharField(max_length=100, blank=False, default='')
    comite = models.CharField(max_length=100, blank=False, default='')
    pages = models.IntegerField(default=1)
    status = models.CharField(choices=Status, default=Status.EM_VIGOR, max_length=100)
    language = models.CharField(choices=Languages, default=Languages.PORTUGUES, max_length=50)
    organization = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=16, decimal_places=2)
    currency = models.CharField(choices=Currencies, default=Currencies.BRL, max_length=5)
    objective = models.TextField(blank=True,null=True)
    url = models.URLField(blank=True, null=True)
    file = models.CharField(max_length=255,blank=True,null=True)

    active = models.BooleanField(default=True)
    deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    objects = StandardManager()

    class Meta:
        ordering = ['created_at', 'organization']
