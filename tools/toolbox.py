class Toolbox:
    def calculator(self, expr: str):
        try:
            return eval(expr, {"__builtins__": {}})
        except Exception as e:
            return f"Error: {e}"

    def summarize_text(self, text: str):
        # Simple offline summary (first 50 chars)
        return text[:50] + "..." if len(text) > 50 else text

    def offline_search(self, query: str):
        # Example local knowledge
        knowledge_base = ["bike", "car", "ship", "train", "plane"]
        results = [item for item in knowledge_base if query.lower() in item.lower()]
        return results or ["No results found"]
