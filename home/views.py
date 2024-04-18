
from django.template import loader
from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    template = loader.get_template("home.html")
    return HttpResponse(template.render())


def trainer(request):
    template = loader.get_template("trainer.html")
    return HttpResponse(template.render())


def signup(request):
    template = loader.get_template("signup.html")
    return HttpResponse(template.render())


def why(request):
    template = loader.get_template("why.html")
    return HttpResponse(template.render())


def contact(request):
    template = loader.get_template("contact.html")
    return HttpResponse(template.render())
