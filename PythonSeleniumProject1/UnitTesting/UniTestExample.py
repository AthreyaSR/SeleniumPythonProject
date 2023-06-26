import unittest
from Examples import Example

class MyTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        print("this will run before ALL the methods")

    @classmethod
    def tearDownClass(cls) -> None:
        print("this will run after ALL the methods")

    def setUp(self) -> None:
        print("This will run before every method")

    def tearDown(self) -> None:
        print("this will run after every method")

    def test_add(self):
        # sum = Example.Add(self,10,20)
        # self.assertEqual
        self.assertEqual(Example.Add(self,10,20),30)
        self.assertEqual(Example.Add(self,0,0),0)
        self.assertEqual(Example.Add(self,-2,2),0)




    def test_sub(self):
        diff = Example.Sub(self,10,20)
        self.assertEqual(diff,-10)



    # def test_something(self):
    #     self.assertEqual(True, False)  # add assertion here

#Below command is used to run using cmd terminal
# if __name__ == '__main__':
#     unittest.main()
