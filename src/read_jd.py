from docx import Document

JD_FILE = r"C:\Users\Sachin\Desktop\RecruitAI\data\[PUB] India_runs_data_and_ai_challenge\India_runs_data_and_ai_challenge\job_description.docx"

doc = Document(JD_FILE)

for para in doc.paragraphs:
    text = para.text.strip()
    if text:
        print(text)