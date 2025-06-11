from flask import Flask, jsonify, request
from flask_cors import CORS
from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel, set_tracing_disabled
from dotenv import load_dotenv
import os
import asyncio

load_dotenv()
set_tracing_disabled(disabled=True)

API_KEY=os.getenv("API_KEY")
MODEL=os.getenv("MODEL")
BASE_URL=os.getenv("BASE_URL")

client = AsyncOpenAI(
    api_key=API_KEY,
    base_url=BASE_URL
)

agent = Agent(
    name="Assistant",
    instructions="You are a helpful assistant",
    model=OpenAIChatCompletionsModel(model=MODEL, openai_client=client)
)


app = Flask(__name__)
CORS(app)

# async def run_agent_async(user_input):
#     result = await Runner.run(agent, user_input)
#     return result.final_output

@app.route("/api/home",methods=["GET","POST"])
async def home():
    if request.method == "POST":
        data = request.get_json()
        user_input = data.get("user_input")
        result = await Runner.run(agent,user_input)
        return jsonify({"message":result.final_output})
    else:
        return jsonify({"message":"Send a message please"})

    
