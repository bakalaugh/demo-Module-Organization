'''
'__init__.py' file will be called first while explicitly doing 'import modules'
in the `main.py`. and the '__init__.py' file itself is exactly a module, which 
represents the package 'modules'.
'''

# Alternative 1:
# rename the module while importing package
from . import m1 as m
from . import m2 as mm

# Alternative 2:
# import the module from package
from . import m1
from . import m2

# Alternative 3:
# import the function from package
from .m1 import func_1
from .m2 import func_2


# select the imported functions/classes
# __all__ = []