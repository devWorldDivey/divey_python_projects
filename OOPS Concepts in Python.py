#!/usr/bin/env python
# coding: utf-8

# # Object

# In[1]:


lst = [1,2,3]


# In[2]:


lst.count(2)


# In[4]:


print(type(1))
print(type([]))
print(type(()))
print(type({}))


# # Class

# In[5]:


class Sample:
    pass
x = Sample()
print(type(x))


# In[6]:


class Dog:
    def __init__(self,breed):
        self.breed = breed
sam = Dog(breed="Labra")
frank = Dog(breed="Huskie")


# In[7]:


sam.breed


# In[8]:


frank.breed


# In[9]:


class Dog:
    species = "mammal"
    def __init__(self,breed,name):
        self.breed = breed
        self.name = name


# In[10]:


sam = Dog("Lab","Sam")


# In[11]:


sam.name


# In[12]:


sam.species


# # Methods

# In[13]:


class Circle:
    pi = 3.14
    def __init__(self,radius=1):
        self.radius = radius
        self.area = radius * radius * Circle.pi
    def setRadius(self, new_radius):
        self.radius = new_radius
        self.area = new_radius * new_radius * self.pi
    def getCircumference(self):
        return self.radius * self.pi * 2
c = Circle()
print("Radius is:",c.radius)
print("Area is:",c.area)
print("Circumference is:",c.getCircumference())


# In[14]:


c.setRadius(2)
print("Radius is:",c.radius)
print("Area is:",c.area)
print("Circumference is:",c.getCircumference())


# # Inheritance

# In[27]:


class Animal:
    def whoAmI(self):
        print("Animal")
    def eat(self):
        print("Eating")
class Dog(Animal):
    def whoAmI(self):
        print("Dog")
d = Dog()


# In[28]:


d.whoAmI()


# In[29]:


d.eat()


# # Polymorphism

# In[31]:


class Dog:
    def __init__(self,name):
        self.name = name
    def speak(self):
        return self.name + "says Woof!"
class Cat:
    def __init__(self,name):
        self.name = name
    def speak(self):
        return self.name + "says Meow"
niko = Dog("Niko ")
felix = Cat("Felix ")
print(niko.speak())
print(felix.speak())


# In[ ]:




