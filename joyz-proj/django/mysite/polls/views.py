from django.shortcuts import render, get_object_or_404
from django.template import loader 
from .models import Question
from django.http import Http404,HttpResponse,HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def index(request):
    latest_question_list\
	 = Question.objects\
		   .order_by('-pub_date')[:5]
    #template = loader.get_template('polls/index.html')
    context = {'latest_question_list':latest_question_list,}
    #output = ', '.join([q.question_text for q in latest_question_list])
    #return HttpResponse(template.render(context,request))
    return render(request, 'polls/index.html',context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk = question_id)
    #msg = "You are looking at question {}." 
    #return HttpResponse(msg.format(question_id))	
    return render(request,'polls/detail.html',{'question':question}) 

def results(request, question_id):
    response = "You are looking at the results of question {}."
    return HttpResponse(response.format(question_id))

def vote(request, question_id):
	question = get_object_or_404(Question, pk = question_id)
	try:
		selected_choice = \
			question.choice_set.get(\
				pk=request.POST['choice'])
	except(KeyError, Choice.DoesNotExist):
		#redisplay the question voting form
		return render(request, 'polls/detail.html'\
			,{'question':question,\
				'error_message': "You didn't select a choice"})
 

	else:
		selected_choice.votes += 1
		selected_choice.save()
		return HttpResponseRedirect(reverse('polls:results',args=(question.id,)))

def results(request, question_id):
	question = get_object_or_404(Question, pk = question_id)
	return render(request,"polls/results.html",{'question':question})
