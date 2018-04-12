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

def query(col, path='stu.db'):
	cnt = 0
	order = ''
	if col.id is not '':
		order += 'id = {}'.format(col.id)
		cnt = cnt + 1
	
	if col.name is not '' and cnt is 0:
		order += 'name = {}'.format(col.name)
		cnt = cnt + 1
	elif col.name is not '':
		order += ' and name = {}'.format(col.name)
	
	if col.gender is not '' and cnt is 0:
		order += 'gender = {}'.format(col.gender)
		cnt = cnt + 1
	elif col.gender is not '':
		order += ' and gender = {}'.format(col.gender)

	if col.grade is not '' and cnt is 0:
		order += 'grade = {}'.format(col.grade)
		cnt = cnt + 1
	elif col.grade is not '':
		order += ' and grade = {}'.format(col.grade)

	if col.major is not '' and cnt is 0:
		order += 'major = {}'.format(col.major)
		cnt = cnt + 1
	elif col.major is not '':
		order += ' and major = {}'.format(col.major)

	print(order)
	if order == '':
		return ()

	conn = sqlite3.connect(path)
	c = conn.cursor()
	c.execute("select * from STU where "+order)
	ans = c.fetchall()
	conn.close()
	return ans