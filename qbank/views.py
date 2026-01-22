from django.http import JsonResponse
from django.shortcuts import render
from sora.models import questions
from django.template import TemplateDoesNotExist

def home(request):
    try:
        context = {
            "universities": questions.objects.values_list('university', flat=True).distinct(),
            "courses": questions.objects.values_list('course', flat=True).distinct(),
            "departments": questions.objects.values_list('department', flat=True).distinct(),
            "semesters": [1,2,3,4,5,6,7,8],
            "subjects": questions.objects.values_list('subject', flat=True).distinct(),
            "topics": questions.objects.values_list('topic', flat=True).distinct(),
            "questions": None,
        }

        if "search" in request.GET:
            qs = questions.objects.all()
            if request.GET.get("university"):
                qs = qs.filter(university=request.GET.get("university"))
            if request.GET.get("course"):
                qs = qs.filter(course=request.GET.get("course"))
            if request.GET.get("department"):
                qs = qs.filter(department=request.GET.get("department"))
            if request.GET.get("semester"):
                qs = qs.filter(semester=request.GET.get("semester"))
            if request.GET.get("subject"):
                qs = qs.filter(subject=request.GET.get("subject"))
            if request.GET.get("topic"):
                qs = qs.filter(topic=request.GET.get("topic"))

            context["questions"] = qs

        return render(request, "index.html", context)

    except TemplateDoesNotExist:
        return JsonResponse({
            "status": "ok",
            "message": "Backend running ✅ (index.html missing in templates folder)"
        })
