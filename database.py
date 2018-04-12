import sqlite3

def get_all_item(path='stu.db'):
    conn = sqlite3.connect(path)
    c = conn.cursor()
    c.execute("select * from STU")
    allStu = c.fetchall()
    conn.close()

    return allStu

def add_new_item(student, path='stu.db'):
    #TODO exception same id(primary key)
    conn = sqlite3.connect(path)
    c = conn.cursor()
    c.execute("insert into STU (id, name, gender, grade, major)\
     values({}, {}, {}, {}, {})".format(student.id, student.name, student.gender, student.grade, student.major)) 
    conn.commit()