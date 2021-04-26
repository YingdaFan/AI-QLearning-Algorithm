import requests

class GameAPI:
    def locate_me(self, teamId):
        url = "https://www.notexponential.com/aip2pgaming/api/rl/gw.php?type=location&teamId="+str(teamId)

        payload = {}
        headers = {
            'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36",
            'Authorization': 'Basic Og==',
            'x-api-key': '9ba3e7cb2fc7f2dbd0b0',
            'userId': '1058',
        }

        response = requests.request("GET", url, headers=headers, data=payload)

        return response.json()

    def enter_world(self, teamId, worldId):
        url = "https://www.notexponential.com/aip2pgaming/api/rl/gw.php"

        payload = {'type': 'enter',
                   'worldId': str(worldId),
                   'teamId': str(teamId)}
        files = []
        headers = {
            'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36",
            'Authorization': 'Basic Og==',
            'x-api-key': '9ba3e7cb2fc7f2dbd0b0',
            'userId': '1058',
        }

        response = requests.request("POST", url, headers=headers, data=payload, files=files)

        return response.json()

    def make_move(self, teamId, worldId, move):
        url = "https://www.notexponential.com/aip2pgaming/api/rl/gw.php"

        payload = {'type': 'move',
                   'teamId': str(teamId),
                   'move': str(move),
                   'worldId': str(worldId)}
        files = []
        headers = {
            'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36",
            'Authorization': 'Basic Og==',
            'x-api-key': '9ba3e7cb2fc7f2dbd0b0',
            'userId': '1058',
        }

        response = requests.request("POST", url, headers=headers, data=payload, files=files)

        return response.json()

    def get_score(self, teamId):
        url = "https://www.notexponential.com/aip2pgaming/api/rl/score.php?type=score&teamId="+str(teamId)

        payload = {}
        headers = {
            'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36",
            'Authorization': 'Basic Og==',
            'x-api-key': '9ba3e7cb2fc7f2dbd0b0',
            'userId': '1058',
        }

        response = requests.request("GET", url, headers=headers, data=payload)

        return response.json()["score"]

    def get_runs(self, teamId, count):
        url = "https://www.notexponential.com/aip2pgaming/api/rl/score.php?type=runs&teamId=" + str(teamId) + "&count=" + str(count)

        payload = {}
        headers = {
            'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36",
            'Authorization': 'Basic Og==',
            'x-api-key': '9ba3e7cb2fc7f2dbd0b0',
            'userId': '1058',
        }

        response = requests.request("GET", url, headers=headers, data=payload)

        return response.json()['runs']