import json
import os
#import libary

file_name = 'library_data.json'
borrowed_books = 'borrowed_books.json'
#name files


def dump():
    with open(file_name, 'w') as f:
        json.dump(booksinstock, f)
# updates file1    


if os.path.exists(file_name):
    with open(file_name, 'r') as f:
        booksinstock = json.load(f)
# updates file2         

else:
    booksinstock = [
    "Harry Potter and the Sorcerer's Stone",
    "Harry Potter and the Chamber of Secrets",
    "The Hobbit",
    "To Kill a Mockingbird",
    "1984",
    "Pride and Prejudice",
    "The Great Gatsby",
    "The Catcher in the Rye",
    "The Lord of the Rings: The Fellowship of the Ring",
    "The Lord of the Rings: The Two Towers",
    "The Lord of the Rings: The Return of the King",
    "Charlotte's Web",
    "The Lion, the Witch and the Wardrobe",
    "Matilda",
    "James and the Giant Peach",
    "Percy Jackson and the Olympians: The Lightning Thief",
    "Diary of a Wimpy Kid",
    "The Hunger Games",
    "Catching Fire",
    "Mockingjay",
    "Wonder",
    "The Maze Runner",
    "Divergent",
    "The Fault in Our Stars",
    "A Wrinkle in Time",
    "Bridge to Terabithia",
    "The BFG",
    "Holes",
    "Anne of Green Gables",
    "Little Women"
    ]
if os.path.exists(borrowed_books):
    with open(borrowed_books, 'r') as f:
        not_booksinstock = json.load(f)
        

else:
    not_booksinstock=[]

def dump2():
    with open(borrowed_books, 'w') as f:
        json.dump(not_booksinstock, f)

collect_return = input("collect or return?... ")
if collect_return == "collect":
    what_book = input("Enter book name... ")
    if what_book in booksinstock:
        booksinstock.remove(what_book)
        not_booksinstock.append(what_book)
        dump()
        dump2()
        print("You may take your book")
    else:
        print("book not in stock")
elif collect_return == "return":
    what_book2 = input("Enter book name... ")
    if what_book2 in not_booksinstock:
        not_booksinstock.remove(what_book2)
        booksinstock.append(what_book2)
        dump()
        dump2()
        print("thank you")
    else:
        print("book not borrowed")
else:
    print("invalid input please rerun the program and type collect or return")

    




