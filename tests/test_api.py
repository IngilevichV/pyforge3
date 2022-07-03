import unittest
from src.protein_api import ProteinApi


class TestProteinApi(unittest.IsolatedAsyncioTestCase):

    async def test_empty_input_string(self):
        """
        Test return value when empty url string is passed
        """
        api = ProteinApi(1)
        res = await api.get_data("")
        self.assertEqual(None, res)

    async def test_valid_compound_name(self):
        """
        Test returned values for valid compound names
        """
        compound_name = 'ADP'
        api = ProteinApi(1)
        res = await api.get_data(f'https://www.ebi.ac.uk/pdbe/graph-api/compound/summary/{compound_name}')
        data = res[compound_name][0]
        self.assertEqual("ADENOSINE-5'-DIPHOSPHATE", data['name'])
        self.assertEqual("C10 H15 N5 O10 P2", data['formula'])
        self.assertEqual("InChI=1S/C10H15N5O10P2/c11-8-5-9(13-2-12-8)15(3-14-5)10-7(17)6(16)4(24-10)1-23-27(21,22)25-26(18,19)20/h2-4,6-7,10,16-17H,1H2,(H,21,22)(H2,11,12,13)(H2,18,19,20)/t4-,6-,7-,10-/m1/s1", data['inchi'])
        self.assertEqual("XTWYTFMLZFPYCI-KQYNXXCUSA-N", data['inchi_key'])
        self.assertEqual("c1nc(c2c(n1)n(cn2)C3C(C(C(O3)COP(=O)(O)OP(=O)(O)O)O)O)N", data['smiles'])
        self.assertEqual(17, len(data['cross_links']))

    async def test_invalid_compound_name(self):
        """
        Test raise exception for invalid url
        """
        api = ProteinApi(1)
        invalid_compound_name = 'Invalid'
        with self.assertRaises(Exception):
            await api.get_data(f'https://www.ebi.ac.uk/pdbe/graph-api/compound/summary/{invalid_compound_name}')


if __name__ == '__main__':
    unittest.main()
