class MessageBus:
    def __init__(self):
        self.messages = {}

    async def send(self, agent_name, message):
        if agent_name not in self.messages:
            self.messages[agent_name] = []
        self.messages[agent_name].append(message)

    async def receive(self, agent_name):
        return self.messages.get(agent_name, [])
