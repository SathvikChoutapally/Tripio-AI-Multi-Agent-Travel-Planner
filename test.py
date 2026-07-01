from tools.tavily_tool import tavily_search
from tools.flight_tool import search_flights
from backend import run_travel_agent
# res = tavily_search("Best hotels in Hyderabad")
# print(res)

# res = search_flights("Plan a 7 days india trip from america")
# print(res)

user_input = input("Enter travel reuest: ")

response = run_travel_agent(
    user_input=user_input,
    thread_id="test_user"
)

print("\nFinal Response:\n")
print(response["answer"])