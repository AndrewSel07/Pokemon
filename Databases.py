import sqlite3

#Student_Data = [["Walter", "White", "Passed", 90.3, 100, 98.7, 89.9, 94.7],["Jesse", "Pinkman", "Failed", 21.3, 55.3, 52.8, 31.2, 40.2],["Gus", "Fring", "Passed", 92.6, 84.5, 87.2, 94.7, 89.8],["Tuco", "Salamanca", "Failed", 40.3, 38.6, 45.8, 67.9, 48.2],["Hank", "Shradder", "Passed", 80.5, 70.4, 68.7, 73.2, 73.2]
#]

'''EvoLevel = 1

if EvoLevel == 100:'''

movelist = [["X Scissor", "Bug Buzz", "Bug Bite", "Signal Beam"], ["Thunderbolt", "Volt Tackle", ""]]
    
def create_connection(db_file):
    #create a database connection to the SQLite database
    #return: Connection object or None
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Exception as e:
        print(e)
    return conn

def create_table(conn,table, columns):
    col = ",".join(columns)
    sql = f'''CREATE TABLE IF NOT EXISTS {table}( id INTEGER PRIMARY KEY, {col});'''
    conn.execute(sql)

def insert_db(conn,table, columns,data):
    sql=f'''INSERT INTO {table} {tuple(columns)} VALUES {tuple(data)};'''
    conn.execute(sql)
    conn.commit()

def select_db(conn,table,columns_and_data=None):
    if not columns_and_data==None:
        col = " AND ".join(columns_and_data)
        sql=f'''SELECT * FROM {table} WHERE {col}'''
        return conn.execute(sql)
    else:
        sql =f"SELECT * from {table}"
        return conn.execute(sql)
   
def delete_db(conn,table,column,what_to_remove):
    sql=f'''DELETE FROM {table} WHERE {column} = {what_to_remove}'''
    conn.execute(sql)
    conn.commit()  

def update_db(conn,table,columns_and_data,where_to_update):
    col = ",".join(columns_and_data)
    sql = f"UPDATE {table} set {col} where {where_to_update}"
    conn.execute(sql)
    conn.commit()

connection = create_connection("db_file.db")
create_table(connection,"Info",["HP REAL","ATK REAL","DEF TEXT","SPA REAL","SPD REAL"," SPE REAL", "EvoLevel REAL"])
results=select_db(connection,"Pokedex").fetchall()
Students = list(map(list, results))