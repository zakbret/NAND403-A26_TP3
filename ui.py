from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QSpinBox, QGroupBox, QGridLayout, QHBoxLayout 


class RandomAnimatorGenerator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("outliner organiser")
        self.resize(500, 100)
        self.create_ui()

    def add_spinbox(self, grille, nom, ligne, colonne, minimum, maximum):
        label = QLabel(nom)
        spin = QSpinBox()
        spin.setRange(minimum, maximum)
        spin.setValue(0)
        
        bloc = QHBoxLayout()
        bloc.addWidget(label)
        bloc.addWidget(spin)
        
        grille.addLayout(bloc, ligne, colonne)
        return spin

  

    def create_ui(self):
        self.translate_parameters = QGroupBox("Translate Parameters")
        grille = QGridLayout()
        self.translate_parameters.setLayout(grille)

        self.t_min_x = self.add_spinbox(grille, "min x:", 0, 0, -500, 500)
        self.t_min_y = self.add_spinbox(grille, "min y:", 0, 1, -500, 500)
        self.t_min_z = self.add_spinbox(grille, "min z:", 0, 2, -500, 500)
        self.t_max_x = self.add_spinbox(grille, "max x:", 1, 0, -500, 500)
        self.t_max_y = self.add_spinbox(grille, "max y:", 1, 1, -500, 500)
        self.t_max_z = self.add_spinbox(grille, "max z:", 1, 2, -500, 500)

        


        

        self.layout = QVBoxLayout(self)
        self.layout.addWidget(self.translate_parameters)
        
