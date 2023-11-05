import openai 
import constants 

print(constants.API_KEY)
openai.api_key = constants.API_KEY


messages =  [ {"role": "system", "content": "You are a intelligent assistant."}] 


chat = openai.ChatCompletion.create( 
            model="gpt-3.5-turbo", messages=messages)

reply = chat.choices[0].message.content 


print(f"ChatGPT: {reply}")









