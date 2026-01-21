import os
from urllib import response
from django.shortcuts import render, redirect
from .models import questions
import mysql.connector as sql
import json
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
import json
from dotenv import load_dotenv
from openai import OpenAI
from PyPDF2 import PdfReader




 

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

load_dotenv()


def extract_text_from_pdf(pdf_path):
    reader = PdfReader(pdf_path)
    text = ""

    for page in reader.pages:
        text += page.extract_text() + "\n"

    return text

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def parse_question_paper(pdf_path):
    pdf_text = extract_text_from_pdf(pdf_path)

    prompt = f"""
You are an academic document parser.

From the following university question paper text,
extract structured information and return ONLY valid JSON
in the exact format below.

FORMAT:
{{
  "university": "",
  "course": "",
  "department": "",
  "year": "",
  "subject": "",
  "semester": "",
  "questions": [
    {{
      "question": "",
      "topic": "",
      "marks": ""
    }}
  ]
}}

RULES:
- Infer topic from question meaning
- Marks may be written like (5), [10], or 10 Marks
- If something is missing, use null
- Return ONLY JSON, no explanation

TEXT:
\"\"\"
{pdf_text}
\"\"\"
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0
    )

    json_output = response.choices[0].message.content

    return json.loads(json_output)


def add_question(request):
    global question, frequency, years, university, course, department, semester, subject, topic, marks
    
    if request.method == "POST" and request.POST.get("form_type") == "pdf_upload":
        data = parse_question_paper(request.FILES['pdf_file'])

        # 3️⃣ Insert into DB (YOUR EXISTING MODEL)
        year_value = int(data["year"])

        for q in data["questions"]:
            obj, created = questions.objects.get_or_create(
                question=q["question"],
                university=data["university"],
                subject=data["subject"],
                topic=q["topic"],
                defaults={
                    "frequency": 1,
                    "years": year_value,
                    "marks": q["marks"],
                    "course": data["course"],
                    "department": data["department"],
                    "semester": int(data["semester"]),
                }
            )

            if not created:
                obj.frequency += 1
                obj.save()
                
                
        return redirect('add_question')
    
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
