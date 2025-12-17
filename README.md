# 📧 Email Spam/Ham Detection ML

### An end-to-end machine learning project that classifies emails as **Spam** or **Ham** using Logistic Regression and Flask, with a responsive CSS frontend.

---

## 🚀 Live Demo

Try it online: [Email Spam/Ham Detection ML](https://email-spam-detection-ml-yi4o.onrender.com)

---

## 🛠 Technologies Used

* **Programming Language:** Python
* **Machine Learning:** Scikit-learn (Logistic Regression), CountVectorizer
* **Web Framework:** Flask
* **Frontend:** HTML, CSS
* **Deployment:** Render (Free hosting)
* **Data:** Email dataset (`email.csv`)

---

## 💡 Features

* Classifies emails as **Spam** or **Ham**
* Converts email text to numeric features using **CountVectorizer**
* **High accuracy** of 98.3%
* Clean, responsive web interface
* Fully deployed online for public use

---

## 📂 Project Structure

```
email-spam-detection-ml/
├── app.py 📝 Flask application
├── spam_model.pkl 📦 Trained ML model
├── vectorizer.pkl 📦 Saved CountVectorizer
├── requirements.txt 📄 Python dependencies
├── templates/ 📁 HTML templates
│   └── index.html 🖥️ Frontend page
├── static/ 📁 Static assets
│   └── style.css 🎨 CSS styling
└── email.csv 📊 Sample email dataset
```

---

## ⚡ Installation & Local Setup

### 1️⃣ Clone the repository

```bash
git clone https://github.com/PavanSurisetti/email-spam-detection-ml.git
```

### 2️⃣ Navigate into the project folder

```bash
cd email-spam-detection-ml
```

### 3️⃣ Install required dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run the Flask application

```bash
python app.py
```

### 5️⃣ Open your browser

```
http://127.0.0.1:10000
```

---

## 🧠 How It Works

1. User enters an email message.
2. Flask loads the trained ML model and vectorizer.
3. The email is converted into numeric form.
4. The model predicts **Spam** or **Ham**.
5. Result is displayed on the webpage.

---

## 🚀 Future Improvements

* Use TF-IDF vectorization
* Display prediction confidence
* Multi-language email support
* Store prediction history

---

## 📫 Contact

* **GitHub:** [https://github.com/PavanSurisetti](https://github.com/PavanSurisetti)
* **LinkedIn:** [https://www.linkedin.com/in/pavan-surisetti-b3281228b/](https://www.linkedin.com/in/pavan-surisetti-b3281228b/)

---

## 📄 License

This project is licensed under the **MIT License**.
