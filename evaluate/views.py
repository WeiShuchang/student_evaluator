from django.shortcuts import render
from datetime import datetime
from .functions import *

# Create your views here.
def home(request):
    return render(request, 'evaluate/evaluation_form.html')

def evaluated(request):
    class_status = request.GET.get('class_status')
    class_day = request.GET.get('class_day')
    endtheme = request.GET.get('endtheme')
    material = request.GET.get('material')
    discussion = request.GET.get('discussion')
    date_now = datetime.now()
    date_final = date_now.strftime("%m-%d-%Y")

    day = identify_day(class_day)
    status = identify_status(class_status)
    material = identify_material(int(material))
    endtheme = identify_endtheme(int(endtheme))


    student = request.GET.get('students')
    return render(request, 'evaluate/evaluated_form.html',
                  {'student':student,
                   'class_status':status,
                   'date':date_final,
                   'class_day':day, 
                   'material':material,
                   'discussion':discussion,
                   'endtheme':endtheme})



    