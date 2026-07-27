from src.model_loader import load_model

model = load_model()


def predict_score(hours, attendance, previous, sleep):
    """
    Predict student's exam score.
    """

    student = [[
        hours,
        attendance,
        previous,
        sleep
    ]]

    prediction = model.predict(student)

    return prediction[0]