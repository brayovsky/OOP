# OOP
This is a repository that demonstrates the sheer power of OOP. Hold on.

The superclass holds properties e.g name,logo,storage and funds that can be used across all 
branches, just like in the real world.
It also defines abstract methods that are implemented in the branches. In the real world, a
company cannot serve chips to you, but a branch can. The superclass therefore defines the 
method and relies on the sub classes to implement it. A feature core to acheiving polymorphism in 
OOP. 
There are also common methods e.g that are best implemented by the superclass. For instance in the real 
world only the main company headquarters would control how money is spent and not individual branches. 
This is demonstrated in KFCP.py.
The program also demonstrates data hiding. In the real world you would not expect KFCP to always tell you 
about their financial situation unless compelled by law. The superclass hides data using private member variables
e.g __funds,__storage to acheive this.
