# OOP
This is a project that models a real world example using Object Oriented Programming in Python.

# About
The program uses an example of a company Kariobangi Fried Chicken and Potatoes(KFCP) with its branches. The super class models the main company whereas subclasses model branches that inherit a lot from the main company but are free to create procedures of their own.  

The superclass holds properties e.g name,logo,storage and funds that can be used across all branches, just like in the real world. It also defines abstract methods that are implemented in the branches. In the real world, a company cannot serve chips to you, but a branch can. The superclass therefore defines the method and relies on the sub classes to implement it. A feature core to acheiving polymorphism in OOP.  

There are also common methods that are best implemented by the superclass. For instance in the real world only the main company headquarters would control how money is spent and not individual branches.  

The program also demonstrates data hiding. In the real world you would not expect KFCP to always tell you about their financial situation unless compelled by law. The superclass hides data using private member variables e.g __funds,__storage to acheive this.

# Python version
Python version 2.6.6
