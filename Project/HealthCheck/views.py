from django.shortcuts import render,redirect
from django.views.generic import TemplateView
from HealthCheck.utils import util
import requests
from requests.auth import HTTPBasicAuth
from getpass import getpass
import paramiko
import os
# Create your views here.

def show(request):
    ut = util()
    p1 = ut.connect("192.168.147.10","vagrant")
    url1 = 'https://sweet.slb.com:8444/sweet-web/#!/login'
    st1 =ut.status(url1)
    u1_tom = ut.checkTomcat(p1)
    rst1 = {"url":url1,
            "status":st1,
            "ser_tom":u1_tom}

    return render(request,"index.html",{'res1': rst1})

    