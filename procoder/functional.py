def format_prompt(prompt, inputs=None, **kwargs):
    """
    Compatibility replacement for procoder.functional.format_prompt

    prompt  : Collection / NamedBlock / prompt object
    inputs  : dict of variables to format into the prompt
    """

    if inputs is None:
        inputs = {}

    # If prompt supports .format(), use it
    if hasattr(prompt, "format"):
        try:
            return prompt.format(**inputs)
        except TypeError:
            # Fallback if formatting fails
            return str(prompt)

    # Fallback to string
    return str(prompt)

