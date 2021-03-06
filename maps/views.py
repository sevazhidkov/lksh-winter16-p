from django.contrib.auth.models import AnonymousUser
from django.shortcuts import render, redirect
from maps.actions import questions
from maps.models import AnswerSet
import json


def logged_in(request):
    return request.user is not None and not isinstance(request.user, AnonymousUser)


def index(request):
    if logged_in(request):
        return redirect('choice')
    return render(request, 'maps/index.html')


def start(request, question_set_id):
    if not logged_in(request):
        return redirect('/')
    answer_set = questions.create_answer_set(request.user, question_set_id)
    return redirect('/run/' + str(answer_set.id) + '/0')


def get_choice(request):
    if not logged_in(request):
        return redirect('/')
    sets = questions.question_set_list()
    return render(request, 'maps/choice.html', {'sets': sets})


def run(request, answer_set_id, idx):
    if not logged_in(request):
        return redirect('/')
    answer_set = AnswerSet.objects.get(pk=answer_set_id)
    idx = int(idx)
    questions = answer_set.question_set.get_questions()
    if idx >= len(questions):
        return redirect('/results/' + str(answer_set_id))
    question = questions[idx]
    area = question.map_area.display_area
    contour_area = question.map_area.contour_map_reference
    binary = question.map_area.contour_map_image
    return render(request, 'maps/task.html', {
        'task': {'title': 'Task #' + str(idx + 1), 'time': question.max_duration.seconds,
                 'bounds': [(area.north, area.west), (area.south, area.east)],
                 'contour_bounds': None if contour_area is None else [(contour_area.west, contour_area.north),
                                                                      (contour_area.east, contour_area.south)],
                 'use_overlay': (binary is not None and binary != b''),
                 'answer_set_id': answer_set_id, 'idx': idx, 'question_id': question.id,
                 'statement': json.loads(question.statement_data)['name']},
    })


def results(request, answer_set_id):
    if not logged_in(request):
        return redirect('/')
    return render(request, 'maps/results.html', {})
