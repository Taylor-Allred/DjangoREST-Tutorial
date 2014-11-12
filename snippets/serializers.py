from django.forms import widgets
from rest_framework import serializers
from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES
from django.contrib.auth.models import User



class SnippetSerializer(serializers.HyperlinkedModelSerializer):
	owner = serializers.Field(source='owner.username')
	highlight = serializers.HyperlinkedIdentityField(view_name='snippet-highlight', format='html')
	class Meta:
		model = Snippet
		fields = ('url', 'highlight', 'owner', 
				  'title', 'code', 'linenos', 'language', 'style')


class UserSerializer(serializers.HyperlinkedModelSerializer):
	snippets = serializers.HyperlinkedRelatedField(many=True, view_name='snippet-detail')


	class Meta:
		model = User
		fields = ('url', 'username', 'snippets')
	# pk = serializers.Field()
	# title = serializers.CharField(required=False,
	# 							  max_length=100)
	# code = serializers.CharField(widget=widgets.Textarea,
	# 							 max_length=100000)
	# linenos = serializers.BooleanField(required=False)
	# language = serializers.ChoiceField(choices=LANGUAGE_CHOICES,
	# 								   default='python')
	# style = serializers.ChoiceField(choices=STYLE_CHOICES,
	# 								default='friendly')


	# def restore_object(self, attrs, instance=None):
	# 	if instance:
	# 		instance.title = attrs.get('title', instance.title)
	# 		instance.code = attrs.get('code', instance.code)
	# 		instance.linenos = attrs.get('lineos', instance.linenos)
	# 		instance.language = attrs.get('language', instance.language)
	# 		instance.style = attrs.get('style', instance.style)
	# 		return instance

	# 	return Snippet(**attrs)