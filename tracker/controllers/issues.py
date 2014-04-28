from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.contrib.syndication.views import Feed
from django.core.context_processors import csrf
from django.forms import forms
from django.forms.models import ModelForm
from django.forms.widgets import HiddenInput
from django.shortcuts import redirect
from django.template import RequestContext
from djangox.mako.shortcuts import render_to_response
from tracker.controllers.actions import ActionForm
from tracker.models import Issue, Tag, IssueHistory, Comment
from django.core.exceptions import ObjectDoesNotExist

import re

class IssueForm(ModelForm):

    class Meta:
        model = Issue
        fields = ['writer', 'status', 'title', 'content']
        widgets = {
            'writer': HiddenInput(),
            'status': HiddenInput(),
        }


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['writer', 'issue', 'content']
        widgets = {
            'writer': HiddenInput(),
            'issue': HiddenInput(),
        }


def strip_tags(text):
    return re.sub('<[^>]+>', '', text)

def index(request):
    objects = Issue.objects.order_by('-updated')

    if 'tag' in request.GET:
        for tag in request.GET.getlist('tag'):
            objects = objects.filter(tags__name=tag)
    else: return render_to_response('issues/index.html', locals())

@login_required
def new(request):
    form = IssueForm(initial={'writer': request.user,
                                            'status': 'open',
                                            })
    return render_to_response('issues/new.html', locals(), RequestContext(request))

@login_required
def create(request):
    form = IssueForm(request.POST)
    if form.is_valid():
        issue = form.save(commit=False)

    issue.updated = datetime.now()
    issue.save()
    issue.save_history()
    # issue.update_tags(request.POST['tags'])

    return redirect('/issues/%d' % issue.id)

def show(request, resource_id):
    issue = Issue.objects.get(id=resource_id)
    issue.read_count += 1
    issue.save()

    if request.user.is_anonymous():
        user_vote = None
    else:
        try:
            user_vote = issue.vote_set.get(voter=request.user)
        except ObjectDoesNotExist:
            user_vote = None

    action_form = ActionForm(initial={'writer': request.user,
                                        'issue': issue})
    comment_form = CommentForm(initial={'writer': request.user,
                                        'issue': issue})

    return render_to_response('issues/show.html', locals(), RequestContext(request))

@login_required
def edit(request, resource_id):
    issue = Issue.objects.get(id=resource_id)
    form = IssueForm(instance=issue)
    return render_to_response('issues/edit.html', locals(), RequestContext(request))

@login_required
def update(request, resource_id):
    issue = Issue.objects.get(id=resource_id)
    issue.title = request.POST['title']
    issue.content=request.POST['content']
    issue.save()

    # issue.update_tags(request.POST['tags'])

    issue.save_history()

    return redirect('/issues/%d' % issue.id)

def destroy(request, resource_id):
    issue = Issue.objects.get(id=resource_id)
    issue.delete()
    return redirect('/issues/')


def histories(request, resource_id):
    issue = Issue.objects.get(id=resource_id)
    return render_to_response('issues/histories.html', locals())

def history(request, resource_id):
    history = IssueHistory.objects.get(id=resource_id)
    return render_to_response('issues/history.html', locals())

@login_required
def restore(request, resource_id):
    history = IssueHistory.objects.get(id=resource_id)
    history.restore()
    return redirect('/issues/%d' % history.target.id)
