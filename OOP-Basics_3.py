# Polymorphism & Abstraction

class SortingAlgorithm:

    def sort(self):
        pass

class InsertionSort(SortingAlgorithm):
    
    def sort(self):
        print("Insertion Sort Is Running !")

class SelectionSort(SortingAlgorithm):
    
    def sort(self):
        print("Selection Sort Is Running !")

class QuickSort(SortingAlgorithm):
    
    def sort(self):
        print("Quick Sort Is Running !")

SNum = input("Select A Sorting Algorithm : \n1 : Insertion Sort \n2 : Selection Sort \n3 : Quick Sort \n")
SNum = int(SNum)

# Creating A NULL Object (None)
SAlgorithm = None

if SNum == 0 :
    SAlgorithm = InsertionSort()

elif SNum == 1 :
    SAlgorithm = SelectionSort()

else :
    SAlgorithm = QuickSort()

SAlgorithm.sort()