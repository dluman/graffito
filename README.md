# Graffito

> Speak softly, but carry a big can of paint.
>
> _Banksy_

## Installtion

Find this tool on`PyPI`: `pip install graffito`

## Usage

Given a program:
```python
from graffito.tags import graffiti, get_tags

func_test = graffiti

@func_test
def test():
    pass

class TestClass:

    method_test = graffiti

    @method_test
    def class_test(self):
        pass

print(get_tags(TestClass))
print(get_tags(test))
```
Executing the program will return:
```bash
{'class_test': ['method_test']}
{'test': ['func_test']}
```
This is a bespoke module. However, let's say that we wanted to characterize functions of a certain
signature with a decorator so that we could handle them the same way. Let's say:
```python
from graffito.tags import graffiti, get_tags

class TestClass:

    two_var_sig = graffiti

    @two_var_sig
    def function_a(self, input_a, input_b):
        print(f"{input_a}, {input_b}")

    @two_var_sig
    def function_b(self, input_a, input_b):
        print(f"{input_b}, {input_a}")

    def function_not_like_them(self, input_a):
        print(f"SIKE!")

t = TestClass()
tags = get_tags(TestClass)
for tag in tags:
    if "two_var_sig" in tags[tag]:
        getattr(t, tag)(1,2)
```
I know it seems really arbitrary, but it helped me write a simple computer emulator and I think I 
can develop it to be useful outside of my silly context. Let's find out.
