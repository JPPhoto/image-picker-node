# Copyright (c) 2024 Jonathan S. Pollack (https://github.com/JPPhoto)

import random

from invokeai.app.invocations.baseinvocation import (
    BaseInvocation,
    BaseInvocationOutput,
    InvocationContext,
    invocation,
    invocation_output,
)
from invokeai.app.invocations.fields import InputField, OutputField
from invokeai.app.invocations.primitives import ImageField


@invocation_output("image_picker_output")
class ImagePickerOutput(BaseInvocationOutput):
    """Used to randomly pick from a collection of Images."""

    image: ImageField = OutputField(description="The image being chosen")


@invocation("image_picker", title="ImagePicker", tags=["random", "image_picker"], version="1.0.1", use_cache=False)
class ImagePickerInvocation(BaseInvocation):
    """Picks one image at random from a list of images"""

    collection: list[ImageField] = InputField(description="The list of images to select from")

    def invoke(self, context: InvocationContext) -> ImagePickerOutput:
        return ImagePickerOutput(image=random.choice(self.collection))
