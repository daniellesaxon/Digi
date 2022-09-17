from flask import Flask, render_template, request, url_for, redirect, session

import sqlite3, random


app = Flask(__name__)


#home page
@app.route("/", methods=['POST', 'GET'])
def home():
   if request.method == "POST":
      connection = sqlite3.connect('aerobicgymnastics.db')
      cursor = connection.cursor()
      id = request.form['delete']
      print(id)
      cursor.execute(f"DELETE FROM Competitor WHERE id = {id}")
      connection.commit()
      connection.close()
   return render_template("home.html")

@app.route("/competitor/add")
def add_competitor():
   connection = sqlite3.connect('aerobicgymnastics.db')
   cursor = connection.cursor()
   cursor.execute("SELECT name, difficulty From Skill")
   skills = cursor.fetchall()
   connection.close()
   session['x'] = "add"
   return render_template("add_competitor.html", skills=skills)

@app.route("/competitor/edit/<string:competitor_name>")
def edit_competitor(competitor_name):
   connection = sqlite3.connect('aerobicgymnastics.db')
   cursor = connection.cursor()
   cursor.execute(f"SELECT id, name, level FROM Competitor WHERE name='{competitor_name}';")
   competitor = cursor.fetchone()
   cursor.execute(f"SELECT name FROM Skill WHERE id IN (SELECT sid FROM SkillList WHERE cid = (SELECT id FROM Competitor WHERE name = '{competitor_name}'));")
   selected_skills = cursor.fetchall()
   cursor.execute("SELECT name FROM Skill")
   all_skills=cursor.fetchall()
   unselected_skills=[]
   selected_skills = list(selected_skills)
   #print(selected_skills)
   '''test = []
   for item in selected_skills:
      print(item)
      test.append(item)
      print(test)'''
   all_skills = list(all_skills)
   for item in all_skills:
      if item not in selected_skills:
         #print(item)
         unselected_skills.append(item)

         '''
   for item in all_skills:
      for i in all_skills:
         if item == i:
            all_skills.remove(i)'''
   unselected_skills = tuple(unselected_skills)
   connection.close()
   session['x'] = "delete"
   return render_template("edit_competitor.html", selected_skills=selected_skills, competitor=competitor, unselected_skills=unselected_skills)


#page to see each singular competitor and their score, skills and category
@app.route("/competitor/<string:competitor_name>", methods=['POST', 'GET'])
def competitor(competitor_name):
   #connect to database
   connection = sqlite3.connect('aerobicgymnastics.db')
   cursor = connection.cursor()
   #getting a singlar competitors information from database
   cursor.execute("SELECT * FROM Competitor where name = ?",(competitor_name,))
   competitor = cursor.fetchone()
   cursor.execute(f"SELECT name, difficulty FROM Skill WHERE id IN (SELECT sid FROM SkillList WHERE cid = (SELECT id FROM Competitor WHERE name = '{competitor_name}'));")
   skills = cursor.fetchall()
   #getting a competitors skills from the joining table
   if request.method == 'POST':
      print("message: method = POST and route =competitor/stringname")
      skill = request.form.getlist('selected_skills')
      print(skill)
      competitor_id = int(request.form['competitor_id'])
      print(competitor_id)
      cursor.execute(f"DELETE FROM SkillList WHERE cid={competitor_id};")
      cursor.execute(f"SELECT name FROM Competitor WHERE id = {competitor_id}")
      name = cursor.fetchone()
      connection.commit()
      for item in skill:
         cursor.execute(f"INSERT INTO SkillList(cid, sid) Values({competitor_id}, (SELECT id FROM Skill WHERE name='{item}'))")
      cursor.execute(f"SELECT name, difficulty FROM Skill WHERE id IN (SELECT sid FROM SkillList WHERE cid = ('{competitor_id}'));")
      skills = cursor.fetchall()
      add_skill = request.form.getlist('unselected_skills')
      for item in add_skill:
         cursor.execute(f"INSERT INTO SkillList(cid, sid) Values({competitor_id}, (SELECT id FROM Skill WHERE name='{item}'))")
      connection.commit()
      connection.close()
      name = "".join(name)
      print(name)
      return redirect(url_for("competitor", competitor_name=name))
   else:
      return render_template("competitor.html", competitor=competitor, skills=skills)
   #return f"<h1>{competitor[1]}</h1><br>Level: <p>{competitor[2]}</p><br>Score: <p>{competitor[3]}</p> <br> {skills}"


