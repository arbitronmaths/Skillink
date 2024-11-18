from flask import Flask, request, jsonify, render_template
import pickle
import fitz  # PyMuPDF
import google.generativeai as genai
import os

genai.configure(api_key="AIzaSyBjTDTfTOto5K_MeUY-Tyna4E1aemEzNw0")  

app = Flask(__name__)

# Load the models
with open('tfidf.pkl', 'rb') as f:
    model1 = pickle.load(f)

with open('cls.pkl', 'rb') as f:
    model2 = pickle.load(f)

# Text extraction
def extract_text_from_pdf(pdf_file):
    text = ""
    with fitz.open(stream=pdf_file.read(), filetype="pdf") as doc:
        for page in doc:
            text += page.get_text()
    return text

# Job prediction
def predict_job_role(resume_content):
    keys = [6, 12, 0, 1, 24, 16, 22, 14, 5, 15, 4, 21, 2, 11, 18, 20, 8, 17, 19, 7, 13, 10, 9, 3, 23]
    values = ['Data Science', 'HR', 'Advocate', 'Arts', 'Web Designing',
              'Mechanical Engineer', 'Sales', 'Health and fitness',
              'Civil Engineer', 'Java Developer', 'Business Analyst',
              'SAP Developer', 'Automation Testing', 'Electrical Engineering',
              'Operations Manager', 'Python Developer', 'DevOps Engineer',
              'Network Security Engineer', 'PMO', 'Database', 'Hadoop',
              'ETL Developer', 'DotNet Developer', 'Blockchain', 'Testing']
    
    job_dict = dict(zip(keys, values))
    
    # Transform the resume content using the tfidf model
    resume_vector = model1.transform([resume_content])

    # Predict the job role
    prediction = model2.predict(resume_vector)[0]

    return job_dict[prediction]

# Course suggestion
def suggest_courses(job_pred):
    model = genai.GenerativeModel('gemini-1.5-flash')
    chat = model.start_chat(history=[])
    response = chat.send_message(f"Suggest some popular online courses and their links for someone pursuing a career as a {job_pred}. Provide course names and brief descriptions.")
    response = chat.send_message(f"{response}+Add proper html links for each course using <a href='url_link'>Learn more</a> tag")
    return response.text

@app.route('/')
def welcome():
    return render_template('front.html')


@app.route('/upload', methods=['POST', 'GET'])
def upload():
    if request.method == 'POST':
        return render_template('index.html')
    
@app.route('/login',methods=['POST','GET'])
def login():
    if request.method == 'POST':
        return render_template('login.html')

@app.route('/Home', methods=['POST','GET'])
def home():
    if request.method == 'POST':
        return render_template('front.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        file = request.files.get('resume')
        if not file:
            return jsonify({'error': 'No file uploaded'}), 400

        if file.filename.endswith('.pdf'):
            resume_content = extract_text_from_pdf(file)
        else:
            resume_content = file.read().decode('utf-8')

        job_role = predict_job_role(resume_content)
        courses = suggest_courses(job_role)
        courses = courses.replace('\n','<br>')

        return render_template('result.html', job_role=job_role, courses=courses)

if __name__ == '__main__':
    app.run(debug=True)
