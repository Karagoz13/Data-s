print ('Users module is imported')


class Human: 
    def __init__(self, name=None, familyname=None, age=None, gender=None, nationality=None):
        self.name = name
        self.familyname = familyname
        self.age = age
        self.gender = gender
        self.nationality = nationality
                
    def set_name(self):
        self.name = name
    
    def set_family(self):
        self.familyname = familyname
    
    def set_age(self):
        self.age = age

    def set_gender(self):
        self.gender = gender
    
    def set_nationality(self):
        self.nationality = nationality
    
    def get_info(self):
        human_dict = {'name':self.name,
        'familyname':self.familyname,
        'age': self.age,
        'gender':self.gender,
        'nationality':self.nationality}
        return human_dict
    

class Student(Human):
    def __init__(self, name=None, familyname=None, age=None, gender=None, nationality=None, school=None, subject=None):
        super().__init__(name, familyname, age, gender, nationality)
        self.school = school
        self.subject = subject
    
    def set_school(self):
        self.school = school
    
    def add_subject(self, subjec):
        self.subject.append(subjec) # Добавляем новый предмет в список предметов
        self.subject = list(set(self.subject)) # Проверяем уникальность предметов в списке
        
    def get_info(self):
        info_dict = super().get_info()
        info_dict['school'] = self.school
        info_dict['subject'] = self.subject
        return info_dict
    
class Teacher(Student):
    def __init__(self, name=None, familyname=None, age=None, gender=None, nationality=None, school=None, subject=None):
        super().__init__(name, familyname, age, gender, nationality, school, subject)

if __name__ == '__main__':
    print(['Human', 'Student', 'Teacher'])
    print(['get_info', 'set_age', 'set_family', 'set_gender', 'set_name', 'set_nationality'])
    print(['add_subject', 'get_info', 'set_age', 'set_family', 'set_gender', 'set_name', 'set_nationality', 'set_school'])
    print(['printd_subject', 'get_info', 'set_age', 'set_family', 'set_gender', 'set_name', 'set_nationality', 'set_school'])
