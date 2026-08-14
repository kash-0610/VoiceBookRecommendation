import speech_recognition as sr


class VoiceRecognizer:
    def __init__(self):
        self.recognizer = sr.Recognizer()

    def listen(self, status_callback=None):
        """
        Listens to microphone input and converts it to text.

        Returns:
            tuple: (success: bool, text_or_error_message: str)
        """

        if status_callback:
            status_callback(
                "Status: Listening... Please speak into microphone."
            )

        try:
            with sr.Microphone() as source:
                # Adjust microphone sensitivity to surrounding noise
                self.recognizer.adjust_for_ambient_noise(
                    source,
                    duration=1
                )

                # Listen for up to 5 seconds for speech to begin,
                # and limit each phrase to 10 seconds.
                audio = self.recognizer.listen(
                    source,
                    timeout=5,
                    phrase_time_limit=10
                )

            if status_callback:
                status_callback("Status: Processing audio...")

            # Convert speech to text using Google's speech recognition service
            text = self.recognizer.recognize_google(audio)

            return True, text

        except sr.WaitTimeoutError:
            return False, "Listening timed out. No speech detected."

        except sr.UnknownValueError:
            return False, "Could not understand audio. Please speak again."

        except sr.RequestError:
            return False, "Speech recognition service is unavailable."

        except Exception as e:
            return False, f"Microphone/Audio Error: {str(e)}"