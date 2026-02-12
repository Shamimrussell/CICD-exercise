import pytest
import requests

base_url = "https://skatteverket.entryscape.net/rowstore/dataset/b4de7df7-63c0-4e7e-bb59-1f156a591763"

def test_get_personnummer_from_skatteverket():
    url = "https://skatteverket.entryscape.net/rowstore/dataset/b4de7df7-63c0-4e7e-bb59-1f156a591763?_limit=10&_offset=0"

    response = requests.get(url)  # Trigger a request towards Skattverket AND save it to the variable 'response'

    assert response.status_code == 200
    assert response.headers.get("Content-Type") == "application/json;charset=utf-8"

    # Prints whole response body from Skatteverket, more than we need
    print(response.json())  

    # Prints the "results" parts of the payload
    print(response.json()["results"])

    # Save list of social security numbers as a variable, for easier usage
    list_of_personnummer = response.json()["results"]
    for personnummer in list_of_personnummer:
        print(personnummer.get("testpersonnummer"))

def test_get_personnummer_from_skatteverket_limit_10():
    """Splitting base URL from limit allows us to change limits without
    changing base URL strings in all tests. Better but not good enough."""
    response = requests.get(base_url + "?_limit=10")


def test_get_personnummer_from_skatteverket_limit_params():
    """Example of using requests get with params as input. Allows
    even better structure of the test. Now the response.get(...) looks same for
    many tests."""
    params = {"_limit": 10}
    response = requests.get(base_url, params=params)

@pytest.mark.parametrize("limit", [10, 15, 20])
def test_get_personnummer_from_skatteverket_limit_params_and_parametize(limit):
    """Example of using requests get with params as input together with pytest
    parameterize"""
    params = {"_limit": limit}
    response = requests.get(base_url, params=params)