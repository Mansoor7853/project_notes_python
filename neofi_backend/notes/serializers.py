from rest_framework import serializers
from .models import Note, NoteUpdate

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ['id', 'owner', 'content', 'shared_users']

class NoteUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = NoteUpdate
        fields = ['content', 'timestamp', 'user']
