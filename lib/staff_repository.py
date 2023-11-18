from staff import Staff

class StaffRepository:
    def __init__(self):
        self.staff_list =[]

    def add_staff(self, staff):
        self.staff_list.append(staff)

    def get_staff_by_id(self, staff_id):
        for staff in self.staff_list:
            if staff.staff_id == staff_id:
                return staff
            return None

    def get_all_staff(self):
        return self.staff_list
    
    def remove_staff(self, staff_id):
        staff = self.get_staff_by_id(staff_id)
        if staff:
            self.staff_list.remove(staff)