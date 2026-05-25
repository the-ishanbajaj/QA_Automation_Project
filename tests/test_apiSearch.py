import requests

def test_WikipediaApi():
    api_url = "https://en.wikipedia.org/w/api.php"

    payload = {
        "action" : "query",
        "format" : "json",
        "titles" : "Python_(programming_language)"

   
    }
    headers = {
        "User-Agent": "MySDETCapstoneProject/1.0 (learning_automation)"
    }
    response = requests.get(api_url , params= payload , headers=headers)

    assert response.status_code == 200 


    data = response.json()

    pages = data['query']['pages']

    assert "-1" not in pages , "Error"