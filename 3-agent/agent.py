import prompty
import prompty.azure
from prompty.tracer import Tracer, trace, PromptyTracer

tracy = PromptyTracer()
Tracer.add("prompty", tracy.tracer)


@trace
def get_current_weather(city: str, unit: str = "Celsius"):
    return f"The weather in {city} is 32 {unit}"


@trace
def execute_agent():
    p = prompty.load("agent.prompty")
    # set the tool function
    p.set_tool_value("get_current_weather", get_current_weather)
    result = prompty.execute(
        p, inputs={"question": "What was the weather like in Tokyo?"}, merge_sample=True
    )
    return result


if __name__ == "__main__":
    result = execute_agent()
    print(result)
