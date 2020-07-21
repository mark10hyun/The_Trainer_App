import _csv

import mysql.connector


def newUser(userfName, userlName, goal):
    connection = mysql.connector.connect(host="34.82.241.205", user="datagrip", password="password123",
                                         database="FitnessTracker")
    curr = connection.cursor()
    newuserID = curr.lastrowid
    print((userlName, userfName, goal))
    if goal == "Weight Loss":
        addNewUser = "INSERT INTO Users(PlanID, GoalID,FirstName, LastName) VALUES (%s,%s,%s,%s)"
        newUserValues = (1, 1, userfName, userlName)
    elif goal == "Bulk":
        addNewUser = "INSERT INTO Users(PlanID, GoalID,FirstName, LastName) VALUES (%s,%s,%s,%s)"
        newUserValues = (2, 2, userfName, userlName)
    else:
        addNewUser = "INSERT INTO Users(PlanID, GoalID,FirstName, LastName) VALUES (%s,%s,%s,%s)"
        newUserValues = (3, 3, userfName, userlName)
    curr.execute(addNewUser, newUserValues)
    connection.commit()
    connection.close()
    output = ''
    output = output + '                        Name: '+userfName + ' ' + userlName + '     Goal: ' + goal
    return output
# Showing all the data on list box
def showData():
    connection = mysql.connector.connect(host="34.82.241.205", user="datagrip", password="password123",
                                         database="FitnessTracker")
    curr = connection.cursor()
    curr.execute("SELECT FirstName, LastName, Description FROM Users Join Goals G on Users.GoalID = G.GoalID WHERE isDeleted = 0 ORDER BY UserID")
    rows = curr.fetchall()
    connection.close()
    output = ''
    for x in rows:
        output = output + '| Name: ' + x[0] + ' ' + x[1] + ' | Goal: ' + x[2] + '| \n'
    return output
    connection.close()
def deleteUser():
    connection = mysql.connector.connect(host="34.82.241.205", user="datagrip", password="password123",
                                         database="FitnessTracker")
    curr = connection.cursor()
    curr.close()
def userUpdate(FirstName="", LastName="", GoalDesc=""):
    connection = mysql.connector.connect(host="34.82.241.205", user="datagrip", password="password123",
                                         database="FitnessTracker")
    curr = connection.cursor()
    finduserID = "SELECT UserID FROM Users WHERE FirstName = %s AND LastName = %s"
    name = (FirstName, LastName)
    curr.execute(finduserID, name)
    result1 = curr.fetchone()
    UID = result1[0]
    print(UID)
    if GoalDesc == "Weight loss" or "weight" or 'weight loss' or "Weight Loss":
        updateSQLgoal = """UPDATE Users SET GoalID = '1', PlanID = '1'  WHERE UserID = %s""" %UID
        curr.execute(updateSQLgoal)
        connection.commit()
    elif GoalDesc == "Bulk":
        updateSQL = """UPDATE Users SET GoalID = '2' , PlanID = '2' WHERE UserID = %s""" %UID
        curr.execute(updateSQL)
    else:
        updateSQL = """UPDATE Users SET GoalID = '3', PlanID = '3' WHERE UserID = %s""" %UID
        curr.execute(updateSQL)
    connection.commit()
    connection.close()
    output = ''
    output = output + '                        Name: ' + FirstName + ' ' + LastName + '     Goal: ' + GoalDesc
    return output
