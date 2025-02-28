# Know Your Places Game

## Overview
This educational app helps users learn the names and locations of places. The program includes two versions: one for Kenya counties and another for U.S. states. It displays a blank map and prompts users to guess the names of counties or states. When a correct guess is made, the name is displayed at the correct position on the map. At the end of the game, a CSV file is generated with the names of places the user failed to guess, allowing them to review and learn.

## How It Works
1. **Select a game version**: Choose either the Kenya Counties Game or the U.S. States Game by running the respective Python file.
2. **Guess place names**: Type the name of a county (Kenya) or state (U.S.) into the prompt.
3. **Correct answers appear on the map**: If the guess is correct, the name is displayed at its corresponding location on the map.
4. **Exit and review missed places**: If the user types "Exit", the game ends, and a CSV file is generated containing the names of places that were not guessed correctly.

## Installation & Usage
### Prerequisites
- Python 3.x
- `turtle` and `pandas` libraries (both included in Python standard installation, but `pandas` may require manual installation via `pip install pandas`)

### Steps to Run the Game
1. **Clone the repository**:
   ```sh
   git clone https://github.com/yourusername/place-names-game.git
   cd place-names-game
   ```
2. **Run the Kenya Counties Game**:
   ```sh
   python Kenya_main.py
   ```
3. **Run the U.S. States Game**:
   ```sh
   python US_main.py
   ```
4. **Exit the game**:
   - Type "Exit" at any time to generate a CSV file containing the names of places not guessed correctly.

## File Structure
```
place-names-game/
│-- Kenya_main.py  # Main script for Kenya counties guessing game
│-- US_main.py  # Main script for U.S. states guessing game
│-- Kenya_counties_coordinates.csv  # CSV file containing Kenya counties and their coordinates
│-- All_50_US_states.csv  # CSV file containing U.S. states and their coordinates
│-- blank_Kenya_counties_map_gif.gif  # Blank map for Kenya counties
│-- blank_US_states_img.gif  # Blank map for U.S. states
│-- extract_coordinates.py  # Script to extract coordinates from a blank map
```

## Extracting Coordinates for a New Map
If you want to create a game for a different country or region, you can use `extract_coordinates.py` to generate a CSV file with place names and coordinates:
1. Replace the map image (`.gif` format) with the new blank map.
2. Run the extraction script:
   ```sh
   python extract_coordinates.py
   ```
3. Click on each location in the map and enter the name of the place.
4. Type "Exit" to save the coordinates into a new CSV file.

## Dependencies
- Python 3.x
- Turtle graphics (built into Python)
- Pandas (`pip install pandas` if not already installed)

Happy learning! 🎓
