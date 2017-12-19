import MySQLdb
import hug

db = MySQLdb.connect(user="root", passwd="gpm17", db="gpm_server2")
db_students = MySQLdb.connect(user="root", passwd="gpm17", db="gpm_server1")


@hug.put("/insertThesis")
def insertThesis(student_id: hug.types.text, title: hug.types.text, supervisor: hug.types.text):
    c = db.cursor()
    c.execute("""INSERT INTO thesis (student_id, title, supervisor, approved) VALUES (%s, %s, %s , %s)""", (student_id, title, supervisor, -1))
    c.close()
    db.commit()

    c = db.cursor()
    c.execute("SELECT id FROM thesis WHERE student_id = %s AND title = %s AND supervisor = %s", (student_id, title, supervisor))
    result = c.fetchone()
    c.close()

    return result[0]

@hug.post("/updateThesis")
def updateThesis(student_id: hug.types.text, title: hug.types.text, supervisor: hug.types.text, approved: hug.types.text):
    c = db.cursor()
    c.execute("""UPDATE thesis SET title=%s, supervisor=%s, approved=%s WHERE student_id = %s""", (title, supervisor, approved, student_id))
    c.close()
    db.commit()
    return "Thesis inserted"

@hug.post("/approveThesis")
def approveThesis(id: hug.types.text):
    c = db.cursor()
    c.execute("""UPDATE thesis SET approved=1 WHERE id = %s""", (id,))
    c.close()
    db.commit()
    return "Thesis approved"

@hug.post("/rejectThesis")
def rejectThesis(id: hug.types.text):
    c = db.cursor()
    c.execute("""UPDATE thesis SET approved=0 WHERE id = %s""", (id,))
    c.close()
    db.commit()
    return "Thesis approved"

@hug.get("/listThesises")
def listThesises():
    c = db.cursor()
    c.execute("SELECT * FROM thesis")
    result = c.fetchall()
    c.close()

    return result

@hug.get("/studentName")
def getStudentName(id: hug.types.text):
    c = db_students.cursor()
    c.execute("""SELECT CONCAT(prename, ' ', name) FROM student WHERE id = %s""", (id,))
    result = c.fetchone()
    c.close
    return result[0]

@hug.delete("/removeThesis")
def removeThesis(id: hug.types.text):
    c = db.cursor()
    c.execute("""DELETE FROM thesis WHERE id = %s""", (id,))
    c.close()

@hug.put("/insertBach")
def insertBachelorMark(student_id: hug.types.text, grade: hug.types.text):
    c = db_students.cursor()
    c.execute("""INSERT INTO written_exam (student_id, grade, subject_id) VALUES (%s, %s, (SELECT id FROM subject WHERE name = 'Bachelorarbeit'))""", (student_id, grade,))
    db_students.commit()
    c.close()

@hug.put("/insertColl")
def insertKolloquiumMark(student_id: hug.types.text, grade: hug.types.text):
    c = db_students.cursor()
    c.execute("""INSERT INTO written_exam (student_id, grade, subject_id) VALUES (%s, %s, (SELECT id FROM subject WHERE name = 'Kolloquium'))""", (student_id, grade,))
    db_students.commit()
    c.close()