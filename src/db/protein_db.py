from sqlalchemy import create_engine, inspect
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy_utils import create_database, database_exists
import pandas as pd
import os
from dotenv import load_dotenv
import logging

from .model import Protein

Base = declarative_base()
load_dotenv()
connection = os.getenv('DATABASE_URL')

log = logging.getLogger(__name__)


class ProteinDB:
    def __init__(self, echo=False):
        # an Engine, which the Session will use for connection
        self.engine = create_engine(connection, echo=echo)

        # create a configured "Session" class
        self.Session = sessionmaker(bind=self.engine)
        log.debug('Initiated Protein db instance')

    def create(self):
        Base.metadata.drop_all(self.engine)
        if not database_exists(self.engine.url):
            create_database(self.engine.url)

        # self.drop_table(Protein.__table__)  # TODO: remove (added for testing purpose)
        if not inspect(self.engine).has_table(Protein.__tablename__):
            Base.metadata.create_all(self.engine, tables=[Protein.__table__])

    def insert(self, proteins_data):
        with self.Session() as session:
            for compound in proteins_data:
                compound_type = list(compound.keys())[0]
                compound_data = compound[compound_type]
                for d in compound_data:
                    # print(compound_id, compound_data)
                    name = d["name"]
                    formula = d["formula"]
                    inchi = d["inchi"]
                    inchi_key = d["inchi_key"]
                    smiles = d["smiles"]
                    cross_links_count = len(d['cross_links'])
                    session.add(Protein(
                        compound=compound_type,
                        name=name,
                        formula=formula,
                        inchi=inchi,
                        inchi_key=inchi_key,
                        smiles=smiles,
                        cross_links_count=cross_links_count)
                    )

            session.commit()
            log.debug('Inserted values to Protein table')

    def print(self):
        df = pd.read_sql_table(Protein.__tablename__, con=self.engine)
        df = df.astype(str).applymap(lambda x: x[:10] + '...' if len(x) >= 13 else x)
        print(df.to_markdown())

    def drop_table(self, table):
        table.drop(self.engine)










