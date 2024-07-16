import openai
import sys
def ai():
           question = input("Q:enter your question\n")
           
           while True:
               try:
                   openai.api_key = "enter your api key"
                   if openai.api_key == "":
                       sys.stderr.write("""
                       You haven't set up your API key yet.
                       
                       If you don't have an API key yet, visit:
                       
                       https://platform.openai.com/signup
                       
                       1. Make an account or sign in
                       2. Click "View API Keys" from the top right menu.
                       3. Click "Create new secret key"
                       
                       Then, open the Secrets Tool and add OPENAI_API_KEY as a secret.
                       """)
                       exit(1)
                   
                   response = openai.chat.completions.create(
                       model="gpt-3.5-turbo",
                       messages=[
                           {
                               "role": "system",
                               "content": "You are a helpful assistant."
                           },
                           {
                               "role": "user",
                               "content": question
                           }
                       ]
                   )
                   
                   output = response.choices[0].message.content
                   print(output)
                   question= input("Q:enter next\n")
           
               except Exception as e:
                    print(f"An error occurred: {e}")     
                    
