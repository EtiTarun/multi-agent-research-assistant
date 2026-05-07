import requests

from app.core.config import settings

from app.core.logging_config import get_logger


logger = get_logger(__name__)


class MistralService:

    def __init__(self):

        self.api_key = settings.MISTRAL_API_KEY

        self.model = settings.MISTRAL_MODEL

        self.base_url = (
            "https://api.mistral.ai/v1/chat/completions"
        )

        logger.info(
            f"Mistral initialized with model: {self.model}"
        )

    def generate_response(self, prompt: str):

        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

        payload = {
            "model": self.model,
            "messages": [
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            "temperature": 0.3,
            "max_tokens": 6000
        }

        try:

            logger.info(
                "Sending request to Mistral"
            )

            response = requests.post(
                self.base_url,
                headers=headers,
                json=payload,
                timeout=120
            )

            response.raise_for_status()

            data = response.json()

            content = data["choices"][0]["message"]["content"]

            logger.info(
                "Received response from Mistral"
            )

            return content

        except Exception as error:

            logger.error(
                f"Mistral API Error: {str(error)}"
            )

            raise