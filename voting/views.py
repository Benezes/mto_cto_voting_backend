from django.contrib.auth.models import User
from rest_framework import generics, permissions, status
from rest_framework.response import Response

from .models import Post, Vote
from .permissions import IsOwnerOrReadOnly
from .serializers import PostSerializer, UserSerializer, VoteSerializer


class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.AllowAny,)


class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)


class VoteCreate(generics.CreateAPIView):
    serializer_class = VoteSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def create(self, request, *args, **kwargs):
        post_id = self.kwargs.get("pk")
        post = Post.objects.get(pk=post_id)
        value = request.data.get("value")

        if value not in [Vote.UPVOTE, Vote.DOWNVOTE]:
            return Response(
                {"error": "Invalid vote value"}, status=status.HTTP_400_BAD_REQUEST
            )

        try:
            vote = Vote.objects.get(user=request.user, post=post)
            if vote.value == value:
                vote.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)
            else:
                vote.value = value
                vote.save()
        except Vote.DoesNotExist:
            vote = Vote.objects.create(user=request.user, post=post, value=value)

        serializer = self.get_serializer(vote)
        return Response(serializer.data, status=status.HTTP_200_OK)
