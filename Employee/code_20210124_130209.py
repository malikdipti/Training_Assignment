class Employee:
    def __init__(self, id, name):
        self.idno = id
        self.name = name


class Developer(Employee):

    def assign_project(self, project_name):
        self.project_name = project_name

    def display_details(self):
        print("IDNO:", self.idno)
        print("Name:", self.name)
        print("Project Name:", self.project_name)


class TempEmployee(Developer):

    def assign_salary(self, total_salary):
        self.total_salary = total_salary

    def display_details(self):
        super().display_details()
        print("Total salary:", self.total_salary)


class PerEmployee(Developer):

    def total_salary(self, basic_sal, hra, da):
        self.basic = basic_sal
        self.hra = hra
        self.da = da

    def display_details(self):
        super().display_details()
        print("total Salary", self.basic+self.hra+self.da)


te = TempEmployee(101, "diptiranjan")
te.assign_salary(185000)
te.assign_project("CISCO")
te.display_details()
print("-----------------------")
pe = PerEmployee(102, "raaj")
pe.total_salary(185000, 20000, 5000)
pe.assign_project("INTEL")
pe.display_details()
