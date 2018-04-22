import sqlite3
import globalVar

def get_all_item(path='stu.db'):
	#获取数据库所有数据
    #path = globalVar.dbPath
    conn = sqlite3.connect(path)
    c = conn.cursor()
    c.execute("select * from STU")
    allStu = c.fetchall()
    conn.close()

    return allStu

def add_new_item(student, path='stu.db'):
    #TODO exception same id(primary key),   done!
    #新添数据项
    #path = globalVar.dbPath
    if not check_unique_id(student):
    	return False
    conn = sqlite3.connect(path)
    c = conn.cursor()
    c.execute("insert into STU (id, name, gender, grade, major, score1, score2, score3, score4)\
     values('{}', '{}', '{}', '{}', '{}', {}, {}, {}, {})".format(student.id, student.name, student.gender, student.grade, student.major, student.score1, student.score2, student.score3, student.score4)) 
    conn.commit()
    conn.close()
    return True

def modify_item_by_id(student, path='stu.db'):
	#根据id, 修改数据库对应的项
    #path = globalVar.dbPath
    conn = sqlite3.connect(path)
    c = conn.cursor()

    c.execute("update STU set name = '{}', gender = '{}', grade = '{}', \
    	major = '{}', score1 = {} , score2 = {}, score3 = {}, score4 = {}\
    	where id = '{}'".format(student.name, student.gender, student.grade, student.major, student.score1, student.score2, student.score3, student.score4, student.id))
    conn.commit()
    conn.close()


def check_unique_id(student, path='stu.db'):
	#检查新建项时，id不得重复
	#path = globalVar.dbPath
	conn = sqlite3.connect(path)
	c = conn.cursor()
	c.execute("select * from STU where id = {}".format(student.id))
	if(len(c.fetchall()) == 0):
		conn.close()
		return True
	else:
		conn.close()
		return False

def check_unique_id_authority(user_name, path='manager.db'):
	#检查新建项时，id不得重复
	conn = sqlite3.connect(path)
	c = conn.cursor()
	c.execute("select * from POWER where user = '{}'".format(user_name))
	if(len(c.fetchall()) == 0):
		conn.close()
		return True
	else:
		conn.close()
		return False

def insert_authority(uname, passwd, path='manager.db'):
	conn = sqlite3.connect(path)
	c = conn.cursor()
	#新建的都是学生账户，权限为1
	c.execute("insert into POWER (user, passwd, authority)\
	values('{}', '{}', 1)".format(uname, passwd))
	conn.commit()
	conn.close()


def delete(id, path='stu.db'):
	#删除数据项，依据id
    conn = sqlite3.connect(path)
    c = conn.cursor()
    c.execute("delete from STU where id = {}".format(id))
    conn.commit()
    conn.close()

def query(col, path='stu.db'):
	#查询对应条件数据项，由于写的很差，所以要求不得全为空
	cnt = 0
	order = ''
	if col.id is not '':
		order += "id = '{}'".format(col.id)
		cnt = cnt + 1
	
	if col.name is not '' and cnt is 0:
		order += "name = '{}'".format(col.name)
		cnt = cnt + 1
	elif col.name is not '':
		order += " and name = '{}'".format(col.name)
	
	if col.gender is not '' and cnt is 0:
		order += "gender = '{}'".format(col.gender)
		cnt = cnt + 1
	elif col.gender is not '':
		order += " and gender = '{}'".format(col.gender)

	if col.grade is not '' and cnt is 0:
		order += "grade = '{}'".format(col.grade)
		cnt = cnt + 1
	elif col.grade is not '':
		order += " and grade = '{}'".format(col.grade)

	if col.major is not '' and cnt is 0:
		order += "major = '{}'".format(col.major)
		cnt = cnt + 1
	elif col.major is not '':
		order += " and major = '{}'".format(col.major)
	'''
	if col.score is not '' and cnt is 0:
		order += "score = {}".format(col.score)
		cnt = cnt + 1
	elif col.score is not '':
		order += " and score = {}".format(col.score)

	#print(order)
	'''
	if order == '':
		#len ans = 0
		return ()

	conn = sqlite3.connect(path)
	c = conn.cursor()
	c.execute("select * from STU where "+order)
	ans = c.fetchall()
	conn.close()
	return ans

def check_authority(user_name, path='manager.db'):
    conn = sqlite3.connect(path)
    c = conn.cursor()
    c.execute("select * from POWER where user = '{}'".format(user_name))
    ans = c.fetchall()
    return ans