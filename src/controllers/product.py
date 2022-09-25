from src.models.product import (
    create_product,
    get_product_by_id,
    delete_product,
    get_products
)
from src.server.database import connect_db,db,disconnect_db


async def products_crud():
    option = input("Entre com a opção de CRUD produto: \n1: Cadastrar produto\n2: Procurar produto pelo ID\n3: Deletar produto selecionado pelo ID\n4: Listar produtos\n")



    await connect_db()
    product_collection = db.product_collection

    product =  {
        "name": "notebook",
        "description": "acer",
        "price": 3000.00,
        "image": "teste",
        "code": 100
    }

    if option == '1':
        # create
        product = await create_product(
            product_collection,
            product
        )
        print(product)
    elif option == '2':
        # get 
        product = await get_product_by_id(
            product_collection,
            product["email"]
        )
        print(product)
   

    elif option == '3':
        # delete por ID
        product = await get_product_by_id(
            product_collection,
            product["_id"]
        )

        result = await delete_product(
            product_collection,
            product["_id"]
        )

        print(result)
    elif option == '4':
        # pagination
        product = await get_products(
            product_collection,
            skip=0,
            limit=0
        )
        print(product)

    await disconnect_db()

