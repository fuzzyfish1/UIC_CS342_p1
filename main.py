## -----------------------------------------------
##	Program 1: Analyzing CTA2 L data in Python
##		program takes user inputs to query SQLite Database

##	Course: CS341, Fall 2023. MWF 12pm lec

##	System: Ubuntu using terminal,
##		Python 3.10.6
##		sqlite3 3.37.2

##	Author: Zain Ali

##	Side note: I aplolgize for the late Hw1,
##	I tried installing Arch Linux and somehow deleted my bootloader the day of the deadline
##	and I didnt have a livestick available
## -----------------------------------------------

## script start


def handleMenu():
    menuOption = -1

    menuOption = input("Please Enter A command ...")

    print("u selected")
    print(menuOption)

    if (menuOption == "x"):
        quit()

    elif (menuOption == "1"):
        print("menuu opt 1")

    elif (menuOption == "opt 2"):
        print("menuu opt 2")

		3    elif (menuOption == "opt 2"):
        print("menuu opt 2")
		4    elif (menuOption == "opt 2"):
        print("menuu opt 2")
		5    elif (menuOption == "opt 2"):
        print("menuu opt 2")
		6    elif (menuOption == "opt 2"):
        print("menuu opt 2")
		7    elif (menuOption == "opt 2"):
        print("menuu opt 2")
		8    elif (menuOption == "opt 2"):
        print("menuu opt 2")
		9    elif (menuOption == "opt 2"):
        print("menuu opt 2")












    else:
        print("else Fuuuk")



## equivalent of main()


print("** Welcome to CTA L analysis app **")

print("General stats:\n" +
      "  # of stations: 147\n" +
      "  # of stops: 302\n" +
      "  # of ride entries: 1,070,894\n" +
      "  date range: 2001-01-01 - 2021-07-31\n" +
      "  Total ridership: 3,377,404,512\n" +
      "  Weekday ridership: 2,778,644,946 (82.27%)\n" +
      "  Saturday ridership: 330,165,977 (9.78%)\n" +
      "  Sunday/holiday ridership: 268,593,589 (7.95%\n)"
      )

while True:
    handleMenu()
