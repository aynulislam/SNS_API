from rest_framework.views import APIView, status
from rest_framework.response import Response
from .models import Share
from .serializers import ShareSerializers


# Create your views here.
class ShareApiList(APIView):
    def get(self,request,pk):
        shares = Share.objects.all().filter(post=pk)
        print(shares)
        if shares:
            print("True")
            serializers = ShareSerializers(shares, many=True)
            return Response(serializers.data)
        else:
            return Response(status.HTTP_400_BAD_REQUEST)

    def post(self,request):
        data = request.data
        data["user"] = request.user.id
        serializers = ShareSerializers(data=data)
        if serializers.is_valid():
            serializers.save()
            return Response({"response": "Success"}, status=status.HTTP_201_CREATED)
        else:
            print(serializers.errors)
            return Response({"response": "Bad Request"}, status=status.HTTP_400_BAD_REQUEST)
