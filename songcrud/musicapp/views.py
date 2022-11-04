from django.shortcuts import render
from .models import Artist, Song, Lyric
from .serializers import ArtistSerializer, SongSerializer, LyricSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponse

# Create your views here.
# class ArtisteList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
#     queryset = Artist.objects.all()
#     serializer_class = ArtistSerializer

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)
@api_view(['GET', 'POST'])
def artistelist(request):
    if request.method == 'GET':
        artist = Artist.objects.all() #Queryset
        serializer = ArtistSerializer(artist, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ArtistSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# class ArtisteDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
#     queryset = Artist.objects.all()
#     serializer_class = ArtistSerializer


#     def get(self, request, pk, *args, **kwargs):
#         return self.retrieve(request, id=pk)

    

#     def put(self, request, pk, *args, **kwargs):
#         return self.update(request, id=pk)

#     def delete(self, request, pk, *args, **kwargs):
#         return self.destroy(request, id=pk)
@api_view(['GET', 'PUT', 'DELETE'])
def artist_detail(request, pk):
    artist = Artist.objects.get(pk = pk) #instance
    if request.method == 'GET':
        serializer = ArtistSerializer(artist)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = ArtistSerializer(artist, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        artist.delete()
        return HttpResponse(status=status.HTTP_200_OK)

# class SongList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
#     queryset = Song.objects.all()
#     serializer_class = SongSerializer

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)

@api_view(['GET', 'POST'])
def songlist(request):
    if request.method == 'GET':
        song = Song.objects.all() #Queryset
        serializer = SongSerializer(song, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = SongSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class SongDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
#     queryset = Song.objects.all()
#     serializer_class = SongSerializer
    # def get(self, request, pk, *args, **kwargs):
    #     return self.retrieve(request, id=pk)

    # def put(self, request, pk, *args, **kwargs):
    #     return self.update(request, id=pk)

    # def patch(self, request, pk, *args, **kwargs):
    #     return self.partial_update(request, id=pk)

    # def delete(self, request, pk, *args, **kwargs):
    #     return self.destroy(request, id=pk)

@api_view(['GET', 'PUT', 'DELETE'])
def song_detail(request, pk):
    song = Song.objects.get(pk = pk) #instance
    if request.method == 'GET':
        serializer = SongSerializer(song)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = SongSerializer(song, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        song.delete()
        return HttpResponse(status=status.HTTP_200_OK)


# class LyricList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
#     queryset = Lyric.objects.all()
#     serializer_class = LyricSerializer

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)
@api_view(['GET', 'POST'])
def lyriclist(request):
    if request.method == 'GET':
        lyric = Lyric.objects.all() #Queryset
        serializer = SongSerializer(lyric, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = SongSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class LyricDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
#     queryset = Lyric.objects.all()
#     serializer_class = LyricSerializer


#     def get(self, request, pk, *args, **kwargs):
#         return self.retrieve(request, id=pk)

#     def put(self, request, pk, *args, **kwargs):
#         return self.update(request, id=pk)

#     def delete(self, request, pk, *args, **kwargs):
#         return self.destroy(request, id=pk)
@api_view(['GET', 'PUT', 'DELETE'])
def lyric_detail(request, pk):
    lyric = Lyric.objects.get(pk = pk) #instance
    if request.method == 'GET':
        serializer = SongSerializer(lyric)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = SongSerializer(lyric, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        lyric.delete()
        return HttpResponse(status=status.HTTP_200_OK)
