from categoryItem import CategoryItem

class CategoryList:

    def __init__(self, title, priority, total, available, status, items):
        self.title = title
        self.priority = priority
        self.total = total
        self.available = available
        self.status = status
        self.items = items if items is not None else []

    def __str__(self):
        items_str = "\n   ".join(str(i) for i in self.items)
        return (f"Title: {self.title}, Priority: {self.priority}\n "
                f"Total: {self.total}, Available: {self.available}, Status: {self.status}\n"
                f"Items:\n   {items_str if items_str else 'No items yet'}")
    
    def addItem(self, subject, amount, date):
        new_item = CategoryItem(subject, amount, date)
        self.items.append(new_item)
        self.available += amount
        return new_item
    
    def removeItem(self, old_item):
        self.items.remove(old_item)
        self.available -= old_item.amount
    
    # def customSum(self):
    #     return sum(item.amount for item in self.items)
    
    def to_dict(self):
        return {
            "title": self.title,
            "priority": self.priority,
            "total": self.total,
            "available": self.available,
            "status": self.status,
            "items": [item.to_dict() for item in self.items]
        }
    
    @staticmethod
    def from_dict(data):
        items = [CategoryItem.from_dict(i) for i in data["items"]]
        return CategoryList(
            data["title"],
            data["priority"],
            data["total"],
            data["available"],
            data["status"],
            items
        )