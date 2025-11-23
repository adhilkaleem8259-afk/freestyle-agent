import logging

class LLMHandler:
    def __init__(self):
        print("⚠️ Using dummy LLM. Replace with GPT4All for real responses.")
        logging.info("Dummy LLM initialized")

    def generate_response(self, prompt):
        response = f"🤖 Dummy response: {prompt}"
        logging.info(f"LLM generated response for prompt: {prompt}")
        return response

    def summarize_tasks(self, tasks):
        if not tasks:
            return "No tasks to summarize."
        summary = "\n".join([f"Task {i+1}: {t}" for i, t in enumerate(tasks)])
        logging.info("LLM summarized tasks")
        return summary

    def categorize_task(self, task):
        logging.info(f"LLM categorized task: {task}")
        return "General"
