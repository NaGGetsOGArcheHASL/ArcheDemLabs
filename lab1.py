from flask import Blueprint, redirect, url_for
lab1 = Blueprint('lab1', __name__)


@lab1.route("/")
@lab1.route("/index")
def start():
    return redirect("/menu", code = 302)


@lab1.route("/menu")
def menu():
   return """
      <!DOCTYPE html>
      <html>
      <link rel="stylesheet" href="static/lab1.css">
         <head>
            <title>Дементьев Артур. Лабораторные работы</title>
         </head>

         <body style="margin-left: 5%; padding: 50px;">
            <header>
               <h1>НГТУ, ФБ, WEB-программирование, часть 2. Список лабораторных</h1> web-сервер на flask
            </header>
            <h2><a href="/lab1">Лабораторная 1</a></h2>
            <h2><a href="/lab2/">Лабораторная 2</a></h2>
            <h2><a href="/lab3/">Лабораторная 3</a></h2>
            <h2><a href="/lab4/">Лабораторная 4</a></h2>
            <h2><a href="/lab5/">Лабораторная 5</a></h2>
            <h2><a href="/lab6/">Лабораторная 6</a></h2>
            <footer>
                  &copy; Дементьев Артур, ФБИ-12, 3 курс 2023
            </footer>
         </body>
      </html>
"""


@lab1.route("/lab1")
def lab():
   return """
      <!DOCTYPE html>
      <html>
      <link rel="stylesheet" href="static/lab1.css">
         <head>
            <title>Дементьев Артур. Лабораторная работа 1</title>
            <p>
               <a href="/menu">Меню</a>
            </p>
         </head>

         <body style="margin-left: 5%; padding: 50px;">
            <header>
                  НГТУ, ФБ, Лабораторная работа 1
            </header>
            <div style="margin-left: 2%; padding: 15px;">
                  Flask — фреймворк для создания веб-приложений на языке
                  программирования Python, использующий набор инструментов
                  Werkzeug, а также шаблонизатор Jinja2. Относится к категории так
                  называемых микрофреймворков — минималистичных каркасов
                  веб-приложений, сознательно предоставляющих лишь самые базовые возможности.
            </div>
            <div style="margin-left: 5%; padding: 20px;">
               <div style="margin-left: -20px; padding: -10px;">
                  <b>Работа:</b>
               </div>
               <p>
                  <a href="/lab1/oak">/lab1/oak - Дуб</a>
               </p>
               <p>
                  <a href="/lab1/student">/lab1/student - Студент</a>
               </p>
               <p>
                  <a href="/lab1/python">/lab1/python - Питон</a>
               </p>
            </div>
            <footer>
                  &copy; Дементьев, ФБИ-12, 3 курс 2023
            </footer>
         </body>
      </html>
"""


@lab1.route('/lab1/oak')
def oak():
   return '''
<!DOCTYPE html>
<html>
<link rel="stylesheet" href="static/lab1.css">
   <head>
      <title>Дементьев Артур. Лабораторные работы</title>
   </head>
   <a href="/lab1">Назад</a>
   <p></p>
   <a href="/menu">Меню</a>
   <body style="margin-left: 5%; padding: 50px;">
      <h1>Мудрый Дуб</h1>
      <img src="''' + url_for('static', filename='oak.jpg') + '''">
      <footer>
         &copy; Дементьев Артур, ФБИ-12, 3 курс 2023
       </footer>
   </body>
</html>
   '''
   