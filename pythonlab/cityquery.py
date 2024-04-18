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

    if (row != None):
        print("Yayyy, we have", row[0])
        print("")
    else:
        print("There is no data about Northfield in this data set.")
        print("")
    
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

    sql_largest_pop = """SELECT city FROM uspop1k ORDER BY pop DESC
             LIMIT 1; """
    
    cur.execute( sql_largest_pop )

    # fetchone() returns one row that matches your query
    row = cur.fetchone()

    if (row != None):
        print("The city with largest population in the United States is:", row[0])
        print("")
    else:
        print("Error.")
        print("")
    
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

    sql_least_MN_city = """SELECT city FROM uspop1k WHERE USstate = 'Minnesota' ORDER BY pop ASC
             LIMIT 1;"""
    
    cur.execute( sql_least_MN_city )

    # fetchone() returns one row that matches your query
    row = cur.fetchone()

    if (row != None):
        print("The city with least population in Minnesota is:", row[0])
        print("")
    else:
        print("Error.")
        print("")
    
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
    print("The furthest North city in this dataset is:", row_1[0])

    sql_directions_2 = "SELECT city FROM uspop1k ORDER BY lat ASC LIMIT 1;"
    cur.execute( sql_directions_2 )
    row_2 = cur.fetchone()
    print("The furthest South city in this dataset is:", row_2[0])

    sql_directions_3 = "SELECT city FROM uspop1k ORDER BY lon DESC LIMIT 1;"
    cur.execute( sql_directions_3 )
    row_3 = cur.fetchone()
    print("The furthest East city in this dataset is:", row_3[0])

    sql_directions_4 = "SELECT city FROM uspop1k ORDER BY lon ASC LIMIT 1;"
    cur.execute( sql_directions_4 )
    row_4 = cur.fetchone()
    print("The furthest West city in this dataset is:", row_4[0])

    
    return None





def test_query_all_5():

    # You will need to change the Password to use this code
    
    conn = psycopg2.connect(
        host="localhost",
        port=5432,   
        database="liangl",
        user="liangl",
        password="ruby383expo")

    cur = conn.cursor()

    statename = input("Please enter a state that you want to know about its total population:")
    sql = "SELECT pop FROM states WHERE USstate = %s"
    
    cur.execute( sql, [statename]  )

    # fetchall() returns a list containing all rows that matches your query
    row_list = cur.fetchall()

    # It is often useful to loop through all rows in a query result
    totalpop = 0
    for row in row_list:
        totalpop += row[0]

    print(totalpop)
    
    return None




# Calling functions
test_query_one_1()
test_query_one_2()
test_query_one_3()
test_query_all_4()
test_query_all_5()