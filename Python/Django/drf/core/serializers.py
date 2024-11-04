from rest_framework import serializers
from core.models import Snippet, LANGUAGE_CHOICE, STYLE_CHOICES

class SnippetSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only = True)
    title = serializers.CharField(required=False, allow_blank=True, max_length=100)
    code = serializers.CharField(style={'base_template': 'textarea.html'})
    linenos = serializers.BooleanField(required=False)
    language = serializers.ChoiceField(choices=LANGUAGE_CHOICE, default='python')
    style = serializers.ChoiceField(choices=STYLE_CHOICES, default='friendly')


    def create(self, validated_data):
        return Snippet.object.create(**validated_data)
        
    
    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.code = validated_data.get('code', instance.code)
        instance.linenos = validated_data.get('linenos', instance.linenos)
        instance.style = validated_data('style',instance.style)
        instance.save()

        return instance