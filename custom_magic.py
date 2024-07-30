import io
import os
from nbformat import write, v4
from IPython.core import magic_arguments
from IPython.core.magic import line_magic, Magics, magics_class

@magics_class
class CustomMagics(Magics):
    
    @magic_arguments.magic_arguments()
    @magic_arguments.argument(
        'filename', type=str,
        help='Notebook name or filename'
    )
    @line_magic
    def custom_notebook(self, line):
        """Export and convert IPython notebooks.

        This function can export the current IPython history to a notebook file.
        For example, to export the history to "foo.ipynb" do "%custom_notebook foo.ipynb".
        """
        args = magic_arguments.parse_argstring(self.custom_notebook, line)
        outfname = os.path.expanduser(args.filename)

        cells = []
        hist = list(self.shell.history_manager.get_range())
        if len(hist) <= 1:
            raise ValueError('History is empty, cannot export')
        
        for session, execution_count, source in hist[:-1] + [hist[-1]]:
            cells.append(v4.new_code_cell(
                execution_count=execution_count,
                source=source
            ))
        
        nb = v4.new_notebook(cells=cells)
        with io.open(outfname, "w", encoding="utf-8") as f:
            write(nb, f, version=4)

def load_ipython_extension(ipython):
    ipython.register_magics(CustomMagics)
