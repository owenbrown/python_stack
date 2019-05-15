### `Pip search`
Search for PyPI packages whose name or summary contains <query>.

### Other str methods
**string.count(substring)**: returns number of occurrences of substring in string.
**string.isalnum()**: returns boolean depending on whether the string's length is > 0 and all characters are alphanumeric (letters and numbers only). Strings that include spaces and punctuation will return False for this method. Similar methods include .isalpha(), .isdigit(), .islower(), .isupper(), and so on. All return booleans.
**string.endswith(substring)**: returns a boolean based upon whether the last characters of string match substring.

### Data types
Primitives include booleans, numbers and strings. Each example he gave is immutable.
Composites include tuples, lists and dicts.

### All
Override all to restrict what can be imported.
```python
__all__ = ['module', 'module2']
```

[SmallTalk reference on testing](https://web.archive.org/web/20150315073817/http://www.xprogramming.com/testfram.htm)
**Fixture**: a single configuration whose behavior is predictable.

Assert statements for Pytest should always be in the order "expected", "actual"


### Angular Material vs Material Design Lite
Both are easy enough to use. 
- [Angular Material QuickStart](https://material.io/develop/web/docs/getting-started/)
- [Material Design Lite QuickStart](https://getmdl.io/started/)

According to the reasonable simple decision chart on [Jad Joubran's comparison article](
https://scotch.io/bar-talk/angular-material-vs-material-design-lite), replicated below

| Already |         |                      |
| using   | Complex | Decision             |
| angular | UI      |                      | 
| ------- | ------- | -------------------- |
| Yes     | Yes     | Material Angular     |
| Yes     | No      | Depends              |
| No      | Yes     | Material Design Lite |
| No      | No      | Material Design Lite |

### Material design lite doesn't have selectors!
This might be a fluke, but it appears tha MDL has some serious shortcomings. 


### Be careful reloading pages when testing flask.
You may continue to get errors. 
Try to figure out the conditions unders which Flask reloads the server.


### Flask - record details that burn up time
Lot's information about how Flask, and the web generally, work feels arbitrary.

For this reason, it's difficult to remember. Why remember something arbitrary and path dependent?

And yet, the web is what is is. So, rather than burn time guessing and checking, write down the arbitrary details of 
how flask and the web work.

### Forms 
Methods must be specified 

## Deferred Learnings / Learning Debt
I'm going to come back and learn these skills later
1. PyCharm shortcuts around committing and pushing to Git
2. Material Design Lite grid layout
3. Facial Recognition assignmentd

## PostGreSQL is sot strictly better than MySQL
[According to Digital Ocean](
https://www.digitalocean
.com/community/tutorials/sqlite-vs-mysql-vs-postgresql-a-comparison-of-relational-database-management-systems), 
there are times when MySQL is a better option than PostGqeSQL

[This guys comparision is decent](https://hackr.io/blog/postgresql-vs-mysql).

My overall feeling is to use PostGreSQL because, initially, when your project has little data, performance doesn't 
matter much. Later, you may have a more complex system, and then you'll be glad you have PostGreSQL. Finally, in 
terms of "ease of use", AWS takes care of administration, and I've found PostGreSQL to be very easy to use.

### MySQL
Table 2.1 on the [MySQL installation page](https://dev.mysql.com/doc/mysql-osx-excerpt/5.7/en/osx-installation-pkg.html)
describes where MySql Server was installed.

### HTML to remember
Remember that Forms specify and action, which is a URL endpoint, and a method, and that type "submit" creates a 
button that will post all <input> fields to the html endpoint.

"value=" is used to pre-populate inputs in forms.

Use form label markup for accessibility.

## Speed tips
"def" before decorators slowed me down several times.

It might have made sense to write out all of my routes first.

I should have always used url_for.

I should have enabled Jinja support at the outset.
When I get to Django, take advantage of PyCharm's Django integration.

I jumped into coding too quickly. I should have really looked at the details of what was being assigned - it would 
have saved me time later. Specifically, 
- which URL endpoints to use
- the endpoint / method combinations

Switching names of routes and functions slowed me down, considerably.

Alarm fatigue in PyCharm slows me down. Disable warnings I won't respond to.

When writing code, close the run-code window. 

Mixing up plural and singular is costly.


### To change table in MySQL workbench, start with Menu->Database->Connect to database

When a bit of logic is intricate, make sure to slow down and also check for error surrounding that logic.
These errors are common because the intricate logic has distracted me.

Paying closer attention to the warning that PyCharm gives me is definitely paying off. It's saving me time. 

### Don't do unimportant work
Focus on doing the minimum amount necessary to complete each task.

### Switching to Flask as the run time required adding environment variables
I don't know why, but I followed instructions [here](https://stackoverflow.com/questions/
51188806/pycharm-error-runtimeerror-click-will-abort-further-execution-because-python-3)
and specified that I wanted to use 
`LC_ALL=en_US.utf-8;LANG=en_US.utf-8`


### Use your IDE - but be wary!
Each time I use a new feature of the IDE, be aware that it could change how I develop in unexpected ways.

Talk out loud, or write out your thoughts, as soon as you experience issues. 

### If something is happening very unexpected in javascript
In addition to using console.log(), also inspect the page elements to see how they are changing.

### DOM
The DOM is a standard object model and programming interface for HTML.
- All html elements are defined as objects.
- Each object has methods and properties.
- A method as an action you can do. 
- A property is a value you can get or set.

"document" is a reserved word. It's always the document.

document.getElementById is a useful
<element>.innerHtml is a useful property to change.

Document has three primary methods for finding HTML elements
- getElementById(id)
- getElementsByTagName(name)
- getElementsByClassName(name)

Style isn't set directly. Instead it's set with element.style.property

### Jquery selector is quirky
The JQuery selector is quirky. In particular, it appears able to select elements who a space in the name, if the 
element is simply being printed. But, if the element is being edited, you have to use the $(['id'="some thing"]) syntax.