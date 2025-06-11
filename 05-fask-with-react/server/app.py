from flask import Flask, jsonify
from flask_cors import CORS
from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel, set_tracing_disabled
from dotenv import load_dotenv
import os

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

@app.route("/api/home",methods=["GET","POST"])
def home():
    result = Runner.run_sync(
    agent,
    "helloooo"
)
    return jsonify({"message":result.final_output})

if __name__ == "__main__":
    app.run(debug=True)

    
