from datetime import date, timedelta

class Book: 
    status_dict = {0: "available", 1: "on_lend", 2: "overdue", 3: "discontinued"}


    def __init__(self, title, author): 
        self.title=title 
        self.author=author 
        self.status = 0
        self.due_date = date.today()

    def __dict__(self):
        return {
            "title": self.title,
            "author": self.author,
            "status": self.status_dict[self.status],
            "due_date": self.due_date.isoformat()
        }
    
    def lend_out(self, lend_days: int = 14):
        self.status = 1 #On lend
        self.due_date = date.today() + timedelta(days = lend_days)
    
    def restock(self):
        self.status = 0 #in stock
    
    def discontinue(self):
        self.status = 3 #discontinued

    def check_overdue(self): #Call this every day for state update. 
        if self.status == 1 and date.today() > self.due_date:
            self.status = 2 #overdue
        
    