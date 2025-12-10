import prompty
import prompty.azure # type: ignore
from prompty.tracer import trace

@trace
async def get_information(question: str, context: str):
    response = await prompty.execute_async(
        "information.prompty",
        inputs={"question": question, "context": context},
    )
    return response

@trace
async def evaluate_async(question: str):

    # get context from somewhere, e.g., a database or an API
    context = """
    The solar system consists of the Sun and the objects that orbit it, including eight planets, their moons, 
    dwarf planets, and countless small bodies like asteroids and comets. The eight planets are Mercury, Venus, 
    Earth, Mars, Jupiter, Saturn, Uranus, and Neptune. Each planet has unique characteristics such as size, 
    composition, atmosphere, and distance from the Sun.
    """

    response = await get_information(question, context)

    result = await prompty.execute_async(
        "groundedness.prompty",
        inputs={
            "query": question,
            "context": context,
            "response": response,
        },
    )
    return result


if __name__ == "__main__":
    import asyncio

    question = "What is the largest planet in our solar system?"
    

    result = asyncio.run(evaluate_async(question=question))
    print(result)
