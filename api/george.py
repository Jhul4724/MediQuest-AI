from http.server import BaseHTTPRequestHandler
import json
from openai import OpenAI

json_form = '{condition: ["heart disease","asthma"]}'

def gpt(input):
    OpenAI.api_key = "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"
    client = OpenAI(api_key="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")

    response = client.chat.completions.create(
    model="gpt-3.5-turbo-1106",
    response_format={ "type": "json_object" },
    messages=[
        {
        "role": "system",
        "content": "From the following message from the user, provide me with a likely diagnosis for their health condition. You will output in this format ( json ) what the condition is in tags and put in most likely to least likey and give maybe 3 and more: + {json_form} You must give atleast 3 no matter what"
        },
        {
        "role": "user",
        "content":input   
        }
    ],
    )
    return json.loads(response.choices[0].message.content)


def inforapi(inputapi):

    output = (gpt(inputapi))['condition']

    print(output)
    f = open("studies.json", "r") 
    test = json.load(f)
    print(len(test['articles']))
    links = []
    i = 0
    while i < len(test['articles']):
        if test['articles'][i]['condition'] in output:
            print(test['articles'][i]['title'])
        i+=1



class handler(BaseHTTPRequestHandler):

   def do_POST(self):
         content_length = int(self.headers['Content-Length'])
         post_data = self.rfile.read(content_length)
         received_data = (post_data.decode('utf-8'))
         htmlhaha = str(inforapi(received_data))

         self.send_response(200)
         self.send_header('Content-type', 'plain/text')
         self.end_headers()
         self.wfile.write(htmlhaha.encode('utf-8'))