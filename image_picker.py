# Copyright (c) 2023 Jonathan S. Pollack (https://github.com/JPPhoto)

from pydantic import BaseModel

from invokeai.app.invocations.primitives import (
    ImageField,
)

from invokeai.app.invocations.baseinvocation import (
    BaseInvocation,
    BaseInvocationOutput,
    InputField,
    InvocationContext,
    invocation,
    invocation_output,
    OutputField,
    UIType,
)

import random


@invocation_output("image_picker_output")
class ImagePickerOutput(BaseInvocationOutput):
    """Used to randomly pick from a collection of Images."""

    image: ImageField = OutputField(description="The image being chosen")


@invocation("image_picker", title="ImagePicker", tags=["random", "image_picker"])
class ImagePickerInvocation(BaseInvocation):
    """Picks one image at random from a list of images"""

    collection: list[ImageField] = InputField(
        description="The list of images to select from", ui_type=UIType.ImageCollection, default_factory=list
    )

    def invoke(self, context: InvocationContext) -> ImagePickerOutput:
        return ImagePickerOutput(image=random.choice(self.collection))
