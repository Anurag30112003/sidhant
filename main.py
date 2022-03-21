import mysql.connector
import os
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd=f'anurag123',
    database="book"
)
mycursor = mydb.cursor()

mycursor.execute("DROP TABLE IF EXISTS bill")
mycursor.execute("CREATE TABLE IF NOT EXISTS bill(BOOK_NAME VARCHAR(220),PRICE VARCHAR(220))")

def add_book():
    isbn_no = int(input("Enter ISBN no: "))
    name = input("Enter the name of the book: ")
    language = input("Enter the language of the book: ")
    quantity = int(input("Enter the quantity of the book: "))
    price = int(input("Enter the price of the book: "))
    sql = "INSERT INTO book (isbn_no,name, language,quantity ,price) VALUES (%s, %s, %s,%s,%s)"
    val = (isbn_no, name, language,quantity, price)
    mycursor.execute(sql, val)
    mydb.commit()
    print(f"{mycursor.rowcount} record inserted.")

def drop_column():
    isbn_no = int(input("Enter the isbn no. to be deleted: "))
    sql = "DELETE FROM book WHERE isbn_no = %s"
    mycursor.execute(sql,(isbn_no,))
    print(f"Column {isbn_no} deleted successfully")
    mydb.commit()

def show_books():
    mycursor.execute("SELECT * FROM book")
    myresult = mycursor.fetchall()
    for x in myresult:
        print(x)

def buy_book():
    isbn_no = int(input("Enter the isbn no. of the book: "))
    mycursor.execute("SELECT * FROM book WHERE isbn_no = %s",(isbn_no,))
    myresult = mycursor.fetchall()
    for x in myresult:
        print(x)
    quantity = int(input("Enter the quantity of the book: "))
    if quantity > x[3]:
        print("Sorry, we don't have that many books in stock")
    elif x[3] == 0:
        print("Sorry, we don't have that book in stock")
    else:
        print("Thank you for your purchase")
        new_quantity = x[3] - quantity
        mycursor.execute("UPDATE book SET quantity = %s WHERE isbn_no = %s",(new_quantity,isbn_no))
        mycursor.execute("INSERT INTO bill (BOOK_NAME,PRICE) VALUES (%s, %s)",(x[1],x[4]))
        mydb.commit()


def bill_print():
    print("Thank you for shopping with us")
    print("Your bill is: ")
    mycursor.execute("SELECT * FROM bill")
    myresult = mycursor.fetchall()
    for x in myresult:
        print(x)

def start():
    while True:
        print("1. Add a book")
        print("2. Drop a column")
        print("3. Show all books")
        print("4. Buy Book")
        print("5. Print bill")
        print("6. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            add_book()
        elif choice == 2:
            drop_column()
        elif choice == 3:
            show_books()
        elif choice == 4:
            buy_book()
        elif choice == 5:
            bill_print()
        elif choice == 6:   
            break
        else:
            print("Invalid choice")
            start()
start()
