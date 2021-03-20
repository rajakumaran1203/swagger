from django.shortcuts import render
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
# Create your views here.
from .responce import my_responce
from .searching import searching
from .serializers import Empserial
from .models import stu
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@swagger_auto_schema(methods=['POST'], responses={201: 'RECORD CREATED', 400: 'Bad Request'},
                     request_body=Empserial)
@api_view(['POST'])
def create_employee(request):
    if request.method == 'POST':
        serialize_data = Empserial(data=request.data)
        if serialize_data.is_valid():
            serialize_data.save()
            return Response(serialize_data.data, status=status.HTTP_201_CREATED)
        return Response(serialize_data.data, status=status.HTTP_400_BAD_REQUEST)


search_record = openapi.Parameter('search_record', openapi.IN_QUERY, type=openapi.TYPE_STRING)


@swagger_auto_schema(methods=['GET'], manual_parameters=[search_record],
                     responses={201: 'RECORD CREATED', 400: 'Bad Request'})
@api_view(['GET'])
def getting_data(request):
    search_re = request.GET.get('search_record', None)
    data = stu.objects.filter(name=search_re)
    result = Empserial(data, many=True)
    return Response(result.data, status=status.HTTP_200_OK)


search = openapi.Parameter('search', openapi.IN_QUERY, type=openapi.TYPE_STRING)


@swagger_auto_schema(methods=['PUT'], manual_parameters=[search],
                     responses={201: 'RECORD CREATED', 400: 'Bad Request'},
                     request_body=Empserial)
@api_view(['PUT'])
def update(request):
    x = request.GET.get('search', None)
    if x is not None:
        try:
            dats = stu.objects.get(name=x)
            print(dats)
        except Exception as e:
            print(e)
        results = Empserial(dats, data=request.data)
        if results.is_valid():
            results.save()
            return Response(results.data, status=status.HTTP_302_FOUND)
    return Response({'Bad request': 'No records found'}, status=status.HTTP_404_NOT_FOUND)


deleteds = openapi.Parameter('deleteds', openapi.IN_QUERY, type=openapi.TYPE_STRING)


@swagger_auto_schema(methods=['GET'], manual_parameters=[deleteds],
                     responses={201: 'RECORD CREATED', 400: 'Bad Request'})
@api_view(['GET'])
def delete(request):
    record = request.GET.get('deleteds', None)
    dats = stu.objects.get(name=record)
    if dats:
        dats.is_delete = True
        dats.save()
        return Response("Record sucessfully", status=status.HTTP_302_FOUND)
    return Response({'Bad request': 'No records found'}, status=status.HTTP_404_NOT_FOUND)


# delete_datas = openapi.Parameter('delete_data', openapi.IN_QUERY, type=openapi.TYPE_STRING)

@swagger_auto_schema(methods=['GET'], responses={201: 'RECORD CREATED', 400: 'Bad Request'})
@api_view(['GET'])
def delete_data(request):
    delete_datas = stu.objects.filter(is_delete=True)
    result = Empserial(delete_datas, many=True)
    return Response(result.data, status=status.HTTP_302_FOUND)


@swagger_auto_schema(methods=['GET'], responses={201: 'RECORD CREATED', 400: 'Bad Request'})
@api_view(['GET'])
def current_data(request):
    # current_datas = request.GET.get('current_datas', None)
    currents = stu.objects.filter(is_delete=False)
    result = Empserial(currents, many=True)
    return Response(result.data, status=status.HTTP_302_FOUND)


@swagger_auto_schema(methods=['GET'], responses={201: 'RECORD CREATED', 400: 'Bad Request'})
@api_view(['GET'])
def getting_all_data(request):
    results = stu.objects.filter(name='kumaran')
    print(results)
    if results:
        re = [my_responce(dats=result) for result in results]
    return Response({"s": re}, status=status.HTTP_200_OK)


filter_data = openapi.Parameter('filter_data', openapi.IN_QUERY, type=openapi.TYPE_STRING)
@swagger_auto_schema(methods=['GET'], manual_parameters=[filter_data],
                     responses={201: 'RECORD CREATED', 400: 'Bad Request'})
@api_view(['GET'])
def filter_field(request):
    search_input1 = request.GET.get('filter_data', None)
    print(search_input1)
    if search_input1 is not None:
        record = searching(search_input=search_input1)
        re = [my_responce(dats=result) for result in record]
        print(re)
        return Response({"success": re}, status=status.HTTP_200_OK)
    return Response("bad request", status=status.HTTP_404_NOT_FOUND)


filter_json_updated = openapi.Parameter('filter_json_updated', openapi.IN_QUERY, type=openapi.TYPE_STRING)

@swagger_auto_schema(methods=['PUT'], manual_parameters=[filter_json_updated],
                     responses={201: 'RECORD CREATED', 400: 'Bad Request'},request_body=Empserial)
@api_view(['PUT'])
def filter_json_update(request):
    #ja = Empserial(data=request.data)
    serializer_data = Empserial(data=request.data)
    if serializer_data.is_valid():
        filter_json = request.GET.get('filter_json_updated',None)
        record = stu.objects.get(name=filter_json)
        jr_data=record.job['opening']
        print(jr_data)
        if record:
            j = serializer_data.data['job']['opening']
            print(j)
            for jr in j:
                if jr not in jr_data:
                    jr_data.append(jr)
                    ju_up={'opening': jr_data}
                    record.j=ju_up
                    record.save()
                    return Response({"Seccuss": serializer_data.data},status=status.HTTP_200_OK)
        else:
            return Response({"Error": "Bad Request"},status=status.HTTP_400_BAD_REQUEST)
'''
filter_json = openapi.Parameter('filter_json', openapi.IN_QUERY, type=openapi.TYPE_STRING)

@swagger_auto_schema(methods=['GET'], manual_parameters=[filter_json_updated],
                     responses={201: 'RECORD CREATED', 400: 'Bad Request'},request_body=Empserial)
@api_view(['GET'])
def filter_json(request):
    filter_json = request.GET.get('filter_json', None)
    record = stu.objects.filter(is_delete=False)
    jr_data = record.job['opening']
    print(jr_data)
    for jr in jr_data:
        if 'python' == jr:
            return Response(record,status=status.HTTP_200_OK)
'''