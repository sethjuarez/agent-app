import asyncio
import prompty
import prompty.azure
from prompty.tracer import Tracer, trace, PromptyTracer

tracy = PromptyTracer()
Tracer.add("prompty", tracy.tracer)


@trace
async def execute_prompt():
    p = await prompty.load_async("completion.prompty")
    result = await prompty.execute_async(
        p, inputs={"question": "MY TENTZ IS BROKEN YO!??"}, merge_sample=True
    )
    return result


if __name__ == "__main__":
    result = asyncio.run(execute_prompt())
    print(result)
