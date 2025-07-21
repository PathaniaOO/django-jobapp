
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import redirect
from django.urls import reverse
from django.template import loader
from app.models import JobPost


job_title=[
    "Software Engineer",
    "Data Scientist",
    "Project Manager",
    "Web Developer",
]

job_description=[
    "Develop and maintain software applications.",
    "Analyze data and build predictive models.",
    "Manage projects and coordinate teams.",
    "Design and implement web applications.",
]

class Tempclass:
    x=5
# def hello_world(request):
#     return HttpResponse("<h3>Welcome to Jobapp</h3>")
def home(request):
    return render(request, 'app/home.html')
def hello(request):
    #template= loader.get_template('app/hello.html')
    is_authenticated = False  # Simulating an authenticated user; replace with actual authentication check
    first_dict={'Age':25,'City':'New York', 'Country':'USA', 'Skills':['Python', 'Django', 'JavaScript']}
    first_list=["Software Engineer","Data Scientist","Project Manager","Web Developer"]
    temp=Tempclass()
    context={"name":"Django Developer","first_list":first_list,"temp_object":temp,"first_dict":first_dict,"is_authenticated":is_authenticated}
    #return HttpResponse(template.render(context, request)) 
    return render(request, 'app/hello.html', context)

def job_list(request):
    jobs=JobPost.objects.all()
    context = {'jobs': jobs}
    return render(request, 'app/job_list.html', context)
    #<ul><li>job1</li><li>job2</li></ul>
    #j is the no of jobs
    #job_title is a list of job titles
    # list_of_jobs="<ul>"
    # for j in job_title:
    #     job_id= job_title.index(j)
    #     details_url=reverse('job_details',args=(job_id,))
    #     list_of_jobs += f"<li><a href='{details_url}'>{j}</a></li>"
    # list_of_jobs+="</ul>"
    # return HttpResponse(list_of_jobs)

    
        

def details(request,id):
    try:
        if id == 0:
            return redirect(reverse('job_list'))
        # context={'job_title': job_title[id], 'job_description': job_description[id]}
        job=JobPost.objects.get(id=id)
        context = {'job': job}
        return render(request, 'app/job_details.html', context)
    except (ValueError, IndexError):
        return HttpResponseNotFound("<h1>Job not found</h1>")
    # try:
    #     if id == 0:
    #         return redirect(reverse('job_list'))
    #     return_html = f"<h1>{job_title[id]}</h1><p>{job_description[id]}</p>"
    #     return HttpResponse(return_html)
    # except IndexError:
    #     return HttpResponseNotFound("<h1>Job not found</h1>")
    
    

