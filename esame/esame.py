# class Student:
#     def __init__(self, student_id ,) -> None:
#         self.student_id = student_id
#         self.courses :list[str] = []

#     def enroll(self,course: str):
#         if course not in self.courses:
#             self.courses.append(course)
#         else: 
#             print(f"Lo studente è già iscritto al corso {course}.")
            
#     def get_courses(self):
#         return self.courses
        
# class School:
#     def __init__(self) -> None:
#         self.students : dict[str, Student] = {}
        
#     def create_student(self, student_id : str):
#         if student_id in self.students:
#             print(f"Lo studente con ID {student_id} esiste già")
#         else:
#             new_student = Student(student_id)
#             self.students[student_id] = new_student
            
#     def enroll_student(self, student_id : str, course : str):
#         if student_id in self.students:
#             self.students[student_id].enroll(course)
#         else:
#             return "Studente non trovato"
            
#     def get_student_courses(self,student_id : str):
#         if student_id in self.students:
#             return self.students[student_id].get_courses()
#         else:
#             return "Studente non trovato"
            
#     def get_student_list(self):
#         list_id = []
        
#         for i in self.students.keys():
#             list_id.append(i)
#         return list_id
        
#     def search_by_course(self,course : str):
#         list_id = []
#         i = 0
#         for j in self.students:
#             if course in self.students[j].courses:
#                 list_id.append(self.students[j].student_id)
#             i+=1
#         if len(list_id) !=0:
#             return list_id
            
#         return f"Nessuno studente è iscritto al corso {course}."


print(302 * 10) /100
