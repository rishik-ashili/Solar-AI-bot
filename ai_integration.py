import os
import json
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class GroqIntegration:
    def __init__(self):
        self.api_key = os.getenv("GROQ_API_KEY")
        self.api_url = "https://api.groq.com/openai/v1/chat/completions"
        self.model = "llama3-70b-8192"  # Using LLaMA3 for high quality responses
        
        if not self.api_key:
            raise ValueError("GROQ_API_KEY not found in environment variables")
        
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
    
    def get_response(self, messages, system_prompt=None):
        """
        Get a response from the Groq API
        
        Args:
            messages (list): List of message dictionaries
            system_prompt (str, optional): System prompt to guide the model
            
        Returns:
            str: The model's response
        """
        if system_prompt:
            full_messages = [{"role": "system", "content": system_prompt}] + messages
        else:
            full_messages = messages
            
        payload = {
            "model": self.model,
            "messages": full_messages,
            "temperature": 0.5,
            "max_tokens": 4000
        }
        
        try:
            response = requests.post(self.api_url, headers=self.headers, json=payload)
            response.raise_for_status()
            
            result = response.json()
            return result["choices"][0]["message"]["content"]
        except requests.exceptions.RequestException as e:
            return f"Error communicating with Groq API: {str(e)}"
        except (KeyError, IndexError) as e:
            return f"Error parsing Groq API response: {str(e)}"