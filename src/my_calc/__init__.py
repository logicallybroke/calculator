try:
    import numpy
except ImportError as e:
    raise RuntimeError("This package requires numpy at build time") from e
