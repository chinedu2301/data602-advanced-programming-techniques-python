'''
Assignment #3

1. Add / modify code ONLY between the marked areas (i.e. "Place code below"). Do not modify or add code elsewhere.
2. Run the associated test harness for a basic check on completeness. A successful run of the test cases does not guarantee accuracy or fulfillment of the requirements. Please do not submit your work if test cases fail.
3. To run unit tests simply use the below command after filling in all of the code:
    python 03_assignment.py
  
4. Unless explicitly stated, please do not import any additional libraries but feel free to use built-in Python packages
5. Submissions must be a Python file and not a notebook file (i.e *.ipynb)
6. Do not use global variables
7. Make sure your work is committed to your master branch in Github
8. Use the test cases to infer requirements wherever feasible


'''
import csv, json, math, pandas as pd, requests, unittest, uuid

# ------ Create your classes here \/ \/ \/ ------

# Box class declaration below here
class Box():
    """
    creates an object box
    
    -------------------------------
    args:
        length: The length of the box
        width: The width of the box
        
        length and width of box should be of the same units
    """
    
    # constructor 
    def __init__(self, length, width):
        """Constructs a box of a given length and width"""
        self.__length = length
        self.__width = width
    
    
    def get_length(self):
        """Returns the length of the box"""
        return self.__length
    
    def get_width(self):
        """Returns the width of the box"""
        return self.__width
        
    def render(self):
        """Renders (draws) a box with asterisks of length and width dimension"""
        for row in range(self.__length):
            for col in range(self.__width):
                if row in (0, self.__length-1) or col in (0, self.__width - 1):
                    print("*", end = " ")
                else:
                    print(" ", end = " ")
            print()
        
    def invert(self):
        """Inverts the box by switching the length and width of the box with each other"""
        a = self.__width
        b = self.__length
        
        return Box(a, b)
        
    def get_area(self):
        """Returns the area of the box"""
        area = self.__length * self.__width
        return round(area, 2)
    
    def get_perimeter(self):
        """Returns the perimeter of the box"""
        perimeter = 2 *(self.__length + self.__width)
        return round(perimeter, 2)
    
    def double(self):
        """Returns a box whose area is double the size of the original box"""
        new_length = self.__length * (2)
        new_width = self.__width * (2)
        return Box(new_length, new_width)
        
    def __eq__(self, other):
        """Checks if two boxes have equal dimensions"""
        if(self.get_length() == other.get_length()):
            if(self.get_width() == other.get_width()):
                return True
        else:
            return False
    
    def print_dim(self):
        """Prints the dimensions of the box"""
        print(f"The length of the box is {self.get_length()}\nThe width of the box is {self.get_width()}")
    
    def get_dim(self):
        """Returns a tuple of the dimensions of the box"""
        dim = (self.get_length(), self.get_width())
        return dim
    
    def combine(self, another_box):
        """Combines the dimensions of one box with that of another box"""
        a = self.__length + another_box.get_length()
        b = self.__width + another_box.get_width()
        return Box(a, b)
    
    def get_hypot(self):
        """Returns the length of the hypotenuse of the box"""
        diagonal = (self.__length**2 + self.__width**2)**0.5
        return round(diagonal, 2)
    
         
# MangoDB class declaration below here
class MangoDB():
    
    def __init__(self):
        self.__d = {
            'default':{
                'version':1.0,
                'db':'mangodb',
                'uuid':uuid.uuid4() #randomly generated uuid
            }
        }
    
    
    
    
    def get_collection_names(self):
        """Returns a list of collections in the database"""
        return self.__d.keys()
    
    def display_collection(self, collection_name):
        """Displays the keys and values of a given collection_name that exists in the database"""
        if collection_name in self.get_collection_names():
            print(f"collection: {collection_name}")
            for key, value in self.__dict[collection_name].items():
                print(f"\t{key}: {value}")
            else:
                raise ValueError(f"{collection_name} does not exist")
                
    def display_all_collections(self):
        """Displays a list of all collections in the database as well as their contents"""
        for collection_name in self.get_collection_names():
            self.display_collection(collection_name)
            
    def add_collection(self, collection_name):
        """Adds an empty collection to the database"""
        if collection_name not in self.get_collection_names():
            self.__d[collection_name] = {}
        else:
            raise ValueError(f"{collection_name} already exists")
    
    def update_collection(self, collection_name, updates):
        """Insert items into a collection that already exists"""
        if collection_name == "default":
            raise ValueError("You cannot update the default collection name")
        elif collection_name in self.get_collection_names():
            self.__d[collection_name].update(updates)
        else:
            raise ValueError(f"{collection_name} does not exists. You cannot update a non-existent collection")
    
    def remove_collection(self, collection_name):
        """Removes a collection and its data from the database"""
        if collection_name == 'default':
            raise ValueError("You cannot remove the default collection")
        elif collection_name in self.get_collection_names():
            del self.__d[collection_name]
        else:
            raise ValueError(f"{collection_name} not found")
    
    def list_collections(self):
        """Displays a list of all collections"""
        for collection in self.get_collection_names():
            print(self.__d.keys())
    
    def get_collection_size(self, collection_name):
        """Returns the number of items in a given collection"""
        if collection_name in self.get_collection_names():
            return len(self.__d[collection_name].keys())
        else:
            raise ValueError(f"{collection_name} does not exist")
    
    def to_json(self, collection_name):
        """Converts a given collection to a json string"""
        if collection_name in self.get_collection_names():
            return json.dumps(self.__d[collection_name])
        else:
            raise ValueError(f"{collection_name} does not exist")
    
    def wipe(self):
        """Cleans out the database and reset it with the default collection"""
        self.__d = {
            'default':{
                'version':1.0,
                'db':'mangodb',
                'uuid':uuid.uuid4() 
            }
        }

