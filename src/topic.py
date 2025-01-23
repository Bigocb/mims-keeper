from llmware.models import ModelCatalog


class Topic:

    def topic(self, resp: str) -> str:
        model = ModelCatalog().load_model("slim-topics-tool")
        response = model.function_call(resp,function="classify", params=["topic"])
        topic = response['llm_response']['topic']

        print(f"Topic applied: {topic}")
        return topic




