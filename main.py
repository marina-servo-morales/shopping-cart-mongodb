import asyncio

from src.controllers.users import users_crud


from bson.objectid import ObjectId


#from src.controllers.products import products_crud
#from src.controllers.carrinho import carrinho_crud
# fazer todos import daqui

loop = asyncio.get_event_loop()
loop.run_until_complete(users_crud())


