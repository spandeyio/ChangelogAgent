from langchain.agents import create_agent
from app.llm import llm_instance
from app.tools import get_tools
from app.prompt import AGENT_SYSTEM_PROMPT


class ChangelogAgent:
    def __init__(self):
        self.agent = create_agent(
            model=llm_instance.get_llm(),
            tools=get_tools(),
            system_prompt=AGENT_SYSTEM_PROMPT,
        )

    def invoke(self, query: str, history: list) -> str:
        messages = []
        for msg in history:
            role = "assistant" if msg["role"] == "agent" else "user"
            messages.append({"role": role, "content": msg["content"]})

        messages.append({"role": "user", "content": query})

        result = self.agent.invoke({"messages": messages})
        content = result["messages"][-1].content
        if isinstance(content, list):
            # Extract text from list of blocks if necessary
            content = " ".join(
                [
                    c.get("text", "")
                    for c in content
                    if isinstance(c, dict) and "text" in c
                ]
            )
        return str(content)


changelog_agent = ChangelogAgent()
