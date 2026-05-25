import requests

def test_post_api():
    api_url = "https://jsonplaceholder.typicode.com/posts"
    user_data ={
        "title" : "Ishan",
        "body" : "SDET senior",
        "userId" : "1"
    }

    response = requests.post(api_url , json= user_data)

    assert response.status_code == 201 ; f"Error , the status code is {response.status_code}"

    data = response.json()

    assert data["title"] == "Ishan"
    assert data["body"] == "SDET senior"

    