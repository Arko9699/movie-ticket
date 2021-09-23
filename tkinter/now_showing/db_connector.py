import mysql.connector

def movieDetails(movie_name, db_con):
    mycursor = db_con.cursor(prepared=True)
    query = "SELECT DISTINCT movie_desc,  movie_genre , movie_length, movie_rating FROM movie_details WHERE UPPER(TRIM(movie_name)) = '" + movie_name.strip() + "' "
    mycursor.execute(query)
    myresult = mycursor.fetchall()
    return myresult

def movieLangDetails(movie_name, db_con):

    mycursor = db_con.cursor(prepared=True)
    query = "SELECT DISTINCT movie_lang, movie_d FROM movie_details WHERE UPPER(TRIM(movie_name)) = '" + movie_name.strip() + "' order by movie_lang"
    mycursor.execute(query)
    myresult = mycursor.fetchall()
    return myresult

def movieHallDetails(movie_name, movie_lang, movie_d, db_con ):

    mycursor = db_con.cursor(prepared=True)
    query = "SELECT DISTINCT movie_venue, movie_timings FROM movie_details WHERE UPPER(TRIM(movie_name)) = '" + movie_name.strip() + "' and movie_lang = '" + movie_lang.strip() + "' and movie_d = '" + movie_d.strip() + "'  order by movie_venue"
    mycursor.execute(query)
    myresult = mycursor.fetchall()
    return myresult

def createCon():
    db_con = getMySQLConnection("localhost", "root", "newpassword69", "master")
    return db_con

def closeCon(db_con):
    db_con.commit()
    db_con.close()

def getMySQLConnection(host, username, password, dbName):
    return mysql.connector.connect(host=host,
                                   user=username,
                                   passwd=password,
                                   database=dbName,
                                   use_pure=True)