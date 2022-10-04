# Alternative 1:
# rename the module while importing package
import modules

modules.m.func_1
modules.mm.func_2

# Alternative 2:
# import the module from package
import modules

modules.m1.func_1
modules.m2.func_2

# Alternative 3:
# import the function from package
import modules

modules.func_1
modules.func_2