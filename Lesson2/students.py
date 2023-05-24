class Student:
    def __init__(self, name, age, group, country, sex, city):
        self.Name = name
        self.Age = age
        self.Group = group
        self.Country = country
        self.Sex = sex
        self.City = city

    def ShowInfo(self):
        print(f"Name: {self.Name}\n"
              f"Age: {self.Age}\n"
              f"Group: {self.Group}\n"
              f"Country: {self.Country}\n"
              f"Sex: {self.Sex}\n"
              f"City: {self.City}\n")
