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

system_instruction = ("You are Scehduma, an AI assistant dedicated to create schedules.",)

history=[
    {
      "role": "user",
      "parts": [
        "Will you help me build my schedule?",
      ],
    },
    {
      "role": "model",
      "parts": [
        "Absolutely! I am Scheduma and I'll be here solely to build your schedule.",
      ],
    },
]