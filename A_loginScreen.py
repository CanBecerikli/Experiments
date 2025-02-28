import sys
from PyQt5 import QtWidgets
import os
import hashlib

# The file where we store hashed usernames and passwords
DOSYA_ADI = "kullanicilar.txt"

# Function to hash passwords using SHA-256
def hash_sifre(sifre):
    return hashlib.sha256(sifre.encode()).hexdigest()

# Create the file if it doesn't exist
if not os.path.exists(DOSYA_ADI):
    with open(DOSYA_ADI, "w") as dosya:
        pass

# Login screen class
class GirisEkrani(QtWidgets.QWidget):
    def __init__(self, ana_ekran):
        super().__init__()
        self.ana_ekran = ana_ekran
        self.init_ui()

    # Initialize the user interface components
    def init_ui(self):
        self.ad = QtWidgets.QLineEdit()
        self.ad.setPlaceholderText("Username")
        self.pin = QtWidgets.QLineEdit()
        self.pin.setPlaceholderText("Password")
        self.pin.setEchoMode(QtWidgets.QLineEdit.Password)
        
        self.bas = QtWidgets.QPushButton("Login")
        self.yazi = QtWidgets.QLabel("")

        # Connect login button click event to the kontrol method
        self.bas.clicked.connect(self.kontrol)

        # Set up layout for the login screen
        v_box = QtWidgets.QVBoxLayout()
        v_box.addWidget(self.ad)
        v_box.addWidget(self.pin)
        v_box.addWidget(self.yazi)
        v_box.addWidget(self.bas)

        self.setLayout(v_box)
        self.setWindowTitle("Login Screen")
        self.setGeometry(400, 400, 300, 200)

    # Method to handle login attempt
    def kontrol(self):
        kullanici_adi = self.ad.text().strip()
        sifre = self.pin.text().strip()
        
        if not kullanici_adi or not sifre:
            self.yazi.setText("Username and password cannot be empty!")
            return
        
        hashed_sifre = hash_sifre(sifre)

        # Read the user data from the file and check if credentials match
        try:
            with open(DOSYA_ADI, "r") as dosya:
                for satir in dosya:
                    kayitli_kullanici, kayitli_sifre = satir.strip().split(":")
                    if kayitli_kullanici == kullanici_adi and kayitli_sifre == hashed_sifre:
                        self.yazi.setText("Login successful!")
                        return
            self.yazi.setText("Incorrect username or password!")
        except Exception as e:
            self.yazi.setText(f"Error reading file: {e}")

    # Override the close event to return to the main screen
    def closeEvent(self, event):
        self.ana_ekran.show()
        event.accept()

# Account creation screen class
class HesapOlustur(QtWidgets.QWidget):
    def __init__(self, ana_ekran):
        super().__init__()
        self.ana_ekran = ana_ekran
        self.init_ui()

    # Initialize the user interface components
    def init_ui(self):
        self.ad = QtWidgets.QLineEdit()
        self.ad.setPlaceholderText("Username")
        self.pin = QtWidgets.QLineEdit()
        self.pin.setPlaceholderText("Password")
        self.pin.setEchoMode(QtWidgets.QLineEdit.Password)
        
        self.bas = QtWidgets.QPushButton("Create Account")
        self.yazi = QtWidgets.QLabel("")

        # Connect account creation button click event to the olustur method
        self.bas.clicked.connect(self.olustur)

        # Set up layout for the account creation screen
        v_box = QtWidgets.QVBoxLayout()
        v_box.addWidget(self.ad)
        v_box.addWidget(self.pin)
        v_box.addWidget(self.yazi)
        v_box.addWidget(self.bas)

        self.setLayout(v_box)
        self.setWindowTitle("Create Account")
        self.setGeometry(400, 400, 300, 200)

    # Override the close event to return to the main screen
    def closeEvent(self, event):
        self.ana_ekran.show()
        event.accept()

    # Method to handle account creation
    def olustur(self):
        kullanici_adi = self.ad.text().strip()
        sifre = self.pin.text().strip()
        
        if not kullanici_adi or not sifre:
            self.yazi.setText("Username and password cannot be empty!")
            return
        
        # Check if the username already exists
        with open(DOSYA_ADI, "r") as dosya:
            for satir in dosya:
                if satir.strip().split(":")[0] == kullanici_adi:
                    self.yazi.setText("This username is already taken!")
                    return
        
        hashed_sifre = hash_sifre(sifre)
        try:
            # Save the new user to the file with hashed password
            with open(DOSYA_ADI, "a") as dosya:
                dosya.write(f"{kullanici_adi}:{hashed_sifre}\n")
            self.yazi.setText("Account created successfully!")
        except Exception as e:
            self.yazi.setText(f"Error saving user: {e}")

# Main screen class
class AnaEkran(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    # Initialize the user interface components
    def init_ui(self):
        self.ya = QtWidgets.QLabel("What do you want to do? Bra") # I am not your bra... I am Tayler Durden
        self.gir = QtWidgets.QPushButton("Login")
        self.ol = QtWidgets.QPushButton("Create Account")

        # Set up layout for the main screen
        v_box = QtWidgets.QVBoxLayout()
        v_box.addWidget(self.ya)
        v_box.addWidget(self.gir)
        v_box.addWidget(self.ol)

        self.setLayout(v_box)
        self.setWindowTitle("Main Screen")
        self.setGeometry(300, 300, 400, 300)

        # Connect buttons to their corresponding actions
        self.gir.clicked.connect(self.giris_ekranini_ac)
        self.ol.clicked.connect(self.hesap_olustur)

    # Open the login screen
    def giris_ekranini_ac(self):
        self.giris_penceresi = GirisEkrani(self)
        self.giris_penceresi.show()
        self.hide()

    # Open the account creation screen
    def hesap_olustur(self):
        self.hesap_penceresi = HesapOlustur(self)
        self.hesap_penceresi.show()
        self.hide()

# Main entry point for the application
def main():
    app = QtWidgets.QApplication(sys.argv)
    ana_pencere = AnaEkran()
    ana_pencere.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()