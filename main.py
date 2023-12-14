
from globals import coordinatePair
from findTrip import getTripSuggestions
from apiHandler import _getCordByName

def main():
    testCordStart = coordinatePair(57.690012, 11.972992)  # Chalmersplatsen
    testCordEnd = _getCordByName("Studiegången")  
    print("THE ANSWER _________________________\n", getTripSuggestions(testCordStart, testCordEnd))

if __name__ == '__main__':
    main()