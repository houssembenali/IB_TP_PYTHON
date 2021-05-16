import crudmachine

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

    def test_readAll2(self):
        file = open("machines.txt","r")
        Counter = 0
        # Reading from file
        Content = file.read()
        CoList = Content.split("\n")
        
        for i in CoList:
            if i:
                Counter += 1
        file.close()
        self.assertEqual(crudmachine.readAll(), 55555)

if __name__ == '__main__':
    unittest.main()