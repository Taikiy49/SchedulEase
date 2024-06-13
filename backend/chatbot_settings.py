import google.generativeai as genai
from ai_training import safety_settings, generation_config, system_instruction, history

class ChatbotSettings:
    def __init__(self):
        self._api_key = "AIzaSyDEEMYSOKL_ybCHp-i34PJPD7PRz_IsoNg"
        self._safety_settings = []
        self._generation_config = {}
        self._model = None
        self._chat_session = None

    def configure_api(self):
        genai.configure(api_key=self._api_key)

    def set_safety_settings(self):
        self._safety_settings = safety_settings
        
    def set_generation_config(self):
        self._generation_config = generation_config

    def set_model(self):
        self.configure_api()
        self.set_safety_settings()
        self.set_generation_config()

        self._model = genai.GenerativeModel(
            model_name="gemini-1.5-pro-latest",
            safety_settings=self._safety_settings,
            generation_config=self._generation_config,
            system_instruction=system_instruction,
        )
        
    def create_chat_session(self):
        self.set_model()
        self._chat_session = self._model.start_chat(history=history)

    def run_program(self):
        self.create_chat_session()

