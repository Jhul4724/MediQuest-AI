# from http.server import BaseHTTPRequestHandler
import json
from openai import OpenAI

def gpt(input):
    OpenAI.api_key = "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"
    client = OpenAI(api_key="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")

    response = client.chat.completions.create(
    model="gpt-3.5-turbo-1106",
   #  response_format={ "type": "json_object" },
    messages=[
        {
        "role": "system",
        "content": "From the following message from the user, provide me with a likely diagnosis for their health condition."
        },
        {
        "role": "user",
        "content":input   
        }
    ],
    )
    return response.choices[0].message.content

print(gpt("When I run for more than a few minutes, breathing becomes difficult."))







# class handler(BaseHTTPRequestHandler):

#    def do_POST(self):
#          content_length = int(self.headers['Content-Length'])
#          post_data = self.rfile.read(content_length)
#          received_data = str(post_data.decode('utf-8'))
#          htmlhaha = str(json_to_html(gpt(received_data)))

#          self.send_response(200)
#          self.send_header('Content-type', 'plain/text')
#          self.end_headers()
#          self.wfile.write(htmlhaha.encode('utf-8'))