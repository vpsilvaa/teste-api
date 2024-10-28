import requests
import json
import time
from flask import Flask, request, jsonify

# data = {
#     "callcenter": False,
#     "createdAt": "2024-10-14T00:00:00Z",
#     "intentionType": "BUY",
#     "user": {
#         "email": " ",
#         "dealerId": 85636,
#         "name": "Vitor Pires",
#         "phone": "65987075454",
#         "departmentId": 965
#     },
#     "vehicle": {
#         "title": "Corolla"
#     },
#     "message": "opa",
#     "updatedAt": "2024-10-14T00:00:00Z",
#     "whatsapp": False,
#     "status": "NEW",
#     "providerCampaignName": "Maia_IA",
#     "tags": ["Maia"]
# }


propostas = []
app = Flask(__name__)

@app.route('/create-lead', methods=['POST'])
def create_lead():
    dados = request.json
    
    url = "https://test-open-api.mobiauto.com.br/api/proposal/v1.0/85636"
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJKZ2V5X2VKVmIzUlFzWnlFb1NOT3ZiQ0hLdm5PZUNNN21uc1p3dDhQMXZFIn0.eyJleHAiOjE3Mjk4NzI4NDAsImlhdCI6MTcyOTg2MjA0MCwiYXV0aF90aW1lIjoxNzI5ODYwODQxLCJqdGkiOiI2NGRjYTdhNi1iY2M1LTRjYjUtODgzYi02NWE0MWU1Nzc4MmIiLCJpc3MiOiJodHRwczovL3Rlc3QtYXV0aC5tb2JpYXV0by5jb20uYnIvYXV0aC9yZWFsbXMvbW9iaWF1dG8iLCJhdWQiOiJhY2NvdW50Iiwic3ViIjoiYTcyMmMyOWItZTQyMS00Y2Y4LWJjZDgtMGQ1YzQyNTU1MWQ2IiwidHlwIjoiQmVhcmVyIiwiYXpwIjoiaW50ZWdyYWRvci1zYWdhIiwic2Vzc2lvbl9zdGF0ZSI6ImFjNDNkOTgyLTA0ODYtNDBhMy1iOTlmLWM1Yjg5OTVlZjUyZSIsImFjciI6IjAiLCJhbGxvd2VkLW9yaWdpbnMiOlsiKiJdLCJyZWFsbV9hY2Nlc3MiOnsicm9sZXMiOlsib2ZmbGluZV9hY2Nlc3MiLCJ1bWFfYXV0aG9yaXphdGlvbiJdfSwicmVzb3VyY2VfYWNjZXNzIjp7ImFjY291bnQiOnsicm9sZXMiOlsibWFuYWdlLWFjY291bnQiLCJtYW5hZ2UtYWNjb3VudC1saW5rcyIsInZpZXctcHJvZmlsZSJdfX0sInNjb3BlIjoicHJvZmlsZSBlbWFpbCBvcGVuaWQiLCJzaWQiOiJhYzQzZDk4Mi0wNDg2LTQwYTMtYjk5Zi1jNWI4OTk1ZWY1MmUiLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwibmFtZSI6IkRvdWdsYXMgU291emEgUlNPVVpBIiwicHJlZmVycmVkX3VzZXJuYW1lIjoiZG91Z2xhcy5yc291emFAZ3J1cG9zYWdhLmNvbS5iciIsImdpdmVuX25hbWUiOiJEb3VnbGFzIFNvdXphIiwiZmFtaWx5X25hbWUiOiJSU09VWkEiLCJlbWFpbCI6ImRvdWdsYXMucnNvdXphQGdydXBvc2FnYS5jb20uYnIifQ.Koc0nccQhub6kz7ZXxyw4z0q250nEG1Y3L3WKJnzHxJbVURu6zzvx-bGMM2b8vJL17i24uCg0ftD3U04DehmpCvhQ3GlIxZMeYg3YwmDe00RVSWI-uBJfcqRSAjlJmTWJHHhNT2qqKbkedov6NFBcSuaXVTi8hea64Ve6vXZpHKLOWtzI6FgNDVeKfF7Pn3kqcefR-gzG-vDyNJ1S_tm7t3ylc_eKaZ_WwAVpcGR2o-ATY3JTicXIYgHtOQNZJdjzorHXydnqQGzgpaf6kaHCBVotMud9jxvfGKZcYnJMO8Hdw5JrF1aFhlTaFHzrzD_vLg0pbyCiQ8YWpXR3zu5ig"
    }

    response = requests.post(url, headers=headers, json=dados) # POST

    if response.status_code == 200:
        return jsonify({"message": "Lead criado com sucesso!", "data": response.json()}), 200
    else:
        return jsonify({"message": "Erro ao criar lead", "error": response.json()}), response.status_code

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

# while True:
#     try:
#         response = requests.post(url, headers=headers, data=json.dumps(data))
        
#         if response.status_code == 200:
#             print("Dados enviados com sucesso:", response.json())
#         else:
#             print("Erro ao enviar dados:", response.status_code, response.text)

#     except Exception as e:
#         print("Erro ao enviar requisição:", e)

#     time.sleep(60)
