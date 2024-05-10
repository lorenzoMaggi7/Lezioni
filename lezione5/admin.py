"""
9-11. Imported Admin: Start with your work from Exercise 9-8. Store the classes User, Privileges, and Admin in one module. 
Create a separate file, make an Admin instance, and call show_privileges() to show that everything is working correctly.
"""

from esercizilz5 import Admin
ciao2 = Admin("Giovanni","Perrella",28,179,["add user"])

ciao2.privileges.show_privileges()