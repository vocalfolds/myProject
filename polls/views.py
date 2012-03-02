# Create your views here.
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.template import RequestContext
from polls.models import Poll, Choice

def vote(request, poll_id):
	p = get_object_or_404(Poll, pk=poll_id)
	try:
		selected_choice = p.choice_set.get(pk=request.POST['choice'])
	except (KeyError, Choice.DoesNotExist):
		#Redisplay the poll voting from.
		return render_to_response('polls/detail.html', {
				'poll': p,
				'error_message': "Your didn't select a choice.",
				}, context_instance=RequestContext(request))
	else:
		selected_choice.votes += 1
		selected_choice.save()
		# Always return an HttpResponseRedirect after successfully dealing 
		#with POST data. This prevents data form being posted twice if a 
		# user hit the Back button.
		return HttpResponseRedirect(reverse('poll_results', args=(p.id,)))



