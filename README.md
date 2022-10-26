# App: python2natural

* Insert code
* GPT-3 analyzes the code and returns human readable text

## Docker Deployment

0. Get OpenAI API Key [here](https://beta.openai.com)
1. Build Container:
```bash
docker build -t python2natural .
```
2. Run Container:
```bash
docker run -d --name python2natural -p 1337:1337 --env OPENAI_ORG="<YOUR ORG_ID HERE>" --env OPENAI_KEY="<YOUR API KEY HERE>" python2natural
```
3. App is running and can be accessed via Web Browser on http://localhost:1337

## Local Deployment

0. Install flask + openai
```bash
pip install openai flask
``` 
1. Navigate to app/ and run `flask run` or `python app.py`
2. App is running and can be accessed via Web Browser on http://localhost:1337