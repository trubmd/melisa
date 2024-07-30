import sys
import os
from qtpy import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QFileDialog, QDialog
from PyQt5.QtCore import QFileInfo, QEventLoop
import nbformat
from qtconsole.rich_jupyter_widget import RichJupyterWidget
from qtconsole.manager import QtKernelManager

USE_KERNEL = 'sagemath'

def make_jupyter_widget_with_kernel():

    kernel_manager = QtKernelManager(kernel_name=USE_KERNEL)
    kernel_manager.start_kernel()

    kernel_client = kernel_manager.client()
    kernel_client.start_channels()

    jupyter_widget = RichJupyterWidget()
    jupyter_widget._display_banner = False
    jupyter_widget.kernel_manager = kernel_manager
    jupyter_widget.kernel_client = kernel_client
    return jupyter_widget

class MainWindow(QtWidgets.QMainWindow):
    counter = 0
    def __init__(self):
        super().__init__()
        MainWindow.counter += 1
        self.setWindowTitle(f"Untitled-{MainWindow.counter}  -  Melisa 1.0")
        self.jupyter_widget = make_jupyter_widget_with_kernel()
        self.setCentralWidget(self.jupyter_widget)
        self.jupyter_widget.kernel_client.execute('pretty_print_default(True)',silent=True)
        self.jupyter_widget.kernel_client.execute('%load_ext custom_magic',silent=True)
        


        self.other_windows = []
        menubar = self.menuBar()

        file_menu = menubar.addMenu("Файл")

        new_action = QAction('Новый документ', self)
        new_action.triggered.connect(self.new_window)
        file_menu.addAction(new_action)

        open_action = QAction('Открыть', self)
        open_action.triggered.connect(self.open_notebook)
        file_menu.addAction(open_action)

        opennew_action = QAction('Открыть в новом окне', self)
        opennew_action.triggered.connect(self.open_notebook_in_new_window)
        file_menu.addAction(opennew_action)
        
        save_action = QAction('Сохранить', self)
        save_action.triggered.connect(self.save_notebook)
        file_menu.addAction(save_action)

        file_menu.addSeparator()  # Добавление разделителя

        exit_action = QAction('Выход', self)
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)

    def new_window(self):
        new_main_window = MainWindow()
        self.other_windows.append(new_main_window)  # сохраняем ссылку на новое окно
        new_main_window.show()
    def on_cell_executed(self):
        self.loop.quit()
    def open_notebook(self):
        # Открываем диалоговое окно для выбора файла
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        file_name, _ = QFileDialog.getOpenFileName(self, "Открыть блокнот Jupyter", "", "Jupyter Notebooks (*.ipynb)", options=options)

        if file_name:
            # Загружаем содержимое блокнота Jupyter
            # Устанавливаем имя файла как заголовок нового окна
            base_name, file_extension = os.path.splitext(os.path.basename(file_name))
            self.setWindowTitle(f"{base_name} - Melisa 1.0")
                
            with open(file_name, 'r') as notebook_file:
                notebook_contents = notebook_file.read()

            # Преобразуем содержимое файла в объект nbformat
            notebook = nbformat.reads(notebook_contents, as_version=4)

            # Выполняем код в ячейках блокнота
            self.loop = QEventLoop()
            self.jupyter_widget.executed.connect(self.on_cell_executed)
            for cell in notebook.cells:
                if cell.cell_type == "code":
                    self.jupyter_widget.execute(cell.source)
                    self.loop.exec_() # Здесь поток будет заблокирован до выполнения ячейки

            self.jupyter_widget.executed.disconnect(self.on_cell_executed)
    
    def open_notebook_in_new_window(self):
        # Открываем диалоговое окно для выбора файла
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        file_name, _ = QFileDialog.getOpenFileName(self, "Открыть блокнот Jupyter", "", "Jupyter Notebooks (*.ipynb)", options=options)

        if file_name:
                # Создаем новое окно
                new_window = MainWindow()

                # Устанавливаем имя файла как заголовок нового окна
                base_name, file_extension = os.path.splitext(os.path.basename(file_name))
                new_window.setWindowTitle(f"{base_name} - Melisa 1.0")
                
                # Показываем новое окно
                new_window.show()

                # Загружаем содержимое блокнота Jupyter
                with open(file_name, 'r') as notebook_file:
                    notebook_contents = notebook_file.read()

                # Преобразуем содержимое файла в объект nbformat
                notebook = nbformat.reads(notebook_contents, as_version=4)

                # Выполняем код в ячейках блокнота
                new_window.loop = QEventLoop()
  
               # Создаем локально временную функцию для обработки и сигнала о выполнении ячейки
                def cell_executed():
                    # После выполнения ячейки отключаем сигнал и выполняем следующую итерацию внешнего цикла
                    new_window.jupyter_widget.executed.disconnect(local_slot)
                    new_window.loop.quit()
                    local_slot = lambda: cell_executed()
                for cell in notebook.cells:
                    if cell.cell_type == "code":
                        # Выполняем текущую ячейку
                        new_window.jupyter_widget.kernel_client.execute(cell.source)

                        # Ждем, пока ячейка выполнится
                        while not new_window.jupyter_widget.executed:
                            new_window.loop.processEvents()
    def save_notebook(self):
            
        dialog = QFileDialog(self)
        dialog.setWindowTitle("Сохранить")


        dialog.setNameFilter("Notebook (*.ipynb)")


        dialog.setAcceptMode(QFileDialog.AcceptSave)
        dialog.setDefaultSuffix("ipynb")
        dialog.selectFile("untitled.ipynb")

        if dialog.exec_() == QDialog.Accepted:
            file_path = dialog.selectedFiles()[0]
            name = QFileInfo(file_path).fileName().split('.')[0] or 'untitled'

            self.jupyter_widget.kernel_client.execute(f" ")
            self.jupyter_widget.kernel_client.execute(f"%custom_notebook {file_path}",silent=True)

            base_name, file_extension = os.path.splitext(os.path.basename(file_path))
            self.setWindowTitle(f"{base_name} - Melisa 1.0")

    def shutdown_kernel(self):
        #print('Выключение ядра...')
        self.jupyter_widget.kernel_client.stop_channels()
        self.jupyter_widget.kernel_manager.shutdown_kernel()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.aboutToQuit.connect(window.shutdown_kernel)
    sys.exit(app.exec_())
