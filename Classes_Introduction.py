#Classes Intriduction:

As you are aware, In all the programs we wrote till now,
we have designed our program around passing the single, multiple line statements, control statemtns,
functions  to view the output (i.e. All these are different blocks of statements which manipulate data and
give us the desired output)

All that we are learnt so far is called 'Procedure-oriented way of Programming'

Now there is onemore beautiful way of organizing your program which is to combine data
and functionality and wrap it inside something called an 'object' . object oriented programming is
specially useful when large projects need to be designed. Just a theory. Dont worry even if you dont get it.

'classes' and 'objects' are the two main aspects of object oriented programming.
A class created a new type where the objects are instance of a class.

An analogy is that you can have variables of type int which translates to saying that
variables that store integers are variables which are instances (objects) of the int class.

int a = 20
int b = 35

Here a & b are objects(instances) of int class. Hope this is clear. You will get it easily once explain it.

Lets create a simple classs as follows (save as oop_simplestclass.py).

class Person:
    pass  # An empty block

p = Person()
print(p)


Output:
$ python oop_simplestclass.py
<__main__.Person object at 0x02096C70>

How It Works

We create a new class using the class statement and the name of the class (Person). This is followed by an indented block of statements which form the body of the class.
In this case, we have an empty block which is indicated using the pass statement. I think You are aware of pass as we have used in the past also.

Next, we create an object/instance(p) of this class using the name of the class followed by a pair of parentheses. (We will learn more about instantiation in the next section).
For our verification, we confirm the type of the variable by simply printing it. It tells us that we have an instance of the Person class in the __main__ module. This address is like stored in the Memory somewhere.
Notice that the address of the computer memory where your object is stored is also printed. The address will have a different value on your computer since Python can store the object wherever it finds space.

Methods

We have already discussed that classes/objects can have methods just like functions except that we have an extra self variable(We will discuss about the self as we progress in the course). We will now see an example (save as oop_method.py).

class Person:
    def say_hi(self):
        print('Hello, how are you?')

p = Person()
p.say_hi()

# The previous 2 lines can also be written as
# Person().say_hi()

Output:
$ python oop_method.py
Hello, how are you?


How It Works+

Here we see the self in action. Notice that the say_hi method takes no parameters but still has the self in the function definition.



The __init__ method: There are many method names which have special significance in Python classes. We will see the significance of the __init__ method now.

The __init__ method is run soon after the  object of a class is instantiated (i.e. created).
The method is useful to do any initialization (i.e. passing initial values to your object) you want to do with your object.
Notice the double underscores both at the beginning and at the end of the name.

Example (save as oop_init.py):

class Person:
     def __init__(self, name):
          self.name = name

    def say_hi(self):
         print('Hello, my name is', self.name)

p = Person('Naren')
p.say_hi()

# The previous 2 lines can also be written as
# Person().say_hi()


Output:
$ python oop_init.py
Hello, my name is Naren


How It Works

Here, we define the __init__ method as taking a parameter name (along with the usual self). Here, we just create a new field also called name. Notice these are two different variables even though they are both called 'name'. There is no problem because the dotted notation self.name means that there is something called "name" that is part of the object called "self" and the other name is a local variable. Since we explicitly indicate which name we are referring to, there is no confusion.
When creating new instance p, of the class Person, we do so by using the class name, followed by the arguments in the parentheses: p = Person('Narendra').
We do not explicitly call the __init__ method. This is the special significance of this method.
Now, we are able to use the self.name field in our methods which is demonstrated in the say_hi method.

Class And Object Variables:

We have already discussed the functionality part of classes and objects (i.e. methods), now let us learn about the data part.
The data part, i.e. fields, are nothing but ordinary variables that are bound to the namespaces of the classes and objects.
This means that these names are valid within the context of these classes and objects only. That's why they are called name spaces.
There are two types of fields - class variables and object variables which are classified depending on whether the class or the object owns the variables respectively.
Class variables are shared - they can be accessed by all instances of that class. There is only one copy of the class variable and when any one object makes a change to a class variable, that change will be seen by all the other instances.
Object variables are owned by each individual object/instance of the class. In this case, each object has its own copy of the field i.e. they are not shared and are not related in any way to the field by the same name in a different instance.
An example will make this easy to understand (save as oop_objvar.py):



#Example Program:
class Company:

    def __init__(self, place, employees, lunchprice, workingdays):
        self.place = place
        self.employees = employees
        self.lunchprice = lunchprice
        self.workingdays = workingdays


Videocon = Company('GreaterNoida', 2000, 25, 22)
Google = Company('San Jose', 5000, 40, 30)
Microsoft = Company('RedMond', 10000, 30, 28)


print(Videocon.place)
print(Google.place)
print(Microsoft.place)

print(Videocon.employees)
print(Google.employees)
print(Microsoft.employees)

print(Videocon.lunchprice)
print(Google.lunchprice)
print(Microsoft.lunchprice)

print(Videocon.workingdays)
print(Google.workingdays)
print(Microsoft.workingdays)


