from PIL import ImageFilter
from PIL.Image import Image
from PySide6.QtCore import QRect, Qt
from PySide6.QtGui import QImage, QTransform


def flip_image(image: QImage, flip_mode) -> QImage:
    if flip_mode == 'X':
        return image.mirrored(True, False)  # Flip horizontally
    elif flip_mode == 'Y':
        return image.mirrored(False, True)  # Flip vertically
    elif flip_mode == 'Both':
        return image.mirrored(True, True)  # Flip horizontally and vertically


def apply_effect(image: Image, effect: str) -> Image:
    match effect:
        case 'Emboss':
            filter_name = ImageFilter.EMBOSS
        case 'Find edges':
            filter_name = ImageFilter.FIND_EDGES
        case 'Contour':
            filter_name = ImageFilter.CONTOUR
        case 'Edge enhance':
            filter_name = ImageFilter.EDGE_ENHANCE

    return image.filter(filter_name)


def zoom_and_crop(qimage: QImage, zoom_factor: float) -> QImage:
    """
    Zoom into a QImage and crop it back to its original size.

    :param qimage: The original QImage
    :param zoom_factor: The zoom factor (e.g., 1.5 for 150% zoom)
    :return: A new QImage zoomed and cropped to the original size
    """
    # Get the original dimensions
    original_width = qimage.width()
    original_height = qimage.height()

    # Create a QTransform for scaling
    transform = QTransform()
    transform.scale(zoom_factor, zoom_factor)

    # Apply the transformation to create a zoomed image
    zoomed_image = qimage.transformed(transform, Qt.TransformationMode.SmoothTransformation)

    # Calculate the crop area
    crop_width = original_width
    crop_height = original_height
    x = (zoomed_image.width() - crop_width) // 2
    y = (zoomed_image.height() - crop_height) // 2

    # Create a QRect for cropping
    crop_rect = QRect(x, y, crop_width, crop_height)

    # Crop the image
    cropped_image = zoomed_image.copy(crop_rect)

    return cropped_image
