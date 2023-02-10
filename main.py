## -----------------------------------------------
##	Program 1: Analyzing CTA2 L data in Python
##		program takes user inputs to query SQLite Database

##	Course: CS341, Fall 2023. MWF 12pm lec

##	System: Ubuntu using terminal,
##		Python 3.10.6
##		sqlite3 3.37.2

##	Author: Zain Ali
## -----------------------------------------------

import sqlite3

# TODO: import matplotlib
import matplotlib

def riderShip(ascending=True, orderByName=True, limit=False):
	sql = "SELECT \n" \
		  "        sum(Num_Riders) as totalNumRiders\n" \
		  "from Ridership r\n" \
		  ";"

	# total = dbCursor.execute(sql).arraysize
	total = float(dbCursor.execute(sql).fetchone()[0])

	sql = "SELECT \n" \
		  "        s.Station_Name, \n" \
		  "        sum(Num_Riders) as total\n" \
		  "from Ridership r\n" \
		  "inner join Stations s on s.Station_ID=r.Station_ID\n" \
		  "group by s.Station_ID\n" \
		  "order by "

	sql += "Station_Name " if orderByName else "total "
	sql += "asc\n" if ascending else "desc\n"

	sql += "limit 10;" if limit else ";"

	output = dbCursor.execute(sql)

	for row in output:
		print(row[0], ":", f"{row[1]:,}", f"({100.0 * row[1] / total:.2f}%)")

def opt1():
	sql = "SELECT\n" \
		  "Station_ID as ID,\n" \
		  "Station_Name as name\n" \
		  "from Stations\n" \
		  "group by name\n" \
		  "having name like ?\n" \
		  "order by name asc;\n"
	inp = input("\nEnter partial station name (wildcards _ and %): ")

	dbCursor.execute(sql, [inp])

	for row in dbCursor:
		print(row[0], ":", row[1])

	print("\n")

def opt5():
	'''Please enter a command (1-9, x to exit): 5
	Enter a line color (e.g. Red or Yellow): yellow
	Dempster-Skokie (Arrival) : direction = N (accessible? yes)
	Dempster-Skokie (Howard-bound) : direction = S (accessible? yes)
	Howard (Linden & Skokie-bound) : direction = N (accessible? yes)
	Howard (Terminal arrival) : direction = S (accessible? yes)
	Oakton-Skokie (Dempster-Skokie-bound) : direction = N (accessible? yes)
	Oakton-Skokie (Howard-bound) : direction = S (accessible? yes)
	Please enter a command (1-9, x to exit): 5
	Enter a line color (e.g. Red or Yellow): Magenta
	**No such line...'''

	color = input("Enter a line color (e.g. Red or Yellow): ")

	sql = "SELECT \n" \
		  "        s.Stop_Name as name, \n" \
		  "        s.Direction, \n" \
		  "        s.ADA \n" \
		  "from Stops s \n" \
		  "inner join StopDetails sd on s.Stop_ID=sd.Stop_ID\n" \
		  "inner join Lines l on l.Line_ID=sd.Line_ID\n" \
		  "group by name;\n" \
		  "having name like ?\n" \
		  "order by name asc;\n"

	output = dbCursor.execute(sql, [color])

	for row in output:
		#print(row[0], ":", f"{row[1]:,}", f"({100.0 * row[1] / total:.2f}%)")
		print(row)

def opt6():
	pass


def opt7():
	pass


def opt8():
	pass


def opt9():
	pass


def handleMenu():
	print("Please enter a command (1-9, x to exit): ", end="")
	menu_option = input()

	if menu_option == "x":
		quit()

	elif menu_option == "1":
		opt1()

	elif menu_option == "2":
		riderShip(ascending=True, orderByName=True, limit=False)

	elif menu_option == "3":
		print("** top-10 stations **")
		riderShip(ascending=False, orderByName=False, limit=True)

	elif menu_option == "4":
		print("** least-10 stations **")
		riderShip(ascending=True, orderByName=False, limit=True)

	elif menu_option == "5":
		opt5()

	elif menu_option == "6":
		opt6()

	elif menu_option == "7":
		opt7()

	elif menu_option == "8":
		opt8()

	elif menu_option == "9":
		opt9()

	else:
		print("**Error, unknown command, try again...\n")


print("** Welcome to CTA L analysis app **\n\n" +
	  "General stats:\n" +
	  "  # of stations: 147\n" +
	  "  # of stops: 302\n" +
	  "  # of ride entries: 1,070,894\n" +
	  "  date range: 2001-01-01 - 2021-07-31\n" +
	  "  Total ridership: 3,377,404,512\n" +
	  "  Weekday ridership: 2,778,644,946 (82.27%)\n" +
	  "  Saturday ridership: 330,165,977 (9.78%)\n" +
	  "  Sunday/holiday ridership: 268,593,589 (7.95%)\n"
	  )

dbConn = sqlite3.connect("CTA2_L_daily_ridership.db")
dbCursor = dbConn.cursor()

while True:
	handleMenu()

