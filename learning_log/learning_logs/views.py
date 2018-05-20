from django.shortcuts import render
from django.http import HttpResponseRedirect,Http404
from django.urls import reverse
from .models import Topic,Entry
from .forms import TopicForm,EntryForm
from django.contrib.auth.decorators import login_required
def index(request):
	return render(request,'learning_logs/index.html')
def topics(request):
	"""显示所有主题"""
	topics = Topic.objects.order_by('date_added')
	context = {'topics':topics}
	return render(request,'learning_logs/topics.html',context)
@login_required
def topic(request,topic_id):
	"""show the item in topics"""
	topic = Topic.objects.get(id=topic_id)
	entries = topic.entry_set.order_by('-date_added')
	context = {'topic':topic,'entries':entries}
	return render(request,'learning_logs/topic.html',context)
@login_required
def new_topic(request):
	"""添加新主题"""
	if request.method != 'POST':
		form = TopicForm()
	else:
		form = TopicForm(request.POST)
		if form.is_valid():
			new_topic = form.save(commit = False)
			new_topic.owner = request.user
			new_topic.save()
			return HttpResponseRedirect(reverse('learning_logs:topics'))
	context = {'form':form}
	return render(request,'learning_logs/new_topic.html',context)
@login_required
def new_entry(request,topic_id):
	"""在特定的主题中添加新条目"""
	topic = Topic.objects.get(id = topic_id)
	if topic.owner != request.user :
		return HttpResponseRedirect(reverse('learning_logs:topics'))
	if request.method != 'POST':
		form = EntryForm
	else:
		form = EntryForm(data=request.POST)
		if form.is_valid():
			new_entry = form.save(commit=False)
			new_entry.topic = topic
			new_entry.save()
			return HttpResponseRedirect(reverse('learning_logs:topic',args=[topic.id]))
	context = {'topic':topic,'form':form}
	return render(request,'learning_logs/new_entry.html',context)

@login_required
def edit_entry(request,entry_id):
	"""编辑既有条目"""
	entry = Entry.objects.get(id=entry_id)
	topic = entry.topic
	if topic.owner != request.user:
		return HttpResponseRedirect(reverse('learning_logs:topics'))
	if request.method != 'POST':
		form = EntryForm(instance = entry)
	else:
		form = EntryForm(instance=entry,data = request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('learning_logs:topic',args=[topic.id]))
	context = {'entry':entry,'topic':topic,'form':form}
	return render(request,'learning_logs/edit_entry.html',context)		
# Create your views here.
