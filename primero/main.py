import requests

if __name__ == "__main__":
    url = "https://hooks.slack.com/services/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"
    msg = input('Introduce tu mensaje')
    result = requests.post(url,json={'text':msg})
    if(result.text == "ok"):
        print('El mensaje se ha enviado')
    else:
        print(result.text)