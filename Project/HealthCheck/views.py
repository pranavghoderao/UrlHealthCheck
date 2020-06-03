from django.shortcuts import render,redirect
from django.views.generic import TemplateView
from HealthCheck.utils import util
import requests
from requests.auth import HTTPBasicAuth
from getpass import getpass
import paramiko
import os
# Create your views here.

import socket
socket.getaddrinfo('localhost', 8000)
def show(request):
    ut = util()
    p1 = ut.connect("192.168.147.10","vagrant")
    url1 = 'https://sweet.slb.com:8444/sweet-web/#!/login'
    st1 =ut.status(url1)
    u1_tom = ut.checkTomcat(p1)
    rst1 = {"url":url1,
            "status":st1,
            "ser_tom":u1_tom}

    p1 = ut.connect("192.168.147.10","vagrant")
    url2 ='https://smgs.ams.slb.com/sv/mfgx/login.jsp;jsessionid=16hgq4dgw1acf.sv_ui2'
    st2 =ut.status(url2)
    u2_tom = ut.checkTomcat(p1)
    rst2 = {"url":url2,
            "status":st2,
            "ser_tom":u2_tom}

    p1 = ut.connect("192.168.147.10","vagrant")
    url3 ='https://swpdm.slb.com:7105/Windchill/app/'
    st3 =ut.status(url3)
    u3_tom = ut.checkTomcat(p1)
    rst3 = {"url":url3,
            "status":st3,
            "ser_tom":u3_tom}
    
    p1 = ut.connect("192.168.147.10","vagrant")
    url4 =' https://teams.sugar-land.oilfield.slb.com/App_Site_Select.cfm'
    st4 =ut.status(url4)
    u4_coldfusion = ut.checkTomcat(p1)
    rst4 = {"url":url4,
            "status":st4,
            "ser_coldfusion":u4_coldfusion}

    p1 = ut.connect("192.168.147.10","vagrant")
    url5 ='https://wiki.slb.com/#all-updates'
    st5 =ut.status(url5)
   
    rst5 = {"url":url5,
            "status":st5,
            }

    p1 = ut.connect("192.168.147.10","vagrant")
    url6 ='https://emspeed.slb.com/portal.aspx'
    st6 =ut.status(url6)
    u6_Apppool = ut.checkTomcat(p1)
    u6_IIS = ut.checkTomcat(p1)
    rst6 = {"url":url6,
            "status":st6,
            "ser_apppool":u6_Apppool,
            "ser_IIS":u6_IIS}

    

    p1 = ut.connect("192.168.147.10","vagrant")
    url7 ='https://www.ptr.slb.com/'
    st7 =ut.status(url7)
    u7_Apppool = ut.checkTomcat(p1)
    u7_IIS = ut.checkTomcat(p1)
    rst7 = {"url":url7,
            "status":st7,
            "ser_apppool":u7_Apppool,
            "ser_IIS":u7_IIS}
    

    p1 = ut.connect("192.168.147.10","vagrant")
    url8 ='https://clms.ems.slb.com/emsix.aspx'
    st8 =ut.status(url8)
    u8_Apppool = ut.checkTomcat(p1)
    u8_IIS = ut.checkTomcat(p1)
    rst8 = {"url":url8,
            "status":st8,
            "ser_apppool":u8_Apppool,
            "ser_IIS":u8_IIS}

    p1 = ut.connect("192.168.147.10","vagrant")
    url9 ='https://equality.slb.com/'
    st9 =ut.status(url9)
    u9_coldfusion = ut.checkTomcat(p1)
    u9_IIS = ut.checkTomcat(p1)
    rst9 = {"url":url9,
            "status":st9,
            "ser_coldfusion":u9_coldfusion,
            "ser_IIS":u9_IIS}
   
    
    p1 = ut.connect("192.168.147.10","vagrant")
    url10 ='https://faatracker.slb.com/login.aspx?msg=account'
    st10 =ut.status(url10)
    
    rst10 = {"url":url10,
            "status":st10,
            }
    """
    p1 = ut.connect("192.168.147.10","vagrant")
    url11 ='https://intime.itt.slb.com/'
    st11 =ut.status(url11)
    u11_Apppool = ut.checkTomcat(p1)
    u11_IIS = ut.checkTomcat(p1)
    rst11 = {"url":url11,
            "status":st11,
            "ser_apppool":u11_Apppool,
            "ser_IIS":u11_IIS}
   
    """
    p1 = ut.connect("192.168.147.10","vagrant")
    url12 ='https://www.gems.slb.com/'
    st12 =ut.status(url12)
    u12_tom = ut.checkTomcat(p1)
    rst12 = {"url":url12,
            "status":st12,
            "ser_tom":u12_tom}

    p1 = ut.connect("192.168.147.10","vagrant")
    url13 ='https://www.pdd.slb.com/'
    st13 =ut.status(url13)
    u13_coldfusion = ut.checkTomcat(p1)
    u13_IIS = ut.checkTomcat(p1)
    rst13 = {"url":url13,
            "status":st13,
            "ser_coldfusion":u13_coldfusion,
            "ser_IIS":u13_IIS}
    
    res ={ "u1":rst1,"u2":rst2,"u3":rst3,"u4":rst4,"u5":rst5,
            "u6":rst6,"u7":rst7,"u8":rst8,"u9":rst9,"u10":rst10,
            "u12":rst12,"u13":rst13 }

        

    

    
        
    return render(request,"index.html",{'r': res})

   








