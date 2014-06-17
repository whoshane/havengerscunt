from django.shortcuts import render, get_object_or_404, render_to_response
from django.core.context_processors import csrf
from django.contrib import auth
from score.models import Team, Item


def index(request):
	if request.user.is_authenticated():
		return render(request, "addscore.html")
	else:
		return scoreboard(request)

def scoreboard(request):
	c = {}	
	teams = Team.objects.all()
	teams = teams.order_by("score")
	ordered = teams.reverse()
	c.update({'teams':ordered})
	return render_to_response("index.html", c)

def addscore(request):
	c = {}
	c.update(csrf(request))
	err = {"err":""}
	try:
		team_id = request.POST['team_id']
		item_id = request.POST['item_id']
		score = request.POST['score']
	except Exception:
		index(request)
	if team_id == '' or item_id == '':
		err['err'] = 'Invalid input'
		c.update(err)
		return render_to_response("addscore.html", c)
	try:
		team = Team.objects.get(number=team_id)
	except Team.DoesNotExist:
		err['err'] = 'Team does not exist. Try again.'
		c.update(err)
		return render_to_response("addscore.html", c)
	try:
		item = Item.objects.get(number=item_id)	
	except Item.DoesNotExist:
		err['err'] = 'Item does not exist. Try again.'
		c.update(err)
		return render_to_response("addscore.html", c)
	if team.items.filter(number=item.number).count():
		err['err'] = 'This item has already been scored for this team.'
		c.update(err)
		return render_to_response("addscore.html", c)
	else:
		if item.score == 500:
			try:
				score = int(score)
				if score > 500 or score < 0:
					err['err'] = "Score must be between 0-500"
					c.update(err)
					return render_to_response("addscore.html",c)
				team.score += score
			except Exception:
				err['err'] = "Invalid Score."
				c.update(err)
				return render_to_response("addscore.html",c)
		else:
			team.score += item.score
		team.items.add(item)
		team.save()
		teams = Team.objects.all()
		c.update({'teams':teams})
		return render_to_response("addscore.html", c) 

def login(request):
	c = {}
	c.update(csrf(request))
	username = request.POST.get('username', '')
	password = request.POST.get('password', '')
	user = auth.authenticate(username=username, password=password)
	if user is not None:
		auth.login(request, user)
		return render_to_response("addscore.html", c)
	else:
		err = 'Invalid credentials. don\'t try to cheat!'
		c.update({'err':err})
		return render_to_response("login.html", c)
