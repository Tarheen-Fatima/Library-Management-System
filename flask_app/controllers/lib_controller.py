from flask_app import app
from flask import Flask, render_template, request, session, redirect, url_for, flash
from flask_app.models.library import Library 

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/admin-login')
def admin_login():
    return render_template('admin-login.html')

@app.route('/register')
def registration():
    return render_template('registration.html')

@app.route('/submit_register', methods=['POST'])
def submit_registration():
    user_data = {
        'username': request.form['username'],
        'college_id': request.form['college_id'],
        'phone_no': request.form['phone_no'],
        'email': request.form['email'],
        'password':request.form['password']  
    }
    result = Library.register(user_data) 
    success=True 
    return render_template("registration.html",success=success)

@app.route('/login_verify', methods=['POST'])
def login_verify():
    data = Library.get_data()
    for i in data:
        if request.form['college_id'] == i['college_id'] and request.form['password'] == i['password']:
            session['username'] = i['username']
            session['college_id'] = i['college_id']
            session['password'] = i['password']
            return redirect("/dashboard/" + session['college_id'])

@app.route("/dashboard/<id>")
def dashboard(id):
    return render_template("dashboard.html")

@app.route('/admin_verify', methods=['POST'])
def admin_verify():
    data = Library.get_data_admin()
    for i in data:
        if request.form['admin_id'] == i['admin_id'] and request.form['password'] == i['password']:
            session['name'] = i['name']
            session['admin_id'] = i['admin_id']
            session['password'] = i['password']
            return redirect("/dashboard2/" + session['admin_id'])
        else:
            return render_template("admin-login.html")

@app.route("/dashboard2/<id>")
def dashboard2(id):
    return render_template("dashboard2.html")      

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/login')


@app.route('/forget_password')
def forget_password():
    return render_template('registration.html')

@app.route('/book_details/<id>')
def show_book(id):
    data={'college_id':id}
    return render_template('books.html',info=Library.get_available_books(data))

@app.route('/authors/<id>')
def author(id):
    data={'college_id':id}
    return render_template('authors.html',info=Library.get_authors(data))

@app.route('/update/<int:bookid>',methods=['POST'])
def update(bookid):
    data={'bookid':bookid,
          'title':request.form['title'],
          'author':request.form['author'],
          'ISBN':request.form['ISBN'],
          'genre':request.form['genre'],
          'publication_year':request.form['publication_year'],
          'quantity':request.form['quantity']
          }
    Library.update_data(data)
    return redirect(f'/books/{bookid}')

@app.route('/delete/<int:bookid>')
def delete(bookid):
    data={'bookid':bookid}
    Library.delete_data(data)
    return redirect('/dashboard')

@app.route("/profile/<int:id>")
def profile(id):
    data = {'studentid': id}
    result = Library.profile_data(data)
    if result:
        return render_template("profile.html", info=result)
    else:
        return "Student not found", 404  

@app.route("/issue/<id>/<bookid>")
def issue(id,bookid):
    data={'student_id':id,
           'book_id':bookid}
    result=Library.issue_book(data)
    book=Library.get_book(data)
    Library.update_book_record(data)
    return redirect(f"/book_details/{id}") 

@app.route("/issue_book/<id>")
def issue_book(id):
    data={'id':id}
    return render_template("issued.html",info=Library.get_issued_data(data))

@app.route('/student_details/<id>')
def show_student(id):
    data={'studentid':id}
    return render_template('show_student.html',info=Library.get_all_students(data))

@app.route("/add_student", methods=['GET', 'POST'])
def add_student():
    if request.method == 'POST':
        student_data = {
            'studentid': request.form.get('studentid'),
            'FirstName': request.form.get('Firstname'),
            'LastName': request.form.get('Lastname'),
            'course': request.form.get('course')
        }
        Library.register3(student_data)
        return redirect("/student_details")
    else:
        return render_template("add_student.html", data=Library.get_student())


@app.route("/admin_profile/<int:id>")
def admin_profile(id):
    data = {'admin_id': id}
    result = Library.profile_data(data)
    if result:
        return render_template("admin_profile.html", info=result)
    else:
        return "Student not found", 404  


