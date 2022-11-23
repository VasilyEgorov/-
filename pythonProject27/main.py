import sqlite3
from tkinter import *


def addartist():
    newartistname = artistname.get()
    newaddress = artistadd.get()
    newcity = artistcity.get()
    newcountry = artistcountry.get()
    cursor.execute("""INSERT INTO Artists(name, address, city, country)
VALUES (?, ?, ?, ?)""", (newartistname, newaddress, newcity, newcountry))
    db.commit()
    artistname.delete(0, END)
    artistadd.delete(0, END)
    artistcity.delete(0, END)
    artistcountry.delete(0, END)
    artistname.focus()


def clearartist():
    artistname.delete(0, END)
    artistadd.delete(0, END)
    artistcity.delete(0, END)
    artistcountry.delete(0, END)
    artistname.focus()


def addart():
    newartname = artname.get()
    newtitle = arttitle.get()
    newmedium = medium.get()
    newprice = artprice.get()
    cursor.execute("""INSERT INTO Art(artistID, title, medium, price)
VALUES (?, ?, ?, ?)""", (newartname, newtitle, newmedium, newprice))
    db.commit()
    artname.delete(0, END)
    arttitle.delete(0, END)
    medium.set("")
    artprice.delete(0, END)
    artistname.focus()


def clearwindow():
    outputwindow.delete(0, END)


def viewartist():
    cursor.execute("SELECT * FROM Artists")
    for x in cursor.fetchall():
        newrecord = str(x[0])+", "+str(x[1])+", "+str(x[2])+", " + str(x[3]) + ", "+str(x[4]) + ", " + "\n"
        outputwindow.insert(END, newrecord)


def viewart():
    cursor.execute("SELECT * FROM Art")
    for x in cursor.fetchall():
        newrecord = str(x[0]) + ", " + str(x[1]) + ", " + str(x[2]) + ", " + str(x[3]) + ", " + str(x[4]) + ", $" + "\n"
        outputwindow.insert(END, newrecord)


def searchartistoutput():
    selectedartist = searchartist.get()
    cursor.execute("SELECT name FROM Artists WHERE artistid = ?", [selectedartist])
    for x in cursor.fetchall():
        outputwindow.insert(END, x)
        cursor.execute("SELECT name FROM Art WHERE artistid = ?", [selectedartist])
        for x in cursor.fetchall():
            newrecord = str(x[0]) + ", " + str(x[1]) + ", " + str(x[2]) + ", " + str(x[3]) + ", $" + str(x[4]) + "\n"
            outputwindow.insert(END, newrecord)
    searchartist.delete(0, END)
    searchartist.focus()


def searchmediumoutput():
    selectedmedium = medium2.get()
    cursor.execute("""SELECT Art.pieceid, Artists.name, Art.title, Art.medium, Art.
price FROM Artists, Art WHERE Artists.artistid = Art.artistid AND Art.medium = ?""",
[selectedmedium])
    for x in cursor.fetchall():
        newrecord = str(x[0]) + ", " + str(x[1]) + ", " + str(x[2]) + ", " + str(x[3]) + ", $" + str(x[4])+ "\n"
        outputwindow.insert(END, newrecord)
    medium2.set("")


def searchbyprice():
    minprice = selectmin.get()
    maxprice = selectmax.get()
    cursor.execute("""SELECT Art.pieceid, Artists.name, Art.title, Art.medium, Art.price
FROM Artists, Art, WHERE  Artists.artistid = Art.artistid AND Art.price >= ? AND Art.price
<= ?""", [minprice, maxprice])
    for x in cursor.fetchall():
        newrecord = str(x[0]) + ", " + str(x[1]) + ", " + str(x[2]) + ", " + str(x[3]) + ", $" + str(x[4]) + "\n"
        outputwindow.insert(END, newrecord)
    selectmin.delete(0, END)
    selectmax.delete(0, END)
    selectmin.focus()


def sold():
    file = open("SoldArt.txt", "a")
    selectedpiece = soldpiece.get()
    cursor.execute("SELECT * FROM Art WHERE pieceid = ?", [selectedpiece])
    for x in cursor.fetchall():
        newrecord = str(x[0]) + ", " + str(x[1]) + ", " + str(x[2]) + ", " + str(x[3]) + ", " + str(x[4]) + "\n"
        file.write(newrecord)
    file.close()
    cursor.execute("DELETE FROM Art WHERE pieceid = ?", [selectedpiece])
    db.commit()


with sqlite3.connect("Art.db") as db:
    cursor = db.cursor()


cursor.execute("""CREATE TABLE IF NOT EXISTS Artists(
artistid integer PRIMARY KEY, name text, address text, city text, country text);""")


cursor.executescript("""CREATE TABLE IF NOT EXISTS Art(
pieceid integer PRIMARY KEY, artistid integer,title text,
medium text, price integer);""")


