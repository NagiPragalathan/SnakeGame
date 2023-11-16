from django.shortcuts import render, redirect
from .models import HighScore, ScoreTable
from django.db.models import Max
import csv
from django.http import HttpResponse
from django.http import JsonResponse
from django.db import transaction
import time
import random 
def generate_unique_usr_id():
    timestamp = int(time.time())
    random_number = random.randint(1, 1000)  # Adjust the range as needed
    return int(f"{timestamp}{random_number}")

def StartGame(request, id):
    print(id)
    return render(request,"index.html",{"id":id})

def update_score(request, id):
    if request.method == 'POST':
        # Assuming you have 'score' and 'timing' in the POST data
        score = request.POST.get('score')
        timing = request.POST.get('timing')
        print(score, timing)
        # Make sure 'score' and 'timing' are not None before proceeding
        if score is not None and timing is not None:
            usr_obj = ScoreTable.objects.get(usr_id=id)
            usr_obj.score = score
            usr_obj.timing = timing
            usr_obj.save()
            onj = HighScore(usr_id=id,score=score)
            onj.save()

            return JsonResponse({'status': 'success'})
        else:
            return JsonResponse({'status': 'error', 'message': 'Invalid data'})
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method'})

def userinp(request):
    try:
        score_obj = ScoreTable.objects.order_by('-score').first()
        score = score_obj.score
        print("Worked",score_obj.usr_id, score)
    except:
        score=0
        usr_obj = None
    if score == None:
        score = 0
    if request.method == 'POST':
        # Retrieve data from the POST request
        name = request.POST.get('name')
        age = int(request.POST.get('age'))
        gender = request.POST.get('gender')
        if name and age:
            obj_usr = len(ScoreTable.objects.all())
            print(obj_usr,obj_usr+1,obj_usr+1)
            # Create a new ScoreTable instance
            with transaction.atomic():
                    new_score = ScoreTable(
                        usr_id = generate_unique_usr_id(),
                        name=name,
                        age=age,
                        gender=gender,
                        score=score,
                        timing=0
                    )

            # Save the instance to the database
            new_score.save()

            return redirect("game", new_score.usr_id)
        else:
            return render(request,"DataGetter.html", {"score":score, 'obj':score_obj.name})
    else:
        return render(request,"DataGetter.html",{"score":score,"obj":score_obj.name})


def leaderboard(request):
    # Query the top scores, order by score in descending order
    top_scores = ScoreTable.objects.order_by('-score')[:10]  # Adjust the number as needed

    context = {'top_scores': top_scores}
    return render(request, 'leaderboard.html', context)


def download_csv(request):
    # Query all data from ScoreTable
    scores = ScoreTable.objects.all()

    # Create a response with CSV content type
    response = HttpResponse(content_type='text/csv')
    
    # Set the header for the CSV file
    response['Content-Disposition'] = 'attachment; filename="scores.csv"'

    # Create a CSV writer
    writer = csv.writer(response)

    # Write header row
    writer.writerow(['User ID', 'Name', 'Age', 'Gender', 'Score', 'Timing'])

    # Write data rows
    for score in scores:
        writer.writerow([score.usr_id, score.name, score.age, score.gender, score.score, score.timing])

    return response