from django.shortcuts import render, redirect
from .models import questions
import mysql.connector as sql
import json
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
import requests
 

question = ''
frequency =1
years = ''
university = ''
course = ''
department = ''
semester = ''
subject = ''
topic = '' 
marks = 0


def send_pdf_to_api(pdf_path):
    api_url = "https://academic-question-backend.onrender.com"  # তোমার API URL
    files = {'file': open(pdf_path, 'rb')}

    response = requests.post(api_url, files=files)

    if response.status_code == 200:
        return response.json()  # এটি JSON রিটার্ন করবে
    else:
        raise Exception("API call failed with status code {}".format(response.status_code))


def add_question(request):
    global question, frequency, years, university, course, department, semester, subject, topic, marks
    
    if request.method == "POST" and request.POST.get("form_type") == "pdf_upload":
        pdf_file = request.FILES.get("pdf_file")
        if pdf_file:
            # Save the uploaded PDF temporarily
            fs = FileSystemStorage()
            filename = fs.save(pdf_file.name, pdf_file)
            pdf_path = fs.path(filename)

            try:
                # Call the external API and get JSON data
                questions_json = send_pdf_to_api(pdf_path)

                # Loop through the returned JSON and save to DB
                for item in questions_json:
                    questions.objects.create(
                        question=item["question"],
                        year=item["year"],
                        marks=item["marks"]
                    )

                return HttpResponse("PDF processed and questions saved!")

            except Exception as e:
                return HttpResponse("Failed to process PDF: " + str(e))
    
    if request.method == "POST" and request.POST.get("form_type") == "manual_entry":
        m=sql.connect(host="localhost",user="root",password="Example@2006#",database="qbank")
        cursor=m.cursor()
        data = request.POST
        
        for key, value in data.items():
            if key == 'Question':
                question = value
            elif key == 'Year':
                years = int(value)
            elif key == 'University':
                university = value
            elif key == 'Course':
                course = value
            elif key == 'Department':
                department = value
            elif key == 'Semester':
                semester = int(value)
            elif key == 'Subject':
                subject = value
            elif key == 'Topic':
                topic = value
            elif key == 'Marks':
                marks = int(value)
        q = """
        INSERT INTO sora_questions
        (question, frequency, years ,university, course, department, semester, subject, topic, marks)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """

        values = (
            question,
            frequency,
            years,
            university,
            course,
            department,
            semester,
            subject,
            topic,
            marks
        )

        cursor.execute(q, values)
        m.commit()

        return redirect('add_question')
 
    return render(request, 'superUser.html')
