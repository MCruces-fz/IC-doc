# Documentation of ***map*** function

This function makes...

```python
from functools import wraps

def closing(target):
    try: yield
    finally: target.close()

def   _exactly_one(spec): return not isinstance(spec, (tuple, list, type(None)))

def coroutine(generator_function):
    @wraps(generator_function)
    def proxy(*args, **kwds):
        coroutine = generator_function(*args, **kwds)
        next(coroutine)
        return coroutine
    return proxy

def map(op=None, *, args=None, out=None, item=None):
    if item is not None:                                                                                                                                                                                         
        if args is not None or out is not None:
            raise ValueError("dataflow.map: use of `item` parameter excludes both `args` and `out`")
        assert args is None and out is None
        args = out = item

    if args is None and out is None:
        def map_loop(target):
            with closing(target):
                while True:
                    target.send(op((yield)))
    else:
        if _exactly_one(args):
            args = args,

        merged_output = _exactly_one(out)
        if merged_output:
            out = out,

        def map_loop(target):
            with closing(target):
                while True:
                    data   = yield
                    values = (data[arg] for arg in args)
                    trans  = op(*values)
                    if merged_output:
                        trans = trans,
                    for name, value in zip(out, trans):
                        data[name] = value
                    target.send(data)

    return coroutine(map_loop)
```
