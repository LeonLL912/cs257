import psycopg2

# This function sends an SQL query to the database
def test_query_one_1():

    # You will need to change the Password to use this code
    
    conn = psycopg2.connect(
        host="localhost",
        port=5432,   
        database="liangl",
        user="liangl",
        password="ruby383expo")

    cur = conn.cursor()

    sql = "SELECT city FROM uspop1k WHERE city = 'Northfield' "
    
    cur.execute( sql )

    # fetchone() returns one row that matches your query
    row = cur.fetchone()

    if (row != "None"):
        print(row)
    else:
        print("There is no data about Northfield in this data set.")
    
    return None






# This function sends an SQL query to the database
def test_query_one_2():

    # You will need to change the Password to use this code
    
    conn = psycopg2.connect(
        host="localhost",
        port=5432,   
        database="liangl",
        user="liangl",
        password="ruby383expo")

    cur = conn.cursor()

    sql_largest_pop = """SELECT * FROM uspop1k ORDER BY pop DESC
             LIMIT 1; """
    
    cur.execute( sql_largest_pop )

    # fetchone() returns one row that matches your query
    row = cur.fetchone()

    if (row != "None"):
        print(row)
    else:
        print("Error.")
    
    return None







# This function sends a query that returns many items
def test_query_one_3():

    # You will need to change the Password to use this code
    
    conn = psycopg2.connect(
        host="localhost",
        port=5432,   
        database="liangl",
        user="liangl",
        password="ruby383expo")

    cur = conn.cursor()

    sql_least_MN_city = """SELECT city FROM uspop1k WHERE city = 'Minnesota' ORDER BY pop ASC
             LIMIT 1;"""
    
    cur.execute( sql_least_MN_city )

    # fetchone() returns one row that matches your query
    row = cur.fetchone()

    if (row != "None"):
        print(row)
    else:
        print("Error.")
    
    return row








# This function sends a query that returns many items
def test_query_all_4():

    # You will need to change the Password to use this code
    
    conn = psycopg2.connect(
        host="localhost",
        port=5432,   
        database="liangl",
        user="liangl",
        password="ruby383expo")

    cur = conn.cursor()

    sql_directions_1 = "SELECT city FROM uspop1k ORDER BY lat DESC LIMIT 1;"
    cur.execute( sql_directions_1 )
    row_1 = cur.fetchone()
    print("Furthest North: "+row_1)

    sql_directions_2 = "SELECT city FROM uspop1k ORDER BY lat ASC LIMIT 1;"
    cur.execute( sql_directions_2 )
    row_2 = cur.fetchone()
    print("Furthest South: "+row_2)

    sql_directions_3 = "SELECT city FROM uspop1k ORDER BY lon DESC LIMIT 1;"
    cur.execute( sql_directions_3 )
    row_3 = cur.fetchone()
    print("Furthest East: "+row_3)

    sql_directions_4 = "SELECT city FROM uspop1k ORDER BY lon ASC LIMIT 1;"
    cur.execute( sql_directions_4 )
    row_4 = cur.fetchone()
    print("Furthest West: "+row_4)

    
    return None




# Calling functions
test_query_one_1()
test_query_one_2()
test_query_one_3()
test_query_all_4()