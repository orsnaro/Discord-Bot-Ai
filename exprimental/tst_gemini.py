import google.generativeai as genai
import os



genai.configure(api_key= os.environ['GEMINI_APIKEY'])
gemi = genai.GenerativeModel('gemini-1.5-flash')
resp = gemi.generate_content("hi gemi are you okay ? send me an image of happy face and text that you okay!")
print(resp.text, "\n\n\n")
resp = gemi.start_chat()
print(resp.candidates, "\n\n\n")