# 🛡️ PhishGuard AI

AI-powered phishing detection system built using **Python, Machine Learning, and Rule-Based Security Engine** to identify malicious URLs in real-time.

---

## 🚀 Features

* 🔍 URL-based phishing detection
* 🤖 Machine Learning model (Random Forest)
* 🛡️ Rule-based security analysis
* 🌐 Flask web interface
* 📊 Confidence score output
* ⚡ Fast and lightweight system

---

## 🧠 Tech Stack

* **Python**
* **Flask**
* **Scikit-learn**
* **Pandas**
* **Joblib**

---

## 📁 Project Structure

```
phishguard-ai/
│
├── app.py
├── model.py
├── utils.py
├── dataset.csv
├── requirements.txt
├── templates/
│   └── index.html
└── README.md
```

---

## ⚙️ Installation

Clone the repository:

```
git clone https://github.com/yourusername/phishguard-ai.git
cd phishguard-ai
```

Install dependencies:

```
pip install -r requirements.txt
```

---

## ▶️ Usage

Train the model:

```
python model.py
```

Run the application:

```
python app.py
```

Open in browser:

```
http://127.0.0.1:5000
```

---

## 🧪 Example

| Input URL                    | Result      |
| ---------------------------- | ----------- |
| https://google.com           | ✅ Safe      |
| http://login-secure-bank.xyz | ⚠️ Phishing |

---

## 🔐 How It Works

* Extracts multiple features from URLs (length, keywords, domain, etc.)
* Uses a **Random Forest model** for classification
* Applies **rule-based checks** for enhanced detection
* Combines ML + rules for better accuracy

---

## 📌 Future Improvements

* Integration with VirusTotal API
* WHOIS domain analysis
* Email phishing detection
* Improved dataset (10K+ URLs)
* UI enhancements

---

## 👨‍💻 Author

**Gaurav Singh**
Cybersecurity Enthusiast 🚀

---

## ⭐ Support

If you like this project, give it a ⭐ on GitHub!
