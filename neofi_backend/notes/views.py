from django.contrib.auth.models import User
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from .models import Note, NoteUpdate
from .serializers import NoteSerializer, NoteUpdateSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_note(request):
    serializer = NoteSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(owner=request.user)
        return Response({'detail': 'Note created successfully.'}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class NoteDetailView(generics.RetrieveAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def share_note(request):
    try:
        note_id = request.data['note_id']
        shared_users = request.data['shared_users']
        note = Note.objects.get(id=note_id, owner=request.user)
        note.shared_users.set(shared_users)
        return Response({'detail': 'Note shared successfully.'}, status=status.HTTP_200_OK)
    except Note.DoesNotExist:
        return Response({'detail': 'Note not found.'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_note(request, pk):
    try:
        note = Note.objects.get(pk=pk)
        if request.user == note.owner or request.user in note.shared_users.all():
            content = request.data['content']
            note.content += f'\n{content}'
            note.save()
            NoteUpdate.objects.create(note=note, content=content, user=request.user)
            return Response({'detail': 'Note updated successfully.'}, status=status.HTTP_200_OK)
        else:
            return Response({'detail': 'Permission denied.'}, status=status.HTTP_403_FORBIDDEN)
    except Note.DoesNotExist:
        return Response({'detail': 'Note not found.'}, status=status.HTTP_404_NOT_FOUND)

class NoteVersionHistoryView(generics.ListAPIView):
    serializer_class = NoteUpdateSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        note_id = self.kwargs['pk']
        return NoteUpdate.objects.filter(note_id=note_id).order_by('-timestamp')



def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                # Redirect to a success page.
                return redirect('success_url')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            # Redirect to a success page.
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def success_url(request):
    return render(request, 'success_page.html')
