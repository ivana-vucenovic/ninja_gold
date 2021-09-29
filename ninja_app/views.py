from django.shortcuts import render, redirect
from datetime import datetime
import random

def ninja(request):
    if 'gold' not in request.session or 'activities' not in request.session:
        request.session['gold'] = 0
        request.session['activities'] = []
    context = {
        "activities":request.session['activities']
    }
    return render(request, 'ninja.html', context)

def process_money(request):
    if request.method == 'POST':
        my_gold = request.session['gold']
        activities = request.session['activities']
        location = request.POST['location']

        if location == 'farm':
            all_gold = round(random.random() * 10 + 10)
        elif location == 'cave':
            all_gold = round(random.random() * 5 + 5)
        elif location == 'house':
            all_gold = round(random.random() * 3 + 2)
        else:
            location == 'casino'
            win_loose = round(random.random())
            if win_loose == 1:
                all_gold = round(random.random() *50)
            else:
                all_gold = round(random.random() *50) * -1 

        my_gold += all_gold
        request.session['gold'] = my_gold

        date_time = datetime.now().strftime("%m/%d/%Y %I:%M%p")

        if all_gold >= 0:
            str = f'Earned ${all_gold} from the {location} {date_time}'
        else:
            all_gold *= -1
            str = f'Loose ${all_gold} from the {location} {date_time}'

        activities.insert(0, str)
        request.session['activities'] = activities

    return redirect('/')
# Create your views here.
