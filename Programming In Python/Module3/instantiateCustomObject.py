# Define class MyFirstClass
class MyFirstClass():
    print("Who wrote this?")
    # Define string variable called index
    index = "Author-Book"
    # Define function hand_list()
    def hand_list(self, philosopher, book):
        # variable + “ wrote the book: ” + variable
        print(philosopher + " wrote the book: " + book)

# Call function handlist()
whodunit = MyFirstClass()
whodunit.hand_list("Sun Tzu", "The Art of War")
