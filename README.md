# hbnb
## Description:
This is a clone of the AirBnB web application

## Command Interpreter
This is an interpreter designed to access the basic features of the project for the purpose of testing using predefined commands

### How to start the console
In the projects root directory/folder execute the console.py file

### How to use the console
####Commands Description
**help**: Returns a list documented command and to get more info about any of those command.
_Usage: help command or help_
> Example: (hbnb) help quit or (hbnb) help

**quit**: It exit the console, you can alsp use ctrl + D to exit
_Usage: quit_
> Example: (hbnb) quit

**create**: creates an instance of a class if the class exists within the project.
_Usage: create ClassName_
> Example: (hbnb) create BaseModel

**show**: Prints the string representation of an instance based on the class name and id.
_Usage: show ClassName id_
> Example: (hbnb) show BaseModel 1234-1234-1234

**destroy**: Deletes an instance based on the class name and id.
_Usage: destroy ClassName id_
> Example: (hbnb) destroy BaeeModel 1234-1234-1234

**all**: Prints all string representation of all instances based or not on the class name.
_Usage: all ClassName or all_
> Example: (hbnb) all BaseModel or (hbnb) all

**update**: Updates an instance based on the class name and id by adding or updating attribute.
_Usage: update ClassName id attributeName \"attribute value\"_
> Example: (hbnb) update BaseModel 1234-1234-1234 email \"ezekiel@mail.com\"

**ClassName.all()**: Retrieves all instance of a class.
> Example: (hbnb) BaseModel.all()

**ClassName.count()**: Retrieves the number of instances of a class.
> Example: (hbnb) BaseModel.count()

####Commands to be added soon
**ClassName.show()**: Retrieves an instance based on its id.
_Usage: ClassName.show(id)_
> Example: BaseModel.show(1234-1234-1234)

**ClassName.destroy()**: Deletes an instance based on its id.
_Usage: ClassName.destroy(id)_
> Example: BaseModel.destroy(1234-1234-1234)

**ClassName.update()**: Updates an instance based on its id.
_Usage: ClassName.update(id, attributeName, attributeValue) or ClassName.update(id, dictionaryOfAttribues)_
> Example: BaseModel.update(1234-1234-1234, name, \"Ezekiel\") or BaseModel.update(1234-1234-1234, \*\*{\"name\": \"Ezekiel\"})
