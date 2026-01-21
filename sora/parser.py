import os
import json
from dotenv import load_dotenv
from openai import OpenAI
from extract_pdf import extract_text_from_pdf

load_dotenv()

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


if __name__ == "__main__":
    result = parse_question_paper("P:\computerVision\qbank\media\BSC(CSE)701_2022.pdf")

    with open("output.json", "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2)

    print("✅ JSON extracted successfully → output.json")
