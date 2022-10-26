# App: python2natural

* Insert code
* GPT-3 analyzes the code and returns human readable text

## Deployment

0. Get OpenAI API Key [here](https://beta.openai.com)
1. Build Container:
```bash
docker build -t python2natural .
```
2. Run Container:
```bash
docker run -d --name python2natural -p 1337:1337 --env OPENAI_ORG="<YOUR ORG_ID HERE>" --env OPENAI_KEY="<YOUR API KEY HERE>" python2natural
```
