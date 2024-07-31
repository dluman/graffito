import ast
import sys
import inspect

from functools import wraps
from types import FunctionType, FrameType
from typing import cast

# This library is a (mis)use of some stuff I found on SO for another project.
# I thought it might be useful, so I made it.

# Decoration functionality taken from the SO:
# https://stackoverflow.com/questions/3232024/introspection-to-get-decorator-names-on-a-method

# Use the following to retrieve the original names
# of wrapped functions:
# https://stackoverflow.com/questions/4887081/get-the-name-of-a-decorated-function

def graffiti(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        return f(*args, **kwargs)
    try:
        tags = get_tags(f)
        setattr(wrapper, "graffiti", tags)
    except IndentationError as e:
        pass
    return wrapper

def get_tags(obj):
    # Is it polymorphic? Kinda.
    target = obj
    tags = {}
    def visit_callable(node):
        tags[node.name] = []
        for n in node.decorator_list:
            name = None
            if isinstance(n, ast.Call):
                name = n.func.attr if isinstance(n.func, ast.Attribute) else n.func.id
            else:
                name = n.attr if isinstance(n, ast.Attribute) else n.id
            tags[node.name].append(name)
    visitor = ast.NodeVisitor()
    visitor.visit_FunctionDef = visit_callable
    visitor.visit(ast.parse(inspect.getsource(target)))
    return tags

# TODO: Drawback that the program has to decorate its classes in order
#       to pass them through parsing; that's inconvenient.
