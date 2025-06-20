from dotenv import load_dotenv
import os
from agents import AsyncOpenAI, OpenAIChatCompletionsModel, Agent, Runner, RunConfig
import asyncio

load_dotenv()

# MODEL_NAME = "gemini/gemini-2.0-flash"  #for litellm we write like this we have to tell litellm that we are using gemini


async def hello_agent():
    MODEL_NAME = "gemini-2.0-flash"
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
    external_client = AsyncOpenAI(
        api_key=GEMINI_API_KEY,
        base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
    )
    model = OpenAIChatCompletionsModel(model=MODEL_NAME, openai_client=external_client)
    config = RunConfig(
        model=model, model_provider=external_client, tracing_disabled=True
    )
    assistant = Agent(
        name="assistant", instructions="Your job is to resolve queries.", model=model
    )

    result = await Runner.run(
        assistant, input="Tell me who is ameen alam.", run_config=config
    )
    print(result.final_output)


if __name__ == "__main__":
    asyncio.run(hello_agent())
