# EthanTangCP2SoloProject
# Qubit Solver

# Warning:
### In the case that the user decides to alter any files, beware that adding a stage with 14 or more qubits in the "levels" dictionary of the QuantumCircut file will cause the cause the program to attempt to allocate more that 4 gigabytes of memory and put your machine in potential danger. After 14 qubits, the memory required will scale exponetially, with the memory needed calculated as: 

$$ 
\huge M = 2^{(q \cdot 2)} \cdot 16
$$

### in which q is the number of qubits in the stage and M is the memory required in bytes. At 20 qubits, the memory needed will exeed 16 terabytes. If the user plans to modify any of the stages in the application or create custom stages of their own, please keep this in mind.

## Third-Party Rescources Used:
* All UI assets where either programically generated in pygame or created in google draw
* The click sound effect was scourced from [here](https://pixabay.com/sound-effects/film-special-effects-computer-mouse-click-351398/) from pixabay, with the sound produced by "Universfield"
* The snap sound effect was scourced from [here](https://pixabay.com/sound-effects/film-special-effects-snap-fingers-fx-421174/) from pixabay, with the sound produced by "Mrstokes302"
* Everything else was created by Ethan Tang

## Needed Rescources:
* Insure that pygame and numpy is downloaded
  * Open your terminal
  * For Mac OS, input python3 -m pip install pygame-ce
  * For Windows, input python -m install pygame-ce
  * If pygame is already installed, but it is not pygame-ce, then you will need to unistall pygame and install pygame-ce
     * Mac OS: pip3 uninstall pygame
     * Windows: pip unistall pygame
  * For mac OS, input pip3 install numpy
  * For Windows, input -m pip install numpy
* If pygame and numpy is installed, then the application should be ready to be ran from either your terminal or an IDE of your choice
  * For VScode, defalt settings does not have "ExecuteInFileDir" enabled, turn it on through your settings, or the game likely wont run
 
## Description:
The Qubit Solver is an application in which the user is tasked with determining the state of a mystery qubit by using various quantum gates, other qubits that the user knows the state of and computational basis measurments for the mystery qubit. The application is designed to educate users about fundamental quantum computing concepts and gates and can be used to test intuition regarding quantum computing. 

## How to Use:
In quantum computing, there is a theorem that states that, given an unknown quantum state, it is impossible to determine its superposition, provided its state is not ket 0 or ket 1. However, there is a way around this using quantum gates, in which applying the corrrect gates in the correct order will transform the mystery state into ket 0 or ket 1, and by working backward after learning its ket state, it is possible to determine the qubit's origigal state. The purpose of this application explores this topic, in which the user has to use various gates to determine the original state of a mystery qubit |&psi;>. The application has multiple of puzzles to solve, and saves the level that user is currently on. Using the "Measure" button will give the current state of |&psi;> expressed as probabilites, and the qubits themselves can be manipulated by clicking on a quantum gate button and hovering and clicking on the quantum wire displayed. The user will only be able to place quantum gates after any existing gates, as that is the order the program will perform the computation with. Similarly, the delete button will only delete the most recent quantum gate. The user will then be able to guess the original state of the qubit using various buttons that represent different quantum states on the side of the screen. If the guess is correct, the application will automatically advance to the next stage. The game automatically saves once exiting the application and will automatically load the save. Restarting the game can be completed by using the "New" button. 

## UML:
![UML](https://github.com/9674036-code/EthanTangCP2SoloProject/blob/main/images/QubtiSolverUML.png?raw=true)

## UI From Running Application:
![UI](https://github.com/9674036-code/EthanTangCP2SoloProject/blob/main/images/QubitSolverUI.png?raw=true)
