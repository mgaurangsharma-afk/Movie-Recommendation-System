# 🎬 CineMatch – Movie Recommendation System

CineMatch is a **Content-Based Movie Recommendation System** developed using Python and Machine Learning. It helps users discover movies similar to their selected movie by analysing movie information and calculating similarity scores.

The system uses **CountVectorizer** for text feature extraction and **Cosine Similarity** to identify movies with similar characteristics. An interactive interface allows users to explore movie recommendations.

## ✨ Features

- 🎥 Movie Recommendations based on selected movies.
- 🤖 Content-Based Filtering for finding similar movies.
- 🔍 Similarity calculation using Cosine Similarity.
- ⚡ Fast recommendations using precomputed similarity scores.
- 🎨 Interactive and user-friendly interface.
- 📊 Movie data processing and feature extraction.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Pandas | Data manipulation and processing |
| NumPy | Numerical operations |
| Scikit-learn | Machine Learning |
| CountVectorizer | Text feature extraction |
| Cosine Similarity | Similarity calculation |
| Streamlit | Application interface |
| Jupyter Notebook | Model development and experimentation |
| Pickle | Storing processed data and similarity scores |

## 🧠 Working Methodology

CineMatch uses Content-Based Filtering to recommend movies.

1. **Data Collection:** Movie information is loaded from `movies.csv` and `credits.csv`.
2. **Data Preprocessing:** Relevant movie information is extracted and processed.
3. **Feature Extraction:** Movie features are combined into a single representation.
4. **Vectorisation:** CountVectorizer converts textual features into numerical vectors.
5. **Similarity Calculation:** Cosine Similarity calculates similarity scores between movies.
6. **Movie Recommendation:** The system identifies and displays movies with the highest similarity scores.

## 📂 Project Structure

```text
Movie-Recommendation-System/
│
├── Recommendation_system.ipynb
├── credits.csv
├── movies.csv
├── new_df.pkl
├── similarity.pkl
├── movie.py
└── README.md
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

### 3. Install Required Libraries

```bash
pip install streamlit pandas numpy scikit-learn
```

### 4. Run the Application

```bash
streamlit run movie.py
```

The application will open in your default web browser.

## 📓 Jupyter Notebook

The `Recommendation_system.ipynb` notebook contains the development and implementation of the movie recommendation system, including data preprocessing, feature extraction and similarity calculation.

## 🎯 Project Objective

The main objective of CineMatch is to make movie discovery easier by providing relevant recommendations based on movie content and similarities.

## 🔮 Future Scope

- Integration of additional movie information.
- Improvement in recommendation accuracy.
- User-based personalised recommendations.
- Deployment on a cloud platform.

## 👨‍💻 Author

**Gaurang Sharma**

B.Tech – Computer Science and Engineering

GitHub: [mgaurangsharma-afk](https://github.com/mgaurangsharma-afk)

---

⭐ If you find this project interesting, consider giving it a star!
