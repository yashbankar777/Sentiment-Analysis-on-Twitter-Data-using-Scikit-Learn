🧠 Sentiment Analysis with Scikit-Learn
A complete and production-ready sentiment analysis pipeline using classical machine learning models. This project performs robust text preprocessing, model training, evaluation, and prediction without relying on heavy NLP libraries like NLTK or SpaCy.

📌 Features
🧹 Preprocessing pipeline with:
• 🛑 Custom stopword removal
• 🔗 URL, hashtag, mention, HTML, and punctuation cleaning
• ✂️ Tokenization without NLTK

🧼 Dataset cleaning and batch-wise processing

📊 Exploratory data analysis:
• 📈 Sentiment distribution
• 📏 Text length analysis

🤖 Model training using:
• ⚙️ Logistic Regression
• 🌲 Random Forest
• 📬 Naive Bayes
• 📐 Linear SVC

🧠 Feature extraction:
• 🧮 CountVectorizer
• 📊 TfidfVectorizer

📏 Evaluation metrics:
• 🎯 Accuracy, precision, recall, F1-score
• 🧊 Confusion matrix heatmaps

🚨 Misclassification pattern analysis

💾 Model persistence:
• 📦 Saves the best-performing model to a .pkl file

🔮 Prediction API:
• 🚀 API-ready complete_sentiment_analysis() function

📂 Dataset
• 🗂️ train.csv and test.csv files with text and sentiment columns
• 🧾 Sentiment labels mapped to numerical values:

0 = ❌ Negative

2 = ⚪ Neutral

4 = ✅ Positive

🏗️ Model Architecture
🧱 Text Preprocessing
→ Clean → Tokenize → Remove Stopwords → Vectorize

⚙️ Model Training (Pipeline)
→ Vectorizer + Classifier (e.g., TF-IDF + Logistic Regression)

📏 Evaluation
→ Accuracy, Classification Report, F1 Scores

💾 Model Saving
→ Save best model using pickle

🧪 Prediction API
→ Reusable function complete_sentiment_analysis() for inference

🛠️ Tech Stack
🧑‍💻 Technologies:
• Python 🐍
• HTML 📝
• CSS 🎨
• Flask 🌐

📚 Libraries:
• scikit-learn 📘
• pandas 🐼
• matplotlib 📊
• seaborn 🌈
• pickle 📦

🧼 No external NLP libraries used (e.g., no NLTK, no SpaCy) ❌📚

🔍 Sample Output
text
Copy
Edit
Text: "Worst purchase ever! Complete waste of money!"
Sentiment: Negative ❌
Confidence: 0.982 🎯
