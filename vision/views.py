import pymongo
from django.shortcuts import render
from django.http import HttpResponse


client = pymongo.MongoClient('localhost', 27017)
db = client.go_db
collection = db.work_detail


def index(request):
    datas = collection.find()
    return render(request, 'vision/index.html', context={'datas': datas})


def about_python(request):
    pass
