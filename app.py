import streamlit as st
import plotly.express as px

from src.predictor import predict_score
from src.utils import create_dataframe

st.set_page_config(
    page_title="Student Score Predictor",
    page_icon="🎓",
    layout="wide"
)

st.title("🎓 Student Score Predictor")

st.write(
    "Predict student exam scores using Machine Learning."
)

hours = st.slider(
    "Study Hours",
    0,
    12,
    5
)

attendance = st.slider(
    "Attendance",
    0,
    100,
    80
)

previous = st.slider(
    "Previous Marks",
    0,
    100,
    70
)

sleep = st.slider(
    "Sleep Hours",
    0,
    12,
    7
)

if st.button("Predict"):

    score = predict_score(
        hours,
        attendance,
        previous,
        sleep
    )

    st.success(
        f"Predicted Score : {score:.2f}"
    )

    df = create_dataframe(
        hours,
        attendance,
        previous,
        sleep
    )

    st.dataframe(df)

    fig = px.bar(
        df,
        x="Feature",
        y="Value"
    )

    st.plotly_chart(fig)