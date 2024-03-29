print ('Organizations module is imported')


import csv
from education.users import *

class School: 
    def __init__(self, name=None, adress=None, phone=None, email = None, num_stud=None, num_teachers=None):
        self.name = name
        self.adress = adress
        self.phone = phone
        self.email = email
        self.num_stud = num_stud
        self.num_teachers = num_teachers
        self.list_stud = []
        self.list_teachers = []
                
    def set_name(self):
        self.name = name
    
    def set_adress(self):
        self.adress = adress

    def set_phone(self):
        self.phone = phone
    
    def set_email(self):
        self.email = email

    def set_num_stud(self):
        self.num_stud = num_stud
    
    def set_num_teachers(self):
        self.num_teachers = num_teachers
       
    def add_student(self, name=None, familyname=None, age=None, gender=None, nationality=None, school=None, subject=None):
        self.list_stud.append(Student(name=name, familyname=familyname, age=age, gender=gender, nationality=nationality, 
        school=school, subject=subject)) #  Добавляем нового студента в список студентов
        self.num_stud += 1 #  Обновляем количество студентов в школе
        
    def add_teacher(self, name=None, familyname=None, age=None, gender=None, nationality=None, school=None, subject=None):
        self.list_teachers.append(Teacher(name=name, familyname=familyname, age=age, gender=gender, nationality=nationality,
        school=school, subject=subject)) #  Добавляем нового учителя в список учителей
        self.num_teachers += 1 #  Обновляем количество учителей в школе
    
    def get_report(self):
        with open(f'{self.name}.csv', 'w', newline='') as f:
            writer = csv.writer(f)
            info = self.get_info()
            for key, value in info.items():
                writer.writerow([f'{key} : {value}'])
                       
            writert = csv.writer(f, quotechar = ' ')
            writert.writerow(['\nStudents'])
            writer = csv.DictWriter(f, fieldnames=self.list_stud[0].get_info().keys(), 
                                     delimiter=',', quoting=csv.QUOTE_MINIMAL)
            writer.writeheader()
            for i in range (0, len(self.list_stud)):
                writer.writerow(self.list_stud[i].get_info())
            
            writert = csv.writer(f, quotechar = ' ')
            writert.writerow(['\nTeachers'])
            writer = csv.DictWriter(f, fieldnames=self.list_teachers[0].get_info().keys(), 
                                     delimiter=',', quoting=csv.QUOTE_MINIMAL)
            writer.writeheader()
            for i in range (0, len(self.list_teachers)):
                writer.writerow(self.list_teachers[i].get_info())

    def get_info(self):
        school_dict = {'Name':self.name,
        'Adress':self.adress,
        'Phone':self.phone,
        'Email':self.email,              
        'Number of student':self.num_stud,
        'Number of teachers':self.num_teachers}
        return school_dict
    
if __name__ == '__main__':
    print(['School'])
    print(['add_student', 'add_teacher', 'get_info', 'get_report', 'set_adress', 
           'set_email', 'set_name', 'set_num_stud', 'set_num_teachers', 'set_phone'])
    