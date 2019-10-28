from rest_framework import serializers
from .models import Music, Artist, Comment

class MusicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Music
        fields = ('id', 'title', 'artist_id')

class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ('id', 'name')

class ArtistDetailSerializer(ArtistSerializer):
    musics = MusicSerializer(source='music_set',many=True) # source='이전이름' => 이전이름(music_set)을 musics로 바꿈, source 생략 가능..
    musics_count = serializers.IntegerField(source='music_set.count') # 개발자가 만듬
    class Meta(ArtistSerializer.Meta): # 위의 ArtistSerializer에서 meta를 상속받음
        fields = ArtistSerializer.Meta.fields +  ('musics', 'musics_count')

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'content', 'music_id')

class MusicDetailSerializer(MusicSerializer):
    comments = CommentSerializer(source='comment_set', many=True)
    class Meta(MusicSerializer.Meta):
        fields = MusicSerializer.Meta.fields + ('comments',)