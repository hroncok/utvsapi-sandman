reverse_models = {}


def register(cls):
    '''Class decorator to register user models

    Register it in dict by table name as we'll need that as well'''
    cls.__url__ = '/{}'.format(cls.__name__.lower())
    reverse_models[cls.__tablename__] = cls
    return cls


def reverse_lookup(table):
    '''Reverse lookup for model belonging to a table'''
    return reverse_models[str(table)]
