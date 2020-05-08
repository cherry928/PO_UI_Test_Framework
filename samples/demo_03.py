import unittest

class testa(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print('setUpClass')

    @classmethod
    def tearDownClass(cls) -> None:  # 针对类级别的
        print('tearDownClass')

    def setUp(self) -> None:
        print('setUp')

    def tearDown(self) -> None:  # 针对方法级别的
        print('tearDown')

    def test_01(self):
        print('test_01')
        self.assertTrue(True)

    def test_02(self):
        print('test_02')
        self.assertTrue(True)

if __name__=='__main__':
    unittest.main()