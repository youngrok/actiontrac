from datetime import datetime
from django.forms.models import ModelForm
from django.forms.widgets import HiddenInput
from django.http import HttpResponseRedirect
from django.template.context import RequestContext
from djangox.mako.shortcuts import render_to_response
from tracker.models import Action


class ActionForm(ModelForm):

    class Meta:
        model = Action
        fields = ['issue', 'writer', 'status', 'title', 'content']
        widgets = {
            'issue': HiddenInput(),
            'writer': HiddenInput(),
            'status': HiddenInput(),
        }

def new(request):
    form = ActionForm()
    return render_to_response('actions/new.html', locals(), RequestContext(request))

def create(request):
    form = ActionForm(request.POST)
    if form.is_valid():
        action = form.save(commit=False)

    action.updated = datetime.now()
    action.save()
    action.save_history()
    # issue.update_tags(request.POST['tags'])

    return HttpResponseRedirect('/issues/%d' % action.issue.id)