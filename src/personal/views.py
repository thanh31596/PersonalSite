from django.shortcuts import render
# from personal.models import Question
from account.models import Account

# Create your views here.
def home_screen_view(request):

	context = {}
	# # context['some_string'] = "this is some string passed into the view"#passing variable some_string
	# # context['some_number'] = 2321321
	# #context ={
	# 	#'dsafa': 1111,
	# 	#'movie': "ASda"
	# #}

	# # list_of_values =[]
	# # list_of_values.append("first_entry")
	# # list_of_values.append("sec_entry")
	# # list_of_values.append("third_entry")
	# # list_of_values.append("fourth_entry")

	# # context['list_of_values']=list_of_values

	# questions = Question.objects.all()
	# context['questions']=questions

	accounts		 	=Account.objects.all()
	context['accounts']	=accounts

	return render(request, 'personal/home.html', context)