#this page will show a dropdown list of the competitors which will link to the singular competitor pages
@app.route("/competitor", methods=['POST', 'GET'])
def home_competitor():
   #connect to database
   connection = sqlite3.connect('aerobicgymnastics.db')
   cursor = connection.cursor()
   cursor.execute("SELECT name FROM Competitor")
   names = cursor.fetchall()
   connection.close()
   connection = sqlite3.connect('aerobicgymnastics.db')
   cursor = connection.cursor()
   cursor.execute("SELECT name FROM Skill")
   skills = cursor.fetchall()
   #DOESNT WORK YET
   if request.method == 'POST':
      if session.get('x') == "delete":
         id = request.form['delete']
         print(id)
         cursor.execute(f"DELETE FROM Competitor WHERE id = {id}")
         connection.commit()
         connection.close()
         return redirect(url_for('home_competitor', names=names, skills=skills))
      if session.get('x') == "add":
         print("it here")
         first_name = request.form['first_name'] 
         last_name = request.form['last_name'] 
         level = int(request.form['level'])
         skills = request.form.getlist('selected_skills')
         cursor.execute(f"INSERT INTO Competitor (name, last_name, level) VALUES('{first_name}','{last_name}', {level});")
         for item in skills:
            cursor.execute(f"INSERT INTO SkillList(cid, sid) Values((SELECT id FROM competitor WHERE name='{first_name}'), (SELECT id FROM Skill WHERE name='{item}'))")
         connection.commit()
         connection.close()
         return redirect(url_for('home_competitor', names=names, skills=skills))
   #elif request.method == "POST-1":
      #connection = sqlite3.connect('aerobicgymnastics.db')
      #cursor = connection.cursor()
   else:
      connection.close()
      return render_template("home_competitor.html", names=names, skills=skills)
   #f"{results}<br> {skills}"


#This is the page where each singular competitor will be judged, it has to send output and get input (of the scores)
#it has two different methods; post and get \. this determines whether it has or hasnt gotten input from the html page
@app.route("/judge/<string:competitor_name>", methods=['POST', 'GET'])
def judge(competitor_name):
   #connect to database
   connection = sqlite3.connect('aerobicgymnastics.db')
   cursor = connection.cursor()
   cursor.execute(f"SELECT name, difficulty FROM Skill WHERE id IN (SELECT sid FROM SkillList WHERE cid = (SELECT id FROM Competitor WHERE name = '{competitor_name}'));")
   skills = cursor.fetchall()
   
   #return request.method
   '''if request.method == 'POST':

      artistic = int(request.form['artistic'])
      
      sql=(f"UPDATE Competitor SET artistic={artistic} WHERE id = (SELECT id FROM Competitor WHERE name = '{competitor_name}');")
      print(sql)
      cursor.execute(sql)
      connection.commit()
      connection.close()
      return redirect(url_for('judge', artistic=artistic))
   else:'''
   return render_template("judge.html", skills=skills, competitor_name=competitor_name)


   

#this will be similar the the home_competitor page, it will show a list of names which will link to the singlar judging page
@app.route("/judge", methods=['POST', 'GET'])
def home_judge():
   #connect to database
   connection = sqlite3.connect('aerobicgymnastics.db')
   cursor = connection.cursor()
   cursor.execute(f"SELECT name FROM Competitor")
   names = cursor.fetchall()
   if request.method == 'POST':
      artistic = float(request.form['artistic'])
      competitor_name = request.form['competitor_name'] 
      execution = float(round(random.uniform(5, 10), 1))
      skills_counted = request.form.getlist('got_skill')
      print(skills_counted)
      difficulty = 0
      for item in skills_counted:
         diff = float(item)
         difficulty+=diff
      difficulty = difficulty/2
      final_score = artistic+execution+difficulty
      print(execution)
      sql=(f"UPDATE Competitor SET artistic={artistic}, difficulty={difficulty}, execution={execution}, score={final_score} WHERE id = (SELECT id FROM Competitor WHERE name = '{competitor_name}');")
      cursor.execute(sql)
      connection.commit()

      '''execution = 0
      
      skill = request.form.get('skill')
      cursor.execute(f"SELECT name, difficulty FROM Skill WHERE id IN (SELECT sid FROM SkillList WHERE cid = (SELECT id FROM Competitor WHERE name = '{competitor_name}'));")
      skills = cursor.fetchall()
      for i in skills:
         return i
      if skill == True:
         skill_value = request.form['skill_value']
         execution+=skill_value
         sql=(f"UPDATE Competitor SET execution={execution} WHERE id = (SELECT id FROM Competitor WHERE name = '{competitor_name}');")
         connection.commit()'''
      connection.close()
      return redirect(url_for('home_judge', names=names, artistic=artistic, competitor_name=competitor_name))
   else:
      return render_template("home_judge.html", names=names)


#this is order the scores in order of best to worst
@app.route("/score")
def score():
   #connect to database
   connection = sqlite3.connect('aerobicgymnastics.db')
   cursor = connection.cursor()
   cursor.execute(f"SELECT name, artistic, execution, difficulty, score FROM Competitor ORDER BY score DESC;")
   scores = cursor.fetchall()
   placings = []
   counter = 0
   scores = list(scores)
   scores_with_placings = []
   print(scores)
   for item in scores:
      counter+=1
      item = list(item)
      item.insert(0, counter)
      item = tuple(item)
      scores_with_placings.append(item)
   scores_with_placings = tuple(scores_with_placings)
   print(scores_with_placings)


   for item in scores:
      
      placings.append(counter)
   placings = tuple(placings)
   print(placings)
      

   return render_template("score.html", scores=scores_with_placings, placings=placings, counter=counter)


#if it is run on this device it will debug because it isn't imported
if __name__ == "__main__": 
   app.secret_key = "xyz"
   app.run(debug=True)