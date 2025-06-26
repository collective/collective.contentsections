try:
    from pkg_resources import declare_namespace
except ImportError:
    pass
else:
    declare_namespace(__name__)
