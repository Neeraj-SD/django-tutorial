from snippets.models import Snippet
from django.contrib.auth.models import User

from  rest_framework import  serializers

class SnippetSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    highlight = serializers.HyperlinkedIdentityField(view_name='snippet-highlight', format='html')

    class Meta:
        model = Snippet
        fields = ['url','title', 'code', 'highlight', 'linenos', 'language', 'style', 'id', 'owner']

class UserSerializer(serializers.ModelSerializer):
    snippets = serializers.HyperlinkedRelatedField(many=True, view_name='snippet-detail', read_only = True)

    class Meta:
        model = User
        fields = ['url','id', 'username', 'snippets']