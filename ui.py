from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QSpinBox, QGroupBox, QGridLayout, QHBoxLayout 

import importlib
import animator
importlib.reload(animator)

class RandomAnimatorGenerator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Random Animation Generator")
        self.resize(500, 100)
        self.create_ui()

    def add_spinbox(self, grille, nom, ligne, colonne, minimum, maximum, base_value):
        label = QLabel(nom)
        spin = QSpinBox()
        spin.setRange(minimum, maximum)
        spin.setValue(base_value)
        bloc = QHBoxLayout()

        #add the spinbox and the label to the box
        bloc.addWidget(label)
        bloc.addWidget(spin)

        #add stretch so the spinbox stay near the label
        bloc.addStretch()

        #add the bloc in the right place (ligne, colonne)
        grille.addLayout(bloc, ligne, colonne)
        return spin

    def create_group(self, titre, minimum, maximum, base_value_min, base_value_max):
        groupe = QGroupBox(titre)
        grille = QGridLayout()

        #use the grid for the group layout
        groupe.setLayout(grille)
        spins = {}
        self.axes = ["X", "Y", "Z"]

        #for all the axes 
        for number, axe in enumerate(self.axes):
            #create a string with the right axe
            min_name = "min " + axe + " :"
            max_name = "max " + axe + " :"

            #create the spin box for the min value
            spin_min = self.add_spinbox(grille, min_name, 0, number, minimum, maximum, base_value_min)
            #store each spinbox in the spins dictionary, with a key based on its axis and min/max
            spins["min_" + axe] = spin_min
            #create the spin box for the max value
            spin_max = self.add_spinbox(grille, max_name, 1, number, minimum, maximum, base_value_max)
            #store each spinbox in the spins dictionary, with a key based on its axis and min/max
            spins["max_" + axe] = spin_max

        return groupe, spins

    def create_ui(self):
        #create the group for the animation timing
        self.animation_timing = QGroupBox("Animation Timing")
        grille_a = QGridLayout()
        self.animation_timing.setLayout(grille_a)

        #create the two spinbox for animation timing
        self.duration_frame = self.add_spinbox(grille_a, "Duration (frames):", 0, 0, 1, 1000, 100)
        self.step_frame = self.add_spinbox(grille_a, "Step (frames):", 0, 1, 1, 1000, 10)

        #create the 3 other groups, first value is the group and second value is the spinbox values
        self.translate_parameters, self.translate_spins = self.create_group("Translate Parameters", -500, 500, -10, 10)
        self.rotate_parameters, self.rotate_spins = self.create_group("Rotate Parameters", -180, 180, -10, 10)
        self.scale_parameters, self.scale_spins = self.create_group("Scale Parameters", 1, 500, 1, 5)

        #create the button and link it to the animation value fonction
        self.bouton_generate = QPushButton("Generate")
        self.bouton_generate.clicked.connect(self.on_click_generate)

        #add all the groups and the button to the layout
        self.main_layout = QVBoxLayout(self)
        self.main_layout.addWidget(self.animation_timing)
        self.main_layout.addWidget(self.translate_parameters)
        self.main_layout.addWidget(self.rotate_parameters)
        self.main_layout.addWidget(self.scale_parameters)
        self.main_layout.addWidget(self.bouton_generate)

    #get the value from the spinbox ine the groups
    def get_spin_values(self, spins, prefixe):
        value_list = []
        #for all the axe in the axes list
        for axe in self.axes:
            #add the value from dictionnary key (combination of the prefix(min/max) and the axe)
            value_list.append(spins[prefixe + axe].value())

        return value_list


    #send the values to the animator.py
    def on_click_generate(self):
        animator.animate(
        number_of_frame=self.duration_frame.value(),
        step_of_frame=self.step_frame.value(),
        translate_min=self.get_spin_values(self.translate_spins, "min_"),
        translate_max=self.get_spin_values(self.translate_spins, "max_"),
        rotate_min=self.get_spin_values(self.rotate_spins, "min_"),
        rotate_max=self.get_spin_values(self.rotate_spins, "max_"),
        scale_min=self.get_spin_values(self.scale_spins, "min_"),
        scale_max=self.get_spin_values(self.scale_spins, "max_"),
        axes=self.axes
        )
