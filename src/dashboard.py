import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt


def create_dashboard(df):
    
    """
    Create the student performance analysis dashboard with visualizations

    """

    # 1. Score Distribution
    st.subheader("1. Score Distribution")
    fig, ax = plt.subplots(figsize=(8, 4))
    

    #  A single histogram with all scores
    all_scores = df[["math_score", "reading_score", "writing_score"]].values.flatten()
    sns.histplot(all_scores, bins=15, kde=True, color="steelblue", alpha=0.7)
    plt.xlabel("Score")
    plt.ylabel("Count")
    plt.title("Distribution of All Subject Scores")
    plt.tight_layout()
    st.pyplot(fig)
    plt.close()

    # 2. Average Scores by Gender
    st.subheader("2. Average Scores by Gender")
    avg_scores = df.groupby("gender")[
        ["math_score", "reading_score", "writing_score"]
    ].mean()
    st.bar_chart(avg_scores, height=300)

    # 3. Parental Education Impact
    st.subheader("3. Math Scores by Parental Education")
    fig, ax = plt.subplots(figsize=(8, 4))
    sns.boxplot(x="parental_level_of_education", y="math_score", data=df, ax=ax)
    plt.xticks(rotation=30, ha="right")
    plt.xlabel("Parental Education")
    plt.ylabel("Math Score")
    plt.tight_layout()
    st.pyplot(fig)
    plt.close()

    # 4. Test Preparation Impact 
    st.subheader("4. Test Preparation Course Impact")
    prep_scores = df.groupby("test_preparation_course")[
        ["math_score", "reading_score", "writing_score"]
    ].mean()
    st.bar_chart(prep_scores, height=300)

    # 5. Race/Ethnicity Performance 
    st.subheader("5. Performance by Race/Ethnicity")
    fig, ax = plt.subplots(figsize=(8, 4))
    race_scores = df.groupby("race_ethnicity")[
        ["math_score", "reading_score", "writing_score"]
    ].mean()
    race_scores.plot(kind="bar", ax=ax, width=0.8)
    plt.xlabel("Race/Ethnicity")
    plt.ylabel("Average Score")
    plt.xticks(rotation=30, ha="right")
    plt.legend(title="Subject", loc="upper left")
    plt.tight_layout()
    st.pyplot(fig)
    plt.close()

    # 6. Math Score Distribution
    st.subheader("6. Math Score Distribution")
    fig, ax = plt.subplots(figsize=(8, 4))
    sns.histplot(df['math_score'], bins=15, kde=True, color="skyblue", alpha=0.7, ax=ax)
    plt.xlabel("Math Score")
    plt.ylabel("Number of Students")
    plt.title("Distribution of Math Scores")
    plt.tight_layout()
    st.pyplot(fig)
    plt.close()

    # 7. Average Reading Score by Test Preparation Course
    st.subheader("7. Average Reading Score by Test Preparation Course")
    avg_reading_prep = df.groupby("test_preparation_course")["reading_score"].mean()
    plt.figure(figsize=(6,4))
    sns.barplot(x=avg_reading_prep.index, y=avg_reading_prep.values, palette="pastel")
    plt.xlabel("Test Preparation Course")
    plt.ylabel("Average Reading Score")
    plt.title("Average Reading Score by Test Preparation Course")
    plt.tight_layout()
    st.pyplot(plt)
    plt.close()
    
    
