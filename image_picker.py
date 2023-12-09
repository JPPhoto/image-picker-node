# Copyright (c) 2023 Jonathan S. Pollack (https://github.com/JPPhoto)

import random

from invokeai.app.invocations.baseinvocation import (
    BaseInvocation,
    BaseInvocationOutput,
    InputField,
    InvocationContext,
    OutputField,
    invocation,
    invocation_output,
)
from invokeai.app.invocations.primitives import ImageField


@invocation_output("image_picker_output")
class ImagePickerOutput(BaseInvocationOutput):
    """Used to randomly pick from a collection of Images."""

    image: ImageField = OutputField(description="The image being chosen")


@invocation("image_picker", title="ImagePicker", tags=["random", "image_picker"], version="1.0.0")
class ImagePickerInvocation(BaseInvocation):
    """Picks one image at random from a list of images"""

    collection: list[ImageField] = InputField(
        description="The list of images to select from"
    )

    def invoke(self, context: InvocationContext) -> ImagePickerOutput:
        return ImagePickerOutput(image=random.choice(self.collection))
