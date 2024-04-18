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

            sql_USpop = """DROP TABLE IF EXISTS USpop
                           CREATE TABLE USpop (
                             code text,
                             USstate text,
                             pop real
                           );"""
            
            sql_1k = """DROP TABLE IF EXISTS USpop1k;
                        CREATE TABLE USpop1k (
                          city text,
                          USstate text,
                          pop real,
                          lat real,
                          lon real
                        );"""
            
            cur.execute( sql_USpop )
            cur.execute( sql_1k )
            

            conn.commit()
    else:
        print( "Problem with Connection" )
    print("The end of create_tables.")
    return None


