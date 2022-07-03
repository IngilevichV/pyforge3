from sqlalchemy import Column, String,  Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Protein(Base):
    __tablename__ = 'proteins'
    id = Column('id', Integer, primary_key=True)
    compound = Column('compound', String)
    name = Column('name', String)
    formula = Column('formula', String)
    inchi = Column('inchi', String)
    inchi_key = Column('inchi_key', String)
    smiles = Column('smiles', String)
    cross_links_count = Column('cross_links_count', Integer)

    def __init__(self, compound, name, formula, inchi, inchi_key, smiles, cross_links_count):
        self.compound = compound
        self.name = name
        self.formula = formula
        self.inchi = inchi
        self.inchi_key = inchi_key
        self.smiles = smiles
        self.cross_links_count = cross_links_count

