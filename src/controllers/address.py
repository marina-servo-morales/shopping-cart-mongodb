from src.models.address import (
    create_address
)
from src.server.database import connect_db, db, disconnect_db


async def adresses_crud():
    option = input("Entre com a opção de CRUD endereço: \n1: Cadastrar endereço\n2: Procurar endereços do usuário\n3: Deletar endereço selecionado pelo seu ID\n")
    
    await connect_db()
    address_collection = db.address_collection


    user_address = {
        "user": 
        {
        "_id": '6330664e9d91870940b12ed6',
        "email": "teste123@gmail.com"
    },
      
    "address":  [{
        "street": "Rua 123",
        "cep": "12345678",
        "district": "Vila Branca",
        "city": "Jacarei",
        "state": "SP",

        "is_delivery": True
    }]
    }

    if option == '1':
        # create user address
        user_address = await create_address(
            address_collection,
            user_address
        )
        print(user_address)

    


    await disconnect_db()
