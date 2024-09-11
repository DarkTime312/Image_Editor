from PySide6.QtCore import QRectF
from PySide6.QtGui import QPainter, Qt, QPixmap, QTransform, QImage
from PySide6.QtWidgets import QGraphicsView, QGraphicsScene


class Canvas(QGraphicsView):
    def __init__(self):
        super().__init__()
        self.original_image = None
        self.pixmap_rect = None
        self.scene = QGraphicsScene(self)
        self.setScene(self.scene)
        self.setStyleSheet("background-color: transparent")
        self.setRenderHint(QPainter.RenderHint.SmoothPixmapTransform | QPainter.Antialiasing)
        # self.setRenderHint()

        self.setViewportUpdateMode(QGraphicsView.ViewportUpdateMode.FullViewportUpdate)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.pixmap_item = None

    def load_image(self, image_path):
        self.original_image = QImage(image_path)
        self.display_image(self.original_image)

    def display_image(self, image):
        pixmap = QPixmap(image)

        self.scene.clear()
        self.pixmap_item = self.scene.addPixmap(pixmap)
        self.pixmap_item.setTransformationMode(Qt.TransformationMode.SmoothTransformation)
        self.pixmap_rect = self.pixmap_item.pixmap().rect()

        self.scale_image()

    def resizeEvent(self, event):
        super().resizeEvent(event)
        self.scale_image()

    def scale_image(self):
        if self.pixmap_item:
            # Get the viewport rectangle
            view_rect = self.viewport().rect()

            # Calculate the scale factor to fit the image within the viewport
            scale = min(view_rect.width() / self.pixmap_rect.width(),
                        view_rect.height() / self.pixmap_rect.height(),
                        1.0)

            # Create a scaling transformation
            transform = QTransform().scale(scale, scale)
            # Apply the scaling transformation to the pixmap item
            self.pixmap_item.setTransform(transform)

            # Calculate the scaled rectangle
            scaled_rect = transform.mapRect(self.pixmap_rect)
            # Calculate the x-position to center the image
            pos_x = (view_rect.width() - scaled_rect.width()) / 2
            # Calculate the y-position to center the image
            pos_y = (view_rect.height() - scaled_rect.height()) / 2

            # Set the position of the pixmap item to center the image
            self.pixmap_item.setPos(pos_x, pos_y)
            # Set the scene rectangle to match the viewport rectangle
            self.scene.setSceneRect(self.viewport().rect())

    def get_image(self) -> QImage:
        return self.original_image.copy()
