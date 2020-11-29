'''
Class vs instance variable
'''


class Boy:
    # gender is a class variable, and so calling it will return
    # the 'male' string in all instances
    gender = 'male'

    # here we are creating the means to initialise objects by passing variables as parameters.
    def __init__(self, name):
        self.name = name


# intialising these objects by passing names

k = Boy('kiesar')
a = Boy('ahsan')

# returns male
print(k.gender)

# returns ahsan
print(a.name)
