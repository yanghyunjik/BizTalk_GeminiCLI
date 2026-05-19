import os
from dotenv import load_dotenv
from langchain_upstage import ChatUpstage
from langchain_core.messages import HumanMessage, SystemMessage
from prompts.templates import PROMPTS

load_dotenv()

class ToneConverter:
    def __init__(self):
        self.api_key = os.getenv("UPSTAGE_API_KEY")
        if not self.api_key:
            raise ValueError("UPSTAGE_API_KEY is not set in .env file")
        self.llm = ChatUpstage(upstage_api_key=self.api_key, model="solar-pro")

    async def convert(self, text: str, target_audience: str) -> str:
        if target_audience not in PROMPTS:
            raise ValueError(f"Invalid target audience: {target_audience}")

        system_prompt = PROMPTS[target_audience]
        
        messages = [
            SystemMessage(content=system_prompt),
            HumanMessage(content=text)
        ]
        
        response = await self.llm.ainvoke(messages)
        return response.content
