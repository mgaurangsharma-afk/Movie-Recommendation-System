# 🎬 CineMatch – Movie Recommendation System

**CineMatch** is a Content-Based Movie Recommendation System developed using Python, Machine Learning, and Streamlit. It recommends movies similar to a user's selected movie by analysing movie features and calculating similarity scores.

The system uses **CountVectorizer** for text feature extraction and **Cosine Similarity** to identify movies with similar content.

## ✨ Features

- 🎥 Movie-based recommendations
- 🤖 Content-Based Filtering
- 🔍 Similarity-based movie matching
- ⚡ Fast recommendations using precomputed similarity scores
- 🌙 Interactive dark-themed user interface
- 🎨 Simple and user-friendly Streamlit application

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Streamlit | Web application interface |
| Pandas | Data manipulation |
| NumPy | Numerical operations |
| Scikit-learn | Machine Learning |
| CountVectorizer | Text feature extraction |
| Cosine Similarity | Similarity calculation |
| Pickle | Model and data storage |

## 🧠 How It Works

CineMatch follows a Content-Based Filtering approach.

1. **Data Processing:** Movie information is loaded and processed.
2. **Feature Extraction:** Relevant movie features are combined into a single text representation.
3. **Vectorisation:** CountVectorizer converts textual features into numerical vectors.
4. **Similarity Calculation:** Cosine Similarity measures the similarity between movie vectors.
5. **Recommendation:** The system identifies and displays movies most similar to the selected movie.

## 📂 Project Structure

```text
Movie-Recommendation-System/
│
├── app.py
├── new_df.pkl
├── similarity.pkl
├── requirements.txt
├── README.md
└── .gitignore
```

## 🚀 Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/mgaurangsharma-afk/Movie-Recommendation-System.git
```

### 2. Navigate to the Project Directory

```bash
cd Movie-Recommendation-System
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Application

```bash
streamlit run app.py
```

The application will open in your default web browser.

## 🎯 Project Objective

The main objective of CineMatch is to simplify movie discovery by providing relevant movie recommendations based on content similarity.

Unlike traditional recommendation approaches, Content-Based Filtering focuses on the characteristics of movies to identify similar content.

## 🔮 Future Scope

- Integration of additional movie features.
- Improved recommendation accuracy.
- User-based recommendation features.
- Deployment on a cloud platform.

## 👨‍💻 Author

**Gaurang Sharma**

B.Tech – Computer Science and Engineering

GitHub: [mgaurangsharma-afk](https://github.com/mgaurangsharma-afk)

---

⭐ If you find this project interesting, consider giving it a star!
