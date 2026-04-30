from google.adk.agents import Agent
from .tools import tools

# This is the "brain" of your travel agent
travel_agent = Agent(
    name="TravelAgent",
    model="gemini-2.5-flash", # Or gemini-2.0-flash
    instruction="You are a travel assistant. Use your tools to find the current time or search for hotels when asked.",
    tools=tools
)

# Export as root_agent for the ADK runner
root_agent = travel_agent
