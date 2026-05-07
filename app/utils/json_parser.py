import json
import re


def extract_json(text: str):

    match = re.search(
        r"\{.*\}",
        text,
        re.DOTALL
    )

    if not match:
        raise ValueError(
            f"No JSON object found in response:\n{text}"
        )

    json_text = match.group()

    try:
        return json.loads(json_text)

    except json.JSONDecodeError as error:

        raise ValueError(
            f"Invalid JSON returned:\n{json_text}"
        ) from error