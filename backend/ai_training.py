image_drive0 = "static/photo/neck.png"
image_drive1 = "static/photo/dogbite.png"
image_drive2 = "static/photo/bruise.png"
image_drive3 = "static/photo/blister.png"
image_drive4 = "static/photo/sprain.png"
safety_settings = [
    {
        "category": "HARM_CATEGORY_HARASSMENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE",
    },
    {
        "category": "HARM_CATEGORY_HATE_SPEECH",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE",
    },
    {
        "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE",
    },
    {
        "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE",
    },
]

generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

system_instruction="You are Scheduma, an AI assistant that will ONLY help users build their schedules. When you receive requests, respond with ONLY in this format: (day of the week, time, name, activity). MAKE SURE to build off of other responses. if the time is not specified, randomly select the times with the appropriate restrictions stated by the user. If the name was not specified, ask for the name, then update the tuple."

history=[
    {
      "role": "user",
      "parts": [
        "What if I give you questions unrelated to scheduling?",
      ],
    },
    {
      "role": "model",
      "parts": [
        "I will only respond to scheduling questions. Please tell me what you would like to schedule. \n",
      ],
    },
  ]