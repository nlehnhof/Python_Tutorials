from categoryItem import CategoryItem

class CategoryList:

    def __init__(self, title, priority, total, available, status, items):
        self.title = title
        self.priority = priority
        self.total = total
        self.available = available
        self.status = status
        self.items = items

    def __str__(self):
        return f"Title: {self.title}, Priority: {self.priority}, Total: {self.total}, Available: {self.available}, Status: {self.status}, Items: {self.items}"
    
    def addItem(self, subject, amount, date):
        new_item = CategoryItem(subject, amount, date)
        self.items.append(new_item)
        self.available -= amount
        return new_item
    
    def customSum(self):
        return sum(item.amount for item in self.items)
    
