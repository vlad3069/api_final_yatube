from django.shortcuts import get_object_or_404
from rest_framework import permissions, viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend

from posts.models import Comment, Group, Post, Follow
from api.ViewSet import ListCreateViewSet
from rest_framework.pagination import LimitOffsetPagination

from .permission import CustomerAccessPermission
from .serializers import CommentSerializer, GroupSerializer, PostSerializer, FollowSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = LimitOffsetPagination 

    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly, CustomerAccessPermission]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly]


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly, CustomerAccessPermission]

    def get_queryset(self):
        post_id = self.kwargs.get('post_id')
        post = get_object_or_404(Post, pk=post_id)
        return post.comments

    def perform_create(self, serializer):
        post_id = self.kwargs.get('post_id')
        author = self.request.user
        post = get_object_or_404(Post, pk=post_id)
        serializer.save(author=author, post=post)



class FollowViewSet(ListCreateViewSet):
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    search_fields = ('following__username',) 

    permission_classes = [
        permissions.IsAuthenticated, CustomerAccessPermission]

    def get_queryset(self):
        return Follow.objects.filter(user=self.request.user) 

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
