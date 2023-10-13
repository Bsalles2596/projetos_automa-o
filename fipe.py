import requests

class FipeIterator:
    def __init__(self, marca_id):
        self.url = f"https://parallelum.com.br/fipe/api/v1/carros/marcas/{marca_id}/modelos"
        self.index = 0
        self.data = self._get_data()

    def _get_data(self):
        response = requests.get(self.url)
        return response.json()["modelos"]

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration
        else:
            carro = self.data[self.index]
            self.index += 1
            return {"nome": carro["nome"], "id": carro["codigo"]}

marca_id = 21 # Exemplo de ID da marca "Chevrolet"
marcas_url = "https://parallelum.com.br/fipe/api/v1/carros/marcas"

response = requests.get(marcas_url)
marcas = response.json()

for marca in marcas:
    if marca["codigo"] == marca_id:
        print(f"Carros da marca {marca['nome']}:\n")
        iterator = FipeIterator(marca_id)
        for carro in iterator:
            print(carro["nome"], carro["id"])
