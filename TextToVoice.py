import sys
import pyttsx3
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QLabel,
    QPushButton,
    QTextEdit
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
# ==========================================
# Temporary Expert System
# ==========================================
def expert_system():

    # Temporary voice-to-text result
    user_query = (
        "I am looking for a thrilling science fiction "
        "book with space exploration."
    )

    # Temporary book recommendation
    book = {
        "title": "Project Hail Mary",
        "author": "Andy Weir",
        "genre": "Sci-Fi / Space Exploration",
        "reason": (
            "It matches your interest in science fiction, "
            "space exploration, survival, and problem-solving."
        )
    }

    return user_query, book
# ==========================================
# Main Window
# ==========================================
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Book Recommendation Expert System")
        self.setFixedSize(700, 550)

        # Text-to-Speech
        self.tts = pyttsx3.init()

        # Stores the text that will be spoken
        self.speech_text = ""

        self.create_ui()
    # ======================================
    # Create User Interface
    # ======================================
    def create_ui(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout()
        layout.setSpacing(12)
        layout.setContentsMargins(25, 25, 25, 25)
        central_widget.setLayout(layout)
        # Window background
        central_widget.setStyleSheet("""
            QWidget {
                background-color: #0f172a;
                color: white;
            }
            QTextEdit {
                background-color: #1e293b;
                color: #f8fafc;
                border: 1px solid #334155;
                border-radius: 8px;
                padding: 8px;
                font-size: 14px;
            }
        """)
        # ==================================
        # Title
        # ==================================
        title = QLabel("📚 Book Recommendation Expert System")
        title.setFont(
            QFont("Arial", 20, QFont.Bold)
        )
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet(
            "color: #38bdf8;"
        )
        layout.addWidget(title)
        # ==================================
        # Status
        # ==================================
        self.status = QLabel("Status: Ready")
        self.status.setAlignment(Qt.AlignCenter)
        self.status.setStyleSheet(
            "color: #a855f7; font-size: 12px;"
        )
        layout.addWidget(self.status)
        # ==================================
        # Recommendation Button
        # ==================================
        self.speak_button = QPushButton(
            "🎙️ Get Book Recommendation"
        )
        self.speak_button.setFixedHeight(50)
        self.speak_button.setStyleSheet("""
            QPushButton {
                background-color: #0284c7;
                color: white;
                font-size: 15px;
                font-weight: bold;
                border-radius: 10px;
            }
            QPushButton:hover {
                background-color: #0369a1;
            }
            QPushButton:pressed {
                background-color: #075985;
            }
        """)
        self.speak_button.clicked.connect(
            self.get_recommendation
        )
        layout.addWidget(self.speak_button)
        # ==================================
        # User Query
        # ==================================
        query_label = QLabel("Your Query:")
        query_label.setFont(
            QFont("Arial", 12, QFont.Bold)
        )
        layout.addWidget(query_label)
        self.query_box = QTextEdit()
        self.query_box.setReadOnly(True)
        self.query_box.setFixedHeight(70)
        layout.addWidget(self.query_box)
        # ==================================
        # Recommendation
        # ==================================
        result_label = QLabel(
            "Expert System Recommendation:"
        )
        result_label.setFont(
            QFont("Arial", 12, QFont.Bold)
        )
        layout.addWidget(result_label)
        self.result_box = QTextEdit()
        self.result_box.setReadOnly(True)
        layout.addWidget(self.result_box)
        # ==================================
        # Replay Button
        # ==================================
        self.replay_button = QPushButton(
            "🔊 Speak Recommendation"
        )
        self.replay_button.setEnabled(False)
        self.replay_button.setFixedHeight(45)
        self.replay_button.setStyleSheet("""
            QPushButton {
                background-color: #10b981;
                color: white;
                font-size: 13px;
                font-weight: bold;
                border-radius: 8px;
            }
            QPushButton:hover {
                background-color: #059669;
            }
            QPushButton:disabled {
                background-color: #334155;
                color: #64748b;
            }
        """)
        self.replay_button.clicked.connect(
            self.speak_recommendation
        )
        layout.addWidget(self.replay_button)
        # ======================================
        # Get Recommendation
        # ======================================
        def get_recommendation(self):
            self.status.setText(
            "Status: Processing..."
        )
            # Run the expert system
        query, book = expert_system()
        # Display user's query
        self.query_box.setText(query)
        # Create recommendation text
        recommendation = (
            f"📖 Title: {book['title']}\n"
            f"✍️ Author: {book['author']}\n"
            f"🏷️ Genre: {book['genre']}\n\n"
            f"💡 Why: {book['reason']}"
        )

        self.result_box.setText(
            recommendation
        )
        # Text that will be spoken
        self.speech_text = (
            f"I recommend {book['title']} "
            f"by {book['author']}. "
            f"{book['reason']}"
        )
        # Enable replay button
        self.replay_button.setEnabled(True)
        # Automatically speak recommendation
        self.speak_recommendation()
        # ======================================
        # Text-to-Speech
        # ======================================
    def speak_recommendation(self):
        if not self.speech_text:
            return
        self.status.setText(
            "Status: Speaking..."
        )
        self.tts.say(
            self.speech_text
        )
        self.tts.runAndWait()
        self.status.setText(
            "Status: Ready"
        )
# ==========================================
# Start Application
# ==========================================
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())