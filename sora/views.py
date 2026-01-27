import os
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from dotenv import load_dotenv
import mysql.connector as sql

load_dotenv()


def add_question(request):

    # =========================
    # FORM 1: PDF / IMAGE UPLOAD
    # =========================
    if request.method == "POST" and request.POST.get("form_type") == "pdf_upload":

        pdf_file = request.FILES.get("pdf_file")

        if not pdf_file:
            return HttpResponse("No file uploaded")

        university = request.POST.get("University", "").upper()
        year = request.POST.get("Year", "")
        course = request.POST.get("Course", "").upper()
        semester = request.POST.get("Semester", "")
        subject = request.POST.get("Subject", "").upper()
        department = request.POST.get("Department", "").upper()

        fs = FileSystemStorage()
        filename = fs.save(pdf_file.name, pdf_file)

        print("PDF UPLOADED")
        print(university, year, course, semester, subject, department)

        return redirect("add_question")

    # =========================
    # FORM 2: MANUAL ENTRY
    # =========================
    if request.method == "POST" and request.POST.get("form_type") == "manual_entry":

        try:
            # Question remains ORIGINAL (NOT UPPERCASE)
            question = request.POST.get("Question", "")

            # ✅ ALL TEXT → CAPITAL LETTERS
            university = request.POST.get("University", "").upper()
            course = request.POST.get("Course", "").upper()
            department = request.POST.get("Department", "").upper()
            subject = request.POST.get("Subject", "").upper()
            topic = request.POST.get("Topic", "").upper()

            years = int(request.POST.get("Year", 0))
            semester = int(request.POST.get("Semester", 0))
            marks = int(request.POST.get("Marks", 0))

            frequency = 1

            conn = sql.connect(
                host=os.getenv("DB_HOST"),
                user=os.getenv("DB_USER"),
                password=os.getenv("DB_PASSWORD"),
                database=os.getenv("DB_NAME")
            )
            cursor = conn.cursor()

            query = """
            INSERT INTO sora_questions
            (question, frequency, years, university, course, department, semester, subject, topic, marks)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """

            cursor.execute(query, (
                question,          # ❗ NOT upper
                frequency,
                years,
                university,        # ✅ upper
                course,            # ✅ upper
                department,        # ✅ upper
                semester,
                subject,           # ✅ upper
                topic,             # ✅ upper
                marks
            ))

            conn.commit()
            cursor.close()
            conn.close()

            return redirect("add_question")

        except Exception as e:
            return HttpResponse(f"ERROR: {e}")

    # =========================
    # PAGE LOAD
    # =========================
    return render(request, "superUser.html")
