from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import MusicSerializer, ArtistSerializer, ArtistDetailSerializer, CommentSerializer, MusicDetailSerializer
from .models import Music, Artist, Comment

# Create your views here.
@api_view()
def music_list(request):
    musics = Music.objects.all()
    serializer = MusicSerializer(musics, many=True) # 단일 객체가 아닐 경우 many=True 해야한다... # musics 라고 하는 queryset을 json 타입으로 바꿔준다.
    return Response(serializer.data)

@api_view(['GET']) # GET만 허용
def music_detail(request, music_pk):
    music = get_object_or_404(Music, pk=music_pk)
    serializer = MusicDetailSerializer(music)
    return Response(serializer.data)

@api_view(['GET'])
def artist_list(request):  # artist의 목록
    artists = Artist.objects.all()
    serializer = ArtistSerializer(artists, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def artist_detail(request, artist_pk):
    artist = get_object_or_404(Artist, pk=artist_pk)
    serializer = ArtistDetailSerializer(artist)
    return Response(serializer.data)

# 댓글 작성
@api_view(['POST'])
def comments_create(request, music_pk):
    serializer = CommentSerializer(data=request.data) # request.POST가 아닌 request.data안에 데이터 들어있음.
    # 유효성 검사
    # 예외처리
    if serializer.is_valid(raise_exception=True): # 분기필요없어짐....
        # 통과하면...
        # 저장
        serializer.save(music_id=music_pk)
    return Response(serializer.data)

# 댓글 수정, 삭제
@api_view(['PUT', 'DELETE'])
def comments_update_and_delete(request, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    if request.method == 'PUT':
        serializer = CommentSerializer(data=request.data, instance=comment)
        if serializer.is_valid(raise_exception=True): # 예외처리
            serializer.save()
            return Response({'message': 'Comment has been updated !'})
    else:
        # 삭제
        comment.delete()
        return Response({'message': 'Comment has been deleted !'})