# ------ Create your classes here /\ /\ /\ ------





def exercise01():

    '''
        Create an immutable class Box that has private attributes length and width that takes values for length and width
        upon construction (instantiation via the constructor). Make sure to use Python 3 semantics. Make sure the length
        and width attributes are private and accessible only via getters. Immutable here means that any change to its internal
        state results in a new Box being returned. This means there are no setter methods and any time the internal state
        (length or width) is modified, a new Box is created containing the modified values. 
        This is applicable to combine(), invert() and double()
        
        Good article on immutability: https://towardsdatascience.com/https-towardsdatascience-com-python-basics-mutable-vs-immutable-objects-829a0cb1530a
        
        In addition, create:
        - A method called render() that prints out to the screen a box made with asterisks of length and width dimensions
        - A method called invert() that switches length and width with each other
        - Methods get_area() and get_perimeter() that return appropriate geometric calculations
        - A method called double() that doubles the size of the box. Hint: Pay attention to return value here
        - Implement __eq__ so that two boxes can be compared using ==. Two boxes are equal if their respective lengths and widths are identical.
        - A method print_dim that prints to screen the length and width details of the box
        - A method get_dim that returns a tuple containing the length and width of the box
        - A method combine() that takes another box as an argument and increases the length and width by the dimensions of the box passed in
        - A method get_hypot() that finds the length of the diagonal that cuts throught the middle

        In the function exercise01():
        - Instantiate 3 boxes of dimensions 5,10 , 3,4 and 5,10 and assign to variables box1, box2 and box3 respectively 
        - Print dimension info for each using print_dim()
        - Evaluate if box1 == box2, and also evaluate if box1 == box3, print True or False to the screen accordingly
        - Combine box3 into box1 (i.e. box1.combine()) creating box4
        - Double the size of box2 creating box5
        - Combine box5 into box4 creating box6
        - Using a for loop, iterate through and print the tuple received from calling box2's get_dim()
        - Find the size of the diagonal of box2

'''

    # ------ Place code below here \/ \/ \/ ------
    box1 = Box(5, 10)
    box2 = Box(3, 4)
    box3 = Box(5, 10)
    
    box1.print_dim() # returns the dimension info for box1
    box2.print_dim() # returns the dimension info for box2
    box3.print_dim() # returns the dimension info for box3
    
    box1 == box2 
    box1 == box3
    
    box4 = box1.combine(box3) # combines box3 into box1
    
    box5 = box2.double() # doubles the size of box2
    
    box6 = box4.combine(box5) # combines box5 into box4
    
    for dim in box2.get_dim():
        print(dim)
    
    box2.get_hypot() # gets the size of the diagonal of box2
    
    
    return box1, box2, box3, box4, box5, box6

    # ------ Place code above here /\ /\ /\ ------


