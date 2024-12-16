from django.shortcuts import render,HttpResponse
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .models import Student
from .serializer import StudentSerializer
import io
from django.views.decorators.csrf import csrf_exempt


# Create your views here.

@csrf_exempt
def student_api(request):
    if request.method == 'GET':
        stu= Student.objects.all()
        ser= StudentSerializer(stu, many=True)
        json_byte_data= JSONRenderer().render(ser.data)
        return HttpResponse(json_byte_data,content_type="application/json")
    if request.method == 'POST':
        json_data = request.body
        stream= io.BytesIO(json_data)
        pydata= JSONParser().parse(stream)
        serializer= StudentSerializer(data=pydata)
        if serializer.is_valid():
            serializer.save()
            json_data=JSONRenderer().render(serializer.data)
        else:
            json_data=JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data,content_type="application/json")
@csrf_exempt
def student_api_detail(request,id):
    if request.method=="GET":
        stu=Student.objects.get(id=id)
        ser=StudentSerializer(stu)
        json_byte_data=JSONRenderer().render(ser.data)
        return HttpResponse(json_byte_data,content_type="application/json")
    
    if request.method=="PUT":
        json_data=request.body
        stream=io.BytesIO(json_data)
        pydata=JSONParser().parse(stream)
        stu_obj= Student.objects.get(id=id)
        serializer=StudentSerializer(stu_obj,data=pydata,partial=True)
        if serializer.is_valid():
            serializer.save()
            json_data=JSONRenderer().render(serializer.data)
        else:
            json_data=JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data,content_type="application/json")
    if request.method=="DELETE":
        stu_obj=Student.objects.get(id=id)
        stu_obj.delete()
        res={
            "msg":"deleted"
        }
        json_data=JSONRenderer().render(res)
        return HttpResponse(json_data,content_type="application/json")





