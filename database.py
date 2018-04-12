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
    if not check_unique_id(student):
    	return False
    conn = sqlite3.connect(path)
    c = conn.cursor()
    c.execute("insert into STU (id, name, gender, grade, major)\
     values({}, {}, {}, {}, {})".format(student.id, student.name, student.gender, student.grade, student.major)) 
    conn.commit()
    conn.close()
    return True


def check_unique_id(student, path='stu.db'):
	conn = sqlite3.connect(path)
	c = conn.cursor()
	c.execute("select * from STU where id = {}".format(student.id))
	if(len(c.fetchall()) == 0):
		conn.close()
		return True
	else:
		conn.close()
		return False