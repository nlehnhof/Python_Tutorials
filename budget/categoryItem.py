import json
class CategoryItem:
    
    def __init__(self, subject, amount, date):
        self.subject = subject
        self.amount = amount
        self.date = date
    
    def __str__(self):
        return f"Subject: {self.subject}, Amount: {self.amount}, Date: {self.date}"
    
    def to_dict(self):
        return {
            "subject": self.subject,
            "amount": self.amount,
            "date": self.date
        }
    
    @staticmethod
    def from_dict(data):
        return CategoryItem(data["subject"], data["amount"], data["date"])