import requests
import os

def buscar_repositorios(usuario):
    token = os.getenv("GITHUB_TOKEN")
    headers = {"Authorization": f"Bearer {token}"} if token else {}
    url = f"https://api.github.com/users/{usuario}/repos"
    resposta = requests.get(url, headers=headers)
    return resposta.json() if resposta.status_code == 200 else []
