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
from PyQt5.QtCore import Qt, QThread, pyqtSignal
from PyQt5.QtGui import QFont

# Import modules created by other team members
from voice_input import VoiceRecognizer
from expert_system import get_recommendation


class SpeechWorker(QThread):
    status_signal = pyqtSignal(str)
    result_signal = pyqtSignal(str, bool)

    def run(self):
        try:
            voice_recognizer = VoiceRecognizer()

            success, result = voice_recognizer.listen(
                status_callback=lambda message: self.status_signal.emit(message)
            )

            self.result_signal.emit(result, success)

        except Exception as e:
            self.result_signal.emit(
                f"Voice recognition error: {str(e)}",
                False
            )


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Book Recommendation Expert System")
        self.setFixedSize(700, 580)

        # Text-to-speech engine
        self.tts = pyttsx3.init()

        self.speech_text = ""
        self.worker = None

        self.create_ui()

    def create_ui(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        # Main window styling
        central_widget.setStyleSheet("""
            QWidget {
                background-color: #0f172a;
                color: white;
            }
        """)

        # Title
        title = QLabel(
            "📚 Voice Book Recommendation Expert System"
        )
        title.setFont(QFont("Arial", 18, QFont.Bold))
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("color: #38bdf8;")
        layout.addWidget(title)

        # Status
        self.status = QLabel("Status: Ready")
        self.status.setAlignment(Qt.AlignCenter)
        self.status.setStyleSheet("color: #a855f7;")
        layout.addWidget(self.status)

        # Speak button
        self.speak_button = QPushButton(
            "🎙️ Speak Recommendation Request"
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

            QPushButton:disabled {
                background-color: #334155;
                color: #64748b;
            }
        """)

        self.speak_button.clicked.connect(self.start_listening)
        layout.addWidget(self.speak_button)

        # Query label
        query_label = QLabel(
            "Your Query (Speech to Text):"
        )
        query_label.setFont(QFont("Arial", 11, QFont.Bold))
        layout.addWidget(query_label)

        # Query text box
        self.query_box = QTextEdit()
        self.query_box.setReadOnly(True)
        self.query_box.setFixedHeight(70)
        layout.addWidget(self.query_box)

        # Recommendation label
        result_label = QLabel(
            "Expert System Recommendation:"
        )
        result_label.setFont(QFont("Arial", 11, QFont.Bold))
        layout.addWidget(result_label)

        # Recommendation text box
        self.result_box = QTextEdit()
        self.result_box.setReadOnly(True)
        layout.addWidget(self.result_box)

        # Replay button
        self.replay_button = QPushButton(
            "🔊 Speak Recommendation"
        )
        self.replay_button.setEnabled(False)
        self.replay_button.setFixedHeight(45)

        self.replay_button.setStyleSheet("""
            QPushButton {
                background-color: #10b981;
                color: white;
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

    def start_listening(self):
        """Start voice recognition in a background thread."""

        self.speak_button.setEnabled(False)
        self.replay_button.setEnabled(False)

        self.status.setText(
            "Status: Starting microphone..."
        )

        self.worker = SpeechWorker()

        self.worker.status_signal.connect(
            self.update_status
        )

        self.worker.result_signal.connect(
            self.process_recognized_speech
        )

        self.worker.start()

    def update_status(self, message):
        """Update the status label."""

        self.status.setText(message)

    def process_recognized_speech(self, text, success):
        """Process the recognized speech and generate a recommendation."""

        self.speak_button.setEnabled(True)

        if not success:
            self.status.setText(
                f"Status: {text}"
            )

            self.query_box.setText(
                "[No Speech / Error Detected]"
            )

            return

        # Display recognized speech
        self.query_box.setText(text)

        # Get recommendation from expert system
        book = get_recommendation(text)

        # Format recommendation
        recommendation_text = (
            f"📖 Title: {book['title']}\n"
            f"✍️ Author: {book['author']}\n"
            f"🏷️ Genre: {book['genre'].title()}\n\n"
            f"💡 Reason: {book['reason']}"
        )

        self.result_box.setText(
            recommendation_text
        )

        # Prepare text-to-speech response
        self.speech_text = (
            f"I recommend {book['title']} by "
            f"{book['author']}. {book['reason']}"
        )

        self.replay_button.setEnabled(True)

        self.status.setText(
            "Status: Ready"
        )

        # Automatically speak the recommendation
        self.speak_recommendation()

    def speak_recommendation(self):
        """Read the recommendation aloud."""

        if not self.speech_text:
            return

        self.status.setText(
            "Status: Speaking recommendation..."
        )

        QApplication.processEvents()

        try:
            self.tts.say(self.speech_text)
            self.tts.runAndWait()

            self.status.setText(
                "Status: Ready"
            )

        except Exception as e:
            self.status.setText(
                f"Status: Text-to-speech error: {str(e)}"
            )


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())