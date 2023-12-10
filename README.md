# hbnb
## Description:
This is a clone of the AirBnB web application

## Command Interpreter
This is an interpreter designed to access the basic features of the project for the purpose of testing using predefined commands

### How to start the console
In the projects root directory/folder execute the console.py file

### How to use the console
**Commands	Description**
help	:	Returns a list documented command and to get more info about any
		of those command.
		Usage: help <command> or help
		Example: (hbnb) help quit or (hbnb) help

quit	:	It exit the console, you can alsp use ctrl + D to exit
		Usage: quit
		Example: (hbnb) quit

create	:	creates an instance of a class if the class exists within the
		project.
		Usage: create <ClassName>
		Example: (hbnb) create BaseModel

show	:	Prints the string representation of an instance based on the
		class name and id.
		Usage: show <ClassName> <id>
		Example: (hbnb) show BaseModel 1234-1234-1234

destroy	:	Deletes an instance based on the class name and id.
		Usage: destroy <ClassName> <id>
		Example: (hbnb) destroy BaeeModel 1234-1234-1234

all	:	Prints all string representation of all instances based or not
		on the class name.
		Usage: all <ClassName> or all
		Example: (hbnb) all BaseModel or (hbnb) all

update	:	Updates an instance based on the class name and id by adding
		or updating attribute.
		Usage: update <class name> <id> <attribute name> "<attribute value>"
		Example: (hbnb) update BaseModel 1234-1234-1234 email "Ezekiel@mail.com"

ClassName.all()	Retrieves all instance of a class.
		Example: (hbnb) BaseModel.all()

ClassName.count(): Retrieves the number of instances of a class
		   Example: (hbnb) BaseModel.count()
