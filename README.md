# 📚 Voice-Based Book Recommendation Expert System

> 🎙️ A voice-powered rule-based expert system that helps users discover books through natural speech.

**Voice-Based Book Recommendation Expert System** is a Python desktop application that makes finding a book more interactive. Instead of typing a search query, users can simply speak into the microphone and describe the type of book they are looking for.

The system listens to the user's request, identifies relevant information such as the **genre or author**, and uses a **Rule-Based Expert System** to recommend a suitable book from its knowledge base. The recommendation is then displayed on the screen and read aloud using **Text-to-Speech**.

We are a team of four **second-year Artificial Intelligence and Data Science (AIDS) engineering students**, and this project was developed as part of our coursework.

---

## 🚀 Features

- 🎙️ **Voice Input**  
  Click the microphone button and simply speak your book request. The application converts your speech into text.

- 🧠 **Rule-Based Expert System**  
  The system uses predefined rules and keywords to identify genres such as Sci-Fi, Horror, Fantasy, Mystery, and Romance. It can also recognize author names.

- 📚 **15-Book Knowledge Base**  
  The system contains a collection of 15 books across five different genres, along with information about their authors and reasons for recommendation.

- 🔊 **Text-to-Speech**  
  Once a book is recommended, the application automatically reads the recommendation aloud. Users can also replay it whenever they want.

- 🎨 **Dark-Mode User Interface**  
  The interface is designed using PyQt5 with a simple and modern dark theme.

- 🧩 **Modular Architecture**  
  The project is divided into separate Python modules, making the code easier to understand, maintain, and develop as a team.

---

## 🛠️ Technologies Used

The project was built using the following technologies:

| Technology | Purpose |
|---|---|
| **Python** | Main programming language |
| **PyQt5** | Graphical User Interface |
| **SpeechRecognition** | Converts speech into text |
| **PyAudio** | Captures microphone input |
| **pyttsx3** | Converts text into speech |
| **Rule-Based Expert System** | Analyzes user input and selects recommendations |

---

## 👥 Team & Project Structure

Since this was a team project, we divided the application into separate modules. This allowed each team member to work on a specific part of the system while keeping the overall project organized.

| File | Responsible Member | Purpose |
|---|---|---|
| `voice_input.py` | Member 1 | Captures microphone input and converts speech into text. |
| `database.py` | Member 2 | Contains the 15-book knowledge base and book information. |
| `expert_system.py` | Member 3 | Analyzes the user's request and finds a suitable book recommendation. |
| `ui_main.py` | Member 4 | Creates the PyQt5 interface, connects the different modules, and handles Text-to-Speech. |

---

## 🧠 How the System Works

The application follows a simple step-by-step process:

```text
🎙️ User speaks
       ↓
🗣️ Speech-to-Text
       ↓
🔍 Keyword / Author Detection
       ↓
🧠 Rule-Based Expert System
       ↓
📚 Book Recommendation
       ↓
🔊 Text-to-Speech
````

### Example

If the user says:

> "Can you recommend me a fantasy book?"

The system identifies **"fantasy"** as the relevant keyword and searches the knowledge base for a fantasy book.

It then displays information such as:

```text
📖 Title: The Hobbit
✍️ Author: J.R.R. Tolkien
🏷️ Genre: Fantasy
💡 Reason: An iconic fantasy quest featuring magic, dragons, and epic journeys.
```

The recommendation is also spoken aloud using the Text-to-Speech feature.

---

## 📚 Book Genres

The current knowledge base contains books from five genres:

* 🚀 **Sci-Fi**
* 👻 **Horror**
* 🧙 **Fantasy**
* 🔎 **Mystery**
* ❤️ **Romance**

There are currently **15 books** in total, with three books representing each genre.

---

## 💡 Example Requests

You can try requests such as:

```text
"I want a fantasy book."
```

```text
"Recommend me a horror novel."
```

```text
"I am looking for a mystery book."
```

```text
"Recommend a book by Andy Weir."
```

```text
"I would like a romance novel."
```

The system looks for relevant keywords or author names in the user's request and uses them to find a suitable book.

---

## 🎯 Project Objective

The main objective of this project is to demonstrate how a **Rule-Based Expert System** can be combined with voice technology and a graphical user interface to create a simple recommendation system.

The project brings together several concepts, including:

* Speech recognition
* Keyword-based reasoning
* Knowledge bases
* Rule-based decision making
* Graphical user interfaces
* Text-to-speech

Rather than using machine learning or a large AI model, our recommendation logic is based on **predefined rules and keywords**. This makes the reasoning process simple, transparent, and easy to understand.

---

## 🛠️ Requirements

Before running the project, make sure you have:

* **Python 3.8 or newer**
* A working **microphone**
* Internet access for Google Speech Recognition
* The required Python libraries

---

## 📦 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/VoiceBookRecommendation.git
```

Then move into the project folder:

```bash
cd VoiceBookRecommendation
```

> Replace `your-username` with your GitHub username.

### 2. Check Your Python Version

Open a terminal or Command Prompt and run:

```bash
python --version
```

You should have Python 3.8 or a newer version.

### 3. Install the Required Libraries

Run:

```bash
pip install PyQt5 SpeechRecognition pyttsx3 pyaudio
```

### Note About PyAudio

On some operating systems, installing `PyAudio` may require additional setup. If `pip install pyaudio` does not work, check the installation instructions for your operating system.

---

## ▶️ Running the Application

Make sure the project files are organized like this:

```text
VoiceBookRecommendation/
│
├── voice_input.py
├── database.py
├── expert_system.py
└── ui_main.py
```

Then run the application using:

```bash
python ui_main.py
```

The application window should open.

Click the **🎙️ Speak Recommendation Request** button and speak into your microphone.

For example:

> "I want a science fiction book."

The system will process your request, display a recommendation, and read the recommendation aloud.

---

## 🔮 Future Improvements

There are several ways we would like to improve the project in the future:

* 📚 Expand the book database with more titles and genres.
* 🎯 Support multiple preferences in a single request.
* ⭐ Add book ratings and reviews.
* 🧠 Improve natural-language understanding.
* ⌨️ Add a text-based input option along with voice input.
* 📖 Provide more than one recommendation when appropriate.
* 👤 Add personalized recommendations based on user preferences or reading history.
* 🌐 Explore additional speech recognition services and offline speech recognition.

---

## 📌 Limitations

This project was developed primarily for coursework and demonstration purposes.

The current system has a relatively small knowledge base of 15 books and relies on predefined keywords and rules. Because of this, it may not understand every possible way a user could describe their preferences.

For example, a complex request containing multiple genres, authors, or very specific preferences may not always produce the most suitable recommendation.

Despite these limitations, the project demonstrates the basic working principles of a **voice-enabled Rule-Based Expert System**.

---

## 🎓 Academic Project

This project was created as part of our coursework as **second-year Artificial Intelligence and Data Science (AIDS) engineering students**.

The project gave us an opportunity to work with:

* Python programming
* Expert systems
* Speech recognition
* GUI development
* Text-to-speech
* Modular software design
* Team-based development

---

## 👋 Conclusion

Building this project gave us practical experience in combining different technologies to create a complete desktop application.

Our goal was to keep the recommendation process simple and understandable while making the interaction more engaging through voice input and speech output.

Thank you for checking out our project! 📚🎙️

We hope you enjoy trying out the **Voice-Based Book Recommendation Expert System**.