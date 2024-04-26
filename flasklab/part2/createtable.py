import psycopg2

# This function creates the two tables
def create_tables():
    
    conn = psycopg2.connect(
        host="localhost",
        port=5432,   
        database="liangl",
        user="liangl",
        password="ruby383expo")

    if conn is not None:
            cur = conn.cursor()

            sql_nt = """DROP TABLE IF EXISTS nametime;
                           CREATE TABLE nametime (
                             Firstname text,
                             Lastname text,
                             year real
                           );"""
            
            cur.execute( sql_nt )
            print("Table created.")
            

            conn.commit()
            
    else:
        print( "Problem with Connection" )
    return None

create_tables()
