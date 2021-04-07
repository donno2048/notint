# notint

## Install it from PyPi

```sh
pip install notint
```

## Install it from GitHub

```sh
pip install git+https://github.com/donno2048/notint
```

## Examples

After installing the package try to run this in the python console (line-by-line):

```py
from notint import NotInt # Import NotInt
noin = NotInt(42) # Create a new NotInt object with the value of 42 (or else)
isinstance(noin, int) # Check whether python thinks it's an int
noin == None
noin is None
noin == noin
noin != noin
noin == "42"
noin == 42
noin == 43
print(notint)
```