def exercise02():
    '''
    Create a class called MangoDB. The MangoDB class wraps a dictionary of dictionaries. At the the root level, each key/value will be called a collection, similar to the terminology used by MongoDB, an inferior version of MangoDB ;) A collection is a series of 2nd level key/value paries. The root value key is the name of the collection and the value is another dictionary containing arbitrary data for that collection.

    For example:

        {
            'default': {
            'version':1.0,
            'db':'mangodb',
            'uuid':'0fd7575d-d331-41b7-9598-33d6c9a1eae3'
            },
        {
            'temperatures': {
                1: 50,
                2: 100,
                3: 120
            }
        }
    
    The above is a representation of a dictionary of dictionaries. Default and temperatures are dictionaries or collections. The default collection has a series of key/value pairs that make up the collection. The MangoDB class should create only the default collection, as shown, on instantiation including a randomly generated uuid using the uuid4() method and have the following methods:
        - display_all_collections() which iterates through every collection and prints to screen each collection names and the collection's content underneath and may look something like:
            collection: default
                version 1.0
                db mangodb
                uuid 739bd6e8-c458-402d-9f2b-7012594cd741
            collection: temperatures
                1 50
                2 100 
        - add_collection(collection_name) allows the caller to add a new collection by providing a name. The collection will be empty but will have a name.
        - update_collection(collection_name,updates) allows the caller to insert new items into a collection i.e. 
                db = MangoDB()
                db.add_collection('temperatures')
                db.update_collection('temperatures',{1:50,2:100})
        - remove_collection() allows caller to delete a specific collection by name and its associated data
        - list_collections() displays a list of all the collections
        - get_collection_size(collection_name) finds the number of key/value pairs in a given collection
        - to_json(collection_name) that converts the collection to a JSON string
        - wipe() that cleans out the db and resets it with just a default collection
        - get_collection_names() that returns a list of collection names


        Make sure to never expose the underlying data structures

        For exercise02(), perform the following:

        - Create an instance of MangoDB
        - Add a collection called testscores
        - Take the testscores list and insert it into the testscores collection, providing a sequential key i.e 1,2,3...
        - Display the size of the testscores collection
        - Display a list of collections
        - Display the db's UUID
        - Wipe the database clean
        - Display the db's UUID again, confirming it has changed
    '''

    testscores = [99,89,88,75,66,92,75,94,88,87,88,68,52]

    # ------ Place code below here \/ \/ \/ ------
    
    # create an instance of MangoDB
    db = MangoDB()
    
    # Add a collection called testscores to the instance of MangoDB
    db.add_collection('testscores')
    
    # Insert the testscores list into the testscores collection providing a sequential key
    db.update_collection( 'testscores', {1:99,2:89,3:88,4:75,5:66,6:92,7:75,8:94,9:88, 10:87,11:88,12:68,13:52})
    
    # Get and display the size of the testscores collection
    db.get_collection_size('testscores')
    
    # Display a list of collections
    db.list_collections()

    # Display the db's UUID
    db._MangoDB__d['default']['uuid']
    
    # Wipe the database clean
    db.wipe()
    
    # Display the db's UUID again, confirming it has changed
    db._MangoDB__d['default']['uuid']
    # ------ Place code above here /\ /\ /\ ------


def exercise03():
    '''
    1. Avocado toast is expensive but enormously yummy. What's going on with avocado prices? Read about avocado prices (https://www.kaggle.com/neuromusic/avocado-prices/home)
    2. Load the avocado.csv file included in this Githb repository and display every line to the screen
    3. Open the file name under csv_file
    4. The reader should be named reader
    5. Use only the imported csv library to read and print out the avacodo file
    
    '''

    # ------ Place code below here \/ \/ \/ ------
    
    # import closing from contextlib --> used to open the response file obtained from the get request
    from contextlib import closing
    url = "https://raw.githubusercontent.com/chainhaus/pythoncourse/master/avocado.csv"
    
    
    with closing(requests.get(url, stream = True)) as r:
        
        # decode the file obtained
        lines = (line.decode('utf-8') for line in r.iter_lines())
        
        # read the decoded file using csv.reader
        reader = csv.reader(lines, delimiter = ",", quotechar='"')
        for row in reader:
            print(row)


    # ------ Place code above here /\ /\ /\ ------

class TestAssignment3(unittest.TestCase):
    def test_exercise01(self):
        print('Testing exercise 1')
        b1, b2, b3, b4, b5, b6 = exercise01()
        self.assertEqual(b1.get_length(),5)
        self.assertEqual(b1.get_width(),10)
        self.assertEqual(b2.get_length(),3)
        self.assertEqual(b2.get_width(),4)
        self.assertEqual(b3.get_length(),5)
        self.assertEqual(b3.get_width(),10)            
        self.assertEqual(b4.get_length(),10)
        self.assertEqual(b4.get_width(),20)        
        self.assertEqual(b5.get_length(),6)
        self.assertEqual(b5.get_width(),8)
        self.assertEqual(b6.get_length(),16)
        self.assertEqual(b6.get_width(),28)
        self.assertTrue(b1==Box(5,10))
        self.assertEqual(b2.get_hypot(),5.0)
        self.assertEqual(b1.double().get_length(),10)
        self.assertEqual(b1.double().get_width(),20)
        self.assertTrue(3 in b2.get_dim())
        self.assertTrue(4 in b2.get_dim())
        self.assertTrue(6 in b2.double().get_dim())
        self.assertTrue(8 in b2.double().get_dim())
        self.assertTrue(b2.combine(Box(1,1))==Box(4,5))
        self.assertTrue(b1.invert()==Box(10,5))

    def test_exercise02(self):
        print('Testing exercise 2')
        exercise02()
        db = MangoDB()
        self.assertEqual(db.get_collection_size('default'),3)
        self.assertEqual(len(db.get_collection_names()),1)
        self.assertTrue('default' in db.get_collection_names() )
        db.add_collection('temperatures')
        self.assertTrue('temperatures' in db.get_collection_names() )
        self.assertEqual(len(db.get_collection_names()),2)
        db.update_collection('temperatures',{1:50})
        db.update_collection('temperatures',{2:100})
        self.assertEqual(db.get_collection_size('temperatures'),2)
        self.assertTrue(type(db.to_json('temperatures')) is str)
        self.assertEqual(db.to_json('temperatures'),'{"1": 50, "2": 100}')
        db.wipe()
        self.assertEqual(db.get_collection_size('default'),3)
        self.assertEqual(len(db.get_collection_names()),1)
        
    def test_exercise03(self):
        print('Exercise 3 not tested')
        exercise03()
     

if __name__ == '__main__':
    unittest.main()