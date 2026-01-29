class NamedBlock:
    def __init__(self, refname=None, name=None, content=""):
        self.refname = refname
        self.name = name
        self.content = content

    def format(self, **kwargs):
        try:
            return self.content.format(**kwargs)
        except KeyError as e:
        # Missing variable → replace with empty string
                safe_kwargs = kwargs.copy()
                missing_key = str(e).strip("'")
                safe_kwargs[missing_key] = ""
                return self.content.format(**safe_kwargs)


    def __str__(self):
        return self.content


class NamedVariable:
    def __init__(self, refname=None, name=None, content=""):
        self.refname = refname
        self.name = name
        self.content = content

    def format(self, **kwargs):
        return self.content.format(**kwargs)

    def __str__(self):
        return self.content

class Collection:
    """
    Compatibility replacement for procoder.prompt.Collection
    Supports chained calls like:
    Collection(...).set_indexing_method(...).set_sep(...)
    """

    def __init__(self, *blocks):
        self.blocks = blocks
        self.sep = "\n"
        self.indexing_method = None

    def set_indexing_method(self, method):
        # Original library uses this for numbering.
        # We store it but don't need to apply it for this project.
        self.indexing_method = method
        return self  # IMPORTANT: allow chaining

    def set_sep(self, sep):
        self.sep = sep
        return self  # IMPORTANT: allow chaining

    def format(self, **kwargs):
        texts = []
        for block in self.blocks:
            if hasattr(block, "format"):
                texts.append(block.format(**kwargs))
            else:
                texts.append(str(block))
        return self.sep.join(texts)

    def __str__(self):
        return self.sep.join(str(b) for b in self.blocks)

def sharp2_indexing(text):
    """
    Dummy replacement for procoder's sharp2_indexing.
    Original function formats numbered prompts.
    For this simulation, raw text is sufficient.
    """
    return text
