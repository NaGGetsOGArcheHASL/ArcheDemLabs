from flask import Flask, redirect, url_for, render_template
app = Flask(__name__)

@app.route("/")
@app.route("/index")
def start():
    return redirect("/menu", code = 302)

@app.route("/menu")
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
            <h2><a href="/defence/">Защита</a></h2>
            <footer>
                  &copy; Дементьев Артур, ФБИ-12, 3 курс 2023
            </footer>
         </body>
      </html>
"""

@app.route("/lab1")
def lab1():
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

@app.route('/lab1/oak')
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

@app.route('/lab2/example') 
def example():
   name = 'Артур Дементьев'
   numberlab = 2
   group = 'ФБИ-12'
   course = 3
   fruits = [
    {'name': 'Яблоки', 'price': 100},
    {'name': 'Груши', 'price': 120}, 
    {'name': 'Апельсины', 'price': 150}, 
    {'name': 'Мандарины', 'price': 180}, 
    {'name': 'Манго', 'price': 210}
    ]

   books = [
      {'name': '1984', 'autor': 'Джордж Оруэлл','page': 328, 'Genre': 'Научная фантастика', 'price': 613},

      {'name': 'Преступление и наказание', 'autor': 'Федор Достоевский','page': 672, 'Genre': 'Классика', 'price': 505},

      {'name': 'Гарри Поттер и философский камень', 'autor': 'Джоан Роулинг','page': 256, 'Genre': 'Фэнтези', 'price': 500},

      {'name': 'Три товарища', 'autor': 'Эрих Мария Ремарк','page': 480, 'Genre': 'Роман', 'price': 1035},

      {'name': 'Улисс', 'autor': 'Джеймс Джойс','page': 732, 'Genre': 'Современная классика', 'price': 1095},

      {'name': 'Война и мир', 'autor': 'Лев Толстой','page': 1225, 'Genre': 'Классика', 'price': 350},

      {'name': 'Гордость и предубеждение', 'autor': 'Джейн Остин','page': 432, 'Genre': 'Роман', 'price': 840},

      {'name': '451 градус по Фаренгейту', 'autor': 'Рэй Брэдбери','page': 256, 'Genre': 'Научная фантастика', 'price': 350},

      {'name': 'Гамлет', 'autor': 'Уильям Шекспир','page': 288, 'Genre': 'Драма', 'price': 380},

      {'name': 'Игра престолов', 'autor': 'Джордж Мартин','page': 694, 'Genre': 'Фэнтези', 'price': 505},
   ]
   
   return render_template('example.html', name=name, numberlab=numberlab, group=group, 
   course=course, fruits=fruits, books=books)

@app.route('/lab2/')
def lab2():
   return render_template('lab2.html')

@app.route('/defence/')
def defence():
    return render_template('defence.html')

@app.route('/defence/for1')
def for1():
    k = 999
    n = 3
    result =  str(k) * n
    return (result)


@app.route('/defence/if16')
def if16():
    a = 3.3
    b = 3.7
    c = 4.4
    if (a > b) & (b > c) or (a < b) & (b < c):
        a *= 2
        b *= 2
        c *= 2
        result = str(a) + ', ' + str(b) + ', ' + str(c)
    else:
        result = str(-a) + ', ' + str(-b) + ', ' + str(-c)
    return (result)
