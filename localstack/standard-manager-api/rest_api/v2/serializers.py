from django.contrib.auth.models import User, Group
from rest_framework import serializers

from rest_api.v1.models import Standard


class ApiSerializer(serializers.Serializer):
    data = serializers.CharField()


class StandardSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Standard
        fields = [
            'uuid',
            'identification',
            'publication_date',
            'validity_start',
            'title',
            'title_global_language',
            # comite = models.CharField(max_length=100, blank=False, default='')
            # pages = models.IntegerField()
            # status = models.CharField(choices=STATUS, default=STATUS[0], max_length=100)
            # language = models.CharField(choices=LANGUAGES, default=LANGUAGES[0], max_length=50)
            # organization = models.CharField(max_length=255)
            'price',
            # currency = models.CharField(choices=CURRENCIES, default=CURRENCIES[0], max_length=5)
            # objective = models.TextField()
            'url',
            'file'
        ]
        extra_kwargs = {
            'price': {'max_digits': 16, 'decimal_places': 2}
        }

        # https://www.django-rest-framework.org/tutorial/1-serialization/


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']
