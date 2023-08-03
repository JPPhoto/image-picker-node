# Copyright (c) 2023 Jonathan S. Pollack (https://github.com/JPPhoto)

from typing import Literal

from pydantic import BaseModel, Field

from ..models.image import (
    ImageField
)

from invokeai.app.invocations.baseinvocation import (
    BaseInvocation,
    BaseInvocationOutput,
    InvocationContext,
    InvocationConfig,
)

import random


class ImagePickerOutput(BaseInvocationOutput):
    """Used to randomly pick from a collection of Images."""

    # fmt: off
    type: Literal["image_picker_output"] = "image_picker_output"
    image: ImageField = Field(description="The image being chosen")
    # fmt: on

    class Config:
        schema_extra = { "required": [ "type", "image" ] }

class ImagePickerInvocation(BaseInvocation):
    """Picks one image at random from a list of images"""

    # fmt: off
    type: Literal["image_picker"] = "image_picker"
    collection: list[ImageField] = Field(description="The list of images to select from", default_factory=list)
    # fmt: on

    class Config(InvocationConfig):
        schema_extra = { "ui": { "title": "ImagePicker", "tags": [ "random", "image_picker" ] } }

    def invoke(self, context: InvocationContext) -> ImagePickerOutput:
        return ImagePickerOutput(image=random.choice(self.collection))
