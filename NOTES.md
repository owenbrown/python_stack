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

# Big Idea
The big idea is, I'd learn faster and get through these modules more quickly if I didn't get hung up on details. 
There is a constant balance between learning deeply instead of guess-and-check, and spending too time on a blocker. 
The rule of thumb might be "guess if there is a high certainty that the first guess will work", and "70% of blocks 
occur because of typos and errors. So avoid these if possible."



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

### MVC vs MTV
(Model, View, Controller) translates to (Model, Template, View) in Django.

One project per application.
Many apps per project.

### Beware - regex keywords in paths are positional
The ordering matters, not the name in the regex


Don't get hung up on Django having a funny regex. 
Keep moving.

### When using regex, for example, in Django's URLs, remember to escape the slashes.

### It's necessary to run `python manage.py migrate` prior to using session.

### Django template notes
Jinja2 is included but not recommended. 
The system for selecting which template backend (DTL or Jinja2) is complex.
The template engine is referred to as a *backend*.

The exists a *urlpatterns* list. It's necessary to understand how this list is generated in order to put urls in your
 code. 

Django's documentation talks a lot about why it offers the features that it offers. It explains the reasoning of the 
authors of the software. If I read the documentation with the attitude that I simply want to finish the Django 
tutorial as soon as possible, then I will be frustrated with what I will view as unnecessary text.

However, if I embrace learning Django as an opportunity to learn a bit about how to write a web server, then I will 
find the documentation interesting. So, I will do that. 

