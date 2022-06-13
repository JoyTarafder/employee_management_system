class person:
    def __init__(self, person_name, date_of_birth, ht):
        self.name = person_name
        self.date_of_birth = date_of_birth
        self.hight = ht

    # def get_name(self):
    #     return self.name

    def set_name(self):
        self.

    def get_summary(self):
        return f"Name : {self.name}, DOB : {self.date_of_birth}, Hight : {self.hight}"



a_person = person("Joy", 2002, 5.4)
# b_person = person("Tarafder")

print(a_person.get_summary())
# print(b_person.get_name())