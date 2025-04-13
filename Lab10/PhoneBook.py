import psycopg2

conn = psycopg2.connect(
    database="postgres",
    user="postgres",
    host="localhost",
    password="12345678",
    port=5432
)
cur = conn.cursor()

# deleting previous table and creating a new table
cur.execute("DROP TABLE IF EXISTS PhoneBook;")
cur.execute("""
    CREATE TABLE PhoneBook(
        Name VARCHAR(255) NOT NULL,
        Phone VARCHAR(255) NOT NULL 
    )
""")
conn.commit() # making changes persistent


while True:
    print("")
    print("Options:")
    print("I: Input")
    print("D: Delete")
    print("U: Update")
    print("R: Read")
    print("Q: Quit")
    command=input("Command: ")
    if command == "Q":
        break
    elif command == "I":
        print("Get information by:")
        print("F: File(csv)")
        print("T: Terminal")
        choice = input("Your choice: ")
        if choice == "T":
            name=input("Name: ")
            phone=input("Phone: ")
            cur.execute("SELECT EXISTS(SELECT 1 FROM PhoneBook WHERE Name = %s AND Phone = %s);", (name, phone))
            exist = cur.fetchone()[0] #to check if user already exists
            if exist:
                print("It already exists.")
            else:
                cur.execute("INSERT INTO PhoneBook(Name, Phone) VALUES(%s, %s)", (name,phone))
        elif choice == "F":
            with open(input("Enter the path: "), 'r') as file:
                cur.copy_expert("""
                    COPY PhoneBook(Name, Phone)
                    FROM STDIN WITH CSV HEADER DELIMITER ','
                """, file)
                
        conn.commit()
    elif command == "U":
        print("Do you want to update Name(N) or Phone(P):")
        choice = input()
        if choice == "N":
            old_name = input("Current Name: ")
            cur.execute("SELECT EXISTS(SELECT 1 FROM PhoneBook WHERE Name = %s);", (old_name,))
            exist = cur.fetchone()[0]
            if exist:
                new_name = input("New Name: ")
                cur.execute("UPDATE PhoneBook SET Name = %s WHERE Name = %s;", (new_name, old_name))
            else:
                print("This name doesnt exist.")
        elif choice == "P":
            old_phone = input("Current Phone: ")
            cur.execute("SELECT EXISTS(SELECT 1 FROM PhoneBook WHERE Phone = %s);", (old_phone,))
            exist = cur.fetchone()[0]
            if exist:
                new_phone = input("New Phone: ")
                cur.execute("UPDATE PhoneBook SET Phone = %s WHERE Phone = %s;", (new_phone, old_phone))
            else:
                print("This phone doesnt exist.")
    elif command == "R":
        print("Sort by column:")
        print("N: Name")
        print("P: Phone")
        print("Anything else: Unsorted data")
        choice = input("Your choice: ")
        whatToShow = "*" # asterisk means everything 
        howToSort = "" 
        if choice == "N" or choice == "P":
            if choice == "N":
                col = "Name"    
            else:
                col = "Phone"
            print("Choose sort order:")
            print("A: Ascending")
            print("D: Descending")
            print("Anything else: Unchanged")
            choice = input("Your choice: ")
            if choice == "A":
                howToSort = f"ORDER BY {col} ASC"
            elif choice == "D":
                howToSort = f"ORDER BY {col} DESC"
            print("Show:")
            print("N: Only names")
            print("P: Only phones")
            print("Anything else: Both names and phones")
            choice = input("Your choice: ")
            if choice == "N":
                whatToShow = "Name"
            elif choice == "P":
                whatToShow = "Phone"
            choice = ""

        cur.execute(f"SELECT {whatToShow} FROM PhoneBook {howToSort};")
        rows = cur.fetchall()
        maxLenOfRow = 0
        for i in range(len(rows)):
            if len(rows[i]) >= maxLenOfRow:
                maxLenOfRow = len(rows[i])
        if whatToShow == "*":
            whatToShow = "Name      Phone"
        if rows:
            print(whatToShow)
            print("-" * len(whatToShow)*3)
            for row in rows:
                print(row[0], end=" "*(maxLenOfRow*4 - len(row[0])) + "|")
                print(row[1])
        else:
            print("")
            print("No records found.")
    elif command == "D":
        print("Delete by:")
        print("N: Name")
        print("P: Phone")
        choice = input("Your choice: ")
        if choice == "N":
            nameToDel = input("Deleting Name: ")
            cur.execute("SELECT EXISTS(SELECT 1 FROM PhoneBook WHERE Name = %s);", (nameToDel,))
            exist = cur.fetchone()[0]
            if exist:
                cur.execute("DELETE FROM PhoneBook WHERE Name = %s;", (nameToDel,))
            else:
                print("This name doesnt exist.")
        elif choice == "P":
            phoneToDel = input("Deleting Phone: ")
            cur.execute("SELECT EXISTS(SELECT 1 FROM PhoneBook WHERE Phone = %s);", (phoneToDel,))
            exist = cur.fetchone()[0]
            if exist:
                cur.execute("DELETE FROM PhoneBook WHERE Phone = %s;", (phoneToDel,))
            else:
                print("This phone doesnt exist.")
            
cur.close()
conn.close()