import openai

#Returns text from OpenAI based off of prompt
def AiGeneration(): 
  # API key
  openai.api_key = "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"
  
  #Model Engine
  model_engine = "gpt-3.5-turbo-instruct"
  prompt = "Generate a very creative and random comment. It can be mean, funny, gross, weird, extreme or scary. The comment would take place in a video game."
  temperature = 1
  max_tokens = 100
  
  # Generate comment using the OpenAI API
  response = openai.Completion.create(
      engine=model_engine,
      prompt=prompt,
      temperature=temperature,
      max_tokens=max_tokens,
      n=1,
      stop=None,
  )
  # Print comment
  comment = response.choices[0].text.strip()
  return comment

#call function
print(AiGeneration())
