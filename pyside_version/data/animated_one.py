import sys
from PySide6.QtWidgets import QApplication, QGraphicsView, QGraphicsScene, QGraphicsPixmapItem, QVBoxLayout, QWidget
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt

class ZoomableImageView(QGraphicsView):
    def __init__(self, image_path):
        super().__init__()

        # Create a QGraphicsScene
        self.scene = QGraphicsScene(self)
        self.setScene(self.scene)

        # Load the image
        self.pixmap_item = QGraphicsPixmapItem(QPixmap(image_path))
        self.scene.addItem(self.pixmap_item)

        # Set the scene rectangle to fit the image
        self.setSceneRect(self.pixmap_item.pixmap().rect())

        # Enable mouse wheel zooming
        # self.setRenderHint(Q)
        # self.setRenderHint(Qt.SmoothPixmapTransform)

        # Initial scale factor
        self.scale_factor = 1.0

    def wheelEvent(self, event):
        # Zoom in or out
        if event.angleDelta().y() > 0:
            self.scale(1.2, 1.2)  # Zoom in
            self.scale_factor *= 1.2
        else:
            self.scale(1 / 1.2, 1 / 1.2)  # Zoom out
            self.scale_factor /= 1.2

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self._last_mouse_pos = event.pos()
            self.setDragMode(QGraphicsView.ScrollHandDrag)

    def mouseMoveEvent(self, event):
        if self.dragMode() == QGraphicsView.ScrollHandDrag:
            # Pan the view
            delta = event.pos() - self._last_mouse_pos
            self.horizontalScrollBar().setValue(self.horizontalScrollBar().value() - delta.x())
            self.verticalScrollBar().setValue(self.verticalScrollBar().value() - delta.y())
            self._last_mouse_pos = event.pos()

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.setDragMode(QGraphicsView.NoDrag)

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Set the layout
        layout = QVBoxLayout()
        self.setLayout(layout)

        # Create the zoomable image view
        self.image_view = ZoomableImageView(r"C:\Users\rozes\OneDrive\Pictures\b0fbnuew8zcd1.jpeg")  # Replace with your image path
        layout.addWidget(self.image_view)

        self.setWindowTitle("Zoomable Image Viewer")
        self.resize(800, 600)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
