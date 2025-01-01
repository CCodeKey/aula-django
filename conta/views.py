from django.shortcuts import render
from .models import Topico 

def home(request):
    return render(request, 'conta/index.html')

def topics(request):
    topics = Topico.objects.order_by('data')
    context = {'topics':topics}
    return render(request, 'conta/topics.html', context)

def topic(request, topic_id):
    topic = Topico.objects.get(id = topic_id)
    entries = topic.comunicado_set.order_by('-data')
    context = {'topic':topic,'entries':entries}
    return render(request, 'conta/topic.html', context)

    