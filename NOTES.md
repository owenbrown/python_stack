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
