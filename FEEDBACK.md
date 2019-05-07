# Feedback
CoderDojo is great, let's make it better
For your convenience, I'll always link to the relevant CoderDojo page.
## [Installation](http://learn.village88.com/m/19/177/1914) doesn't need brew.
It's simpler for new people to simply [download from Python.org](https://www.python.org/downloads/)
## Python3.5 and above [don't require installing virtualenv](http://learn.village88.com/m/19/177/1917)
Instead do `python3 -m venv my_virtual_environment`
## Don't encourage shadowing built-in names
[Assignment: Functions Intermediate I](http://learn.village88.com/m/19/178/1931) uses "min" and "max" as parameter 
names. Shadowing the built in max and min is bad. Instead, used the names "highest" and "lowest'

### Python functions should be snake_case
Pep8 states "Function names should be lowercase, with words separated by underscores as necessary to improve 
readability." ([python.org](https://www.python.org/dev/peps/pep-0008/#function-and-variable-names)) 

However, [Assignment: Functions Intermediate II](http://learn.village88.com/m/19/178/1932) and elsewhere have 
functions using camelCase names.

### [Singly linked lists](http://learn.village88.com/m/19/185/1957) should use idiomatic python
`while (runner != None):` should be replaced with `while runner is not none`