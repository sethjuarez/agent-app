import prompty
import prompty.azure
from prompty.tracer import Tracer, trace, PromptyTracer
from colorama import Fore, Style, init

tracy = PromptyTracer()
Tracer.add("prompty", tracy.tracer)

USER = f"{Fore.GREEN}user> {Style.RESET_ALL}"
AGENT = f"{Fore.BLUE}agent> {Style.RESET_ALL}"

@trace
def execute_chat():
    p = prompty.load("chat.prompty")
    while (prompt := input(USER)) != "exit":
        result = prompty.execute(
            p, inputs={"query": prompt}, merge_sample=True
        )
        print(f"\n{AGENT}{result}\n")


if __name__ == "__main__":
    init(autoreset=True)
    execute_chat()
