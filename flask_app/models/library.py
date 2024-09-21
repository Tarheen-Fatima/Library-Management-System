from flask_app.config.mysqlconnection import connectToMySQL

class Library:
    def __init__(self, data):
        self.college_id = data['college_id']
        self.bookid=data['bookid']
        self.studentid=data['studentid'] 
       
    @classmethod
    def get_user_by_email(cls,data):
        query = "SELECT college_id,password FROM registration;"
        results = connectToMySQL().query_db(query)
        print(results)
        return [cls(row) for row in results]

    @classmethod
    def get_data(cls):
        query="""Select * from registration;"""
        results=connectToMySQL().query_db(query)
        lst=[]
        for i in results:
            lst.append( i )
        print(lst)
        return lst

    @classmethod
    def register(cls, data):
        query = """INSERT INTO registration (username, college_id, phone_no, email, password)
            VALUES (%(username)s, %(college_id)s, %(phone_no)s, %(email)s, %(password)s);"""
        return connectToMySQL().query_db(query, data)

    @classmethod
    def get_data1(cls):
        query="""Select * from books;"""
        results=connectToMySQL().query_db(query)
        lst=[]
        for i in results:
            lst.append(i)
        print(lst)
        return lst

        
    @classmethod
    def register1(cls,data):
        print("books: ",data)
        query="""insert into books(bookid,title,,author,ISBN,genre,publication_year,quantity)values(%(bookid)s,%(title)s,%(author)s,%(ISBN)s,%(genre)s,%(publication_year)s,%(quantity)s);"""
        result=connectToMySQL().query_db(query,data)
        return result

    @classmethod
    def get_book(cls, data):
        query = "SELECT * FROM books WHERE bookid = %(book_id)s;"
        result = connectToMySQL().query_db(query, data)
        print(result[0])
        return result[0]
        
    @classmethod
    def update_data(cls,data):
        query="""UPDATE books SET title = %(title)s, author=%(author)s,ISBN=%(ISBN)s,genre=%(genre)s,publication_year=%(publication_year)s,quantity=%(quantity)s where bookid = %(bookid)s"""
        result=connectToMySQL().query_db(query,data)
        return result

    @classmethod
    def get_available_books(cls,data):
        query = """SELECT b.*
                    FROM books b
                    LEFT JOIN issue i ON b.bookid = i.book_id AND i.student_id = '%(college_id)s'
                    WHERE b.quantity > 0 AND i.book_id IS NULL;
                        """
        results = connectToMySQL().query_db(query)
        return results

    @classmethod
    def profile_data(cls, data):
        query = "SELECT * FROM registration WHERE college_id = %(studentid)s;"
        result = connectToMySQL().query_db(query, data)
        print(result[0])
        return result[0]

    

    @classmethod
    def issue_book(cls,data):
        print("books: ",data)
        query="""insert into issue(student_id,book_id)values(%(student_id)s,%(book_id)s);"""
        result=connectToMySQL().query_db(query,data)
        return result

    @classmethod
    def update_book_record(cls,data):
        query="""UPDATE books SET quantity=quantity-1 where bookid = %(book_id)s"""
        result=connectToMySQL().query_db(query,data)
        return result
    
    @classmethod
    def get_issued_data(cls,data):
        query="""SELECT bookid, title AS "title", author AS "Author", ISBN, genre AS "Genre", publication_year AS "publication_year", quantity
                FROM books
                WHERE bookid IN (
                SELECT book_id
                FROM issue
                WHERE student_id = 1 )"""
        results=connectToMySQL().query_db(query)
        lst=[]
        for i in results:
            lst.append(i)
        print(lst)
        return lst

    @classmethod
    def get_all_students(cls,data):
        query = "SELECT * FROM student;"
        results = connectToMySQL().query_db(query)
        return results

    @classmethod
    def get_student(cls):
        query="""Select * from student;"""
        results=connectToMySQL().query_db(query)
        lst=[]
        for i in results:
            lst.append( i )
        print(lst)
        return lst

    @classmethod
    def register3(cls,data):
        print("STUDENT: ",data)
        query="""insert into student(studentid,FirstName,LastName,course)values(%(studentid)s,%(FirstName)s,%(LastName)s,%(course)s);"""
        result=connectToMySQL().query_db(query,data)
        return result

    @classmethod
    def get_data_admin(cls):
        query="""Select * from admin;"""
        results=connectToMySQL().query_db(query)
        lst=[]
        for i in results:
            lst.append(i)
        print(lst)
        return lst

    @classmethod
    def profile_admin(cls, data):
        query = "SELECT * FROM admin WHERE admin_id = 11;"
        result = connectToMySQL().query_db(query, data)
        print(result[0])
        return result[0]

    @classmethod
    def get_authors(cls, data):
        query = "SELECT * FROM Authors;"
        result=connectToMySQL().query_db(query,data)
        return result
