import asyncio


from src.controllers.users import users_crud
from src.controllers.address import adresses_crud
from src.controllers.product import products_crud


from bson.objectid import ObjectId


#from src.controllers.products import products_crud
#from src.controllers.carrinho import carrinho_crud
# fazer todos import daqui

loop = asyncio.get_event_loop()
loop.run_until_complete(users_crud())


loop = asyncio.get_event_loop()
loop.run_until_complete(adresses_crud())


loop = asyncio.get_event_loop()
loop.run_until_complete(products_crud())