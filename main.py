from worklog import *
from record import Record
import csv
import re

def main():
    initialize_header('logs.csv')
    dont_quit = True
    while dont_quit:
        action = input("\nEnter number of desired choice\n\n1. Add record\n2. Search\n3. Exit\n\n")
        try:
            int(action)
        except:
            print("\nThat is not a number.")
        else:
            action = int(action)
            if action > 3 or action < 1:
                print("\nThat is not one of the options.")
            else:
                if action == 1:
                    add_record()
                elif action == 2:
                    choice = input("\n1. Search by time spent\n2. Search by exact string\n3. Search by regex\n4. Search by date(s)\n\n")
                    try:
                        int(choice)
                    except:
                        print("\nThat is not a number.")
                    else:
                        choice = int(choice)
                        if choice > 4 or choice < 1:
                            print("\nThat is not one of the options.")
                        else:
                            if choice == 1:
                                time = int(input("\nEnter time spent value: "))
                                try:
                                    int(time)
                                except:
                                    print("\nThat is not a number.")
                                else:
                                    search_by_time_spent(time)
                            elif choice == 2:
                                string = input("\nEnter a string you would like to search for in title and notes: ")
                                search_by_exact_search(string)
                            elif choice == 3:
                                regex = input("\nEnter a regex: ")
                                search_by_regex(regex)
                            elif choice == 4:
                                option = input("\n1. Search by date\n2. Search by range of dates")
                                try:
                                    int(option)
                                except:
                                    print("\nThat is not a number.")
                                else:
                                    option = int(option)
                                    if option < 1 or option > 2:
                                        print("\nThat is not one of the options")
                                    else:
                                        if option == 1:
                                            date = input("\nEnter date (DD/MM/YYYY): ")
                                            search_by_date(date)
                                        elif option == 2:
                                            date1 = input("\nEnter the start date of the range (DD/MM/YYYY): ")
                                            date2 = input("\nEnter the end date of the range (DD/MM/YYYY): ")
                                            search_by_date(0, rang=True, dates=[date1, date2])
                elif action == 3:
                    dont_quit = False
                                            
                                
main()
