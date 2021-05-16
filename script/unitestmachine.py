import crudmachine
import unittest

#################################
######## test unitair ###########
#################################
class TestStringMethods(unittest.TestCase):

    def test_readAll(self):

        file = open("machines.txt","r")
        Counter = 0
        # Reading from file
        Content = file.read()
        CoList = Content.split("\n")
        
        for i in CoList:
            if i:
                Counter += 1
        file.close()
        self.assertEqual(crudmachine.readAll(), Counter)

   

if __name__ == '__main__':
    unittest.main()