window = Tk()
window.title("Art")
window.geometry("1220x600")


titlel1 = Label(text = "Name: ")
titlel1.place(x = 10, y = 10, width = 100, height = 25)
artistnamelbl = Label(text = "Name: ")
titlel1.place(x = 50, y = 40, width = 80, height = 25)
artistname = Entry(text = "")
artistname.place(x = 110, y = 40, width = 200, height = 25)
artistname.focus()
artistaddlbl = Label(text="Museum: ")
artistaddlbl.place(x = 310, y = 40, width = 80, height = 25)
artistadd = Entry(text = "")
artistadd.place(x = 390, y=40, width = 200, height = 25)
artistcitylbl = Label(text = "City: ")
artistcitylbl.place(x = 590, y = 40, width = 80, height = 25)
artistcity = Entry(text = "")
artistcity.place(x = 670, y = 40, width = 100, height = 25)
artistcountylbl = Label(text = "Country: ")
artistcountylbl.place(x = 770, y = 40, width = 80, height = 25)
artistcountry = Entry(text = "")
artistcountry.place(x = 850, y = 40, width = 100, height = 25)
addbtn = Button(text="Add Artist", command=addartist)
addbtn.place(x=110, y=80, width=130, height=25)
clearbtn = Button(text = "Remove Artist", command = addartist)
clearbtn.place(x = 250, y = 80, width = 130, height = 25)
artnamelbl = Label(text = "Artist ID: ")
artnamelbl.place(x = 30,  y = 120, width = 80, height = 25)
artname = Entry(text = "")
artname.place(x = 110, y = 120, width = 50, height = 25)
arttitlelbl = Label(text = "Title: ")
arttitlelbl.place(x = 200, y = 120, width = 80, height = 25)
arttitle = Entry(text = "")
arttitle.place(x = 280, y = 120, width = 280, height = 25)
artmediumlbl = Label(text = "Medium: ")
artmediumlbl.place(x = 590, y = 120, width= 80, height = 25)
medium = StringVar(window)
artmedium = OptionMenu(window, medium, "Oil", "Watercolour", "Ink", "Acrylic")
artmedium.place(x = 670, y = 120, width = 100, height = 25)
artpricelbl = Label(text = "Price: ")
artpricelbl.place(x = 770, y = 120, width = 80, height = 25 )
artprice = Entry(text = "")
artprice.place(x = 850, y = 120, width = 100, height = 25)
addartbtn = Button(text = "Add Detail", command = addart)
addartbtn.place(x = 110, y = 150, width = 130, height = 25)
clearartbtn = Button(text = "Clear Piece", command = addart)
clearartbtn.place(x = 250, y = 150,  width= 130, height = 25)
outputwindow = Listbox()
outputwindow.place(x = 10, y = 200, width= 1000, height = 350)
clearoutputwindow = Button(text = "Clear Output", command = clearwindow)
clearoutputwindow.place(x = 1020, y = 200, width= 155 , height = 25)
viewallartists = Button(text = "View All Artists", command = viewartist)
viewallartists.place(x = 1020, y = 230, width = 155, height = 25)
viewallart = Button(text="View All Art", command=viewart)
viewallart.place(x=1020, y = 260, width= 155, height = 25)
searchartist = Entry(text="")
searchartist.place(x=1020, y=300, width = 50, height = 25)
searchartistbtn = Button(text = "Search by Artist", command = searchartistoutput)
searchartistbtn.place(x = 1075, y = 300, width = 100, height = 25)
medium2 = StringVar(window)
searchmedium = OptionMenu(window, medium2, "Oil", "Watercolour", "Ink  ", "Acrylic")
searchmedium.place(x = 1020, y = 330, width = 100, height = 25)
searchmediumbtn = Button(text = "Search", command = searchmediumoutput)
searchmediumbtn.place(x = 1125, y = 330, width = 50, height = 25)
minlbl = Label(text="Min: ")
minlbl.place(x = 1020, y = 360, width = 75, height = 25)
maxlbl = Label(text = "Max: ")
maxlbl.place(x = 1100, y = 360, width = 75, height = 25)
selectmin = Entry(text="")
selectmin.place(x = 1020, y = 380, width = 75, height = 25)
selectmax = Entry(text="")
selectmax.place(x = 1100, y = 380, width = 75, height = 25)
searchpricebtn = Button(text = "Search by price", command = searchbyprice)
searchpricebtn.place(x = 1020, y = 410  , width = 155, height = 25)
soldpiece = Entry(text="")
soldpiece.place(x = 1020, y = 450, width = 50, height = 25)
soldbtn = Button(text = "Sold", command = sold)
soldbtn.place(x = 1075, y = 450, width = 100, height = 25)


window.mainloop()
db.close()