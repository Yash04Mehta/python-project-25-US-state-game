# U.S. States Guessing Game

## Project Overview

The **U.S. States Guessing Game** is an interactive Python-based geography quiz built using **Turtle Graphics** and **Pandas**.

Players guess the names of U.S. states. Each correct answer appears on its correct position on the map. If the player exits early, the program generates a list of missing states for future learning.

This project demonstrates how graphical interfaces can be combined with data processing to create engaging learning tools.

---

## Features

* Interactive map-based guessing system
* Real-time display of correctly guessed states
* Score tracking during gameplay
* Duplicate guess prevention
* Exit option to stop the game anytime
* Automatic export of missing states into a CSV file
* Uses Pandas for dataset handling and filtering

---

## 🛠️ Technologies Used

* Python
* Turtle Graphics
* Pandas
* CSV File Handling

---

## Project Structure

```
US-States-Game/
│
├── main.py
├── 50_states.csv
├── blank_states_img.gif
└── states_to_learn.csv (generated after exit)
```

---

## How the Game Works

1. The program displays a blank U.S. map.
2. The player enters the name of a state.
3. If correct:

   * The state name appears on the map
   * Score increases
4. If the player types **Exit**:

   * A CSV file is created containing missing states
   * Useful for revision practice later

---

## Learning Concepts Practiced

This project strengthens understanding of:

* Object interaction with Turtle Graphics
* Working with CSV files using Pandas
* Data filtering and lookup operations
* Lists and condition handling
* User input validation
* File generation for progress tracking

---

## Future Improvements (Optional Enhancements)

Possible upgrades:

* Timer-based challenge mode
* Hint system
* Difficulty levels
* Sound effects for correct guesses
* Leaderboard tracking
* Support for maps of other countries

---

## Learning Outcome

This project demonstrates how Python can combine **data processing + visualization + user interaction** to create educational applications.

It also builds a foundation for future GUI-based projects.

---

## Tech Stack

Python (Intermediate Level)