#### Url resolution works in two directions
It's necessary both to map a request from the user / browser to a view, and it is necessary to map a view plus a list
 of arguments to an associated URL. 
 
 I'm struggling to understand how to use the *url template tag*.
 
 The article makes a reference to URLConf. 
 I'm going to return here - https://docs.djangoproject.com/en/2.2/topics/http/urls/#examples - after I finish reading
  about URLConf. 
  
 #### URLConf
 The URL Configuration, maps URL Path expressions to python functions (views). Written in pure python.
 
 This document is 10 pages. I'm going to read the whole document, slowly, because I think doing so will really help 
 me understand Django. When I read long documents, I tend to check out. So, to get around that I'll take good notes.
 
 There are multiple URL confs.  
 We can trace the resolution
 - settings.py specifies the URLConf file, urls.py
 - urls.py `include`s other URLConf files. For example, apps/only_app/urls.py
 
 Middleware can overload this. I don't know what "middleware" refers to, so I'll assume that my current apps aren't 
 using any middleware. But, if it did have middleware, the middle ware could permute the HttpRequest object with its 
 own urlconf.
 
 The URLConf generates a sequence of django.urls.path() or django.urls.re_path().
 
 Django supports custom pather converters. 
 
 I don't understand what this FourDigitYearConverter does.
 
 The docs suggest that custom path converters are simpler than regular expression converters.
 
 Use named, rather than un-named, regular expression groups.
 
 Often, two regex's that both resolve a ul to the same view, are different in that one can be reversed, and the other
  cannot. 
  
 [A trick for specifying default views can be found here](
 https://docs.djangoproject.com/en/2.2/topics/http/urls/#specifying-defaults-for-view-arguments)
 
 ### Faster resolution
 I got mired because the examples given to me in the Django tutorial didn't mention the use of a named view.  
 I don't know how I could have gotten past that part faster. This deserves further contemplation.
 
 
 Forms can use GET in addition to POST.
 
 ### Forms are built in
 We probably want to use Django's built in forms feature for pretty much every form.
 I'm going to skip it now, and use it on the next form.
 
 ## wsgi is the entrypoint for your wsgi server
 Gunicorn and uwsgi are two popular wsgi servers that work with both Django and Flask.
 
### Django is a web framework, not a web server 
 
### Adding files does not trigger a Django restart.

### Django apps and projects have a many-to-many relationship
A useful microservice app might be identical and used in multiple Django projects.

Apps are de-coupled from the Django project. The word "pluggable" references this decoupling.

### Lots and lots of code is generated.
Creating an app generates five files, plus a migrations directory. 

### Always use "include()" to include other URL patterns. `admin.site.urls` is the only exception to this.

### include() -> path()
Path accepts 4 arguments: route, view, kwargs, name
- Route - method and the domain name are not searched.
- View - calls a function whose first positional argument is type HttpRequest. Arguments parsed out of the url are 
passed as keyword arguments 
- kwargs - arbitrary key word arguments can be passed in a dictionary to the target view. 
- name - used for generating urls


### Database defaults to SQLLite
To change database, update the settings.py file, DATABASE.
You'll need to add USER, PASSWORD, and HOST.
'django.db.backends.postgresql' or 'django.db.backends.mysql'.

There's a method for packaging and distributing Django apps.

### Each app has database migrations.
Running `django startproject mysite` automatically added 6 apps. The six apps each have their own migrations. It was 
necessary to run `python manage.py migrate` in order to perform those migrations.

### Design choices
"Fields shouldn't assume certain behaviors based solely on the name of the field". This is in contrast to Ruby on Rails.

Django appears to have a better migrations system then Ruby on Rails. Simpler, anyway. 


#### [Field](https://docs.djangoproject.com/en/2.2/ref/models/fields/#django.db.models.Field) is an abstract class that represents a database table column
Required arguments such as max_length are used for validation by Django.

#### In settings, INSTALLED_APPS is a list of AppConfig classes.
Migrations are done in two steps:
- python manage.py makemigrations
- python manage.py migrate

### Timezone support is built in
Use `from django.utils import timezone; timestamp = timezone.now()` for timestamps.

### ORM
Each models.Model has an attribute 'objects' of type django.db.models.manager.Manager, with query methods.
"get" expects only one response; it will error otherwise. 

Something that makes Django's ORM different than most python functions is that attributes are created, and the 
attributes named using the name of associated models. In the official Django tutorial, for example, "Question" has a 
one-to-many relationship with "Choice". So, for Question instance q, q.choice_set.all() gives me all Choices whose 
question_id (foreign key) equals the id of q.

The double-underscore plays a similar role to a period.
I looks like delete and create automatically save.

 
A missing comma between function arguments can generate the "can't assign to function call" error message in PyCharm.
 In a addition, it will underline in red correct items in a list, that may occur prior to the missing comma.
 
### Django avoids coupling the model, template, and view
However, the django.shortcuts module provides useful methods that couple different components. For example, 
get_object_or_404() couples the model and the view. 

### Django - queer templating
I find it inconsistent that Django does not let you do simple Python inside the template, but appears to allow you to 
use advanced ORM features. 

One counter-intuitive feature is that it drops the parenthesis from functions. For example, question.choice_set.all, 
is equivalent to calling question.choice_set.all() in python.

### I don't know what this means
>>>
The template system uses dot-lookup syntax to access variable attributes. In the example of {{ question.question_text }}, first Django does a dictionary lookup on the object question. Failing that, it tries an attribute lookup – which works, in this case. If attribute lookup had failed, it would’ve tried a list-index lookup.
>>>

### HTML
Radio buttons all have the same name, but different ids and values. 

request.POST['key'] values are always strings.

HttpResponseRedirect appears unable to forward along values as parameters; it accepts only one argument.

reverse() args are positional, and must be a tuple, even if they are a tuple of one.

### [Use F() to avoid race conditions](https://docs.djangoproject.com/en/2.2/ref/models/expressions/#avoiding-race-conditions-using-f)
Specifically, when incrementing something in the database.


Testing in Django uses Django's testing framework. 


## [Checking test coverage is easy!](https://docs.djangoproject.com/en/2.2/topics/testing/advanced/#topics-testing-code-coverage)

At some point I'll need to learn how to store static files in S3.
There appears to be two common strategies for deploying static files
- Have a dedicated static files server (nginx, perhaps)
- Use a CDN like AWS Cloudfront, S3, Akamai, etc.

In either case, Django allows you to collect all of the static files. It appears that you can get

### Static files can't use Django's path generator
Use relative paths instead.   