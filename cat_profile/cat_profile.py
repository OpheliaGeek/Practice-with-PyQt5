import sys
from PyQt5.QtWidgets import QApplication, QLabel, QWidget
from PyQt5.QtGui import QFont, QPixmap


class CatProfile(QWidget):
    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        """
        Initialize the window and display its contents to the screen.
        """
        self.setGeometry(250, 250, 600, 300)
        self.setWindowTitle("Ragdoll cat profile")
        self.setStyleSheet("background-color: #EAE0DA")
        self.displayImages()
        self.displayUserInfo()
        self.show()

    def displayImages(self):
        """
        Display profile images.
        Check to see if image files exist, if not throw an exception.
        """
        profile_image = "images\\ragdoll_small.png"
        try:
            with open(profile_image):
                user_image = QLabel(self)
                pixmap = QPixmap(profile_image)
                user_image.setPixmap(pixmap)
                user_image.move(375, 60)
        except FileNotFoundError:
            print("Image not found.")

    def displayUserInfo(self):
        """
        Create the labels to be displayed for the Profile.
        """
        user_name = QLabel(self)
        user_name.setText("Ragdoll cat")
        user_name.move(185, 20)
        user_name.setFont(QFont('Arial', 20))

        bio_title = QLabel(self)
        bio_title.setText("Overview")
        bio_title.move(15, 60)
        bio_title.setFont(QFont('Arial', 15))

        about = QLabel(self)
        about.setText("Ragdoll cats are beautiful and powerful felines. This kitty is a highly sought-after companion. Though poised and regal, Ragdoll cats are extremely loving and playful. You'll find your Ragdoll following you around and wanting to spend time anywhere they can keep an eye on you. (A trait we totally love.)")
        about.setWordWrap(True)
        about.setMaximumWidth(350)
        about.move(15, 90)

        personality_title = QLabel(self)
        personality_title.setText("Personality\r")
        personality_title.move(15, 170)
        personality_title.setFont(QFont('Arial', 15))

        personality = QLabel(self)
        personality.setText("Loving | Laid-back | Sweet ")
        personality.move(15, 200)

        coat_title = QLabel(self)
        coat_title.setText("Coat & colors\r")
        coat_title.move(15, 230)
        coat_title.setFont(QFont('Arial', 15))

        coat = QLabel(self)
        coat.setText("Long | Silky | White & colorpoint")
        coat.move(15, 260)


# Run program
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = CatProfile()
    sys.exit(app.exec_())
