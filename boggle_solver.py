"""
NAME: Sam-joel Blankson
SID: @03057213
"""

class Boggle:
    def __init__(self, GRID, DICTIONARY):
        
        
       
        self.GRID = GRID  # Set the grid of letters
        self.DICTIONARY = set(DICTIONARY)  # Convert dictionary to a set for faster lookups
        self.FOUND_WORDS = set()  # Initialize an empty set to store found words
        self.maxRow = len(GRID)  # Number of rows in the grid
        self.maxCol = len(GRID[0])  # Number of columns in the grid
        # Possible directions to move in the grid (8 directions: vertical, horizontal, and diagonal)
        self.DIRECTIONS = [(-1, -1), (-1, 0), (-1, 1),
                           (0, -1), (0, 1),
                           (1, -1), (1, 0), (1, 1)]
        self.solve()  # Start solving the Boggle puzzle

    def setGrid(self, GRID):
        
       
      
        self.GRID = GRID  # Updates the grid
        self.maxRow = len(GRID)  #  number of rows
        self.maxCol = len(GRID[0])  #  number of columns

    def setDictionary(self, DICTIONARY):
        
        #Set the dictionary for the Boggle game.
        
        self.DICTIONARY = set(DICTIONARY)  # sets the dictionary for the Boggle game 

    def first_letter(self, LETTER):
        
        
        FIRST_LETTER_IND = []  # List to store the indices of the letter
        for ROW in range(self.maxRow):  # Iterate over each row
            for COL in range(self.maxCol):  # Iterate over each column
                if self.GRID[ROW][COL] == LETTER:  # Check if the current cell contains the letter
                    FIRST_LETTER_IND.append((ROW, COL))  # Add the index to the list
        return FIRST_LETTER_IND  # Return the list of indices

    def check_presence(self, ROW, COL, nextLetter, VISITED):
        """
        Check all possible neighbors to find the nextLetter.
        """
        VALID_NEIGHBORS = []  # List to store valid neighboring cells
        for DIRECTION in self.DIRECTIONS:  # Iterate over all possible directions
            NEXT_ROW = ROW + DIRECTION[0]  # Calculate the next row based on direction
            NEXT_COL = COL + DIRECTION[1]  # Calculate the next column based on direction
            # Check if the next cell is within bounds, not visited, and contains the nextLetter
            if (0 <= NEXT_ROW < self.maxRow and
                0 <= NEXT_COL < self.maxCol and
                (NEXT_ROW, NEXT_COL) not in VISITED and
                self.GRID[NEXT_ROW][NEXT_COL] == nextLetter):
                VALID_NEIGHBORS.append((NEXT_ROW, NEXT_COL))  # Add the valid neighbor to the list
        return VALID_NEIGHBORS  # Return the list of valid neighbors

    def check_for_valid_word(self, WORD):
        """
        Check if a WORD can be formed in the grid.
        """
        if len(WORD) < 3:  # Words should  be at least 3 letters long
            return False

        FIRST_LETTERS = self.first_letter(WORD[0])  # Get  the starting positions for the first letter of the word
        for COORD in FIRST_LETTERS:  # Iterate  all starting positions
            VISITED = [COORD]  # Initialize visited cells with the starting position
            CURR_ROW, CURR_COL = COORD  # Current position
            VALID_WORD = False  # Flag to indicate if the word is valid
            for LETTER in WORD[1:]:  # Iterate over the remaining letters in the word
                NEIGHBORS = self.check_presence(CURR_ROW, CURR_COL, LETTER, VISITED)  # Find neighbors
                if not NEIGHBORS:  # If no valid neighbors, break out of the loop
                    break
                CURR_ROW, CURR_COL = NEIGHBORS[-1]  # Move to the last valid neighbor
                VISITED.append((CURR_ROW, CURR_COL))  # Add the new position to visited
                if len(VISITED) == len(WORD):  # Check if the entire word has been visited
                    VALID_WORD = True  # The word is valid
                    break
            if VALID_WORD:  # If the word is valid, return True
                return True
        return False  # If no valid path is found, return False

    def solve(self):
        """
        Find all valid words in the Boggle grid.
        """
        for WORD in self.DICTIONARY:  # Iterate over all words in the dictionary
            if self.check_for_valid_word(WORD):  # Check if the word can be formed
                self.FOUND_WORDS.add(WORD)  # Add the valid word to the set of found words

    def getSolution(self):
        """
        Get the list of found words.
        """
        return sorted(list(self.FOUND_WORDS))  # Return a sorted list of found words

def main():
    """
    Main function to test the Boggle solver.
    """
    GRID = [
        ["A", "B", "C", "D"],
        ["E", "F", "G", "H"],
        ["I", "J", "K", "L"],
        ["A", "B", "C", "D"]
    ]
    DICTIONARY = ["ABEF", "AFJIEB", "DGKD", "DGKA"]  # Sample dictionary

    MY_GAME = Boggle(GRID, DICTIONARY)  # Create a Boggle game instance
    print(MY_GAME.getSolution())  # Print the list of found words

if __name__ == "__main__":
    main()  # Run the main function if the script is executed directly
