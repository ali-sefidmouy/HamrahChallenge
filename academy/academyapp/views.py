from django.db import models
from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view


def sum(a, b):
    return int(a) + int(b)


@api_view(['GET',])
def SumView(request):
    if request.method == 'GET':
        a = request.query_params.get('a', None)
        b = request.query_params.get('b', None)
        if a is None or b is None:
            return JsonResponse({"error": "a or b is undefined!"}, status=status.HTTP_400_BAD_REQUEST)
        try:
            return JsonResponse({"sum": sum(a, b)}, status=status.HTTP_200_OK)
        except ValueError as e:
            return JsonResponse({"error": "Invalid input! Please provide integer number for a & b"}, status=status.HTTP_400_BAD_REQUEST)
