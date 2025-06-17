

# class Base:
#     pass


# class Zebra(Base):
#     a = []

#     @classmethod
#     def update_a(cls, value):
#         cls.a = value
#         print('cs', cls.a)

#     def test2(self):
#         self.a = [1, 2]
#         print(self.a)


# class Login(Base):
#     def test3(self):
#         self.a = [11111111111, 2222222222]
#         print(self.a)


# class Service(Login):
#     a = ['A', '2222222222']

#     def test4(self):
#         self.a = ['A', '2222222222']
#         print(self.a)


# def wrapper(skip):
#     def task_wrapper(func):
#         def inner(*args, **kwargs):
#             print('in wrapper', skip)
#             func(*args, **kwargs)
#         return inner
#     return task_wrapper


# class Taskset(Zebra):
#     a = False

#     def testss4(self):
#         self.update_a(True)
#         print('update', self.a)

#     @wrapper(Zebra.a)
#     def test5(self):
#         # self.a = ['11111111111', '2222222222']
#         print(self.a)


# t = Taskset()
# # t.a
# # t.test()
# # t.test2()
# # t.test3()
# t.testss4()
# t.test5()

class Base:
    pass


class Zebra(Base):
    a = []  # Class variable

    @classmethod
    def update_a(cls, value):
        cls.a = value  # Update the class variable
        print('Updated class variable a:', cls.a)

    def test2(self):
        # Creating an instance variable 'self.a'
        self.a = [1, 2]
        print('Instance variable a:', self.a)


def wrapper():
    def task_wrapper(func):
        def inner(*args, **kwargs):
            print('In wrapper, skip:', Zebra.a)
            func(*args, **kwargs)
        return inner
    return task_wrapper


class Taskset(Zebra):
    a = False  # Taskset class has its own variable a

    def testss4(self):
        # Calling the class method update_a to modify the class variable 'a'
        Zebra.a = 1000
        # Will print the instance variable 'a'
        print('In Taskset testss4, a (class variable):', self.a)

    @wrapper()  # Using Zebra's 'a' as skip value
    def test5(self):
        # Will print instance 'self.a' if set, otherwise class variable 'Zebra.a'
        print('In Taskset test5, a (class or instance variable):', self.a)


# Example usage:
taskset = Taskset()
taskset.test5()
taskset.testss4()  # Should update class variable a and print it
taskset.test5()    # Should print Zebra.a because wrapper uses Zebra.a
taskset.test2()    # Should print the instance variable a
