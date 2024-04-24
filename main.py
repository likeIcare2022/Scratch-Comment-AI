import google.generativeai as palm
import time
import scratchattach as scratch3


session = scratch3.login("RECTIONPROBE-34", "PROBE#34SRL-483")
model = palm.GenerativeModel('gemini-pro')
palm.configure(api_key="AIzaSyCNkWYyP4SkoEXasZz32YcvH2Y1towxx_Y")
project = session.connect_project(int(input(": ")))


while True:
    print(str(project.comments(limit=1))[1:-1])
    response = model.generate_content(f"Go to the content part of the string and summarise it please: {str(project.comments(limit=1))[1:-1]}")
    print(response.text)
    project.post_comment(response.text)
    time.sleep(60)
