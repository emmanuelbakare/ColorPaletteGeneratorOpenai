import json
from openai import OpenAI

def generate_colors(userPrompt):
    systemPrompt = """
    You are a color palette generating assitant that responds to next prompts using color palette
    Desired Format: hexadecimal color code in in Json array format   e.g [hex1, hex2, hex3...]
    """
    
    # userPrompt = "african colors"
    client = OpenAI()
    
    response = client.chat.completions.create(
        model = "gpt-3.5-turbo",
        messages = [
            {"role":"system","content":systemPrompt},
            {"role":"user","content": userPrompt}
        ] ,
        max_tokens = 100,
        
    )
    
    color_response = response.choices[0].message.content
    colors = json.loads(color_response)
    return colors    