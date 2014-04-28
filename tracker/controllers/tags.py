from tracker.models import Tag
from djangox.mako.shortcuts import render_to_response
def index(request, resource_id):
    tags = Tag.objects.all()
    return render_to_response('tags/index.html', locals())