from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Note

class NoteAPITestCase(APITestCase):
    def setUp(self):
        # Create a user for authentication
        self.user = User.objects.create_user(username='testuser', password='testpassword')

        # Create a note for testing
        self.note = Note.objects.create(owner=self.user, content='Test content')

        # Authenticate the client
        self.client.force_authenticate(user=self.user)

    def test_create_note(self):
        url = '/notes/create/'
        data = {'content': 'New note content'}
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Note.objects.count(), 2)  # One additional note should be created
        self.assertEqual(Note.objects.last().content, 'New note content')
        self.assertEqual(Note.objects.last().owner, self.user)

    def test_get_note(self):
        url = f'/notes/{self.note.id}/'
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['content'], 'Test content')

    def test_share_note(self):
        # Create another user to share the note with
        other_user = User.objects.create_user(username='otheruser', password='otherpassword')

        url = f'/notes/share/'
        data = {'shared_users': [other_user.id]}
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(self.note.shared_users.count(), 1)
        self.assertEqual(self.note.shared_users.first(), other_user)

    def test_update_note(self):
        url = f'/notes/{self.note.id}/update/'
        data = {'content': 'Updated content'}
        response = self.client.put(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Note.objects.last().content, 'Test content\nUpdated content')

    def test_note_version_history(self):
        url = f'/notes/version-history/{self.note.id}/'
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Implement assertions for version history data
        # Example: self.assertIn('version_history', response.data)
