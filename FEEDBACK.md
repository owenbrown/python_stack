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

### The (copy) button in the sample code results in bugs
If a user copy-and-pastes the sample code, sometimes the word "copy" is taken from the copy button, and injected into
 the copied code, in a random spot. This is annoying. 
 
 I don't use the copy button because one time it copied in characters that through bugs. So, I copy-and-paste.
 
 In addition, the copy button is really small to click, and hidden until hovered over.
 
 An improvement would be to make the copy button larger, always visible, and in-line, right, justified with the file 
 name. The text "copy" should not be selectable by the user. 
 
 
 ### [GET requests should not be used to delete resources](http://learn.village88.com/m/19/183/2042)
 I could be mistaken but I think sending a GET request to user/<id>/delete makes the API non-restful.
 
 Instead the user should be sending a DELETE request to user/<id>
 https://restfulapi.net/http-methods/#delete
 
 
 ### debugHelp not imported in [Conference Registration Demo](http://learn.village88.com/m/19/183/2038)
This method, `debugHelp("INDEX METHOD")`, would err out.


### Quiz wouldn't let me re-take
I try to "retake quiz" on the [quiz results page](http://learn.village88.com/m/19/183/2036),
it always grades me using whatever I entered the very first time I took the quiz. 

### Always have written text in addition to the video
For some people (me) have a strong preference for written text rather than video.
Almost all of the material is written, which I really appreciate.

However, [Session Security with Login](http://learn.village88.com/m/19/183/2043) is only in video form.
 
## On the [Django Ninja Gold assignment](http://learn.village88.com/m/19/180/1974), tell wear to put logic files.
Where is the idiomatic place to put logic related to an app? At the route of the app folder?
