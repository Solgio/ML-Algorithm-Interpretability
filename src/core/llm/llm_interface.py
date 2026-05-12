import requests
import json

API_KEY = "sk-uqDhskweZ_9nrhEtyfHiHg"  # sostituisci con la tua
BASE_URL = "https://llm.padova.zucchettitest.it/v1/responses"

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}



data = {
    "model": "gemma4:e4b",  # o quello supportato dal server
    "input": 
            [
                {
                    "role": "user",
                    "content": "What's the capital of Italy?"
                }
            ],
    "max_output_tokens": 150,

}

try:
    response = requests.post(BASE_URL, headers=headers, json=data)
    response.raise_for_status()

    result = response.json()

    # Estrai testo (struttura tipica responses API)
    output_text = result["output"][0]["content"][0]["text"]
    print(result)
    
    print("-----------------------------------------------------------------------------------------------")
    print(json.dumps(result, indent=2))

except requests.exceptions.RequestException as e:
    print("Errore:", e)
    if 'response' in locals():
        print(response.text)
