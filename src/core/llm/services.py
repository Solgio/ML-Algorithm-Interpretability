import os
import base64
import json
import logging
import pandas as pd
from pathlib import Path
from openai import OpenAI
from src.core.llm.interfaces import LLMService

logger = logging.getLogger("LLM_Services")

class OpenAILLMService(LLMService):
    """Concrete implementation of LLMService using OpenAI client."""
    
    def __init__(self, client=None):
        if client is not None:
            self.client = client
        else:
            self.client = OpenAI(
                base_url=os.getenv("BASE_URL", "https://llm.padova.zucchettitest.it/"),
                api_key=os.getenv("OPENAI_API_KEY"),
                max_retries=0
            )

    def generate_response(
        self, 
        model: str, 
        system_prompt: str, 
        user_prompt: str, 
        images: list = None
    ) -> str:
        logger.info(f"Querying OpenAI-compatible model: {model}")
        
        message_content = [{
            "type": "text",
            "text": user_prompt
        }]
        
        if images:
            for idx, img in enumerate(images):
                if isinstance(img, dict) and "name" in img and "base64" in img:
                    name = img["name"]
                    img_b64 = img["base64"]
                else:
                    name = f"image_{idx + 1}.png"
                    img_b64 = img
                
                message_content.append({
                    "type": "text",
                    "text": f"\n[Attached Graph/Plot: {name}]"
                })
                
                mime_type = "image/png" if name.lower().endswith(".png") else "image/jpeg"
                message_content.append({
                    "type": "image_url",
                    "image_url": {"url": f"data:{mime_type};base64,{img_b64}"}
                })
                
        try:
            response = self.client.chat.completions.create(
                model=model,
                messages=[
                    {
                        "role": "system",
                        "content": system_prompt
                    },
                    {
                        "role": "user",
                        "content": message_content
                    }
                ],
            )
            logger.info(f"API call successful for model: {model}")
            return response.choices[0].message.content
        except Exception as e:
            logger.exception(f"Error during API call for {model}: {e}")
            return f"Error: {str(e)}"


class DataPreparationService:
    """Service class responsible for loading files and encoding images."""
    
    @staticmethod
    def load_metrics(file_path: str) -> str:
        """Loads and formats metrics from a JSON or CSV file."""
        if not file_path:
            return "No metrics path provided."
            
        path = Path(file_path)
        if not path.exists():
            return "Metrics file not found."
            
        if path.suffix == '.json':
            try:
                with open(path, 'r', encoding='utf-8') as f:
                    return json.dumps(json.load(f), indent=2)
            except Exception as e:
                logger.exception(f"Error loading JSON metrics: {e}")
                return "Error loading JSON metrics."
        elif path.suffix == '.csv':
            try:
                df = pd.read_csv(path)
                return df.to_string(index=False)
            except Exception as e:
                logger.exception(f"Error loading CSV metrics: {e}")
                return "Error loading CSV metrics."
        return "No textual metrics available."

    @staticmethod
    def load_coefficients(file_path: str) -> str:
        """Loads and formats coefficients from a JSON or CSV file."""
        if not file_path:
            return "No coefficients path provided."
            
        path = Path(file_path)
        if not path.exists():
            return "Coefficients file not found."
            
        if path.suffix == '.json':
            try:
                with open(path, 'r', encoding='utf-8') as f:
                    return json.dumps(json.load(f), indent=2)
            except Exception as e:
                logger.exception(f"Error loading JSON coefficients: {e}")
                return "Error loading JSON coefficients."
        elif path.suffix == '.csv':
            try:
                df = pd.read_csv(path)
                return df.to_string(index=False)
            except Exception as e:
                logger.exception(f"Error loading CSV coefficients: {e}")
                return "Error loading CSV coefficients."
        return "No textual coefficients available."

    @staticmethod
    def encode_images(image_paths: list[str]) -> list[str]:
        """Encodes multiple images to base64 strings."""
        encoded_images = []
        for img_path in image_paths:
            path = Path(img_path)
            if not path.exists():
                raise FileNotFoundError(f"File not found: {img_path}")
            logger.info(f"Encoding image: {img_path}")
            with open(path, "rb") as image_file:
                encoded_images.append(base64.b64encode(image_file.read()).decode("utf-8"))
        return encoded_images


class PromptBuilder:
    """Service class responsible for formatting LLM prompts."""
    
    @staticmethod
    def build_prompt(
        algo_name: str,
        algo_type: str,
        dataset_description: str,
        user_prompt: str,
        algo_prompt: str,
        raw_metrics: str,
        raw_coefficients: str,
        general_prompt: str
    ) -> str:
        """Builds a formatted string for the user prompt."""
        return (
            f"Analysis context:\n\n"
            f"# ALGORITHM: {algo_name}\n"
            f"## Algorithm type: {algo_type}\n"
            f"## Dataset description: {dataset_description}\n"
            f"## User expectations: {user_prompt or 'None'}\n\n"
            f"# NUMERICAL DATA:\n{raw_metrics}\n\n"
            f"# COEFFICIENTS: \n{raw_coefficients}\n\n"
            f"# SPECIFIC INSTRUCTIONS: {algo_prompt}\n"
            f"{general_prompt}\n"
        )
