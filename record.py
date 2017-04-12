import datetime
import csv

class Record:
    def __init__(self, title, time_spent, notes=''):
        """Initializes the record with a title, time spent, date
           and notes(optional)"""
        self.title = title
        self.time_spent = time_spent
        self.notes = notes
        
        self.date = datetime.datetime.now().strftime("%d/%m/%Y")

        self.add_to_db()

    def add_to_db(self):
        "Adds the record to the csv file as a new row"""
        with open('logs.csv', 'a') as logs:
            
            fieldnames = ['title', 'time_spent', 'date', 'notes']
            writer = csv.DictWriter(logs, fieldnames = fieldnames)
         
            writer.writerow({
                'title': self.title,
                'time_spent': self.time_spent,
                'date': self.date,
                'notes': self.notes,
                })
            
            logs.close()
