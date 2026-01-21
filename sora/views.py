import os
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





def add_question(request):
    global question, frequency, years, university, course, department, semester, subject, topic, marks
    
    # if request.method == "POST" and request.POST.get("form_type") == "pdf_upload":
    #     pdf_file = request.FILES.get("pdf_file")
    #     if pdf_file:
    #         # Save the uploaded PDF temporarily
    #         fs = FileSystemStorage()
    #         filename = fs.save(pdf_file.name, pdf_file)
    #         pdf_path = fs.path(filename)

    #         try:
    #             # Call the external API and get JSON data
    #             questions_json = send_pdf_to_api(pdf_path)

    #             # Loop through the returned JSON and save to DB
    #             for item in questions_json:
    #                 questions.objects.create(
    #                     question=item["question"],
    #                     year=item["year"],
    #                     marks=item["marks"]
    #                 )

    #             return HttpResponse("PDF processed and questions saved!")

    #         except Exception as e:
    #             return HttpResponse("Failed to process PDF: " + str(e))
    
    if request.method == "POST" and request.POST.get("form_type") == "manual_entry":
        m=sql.connect(host=os.getenv("DB_HOST"),user=os.getenv("DB_USER"),password=os.getenv("DB_PASSWORD"),database=os.getenv("DB_NAME"))
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
