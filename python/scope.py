# Built-in: These are reserved names for Python built-in modules.
# Global: These variables are defined at the highest level.
# Enclosed: These variables are defined inside some enclosing functions.
# Local: These variables are defined inside the functions or class and are local to
# them.


#---------------  Global Statement ------------
def func():
    global val
    val = 'Yes'

val = 'Naa'
print(val)
func()
print(val)

# We set the value of “value” as Global. To change its value from inside the function, we
# use the global keyword along with “value” to change its value to local, and then print
# it.