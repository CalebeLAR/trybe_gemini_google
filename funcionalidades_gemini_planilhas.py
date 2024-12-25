import google.generativeai as genai
import os

genai.configure(api_key=os.environ["GOOGLE_API_KEY"])
model = genai.GenerativeModel("gemini-1.5-flash")

students_spreadsheet = genai.upload_file(
   path="funcionalidades_gemini_planilhas.py",
   display_name="Notas do Enem"
)

prompt = "Pode gerar um relatório de dois ou três parágrafos baseado nesses \
dados? Fale de tendências nos grupos de estudantes."

response = model.generate_content([students_spreadsheet, prompt])
response = model.generate_content(prompt)

print(response.text)
