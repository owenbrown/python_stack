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