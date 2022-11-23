

"""
Context processor added to settings.py to allow it to be active
everywhere in application. 

Dict of basket class to get data (skey)
"""


from .basket import Basket


def basket(request):
    return {'basket': Basket(request)}
