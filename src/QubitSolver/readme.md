# Phase I Development Progress:
* Created Main file, Atom, Electron, Nucleus, Button and Molecule classes
* The Main File is the engine that will run the simulation, the atom class will store information about the atom as well as perform calculations regarding its behavior, the electron and nucleus classes are support classes for the Atom class by dividing the atom into individual units that will store information and perform more specialized calculations, the Button class will provide the buttons for the UI and user interactivity of the simulation and the Molecule class will extend the atom class, stores extra information such as bond angles perform extra calculations, although it is treated like an atom.
* For now, the game can render a black background as well as one hydrogen atom through a basic loop that retrives the position of an instantiation of the atom class and draws it onto the screen
## Next tasks:
* create more robust structure to avoid minimum hard-coding
* expand on atom class to have rudimentary interactions between instances of atoms
* finish button class to allow for user to control the simulation
