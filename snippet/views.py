import io
from rest_framework.parsers import JSONParser
from django.shortcuts import render
from snippet.models import Student
from snippet.serializers import StudentSer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

# for single record
def student_details(request,pk):
    stu=Student.objects.get(id=pk)
    ser=StudentSer(stu)
    #### we can write the below code or we can directly write the JSONResponse ####
    # json_data=JSONRenderer().render(ser.data)
    # return HttpResponse(json_data, content_type='application/json')
    return JsonResponse(ser.data)

#for all records
def student_det(request):
    stu=Student.objects.all()
    ser=StudentSer(stu,many=True)
    json_data=JSONRenderer().render(ser.data)
    return HttpResponse(json_data, content_type='application/json')

#for inserting data into database(deserialization)
@csrf_exempt
def create(request):
    if request.method == 'POST':
        json_data=request.body
        stream=io.BytesIO(json_data)
        python_data=JSONParser().parse(stream)
        serializer= StudentSer(data= python_data)
        if serializer.is_valid():
            serializer.save()
            res={'msg':'Parser worked'}
            json_data=JSONRenderer().render(res)
            return HttpResponse(json_data,content_type='application/json')
            # return JsonResponse(res)
        json_data=JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type='application/json')
