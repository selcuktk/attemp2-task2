import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../src')))

import pytest
from fastapi.testclient import TestClient
from src.app.app import app
from src.pred.image_classifier import *
from tests.helpers import predict_test

client = TestClient(app)


"""def test_predict_internship1():
    response = predict_test(client, "/predict/internship/")
    assert response["status_code"] == 200
PYTHONPATH=src pytest tests/unit-tests/
def test_predict_internship2():
    response = predict_test(client, "/predict/internship/")
    assert response["class"] is not None
    assert isinstance(response["confidence"], float)"""

@pytest.mark.asyncio
async def test_predict_internship():
    response = await client.post(
        "/predict/internship/",
        json={"img_url": "https://i.imgur.com/VOPrfSo.png"}
    )
    assert response.status_code == 200
    json_data = response.json()
    assert "class" in json_data
    assert "confidence" in json_data
    assert isinstance(json_data["confidence"], float)
