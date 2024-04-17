import psycopg2

# This function sends an SQL query to the database
def test_query_one_1():

    # You will need to change the Password to use this code
    
    conn = psycopg2.connect(
        host="localhost",
        port=5432,   
        database="liangl",
        user="liangl",
        password=" ruby383expo")

    cur = conn.cursor()

    sql = "SELECT name, abb FROM city WHERE abb = 'Northfield' "
    
    cur.execute( sql )

    # fetchone() returns one row that matches your query
    row = cur.fetchone()

    if (row != "None"):
        print(row)
    else:
        print("There is no data about Northfield in this data set.")
    # Note: We could access individual items in the row
    # That is, row[0] would be the name column in the previous example
    #   ... and row[1] would be the abb column

    #IMPORTANT: This function doesn't actually change the database
    #If we are trying to change the database ...
    # ... for example, creating a table
    #Then we need the following command to finalize our changes

    conn.commit()
    
    return row






# This function sends an SQL query to the database
def test_query_one_2():

    # You will need to change the Password to use this code
    
    conn = psycopg2.connect(
        host="localhost",
        port=5432,   
        database="liangl",
        user="liangl",
        password=" ruby383expo")

    cur = conn.cursor()

    sql_largest_pop = """ORDER BY population DESC
             LIMIT 1; """
    
    cur.execute( sql_largest_pop )

    # fetchone() returns one row that matches your query
    row = cur.fetchone()

    if (row != "None"):
        print(row)
    else:
        print("Error.")
    # Note: We could access individual items in the row
    # That is, row[0] would be the name column in the previous example
    #   ... and row[1] would be the abb column

    #IMPORTANT: This function doesn't actually change the database
    #If we are trying to change the database ...
    # ... for example, creating a table
    #Then we need the following command to finalize our changes

    conn.commit()
    
    return row







# This function sends a query that returns many items
def test_query_one_3():

    # You will need to change the Password to use this code
    
    conn = psycopg2.connect(
        host="localhost",
        port=5432,   
        database="liangl",
        user="liangl",
        password=" ruby383expo")

    cur = conn.cursor()

    sql_least_MN_city = """SELECT name, abb FROM states WHERE abb = 'MN' ORDER BY pop ASC
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
        password=" ruby383expo")

    cur = conn.cursor()

    sql_directions_1 = "SELECT city_name FROM cities ORDER BY latitude DESC LIMIT 1;"
    cur.execute( sql_directions_1 )
    row_1 = cur.fetchone()
    print("Furthest North: "+row_1)

    sql_directions_2 = "SELECT city_name FROM cities ORDER BY latitude ASC LIMIT 1;"
    cur.execute( sql_directions_2 )
    row_2 = cur.fetchone()
    print("Furthest South: "+row_2)

    sql_directions_3 = "SELECT city_name FROM cities ORDER BY longitude DESC LIMIT 1;"
    cur.execute( sql_directions_3 )
    row_3 = cur.fetchone()
    print("Furthest East: "+row_3)

    sql_directions_4 = "SELECT city_name FROM cities ORDER BY longitude ASC LIMIT 1;"
    cur.execute( sql_directions_4 )
    row_4 = cur.fetchone()
    print("Furthest West: "+row_4)

    
    return None