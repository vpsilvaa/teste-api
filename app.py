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
#         "dealerId": 58200,
#         "name": "Vitor Pires",
#         "phone": "65987075454",
#         "departmentId": 79962
#     },
#     "vehicle": {
#         "title": "Corolla"
#     },
#     "message": "opa",
#     "updatedAt": "2024-10-14T00:00:00Z",
#     "whatsapp": False,
#     "status": "NEW",
#     "providerCampaignName": "send",
#     "tags": ["others"]
# }


propostas = []
app = Flask(__name__)

@app.route('/create-lead', methods=['POST'])
def create_lead():
    dados = request.json
    
    url = "{URL}"
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer {TOKEN}"
    }

    response = requests.post(url, headers=headers, json=dados) # POST

    if response.status_code == 200:
        return jsonify({"message": "sucesso!", "data": response.json()}), 200
    else:
        return jsonify({"message": "Erro", "error": response.json()}), response.status_code

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
