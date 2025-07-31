import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import roc_curve, roc_auc_score
import matplotlib.pyplot as plt

st.set_page_config(page_title="Dự đoán Giáo dục", layout="centered")

st.title("🎓 Dự đoán cảm xúc văn bản bằng Logistic Regression")

uploaded_file = st.file_uploader("📂 Tải lên file CSV dữ liệu", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    st.subheader("📊 Dữ liệu đầu vào")
    st.write(df.head())

    try:
        X = df["Text"]
        y = df["Label"].map({"positive": 1, "negative": 0})  

        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.3, random_state=42
        )

        vectorizer = TfidfVectorizer()
        X_train_vec = vectorizer.fit_transform(X_train)
        X_test_vec = vectorizer.transform(X_test)

        model = LogisticRegression()
        model.fit(X_train_vec, y_train)

        y_probs = model.predict_proba(X_test_vec)[:, 1]

        fpr, tpr, _ = roc_curve(y_test, y_probs)
        auc_score = roc_auc_score(y_test, y_probs)

        st.subheader("📈 Đường cong ROC")

        fig, ax = plt.subplots()
        ax.plot([0, 1], [0, 1], linestyle='--', color='gray')
        ax.plot(fpr, tpr, marker='.', color='green', label=f"AUC = {auc_score:.2f}")
        ax.set_xlabel("False Positive Rate")
        ax.set_ylabel("True Positive Rate")
        ax.set_title("ROC Curve")
        ax.legend()
        st.pyplot(fig)

        st.success("✅ Logistic Regression đã huấn luyện xong!")

    except Exception as e:
        st.error(f"❌ Lỗi: {e}")
