from record import Record
import csv
import re

def add_record():
    """Takes title, date and notes from the user and creates
       an instance of Record with them"""
    
    title = input("Title: ")
    done = False
    while not done:
        try:
            time_spent = int(input("Time spent in minutes: "))
        except ValueError:
            print("That is not a number.")
        else:
            done = True
            
    notes = input("Notes(optional): ")

    Record(title, time_spent, notes)
    
    
def initialize_header(file):
    """Checks to see if the header has already been written.
       If not, writeheader() is called"""
    a = 0
    with open(file, 'r', newline = '') as o:
        reader = csv.DictReader(o)
        records = list(reader)
        if records == []:
            a=1
            o.close()

    if a == 1:
        with open(file, 'a') as o:
            fieldnames = ['title', 'time_spent', 'date', 'notes']
            writer = csv.DictWriter(o, fieldnames = fieldnames)
            writer.writeheader()
            o.close()
                
            
def search_by_exact_search(string):
    """Searches through all the records until one with the
       specified title is found"""
    
    found = False
    matches = []
    num = 0
    with open('logs.csv', newline = '') as logs:
        reader = csv.DictReader(logs)
        records = list(reader)
        if len(records) > 1:
            for record in records:
                if string in record['title'] or string in record['notes']:
                    matches.append(record)
                    num += 1
                    found = True
            logs.close()

        if not found:
            print("A record with that title does not exist.")
        else:
            print("{} records contain that string".format(num))
            display_records(matches, 0)

        logs.close()


def search_by_time_spent(time):
    """Searches through all records and finds all with the specified
       time_spent value"""

    found = False
    matches = []
    num = 0
    with open('logs.csv', newline = '') as logs:
        reader = csv.DictReader(logs)
        records = list(reader)
        if len(records) > 1:
            for record in records:
                if time == int(record['time_spent']):
                    matches.append(record)
                    num += 1
                    found = True
            logs.close()

        if not found:
            print("A record with that much time spent does not exist.")
        else:
            print("{} records have that much time spent".format(num))
            display_records(matches, 0)


def search_by_regex(regex):
    """matches the title and notes of each record against the
       provided regular expression"""
    
    found = False
    matches = []
    num = 0
    with open('logs.csv', newline = '') as logs:
        reader = csv.DictReader(logs)
        records = list(reader)
        if len(records) > 1:
            for record in records:
                if re.match(regex, record['title']) is not None:
                    matches.append(record)
                    num += 1
                    found = True
                elif re.match(regex, record['notes']) is not None:
                    matches.append(record)
                    num += 1
                    found = True

        logs.close()
    if not found:
        print("No record's notes or title match that regex.")
    else:
        print("{} records have been matched against that regex.".format(num))
        display_records(matches, 0)


def search_by_date(date, rang=False, dates=None):
    """Allows for a record to be searched for using either a
       date or a range of dates"""
    
    found = False
    matches = []
    final = []
    num = 0
    if rang == False:
        with open('logs.csv', newline = '') as logs:
            reader = csv.DictReader(logs)
            records = list(reader)
            if len(records) > 1:
                for record in records:
                    if record['date'] == date:
                        matches.append(record)
                        num += 1
                        found = True
            logs.close()

        if not found:
            print("No record was found with the date {}".format(date))
        else:
            print("{} records were found with that date".format(num))
            display_records(matches, 0)

    else:
        with open('logs.csv', newline = '') as logs:
            reader = csv.DictReader(logs)
            records = list(reader)
            logs.close()
            if len(records) > 1:
                for record in records:
                    date = record['date']
                    print(date[6:])
                    if int(date[6:]) > int(dates[0][6:]):
                        matches.append(record)
                    elif int(date[6:]) == int(dates[0][6:]):
                        if int(date[3:5]) > int(dates[0][3:5]):
                            matches.append(record)
                        elif int(date[3:5]) == int(dates[0][3:5]):
                            if int(date[0:2]) > int(dates[0][0:2]):
                            
                                matches.append(record)

                for record in matches:
                    date = record['date']
                    if int(date[6:]) < int(dates[1][6:]):
                        final.append(record)
                        num += 1
                        found = True
                    elif int(date[6:]) == int(dates[1][6:]):
                        if int(date[3:5]) < int(dates[1][3:5]):
                            final.append(record)
                            num += 1
                            found = True
                        elif int(date[3:5]) ==int(dates[1][3:5]):
                            if int(date[0:2]) < int(dates[1][0:2]):
                                final.append(record)
                                num += 1
                                found = True
        if not found:
            print("No records were found within the specified range of dates.".format(date))
        else:
            print("{} records were found inside that range of dates.".format(num))
            display_records(final, 0)
                    
                    
        

