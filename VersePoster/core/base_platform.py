class BasePlatform:
    """Interface for platform clients."""

    def post(self, content: str):
        raise NotImplementedError("Subclasses must implement 'post'")