from typing import Annotated, Union

from pydantic import AfterValidator, BaseModel, FilePath, AnyHttpUrl


def validate_youtube_link(url: AnyHttpUrl) -> AnyHttpUrl:
    if "youtube.com/watch" not in url.encoded_string():
        raise ValueError(f"{url} is not a valid youtube url")

    return url


YoutubeUrl = Annotated[AnyHttpUrl, AfterValidator(validate_youtube_link)]
InputSource = Union[YoutubeUrl, FilePath]


class CLIConfig(BaseModel):
    input_src: InputSource
