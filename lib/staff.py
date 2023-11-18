class Staff:
    def __init__(self, staff_id, name, position):
        self.staff_id = staff_id
        self.name = name
        self.position = position

    def __str__(self):
        return f"{self.name}({self.position})"