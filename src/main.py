from protein_api import ProteinApi
from db import ProteinDB
import logging.config


api_endpoint = 'https://www.ebi.ac.uk/pdbe/graph-api/compound/summary/'
timeout = 1
compounds = ['ADP', 'ATP', 'STI', 'ZID', 'DPM', 'XP9', '18W', '29P']
urls = [api_endpoint + c for c in compounds]

if __name__ == '__main__':
    logging.basicConfig(filename="../logs.txt", filemode='a', level=logging.DEBUG)

    proteinDBApi = ProteinApi(timeout)
    proteinDBApi.get_data_in_loop(urls)
    proteins_data = proteinDBApi.data

    db = ProteinDB()
    db.create()
    db.insert(proteins_data)
    db.print()

