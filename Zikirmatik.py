import sys
from PyQt5 import QtWidgets
import random


zikirler = [
    "Subhanallah", "Elhamdülillah", "Allahu Ekber", "La ilahe illallah",
    "La havle vela kuvvete illa billah", "Astaghfirullah",
    "Sübhanallah ve bihamdihi", "Sübhanallahil azim",
]

zikir = 0  # Initial zikr counter
a = 33  # Initial zikr interval

def main():
    """
    The main function is the starting point of the application.
    It creates and runs the PyQt5 application, sets up the GUI, and starts it.
    """
    app = QtWidgets.QApplication(sys.argv)  # Creating the application

    h_box = QtWidgets.QHBoxLayout()  # Horizontal layout
    v_box = QtWidgets.QVBoxLayout()  # Vertical layout

    # Zikir button
    ziku = QtWidgets.QPushButton("ZİKİR ÇEK")

    # Initial message label
    za = QtWidgets.QLabel("Henüz zikrin yok ya ümmeti muhammet")

    # Layout the message and button
    v_box.addStretch()  # Vertical stretch space
    v_box.addWidget(za)  # Adding message label
    v_box.addStretch()  # Vertical stretch space
    v_box.addWidget(ziku)  # Adding the zikir button

    # Adding vertical layout to the horizontal layout
    h_box.addStretch()  # Horizontal stretch space
    h_box.addLayout(v_box)  # Adding the vertical layout
    h_box.addStretch()  # Horizontal stretch space

    # Setting up the main window
    pencere = QtWidgets.QWidget()
    pencere.setWindowTitle("ZİKİRMATİK")  # Window title
    pencere.setLayout(h_box)  # Applying the layout
    pencere.show()  # Showing the window
    pencere.setGeometry(100, 100, 500, 500)  # Setting the window size

    # Connecting the button click to the zikir_cek function
    ziku.clicked.connect(lambda: zikir_cek(za))

    # Running the application
    sys.exit(app.exec_())

def zikir_cek(za):
    """
    Zikir function, called when the button is clicked.
    It increments the zikr count and updates the label text.
    """
    global zikir, a  # Using global variables for zikr counter and 'a'
    zikir += 1  # Increment the zikr count

    if zikir == a:
        # If the zikr count reaches 'a', show a random zikr from the list
        za.setText("{}".format(random.choice(zikirler)))
        a += 33  # Increase the target number of zikr for the next time
    else:
        # Display the current zikr count
        za.setText("Maşaallah, Tam {} defa zikir çektin ".format(zikir))

    # If the zikr count reaches 1000, show a special message
    if zikir == 1000:
        za.setText("Birader sen allahın bir lütfu musun ya 1000 defa zikir çektin")
    
    # If the zikr count reaches 10000, show another special message
    if zikir == 10000:
        za.setText("Vallahi sana diyecek hiçbir şeyim yok cennetlik adam")

if __name__ == "__main__":
    main()  # Starting the program
