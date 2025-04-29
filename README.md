
# 🍎 Fruit Identifier

A deep learning-powered application designed to detect 6 types of fruit in an uploaded image: apple, avocado, banana, kiwi, lemon, and orange. Leveraging a hand-crafted Convolutional Neural Network model, this project aims to demonstrate image identification of objects.

---

## 🚀 Features

- **Multi-Class Classification**: Predicts one of six possible fruits classes.
- **Pre-trained Model**: Utilizes a custom Convolutional Neural Network saved as model.h5.
- **Simple Interface**: Accepts user input through a simple graphical user interface.
- **Lightweight Deployment**: Runs as a streamlit application locally.

---

## 🧠 How It Works

The application loads a pre-trained CNN model and prompts the user to upload an image of a fruit. It then processes the image through the model to predict the type of fruit.

---

## 📁 Project Structure

```
fruit-identifier/
├── model.h5                     # Trained ML model
├── fruit-identifier.py          # Main application script
├── requirements.txt             # Python dependencies
└── README.md                    # Project documentation
```

---

## 🛠️ Getting Started

### Prerequisites

- Python 3.8 or higher
- pip package manager

### Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/JAl-Hassani/fruit-identifier.git
   cd fruit-identifier
   ```

2. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Application**:

   ```bash
   streamlit run fruit-identifier.py
   ```

---

## 📦 Dependencies

- `streamlit`
- `tensorflow`
- `keras`
- `scikit-learn`

*(Refer to `requirements.txt` for the complete list.)*

---

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## 🙋‍♂️ Author

- **JAl-Hassani** – [GitHub Profile](https://github.com/JAl-Hassani)
