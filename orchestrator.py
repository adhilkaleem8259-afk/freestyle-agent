import asyncio
import logging

class AgentOrchestrator:
    def __init__(self, agents):
        self.agents = agents
        logging.info(f"Orchestrator initialized with {len(agents)} agents")

    async def run_parallel(self):
        await asyncio.gather(*(agent.run() for agent in self.agents))
    
    async def run_sequential(self):
        for agent in self.agents:
            await agent.run()
