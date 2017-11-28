import MySQLdb
import hug

db = MySQLdb.connect(user="root", passwd="gpm17", db="gpm_server2")


@hug.put("/insertThesis", )
def insertThesis(student_id: hug.types.text, title: hug.types.text, supervisor: hug.types.text):
    c = db.cursor()
    c.execute("""INSERT INTO thesis (student_id, title, supervisor, approved) VALUES (%s, %s, %s , %s)""", (student_id, title, supervisor, -1))
    result = c.fetchall()
    c.close()
    db.commit()
    return result

@hug.post("/updateThesis", )
def updateThesis(student_id: hug.types.text, title: hug.types.text, supervisor: hug.types.text, approved: hug.types.text):
    c = db.cursor()
    c.execute("""UPDATE thesis SET title=%s, supervisor=%s, approved=%s WHERE student_id = %s""", (title, supervisor, approved, student_id))
    c.close()
    db.commit()
    return "Thesis inserted"

@hug.post("/approveThesis", )
def approveThesis(id: hug.types.text):
    c = db.cursor()
    c.execute("""UPDATE thesis SET approved=1 WHERE id = %s""", (student_id))
    c.close()
    db.commit()
    return "Thesis approved"

@hug.post("/rejectThesis", )
def rejectThesis(id: hug.types.text):
    c = db.cursor()
    c.execute("""UPDATE thesis SET approved=0 WHERE id = %s""", (student_id))
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

@hug.delete("/removeThesis")
def removeThesis(id: hug.types.text):
    c = db.cursor()
    c.execute("""DELETE FROM thesis WHERE id = %s""", (id,))
    c.close()
