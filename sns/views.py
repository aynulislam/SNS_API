from rest_framework.views import APIView, status
from .serializers import RequestSerializer,BlockSerializer,FollowSerializer,FriendSerializer
from rest_framework.response import Response
from .models import SnRequest, SnFriend, SnBlock, SnFollow
from django.shortcuts import get_object_or_404
# Create your views here.


#Done.......
class SnGiveFriendRequest(APIView):
    def post(self, request):
        data = request.data
        if request.user.id == int(data["user_id"]):
            print(data)
            serializer = RequestSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response({"response": "Success"}, status=status.HTTP_201_CREATED)
            else:
                print(serializer.errors)
                return Response({"response": "Bad Request"}, status = status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"response": "Unauthorized"}, status=status.HTTP_401_UNAUTHORIZED)


#Done........
class DeleteRequest(APIView):

    def delete(self, request, pk, format=None):
        instance = get_object_or_404(SnRequest,pk=pk)
        print("hello")
        r_to = instance.user_id_to
        if r_to == request.user:
            instance.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({"response": "Unauthorized"}, status=status.HTTP_401_UNAUTHORIZED)


#Done....
class AcceptRequest(APIView):
    def post(self, request, pk, format=None):
        instance = get_object_or_404(SnRequest, pk = pk)
        r_from = instance.user_id
        r_to = instance.user_id_to
        print(r_to," ", request.user)
        if r_to == request.user:
            serializer = FriendSerializer(data={"user_id":r_from.id,"user_id_to":r_to.id})
            if serializer.is_valid():
                serializer.save()
                instance.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)
            else:
                print(serializer.errors)
                return Response({"response": "Bad Request"}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"response": "Unauthorized"}, status=status.HTTP_401_UNAUTHORIZED)


#Done....
class SkipRequest(APIView):
    def patch(self, request, pk):
        instance = get_object_or_404(SnRequest, pk=pk)
        r_from = instance.user_id
        r_to = instance.user_id_to

        if r_to == request.user:
            serializer = FollowSerializer(data={"follow_id": r_from.id, "user_id_to": r_to.id})
            if serializer.is_valid():
                serializer.save()
                instance.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)
            else:
                print(serializer.errors)
                return Response({"response": "Bad Request"}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"response": "Unauthorized"}, status=status.HTTP_401_UNAUTHORIZED)


#Done...
class BlockFriend(APIView):
    def patch(self, request, pk):
        instance = get_object_or_404(SnFriend, pk=pk)
        r_from = instance.user_id
        r_to = instance.user_id_to

        if r_to == request.user:
            serializer = BlockSerializer(data={"block_id": r_from.id, "user_id_to": r_to.id})
            if serializer.is_valid():
                serializer.save()
                instance.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)
            else:
                print(serializer.errors)
                return Response({"response": "Bad Request"}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"response": "Unauthorized"}, status=status.HTTP_401_UNAUTHORIZED)


#Done...
class UnBlock(APIView):
    def delete(self, request, pk):
        instance = get_object_or_404(SnBlock,pk=pk)
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


#Done...
class UnFriend(APIView):
    def delete(self, request, pk):
        instance = get_object_or_404(SnFriend, pk=pk)
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


#Done....
class UnFollow(APIView):
    def delete(self, request, pk):
        instance = get_object_or_404(SnFollow, pk=pk)
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


#Done...
class SnFollowView(APIView):
    def post(self, request):
        data = request.data

        if request.user.id == int(data["follow_id"]):
            print("Yesssss....")
            serializer = FollowSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response({"response": "Success"}, status=status.HTTP_201_CREATED)
            else:
                return Response({"response": "Bad Request"}, status = status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"response": "Unauthorized"}, status=status.HTTP_401_UNAUTHORIZED)
