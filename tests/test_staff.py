from lib.staff import Staff

def test_staff_management():
    staff = Staff(1, "David Bowie", "Manager")
    assert staff.staff_id == 1
    assert staff.name == "David Bowie"
    assert staff.position == "Manager"

def test_staff_str_representation():
    staff = Staff(2, "George Underwood", "Assistant Manager")
    assert str(staff) == "George Underwood(Assistant Manager)"

def test_staff_equality():
    staff1 = Staff(1, "David Bowie", "Manager")
    staff2 = Staff(1, "David Bowie", "Star")
    staff3 = Staff(2, "Geroge Underwood", "Assistant Manager")

    assert staff1 == staff2
    assert staff1 != staff3
    assert staff2 != staff3