import sys
import serial
from PyQt5.QtWidgets import (
    QApplication, QWidget, QPushButton, QLabel, QVBoxLayout,
    QHBoxLayout, QFrame
)
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QPixmap, QTransform, QPainter, QColor, QFont

# Serial haberleşme başlat
try:
    ser = serial.Serial('COM4', 9600, timeout=1)
    print("[INFO] Serial bağlantısı kuruldu (COM4)")
except Exception as e:
    ser = None
    print(f"[ERROR] Serial bağlantı hatası: {e}")

def send_serial(data):
    if ser and ser.is_open:
        ser.write((data + "\n").encode())
        print(f"[TX] {data}")


class LedCircle(QLabel):
    def __init__(self):
        super().__init__()
        self.setFixedSize(100, 100)
        self.setStyleSheet("border-radius: 50px; background-color: black;")
        self.is_on = False

    def toggle(self):
        self.is_on = not self.is_on
        color = "#00ff00" if self.is_on else "black"
        self.setStyleSheet(f"border-radius: 50px; background-color: {color};")

    def state(self):
        return "1" if self.is_on else "0"


class MotorWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.angle = 0
        self.direction = None

        self.bar_pixmap = QPixmap(14, 80)
        self.bar_pixmap.fill(Qt.transparent)
        painter = QPainter(self.bar_pixmap)
        painter.fillRect(0, 0, 14, 80, QColor("#007BFF"))
        painter.end()

        self.label = QLabel()
        self.label.setFixedSize(120, 120)
        self.label.setAlignment(Qt.AlignCenter)

        self.timer = QTimer()
        self.timer.timeout.connect(self.rotate)

        self.left_btn = QPushButton("← Sol")
        self.right_btn = QPushButton("Sağ →")
        self.style_button(self.left_btn)
        self.style_button(self.right_btn)

        self.left_btn.clicked.connect(self.turn_left)
        self.right_btn.clicked.connect(self.turn_right)

        layout = QVBoxLayout()
        layout.addWidget(self.label, alignment=Qt.AlignCenter)
        layout.addWidget(self.left_btn)
        layout.addWidget(self.right_btn)
        self.setLayout(layout)

        self.update_bar()

    def style_button(self, btn):
        btn.setFixedSize(100, 40)
        btn.setStyleSheet("""
            QPushButton {
                background-color: #007BFF;
                color: white;
                border-radius: 10px;
                font-weight: bold;
                font-size: 14px;
            }
            QPushButton:hover {
                background-color: #3399FF;
            }
        """)

    def rotate(self):
        if self.direction == 'right':
            self.angle += 10
        elif self.direction == 'left':
            self.angle -= 10
        self.update_bar()

    def update_bar(self):
        transform = QTransform()
        transform.translate(self.bar_pixmap.width()/2, self.bar_pixmap.height()/2)
        transform.rotate(self.angle)
        transform.translate(-self.bar_pixmap.width()/2, -self.bar_pixmap.height()/2)
        rotated = self.bar_pixmap.transformed(transform, Qt.SmoothTransformation)

        canvas = QPixmap(self.label.size())
        canvas.fill(Qt.transparent)
        painter = QPainter(canvas)
        x = int((canvas.width() - rotated.width()) / 2)
        y = int((canvas.height() - rotated.height()) / 2)
        painter.drawPixmap(x, y, rotated)
        painter.end()

        self.label.setPixmap(canvas)

    def turn_left(self):
        if self.direction == 'left':
            self.stop()
        else:
            self.direction = 'left'
            self.timer.start(50)
            send_serial("m,1,0")

    def turn_right(self):
        if self.direction == 'right':
            self.stop()
        else:
            self.direction = 'right'
            self.timer.start(50)
            send_serial("m,0,1")

    def stop(self):
        self.direction = None
        self.timer.stop()
        send_serial("m,0,0")


class LedControlUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Arduino Kontrol Paneli")
        self.setStyleSheet("background-color: #fafafa;")
        self.initUI()

    def initUI(self):
        main_layout = QHBoxLayout()

        self.leds = []
        led_panel = QHBoxLayout()
        for i in range(4):
            vbox = QVBoxLayout()
            led = LedCircle()
            button = QPushButton(f"LED {i+1}")
            button.setFixedSize(100, 40)
            button.setStyleSheet("""
                QPushButton {
                    background-color: #28a745;
                    color: white;
                    border-radius: 10px;
                    font-weight: bold;
                    font-size: 14px;
                }
                QPushButton:hover {
                    background-color: #43c162;
                }
            """)
            button.clicked.connect(lambda _, l=led: self.toggle_led(l))
            vbox.addWidget(led, alignment=Qt.AlignCenter)
            vbox.addWidget(button, alignment=Qt.AlignCenter)
            led_panel.addLayout(vbox)
            self.leds.append(led)

        self.motor_widget = MotorWidget()

        main_layout.addLayout(led_panel)
        line = QFrame()
        line.setFrameShape(QFrame.VLine)
        line.setFrameShadow(QFrame.Sunken)
        main_layout.addWidget(line)
        main_layout.addWidget(self.motor_widget)

        self.setLayout(main_layout)
        self.setFixedSize(850, 350)

    def toggle_led(self, led):
        led.toggle()
        state_str = ",".join([l.state() for l in self.leds])
        send_serial(f"l,{state_str}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LedControlUI()
    window.show()
    sys.exit(app.exec_())
