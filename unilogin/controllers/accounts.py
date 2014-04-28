# coding=UTF-8
from django.contrib import messages
from django.contrib.auth import logout as auth_logout
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.template.context import RequestContext
from djangox.mako.shortcuts import render_to_response


def login(request):
    return render_to_response('accounts/login.html', locals(), RequestContext(request))

def logout(request):
    """Logs out user"""
    auth_logout(request)
    return HttpResponseRedirect('/')
    