def searchData(FirstName="", LastName=""):
    connection = mysql.connector.connect(host="34.82.241.205", user="datagrip", password="password123",
                                         database="FitnessTracker")
    curr = connection.cursor()
    print("hello")
    intialSearch = (FirstName, LastName)
    finduserID = "SELECT UserID FROM Users WHERE FirstName = %s AND LastName = %s"
    findPlanID = "SELECT PlanID FROM Users WHERE FirstName = %s AND LastName = %s"
    deleted = "SELECT isDeleted FROM Users WHERE FirstName = %s AND LastName = %s"
    curr.execute(finduserID, intialSearch)
    result1 = curr.fetchone()
    UID = result1[0]
    UID = (int(UID),)
    curr.execute(findPlanID, intialSearch)
    result2 = curr.fetchone()
    PID = result2[0]
    PID = int(PID)
    curr.execute(deleted, intialSearch)
    result3 = curr.fetchone()
    isdeleted = result3[0]
    while isdeleted == 0:
        if PID == 1:
            search = """SELECT FirstName, Lastname, PlanDisc AS plan, (SELECT ExerciseName FROM Exercises JOIN plan P on Exercises.ExerciseID = P.Ex1ID WHERE ExerciseID = P.Ex1ID AND PlanID = 1) AS EX1, (SELECT ExerciseName FROM Exercises JOIN plan P on Exercises.ExerciseID = P.Ex2ID WHERE ExerciseID = P.Ex2ID AND PlanID = 1) AS EX2,(SELECT ExerciseName FROM Exercises JOIN plan P on Exercises.ExerciseID = P.Ex3ID WHERE ExerciseID = P.Ex3ID AND PlanID = 1) AS EX3, (SELECT ExerciseName FROM Exercises JOIN plan P on Exercises.ExerciseID = P.Ex4ID WHERE ExerciseID = P.Ex4ID AND PlanID = 1) AS EX4, (SELECT ExerciseName FROM Exercises JOIN plan P on Exercises.ExerciseID = P.Ex5ID WHERE ExerciseID = P.Ex5ID AND PlanID = 1) AS EX5,(SELECT ExerciseName FROM Exercises JOIN plan P on Exercises.ExerciseID = P.Ex6ID WHERE ExerciseID = P.Ex6ID AND PlanID = 1) AS EX6 FROM Users JOIN plan p2 on Users.PlanID = p2.PlanID WHERE UserID = %d AND isDeleted = 0""" % (
                UID)
        elif PID == 2:
            search = """SELECT FirstName, Lastname, PlanDisc AS plan, (SELECT ExerciseName FROM Exercises JOIN plan P on Exercises.ExerciseID = P.Ex1ID WHERE ExerciseID = P.Ex1ID AND PlanID = 2) AS EX1, (SELECT ExerciseName FROM Exercises JOIN plan P on Exercises.ExerciseID = P.Ex2ID WHERE ExerciseID = P.Ex2ID AND PlanID = 2) AS EX2,(SELECT ExerciseName FROM Exercises JOIN plan P on Exercises.ExerciseID = P.Ex3ID WHERE ExerciseID = P.Ex3ID AND PlanID = 2) AS EX3, (SELECT ExerciseName FROM Exercises JOIN plan P on Exercises.ExerciseID = P.Ex4ID WHERE ExerciseID = P.Ex4ID AND PlanID = 2) AS EX4, (SELECT ExerciseName FROM Exercises JOIN plan P on Exercises.ExerciseID = P.Ex5ID WHERE ExerciseID = P.Ex5ID AND PlanID = 2) AS EX5,(SELECT ExerciseName FROM Exercises JOIN plan P on Exercises.ExerciseID = P.Ex6ID WHERE ExerciseID = P.Ex6ID AND PlanID = 2) AS EX6 FROM Users JOIN plan p2 on Users.PlanID = p2.PlanID WHERE UserID = %d AND isDeleted = 0""" % (
                UID)
        else:
            search = "SELECT FirstName, Lastname, PlanDisc AS plan, (SELECT ExerciseName FROM Exercises JOIN plan P on Exercises.ExerciseID = P.Ex1ID WHERE ExerciseID = P.Ex1ID AND PlanID = 3) AS EX1, (SELECT ExerciseName FROM Exercises JOIN plan P on Exercises.ExerciseID = P.Ex2ID WHERE ExerciseID = P.Ex2ID AND PlanID = 3) AS EX2, (SELECT ExerciseName FROM Exercises JOIN plan P on Exercises.ExerciseID = P.Ex3ID WHERE ExerciseID = P.Ex3ID AND PlanID = 3) AS EX3, (SELECT ExerciseName FROM Exercises JOIN plan P on Exercises.ExerciseID = P.Ex4ID WHERE ExerciseID = P.Ex4ID AND PlanID = 3) AS EX4, (SELECT ExerciseName FROM Exercises JOIN plan P on Exercises.ExerciseID = P.Ex5ID WHERE ExerciseID = P.Ex5ID AND PlanID = 3) AS EX5, (SELECT ExerciseName FROM Exercises JOIN plan P on Exercises.ExerciseID = P.Ex6ID WHERE ExerciseID = P.Ex6ID AND PlanID = 3) AS EX6 FROM Users JOIN plan p2 on Users.PlanID = p2.PlanID WHERE UserID = %d AND isDeleted = 0" % (
                UID)
        curr.execute(search)
        rows = curr.fetchall()
        output = ''
        for x in rows:
            output = output + '\n' + ' Name: ' + x[0] + ' ' + x[1] + ' \n' + '\n' + ' Goal: ' + x[
                2] + ' ' + '\n' + '\n' + ' Plan: ' + '\n' + '     Exercise 1: ' + x[3] + '\n' + '     Exercise 2: ' + x[
                     4] + '\n' + '     Exercise 3: ' + x[5] + '\n' + '     Exercise 4: ' + x[
                     6] + '\n' + '     Exercise 5: ' + x[7] + '\n' + '     Exercise 6: ' + x[8]
        return output
        connection.close()
    if isdeleted == 1:
        return '\n' + "This user has been deleted."

def userDelete(FirstName, LastName):
    connection = mysql.connector.connect(host="34.82.241.205", user="datagrip", password="password123",
                                         database="FitnessTracker")
    curr = connection.cursor()
    finduserID = "SELECT UserID FROM Users WHERE FirstName = %s AND LastName = %s"
    name = (FirstName, LastName)
    curr.execute(finduserID, name)
    result1 = curr.fetchone()
    UID = result1[0]
    deleteSQL = """UPDATE Users SET isDeleted = 1 WHERE UserID = %s""" %UID
    curr.execute(deleteSQL)
    connection.commit()
    connection.close()
    return '\n' + "User is Deleted"

def exportCSV():
    connection = mysql.connector.connect(host="34.82.241.205", user="datagrip", password="password123",
                                         database="FitnessTracker")
    curr = connection.cursor()
    with open('FitnessUsers.csv', 'w') as f:
        curr.execute(
            "SELECT FirstName, LastName, Description FROM Users Join Goals G on Users.GoalID = G.GoalID WHERE isDeleted = 0 ORDER BY UserID")
        rows = curr.fetchall()
        w = _csv.writer(f)
        for x in rows:
            w.writerow(rows)