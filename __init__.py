from flask import Flask
from flask import url_for, render_template
from flask_sqlalchemy import SQLAlchemy
import os
from sqlalchemy import text

app = Flask(__name__, static_folder="static")

basedir = os.path.abspath(os.path.dirname(__file__))
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(basedir, 'flask_hello_world_2.db')

db = SQLAlchemy(app)

@app.route("/")
def hello_world():
    return render_template('home.html')

@app.route("/skills")
def load_skills():
    sql_technical = f"SELECT Skill_Name, Proficiency_Level FROM Technical_Skills;" 
    sql_technical = text(sql_technical)


    result_technical = db.engine.connect().execute(sql_technical)

    found_technical_skills = []
    for skills in result_technical:
        found_technical_skills.append({
            'Skill_Name': skills[0],
            'Proficiency_Level': skills[1]})
        
    sql_soft = f"SELECT Skill_Name, Proficiency_Level FROM Soft_Skills;" 
    sql_soft = text(sql_soft)

    result_soft = db.engine.connect().execute(sql_soft)

    found_soft_skills = []
    for skills in result_soft:
        found_soft_skills.append({
            'Skill_Name': skills[0],
            'Proficiency_Level': skills[1]})
        
    all_skills = {
        'technical_skills': found_technical_skills,
        'soft_skills': found_soft_skills}
        
    return render_template('skills.html', skills=all_skills)

@app.route("/work")
def load_work():
    sql_work = f"SELECT Company_Name, Job_Title, Start_Date, End_Date, Responsibilities FROM Work"
    sql_work = text(sql_work)

    result_work = db.engine.connect().execute(sql_work)

    found_work = [
                {
                    'Company_Name': row[0],  
                    'Job_Title': row[1],
                    'Start_Date': row[2],
                    'End_Date': row[3],
                    'Responsibilities': row[4]
                }
                for row in result_work
            ]
        
    return render_template('work.html', found_work=found_work)
    
@app.route("/education")
def load_education():
    sql_education = f"SELECT Qualification, Institution, Start_Year, End_Year, Description FROM Education"
    sql_education = text(sql_education)

    result_education = db.engine.connect().execute(sql_education)

    found_education = [
                {
                    'Qualification': row[0],  
                    'Institution': row[1],
                    'Start_Year': row[2],
                    'End_Year': row[3],
                    'Description': row[4]
                }
                for row in result_education
            ]
        
    return render_template('education.html', found_education=found_education)

@app.route("/contact")
def load_contact():
    return render_template('contact.html')
    