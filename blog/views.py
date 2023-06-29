from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET', 'POST'])
def home(request):
    if request.method == 'GET':
        return Response('<p>GET Home</p>')
    elif request.method == 'POST':
        return Response('<p>POST Home</p>')
