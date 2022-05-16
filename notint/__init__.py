class NotInt(int):
    def __eq__(): pass
    def __ne__(): pass
    __eq__, __ne__ = map(lambda _: lambda __, ___: int(__).__getattribute__(_.__name__)(___), (__ne__, __eq__))