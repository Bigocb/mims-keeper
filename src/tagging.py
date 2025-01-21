from llmware.models import ModelCatalog


class Tagging:

    def tag(self, resp: str) -> list[str]:
        model = ModelCatalog().load_model("slim-tags-tool")
        response = model.function_call(resp, function="classify", params=["tags"])
        tags = response['llm_response']['tags']

        print(f"Tags applied: {tags}")
        return tags
