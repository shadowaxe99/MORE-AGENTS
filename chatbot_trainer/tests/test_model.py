
import pytest
from src.chatbot.models.model import ChatbotModel

def test_model_initialization():
    model = ChatbotModel()
    assert model is not None, "Model initialization failed"

def test_model_training():
    model = ChatbotModel()
    model.train()
    assert model.is_trained, "Model training failed"

def test_model_prediction():
    model = ChatbotModel()
    model.train()
    response = model.predict("Hello")
    assert isinstance(response, str), "Model prediction failed"

@pytest.mark.parametrize("input_data, expected_output", [
    ("Hello", "Hello, how can I help you?"),
    ("What's the weather?", "I'm sorry, I can't provide weather updates."),
])
def test_model_responses(input_data, expected_output):
    model = ChatbotModel()
    model.train()
    response = model.predict(input_data)
    assert response == expected_output, "Model response incorrect"