def display_records(records, index):
    """Displays a record previously found in a search and gives options
       on what to do with it"""
    
    record = records[index]
    print("\n\nRecord number {}\n".format(index + 1))
    
    print('{}     {} minutes spent'.format(record['date'], record['time_spent']))
    print('Title: {}'.format(record['title']))
    print('Notes: {}\n'.format(record['notes']))
    choice = None
    continu = True

    while continu:
        try:
            choice = int(input('1. Next record\n2. Previous record\n3. Edit this record\n4. Delete this record\n5. Back\n\n'))
        except ValueError:
            print("That is not a valid choice; enter the number of your desired option")
        if choice == 1:
            if records[-1] == record:
                print('This is the last record, please choose a different option')
            else:
                display_records(records, index + 1)   
        elif choice == 2:
            if records[0] == record:
                print('This is the first record, please choose a different option')
            else:
                display_records(records, index - 1)
        elif choice == 3:
            edit_record(index, record)
        elif choice == 4:
            delete_record(record)
            continu = False
        elif choice == 5:
            continu = False
        elif choice > 5:
            print("That is not a valid choice; enter the number of your desired option")


def edit_record(index, record):
    """Allows user to edit either title, date, time_spent or notes
       of a record"""
    
    choice = int(input("1. Edit the title\n2. Edit the date\n3. Edit time spent\n4. Edit notes\n5. Back"))
    if choice == 1:
        edit_str = 'title'
        edit = input("New title: ")
        print("Title has been changed to {}.".format(edit))
    elif choice == 2:
        edit_str = 'date'
        done = False
        while not done:
            edit = input("New date (DD/MM/YYYY): ")
            if re.match('\d\d/\d\d/\d\d\d\d', edit) is not None:
                print("Date has been changed to {}".format(edit))
                done = True
            else:
                print("The date must be in the format DD/MM/YYYY.")
    elif choice == 3:
        edit_str = 'time_spent'
        done = False
        while not done:
            try:
                edit = int(input("New time spent: "))
            except:
                print("That is not a number.")
            else:
                done = True
    elif choice == 4:
        edit_str = 'notes'
        edit = input("Enter new notes: ")
        print("Notes have been updated")

    record_copy = record
    record_copy[edit_str] = edit

    with open('logs.csv', 'a') as logs:
        fieldnames = ['title', 'time_spent', 'date', 'notes']
        writer = csv.DictWriter(logs, fieldnames = fieldnames)
        writer.writerow({
            'title': record_copy['title'],
            'time_spent': record_copy['time_spent'],
            'date': record_copy['date'],
            'notes': record_copy['notes']
            })
        logs.close()

    with open('logs.csv', newline='') as logs:
        reader = csv.DictReader(logs)
        records = list(reader)

    with open('transfer_file.csv', 'w') as tran:
        tran.close()

    with open('transfer_file.csv', 'a') as tran:
        initialize_header('transfer_file.csv')
        fieldnames = ['title', 'time_spent', 'date', 'notes']
        tran_writer = csv.DictWriter(tran, fieldnames = fieldnames)
        for a in records:
            if a['title'] != record['title']:
                if a['date'] != record['date']:
                    if a['notes'] != record['notes']:
                        tran_writer.writerow({
                            'title': a['title'],
                            'time_spent': a['time_spent'],
                            'date': a['date'],
                            'notes': a['notes']
                            })
        logs.close()
        tran.close()

    with open('transfer_file.csv', newline='') as tran:
        final_reader = csv.DictReader(tran)
        final = list(final_reader)

    

    with open('logs.csv', 'w') as logs:
        logs.close()

    with open('logs.csv', 'a') as logs:
        initialize_header('logs.csv')
        fieldnames = ['title', 'time_spent', 'date', 'notes']
        writer = csv.DictWriter(logs, fieldnames = fieldnames)

        for rec in final:
            writer.writerow({
                'title': rec['title'],
                'time_spent': rec['time_spent'],
                'date': rec['date'],
                'notes': rec['notes']
                })

        tran.close()
        logs.close()


def delete_record(record):
    """deletes a record from logs.csv by copying all records apart from the
       one that is going to be deleted to transfer_file.csv and by then
       overwriting logs.csv with the contents of transferfile.csv"""
    final = []
    with open('logs.csv', 'r') as logs:
        reader = csv.DictReader(logs)
        records = list(reader)
        for log in records:
            if log['time_spent'] != record['time_spent']:
                if log['title'] != record['title']:
                    final.append(log)
                elif log['date'] != record['date']:
                    final.append(log)
                elif log['notes'] != record['notes']:
                    final.append(log)
                    
        logs.close()

    with open('transfer_file.csv', 'w') as tran:
        tran.close()

    with open('transfer_file.csv', 'a') as tran:
        initialize_header('transfer_file.csv')
        fieldnames = ['title', 'time_spent', 'date', 'notes']
        writer = csv.DictWriter(tran, fieldnames = fieldnames)

        for rec in final:
            writer.writerow({
                'title': rec['title'],
                'time_spent': rec['time_spent'],
                'date': rec['date'],
                'notes': rec['notes']
                })
        tran.close()

    with open('logs.csv', 'w') as logs:
        logs.close()

    with open('logs.csv', 'a') as logs:
        initialize_header('logs.csv')
        fieldnames = ['title', 'time_spent', 'date', 'notes']
        writer = csv.DictWriter(logs, fieldnames = fieldnames)

        for rec in final:
            writer.writerow({
                'title': rec['title'],
                'time_spent': rec['time_spent'],
                'date': rec['date'],
                'notes': rec['notes']
                })
        logs.close()


