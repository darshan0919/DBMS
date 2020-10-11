import psycopg2
import sys
import os
import Queries_file

def exe_query(cursor, query):
    try:
        cursor.execute(query)
        answer = cursor.fetchall()
        print("\n\nAnswer : ")
        if len(answer)==0:
            print("Answer to your query is NULL.")
        else:
            for ans in answer:
                print(ans)
    except (Exception, psycopg2.Error) as error:
        print("Please enter valid query")
        

conn = psycopg2.connect(database = '201701436', user = '201701436',
                       password = 'Drskrishna1903@',
                       host = '10.100.71.21', port = '5432' )
cursor = conn.cursor()



cursor.execute("SET SEARCH_PATH TO forest_management");
os.system("cls")
print("\n----------------Welcome to Forest Management Database-------------------")


while True:
    print("\n\nWe have so many quries for you : ")
    with open("Queries.txt","r") as file:
        print(file.read())
    print("  17). Or you can enter your own query.")
    print("  18). Insert Data.")
    print("  19). Exit.\n")

    try:
        inp = int(input("What would you like to do : "))

        if inp<=16:
            answer = Queries_file.give_answer(inp)
            exe_query(cursor, answer)    
        elif inp==17:
            q = input("Enter your query : ")
            exe_query(cursor, q)
        elif inp==18:
            answer = Queries_file.insert()
            cursor.execute(answer)
            conn.commit()
        elif inp==19:
            os.system("cls")
            print("Sayonara.\nThank you for visiting us.\nSee you next time.")
            print("Project Given by Prof. PM Jat from DAIICT")
            break
        else:
            print("Invalid option. Please enter valid option.")
            
    except (Exception, psycopg2.Error) as error :
        print("Invalid option. Please enter valid option.")

cursor.close()
