import asyncio
import prompty
import prompty.azure
from prompty.tracer import Tracer, trace, PromptyTracer

tracy = PromptyTracer()
Tracer.add("prompty", tracy.tracer)


@trace
async def run_simple():
    p = await prompty.load_async("completion.prompty")
    messages = await prompty.execute_async(
        p, inputs={"question": "What kind of tents do you sell?"}, merge_sample=True
    )

    return messages


if __name__ == "__main__":
    result = asyncio.run(run_simple())
