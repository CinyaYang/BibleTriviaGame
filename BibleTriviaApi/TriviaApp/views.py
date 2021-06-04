from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse
from django.core.files.storage import default_storage
from rest_framework.parsers import JSONParser

from TriviaApp.models import BibleQuestion, QuestionInfo
from TriviaApp.serializers import BibleQuestionSerializer, QuestionInfoSerializer

# Create your views here.

@csrf_exempt
def bibleQuestionApi(request, category=0):
    if request.method == 'GET':
        bibleQuestion = BibleQuestion.objects.raw("select * from TriviaApp_biblequestion where Category = " + category)
        bibleQuestion_serializer = BibleQuestionSerializer(bibleQuestion, many = True)
        return JsonResponse(bibleQuestion_serializer.data, safe = False)
    elif request.method == 'POST':
        bibleQuestion_data = JSONParser().parse(request)
        bibleQuestion_serializer = BibleQuestionSerializer(data = bibleQuestion_data)
        if bibleQuestion_serializer.is_valid():
            bibleQuestion_serializer.save()
            return JsonResponse('Added Successfully', safe = False)
        return JsonResponse('Failed to add', safe = False)
    elif request.method == 'PUT':
        bibleQuestion_data = JSONParser().parse(request)
        print(bibleQuestion_data['Answered'])
        bibleQuestion = BibleQuestion.objects.get(Id = bibleQuestion_data['Id'])
        bibleQuestion_serializer = BibleQuestionSerializer(bibleQuestion, data = bibleQuestion_data)
        if bibleQuestion_serializer.is_valid():
            bibleQuestion_serializer.save()
            return JsonResponse('Updated Successfully', safe = False)
        return JsonResponse('Failed to update', safe = False)
    

       
@csrf_exempt
def questioInfoApi(request, id=0):
    if request.method == 'GET':
        questionInfo = QuestionInfo.objects.get(Id = id)
        questionInfo_serializer = QuestionInfoSerializer(questionInfo)
        return JsonResponse(questionInfo_serializer.data, safe = False)
    elif request.method == 'POST':
        questionInfo_data = JSONParser().parse(request)
        
        questionInfo_serializer = QuestionInfoSerializer(data = questionInfo_data)
        if questionInfo_serializer.is_valid():
            questionInfo_serializer.save()
            return JsonResponse('Added Successfully', safe = False)
        return JsonResponse('Failed to add', safe = False)
    
    elif request.method == 'PUT':
        questionInfo_data = JSONParser().parse(request)
        questionInfo = QuestionInfo.objects.get(questionInfoId = questionInfo_data['Id'])
        questionInfo_serializer = QuestionInfoSerializer(questionInfo, data = questionInfo_data)
        if questionInfo_serializer.is_valid():
            questionInfo_serializer.save()
            return JsonResponse('Updated Successfully', safe = False)
        return JsonResponse('Failed to update', safe = False)
    
    elif request.method == 'DELETE':
        questionInfo = QuestionInfo.objects.get(questionInfoId = id)
        questionInfo.delete()
        return JsonResponse('Deleted Successfully', safe = False)

@csrf_exempt
def updateStatusApi(request):
    if request.method == 'PUT':
        questionInfo_data = JSONParser().parse(request)
        questionInfo = QuestionInfo.objects.get(questionInfoId = questionInfo_data['Id'])
        questionInfo_serializer = QuestionInfoSerializer(questionInfo, data = questionInfo_data)
        if questionInfo_serializer.is_valid():
            questionInfo_serializer.save()
            return JsonResponse('Updated Successfully', safe = False)
        return JsonResponse('Failed to update', safe = False)

@csrf_exempt
def saveFile(request):
    print(request.FILES)
    file = request.FILES['uploadedFile']
    file_name = default_storage.save(file.name, file)

    return JsonResponse(file_name, safe = False)