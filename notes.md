- That’s why an array of floats is much more compact than a tuple of floats: the array is a single object holding the raw values of the floats, while the tuple consists of several objects—the tuple itself and each float object contained in it. p.23
- pattern matching
```python
class C:
    pass
row = ('hi', C(), 2, 3, (4.5, 5.5))
match row:
    case [str(name), C() as cls, *_, (float(f1), float(f2))]:
        print('pass')
```
