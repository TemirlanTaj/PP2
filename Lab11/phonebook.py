import psycopg2
import csv

conn = psycopg2.connect(
    database="postgres",
    user="postgres",
    host="localhost",
    password="12345678",
    port=5432
)
cur = conn.cursor()

# Create table and database functions
cur.execute("DROP TABLE IF EXISTS PhoneBook CASCADE;")
cur.execute("""
    CREATE TABLE PhoneBook(
        Name VARCHAR(255) UNIQUE NOT NULL,
        Phone VARCHAR(255) NOT NULL 
    )
""")

#search by pattern
cur.execute("""
    CREATE OR REPLACE FUNCTION search_by_pattern(pattern TEXT)
    RETURNS TABLE (name VARCHAR, phone VARCHAR) AS $$
    BEGIN
        RETURN QUERY
        SELECT Name, Phone FROM PhoneBook
        WHERE Name ILIKE '%%' || pattern || '%%' OR Phone LIKE '%%' || pattern || '%%';
    END;
    $$ LANGUAGE plpgsql;""")

#update users phone number
cur.execute("""
    CREATE OR REPLACE PROCEDURE insert_update_user(user_name VARCHAR, user_phone VARCHAR)
    AS $$
    BEGIN
        INSERT INTO PhoneBook (Name, Phone)
        VALUES (user_name, user_phone)
        ON CONFLICT (Name) DO UPDATE
        SET Phone = EXCLUDED.Phone;
    END;
    $$ LANGUAGE plpgsql; """)

#get phone numbers paginated
cur.execute("""CREATE OR REPLACE FUNCTION get_phones_paginated(lim INT, offs INT)
    RETURNS TABLE (name VARCHAR, phone VARCHAR) AS $$
    BEGIN
        RETURN QUERY
        SELECT pb.Name, pb.Phone FROM PhoneBook pb
        ORDER BY Name
        LIMIT lim OFFSET offs;
    END;
    $$ LANGUAGE plpgsql;""")

#insert multiple users
cur.execute("""
    CREATE OR REPLACE FUNCTION insert_many_users(names TEXT[], phones TEXT[])
    RETURNS TABLE (invalid_name TEXT, invalid_phone TEXT) AS $$
    DECLARE
        i INT;
    BEGIN
        FOR i IN 1..array_length(names, 1) LOOP
            IF phones[i] ~ '^[0-9]{8,}$' THEN
                INSERT INTO PhoneBook (Name, Phone)
                VALUES (names[i], phones[i])
                ON CONFLICT (Name) DO UPDATE
                SET Phone = EXCLUDED.Phone;
            ELSE
                invalid_name := names[i];
                invalid_phone := phones[i];
                RETURN NEXT;
            END IF;
        END LOOP;
    END;
    $$ LANGUAGE plpgsql; """)

#delete user by name or number (can delete multiple names and numbers)
cur.execute("""
    CREATE OR REPLACE FUNCTION delete_user(search_term TEXT, by_name BOOLEAN)
    RETURNS INTEGER AS $$
    DECLARE
        deleted_rows INTEGER;
    BEGIN
        IF by_name THEN
            DELETE FROM PhoneBook WHERE Name = search_term;
        ELSE
            DELETE FROM PhoneBook WHERE Phone = search_term;
        END IF;
        GET DIAGNOSTICS deleted_rows = ROW_COUNT;
        RETURN deleted_rows;
    END;
    $$ LANGUAGE plpgsql;
""")
conn.commit()

while True:
    print("========================================")
    print("I: Input")
    print("D: Delete")
    print("U: Update")
    print("R: Read")
    print("Q: Quit")
    command = input("Command: ").upper() #added upper to make it more user friendly
    
    if command == "Q":
        break
        
    elif command == "I":
        print("Get information by:")
        print("F: File(csv)")
        print("T: Terminal")
        choice = input("Your choice: ").upper()
        
        if choice == "T":
            name = input("Name: ")
            phone = input("Phone: ")
            try:
                cur.execute("CALL insert_update_user(%s, %s);", (name, phone))
                conn.commit()
                print("Data inserted/updated successfully")
            except Exception as e:
                print(f"Error: {e}")
                conn.rollback()
                
        elif choice == "F":
            try:
                names = []
                phones = []
                with open(input("Enter the path: "), 'r') as file:
                    reader = csv.reader(file)
                    next(reader)  # Skip header of the file
                    for row in reader:
                        names.append(row[0])
                        phones.append(row[1])
                
                cur.execute("SELECT * FROM insert_many_users(%s, %s);", (names, phones))
                invalid = cur.fetchall()
                conn.commit()
                
                if invalid:
                    print("\nInvalid entries:")
                    for row in invalid:
                        print(f"Name: {row[0]}, Phone: {row[1]}")
                else:
                    print("All entries inserted successfully")
                    
            except Exception as e:
                print(f"Error: {e}")
                conn.rollback()
                
    elif command == "U":
        print("Update phone for:")
        name = input("Enter name: ")
        new_phone = input("New phone: ")
        try:
            cur.execute("CALL insert_update_user(%s, %s);", (name, new_phone))
            conn.commit()
            print("Phone number updated")
        except Exception as e:
            print(f"Error: {e}")
            conn.rollback()
            
    elif command == "R":
        print("Read options:")
        print("1. Search by pattern")
        print("2. Paginated view")
        print("3. Standard view")
        choice = input("Choose read mode: ")
        
        if choice == "1":
            pattern = input("Enter search pattern: ")
            cur.execute("SELECT * FROM search_by_pattern(%s);", (pattern,))
        elif choice == "2":
            limit = input("Enter limit: ")
            offset = input("Enter offset: ")
            cur.execute("SELECT * FROM get_phones_paginated(%s, %s);", (limit, offset))
        else:
            cur.execute("SELECT * FROM PhoneBook;")
            
        rows = cur.fetchall()
        print("Name      Phone")
        if rows:
            maxLenOfRow = 0
            for i in range(len(rows)):
                if len(rows[i]) >= maxLenOfRow:
                    maxLenOfRow = len(rows[i])
        if rows:
            for row in rows:
                print(row[0], end=" "*(maxLenOfRow*4 - len(row[0])) + "|")
                print(row[1])
        else:
            print("No records found")
            
    elif command == "D":
        print("Delete by:")
        print("N: Name")
        print("P: Phone")
        choice = input("Your choice: ").upper()
        
        if choice == "N":
            term = input("Enter name to delete: ")
            cur.execute("SELECT delete_user(%s, TRUE);", (term,))
        elif choice == "P":
            term = input("Enter phone to delete: ")
            cur.execute("SELECT delete_user(%s, FALSE);", (term,))
            
        deleted = cur.fetchone()[0]
        conn.commit()
        if deleted > 0:
            print(f"Deleted {deleted} records")
        else:
            print("No records deleted")
cur.close()
conn.close()