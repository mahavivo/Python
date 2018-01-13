# code snippet to include in your sitecustomize.py
import sys
def info(type, value, tb):
    if hasattr(sys, 'ps1') or not (
          sys.stderr.isatty() and sys.stdin.isatty()
          ) or issubclass(type, SyntaxError):
        # Interactive mode, no tty-like device, or syntax error: nothing
        # to do but call the default hook
        sys.__excepthook__(type, value, tb)
    else:
        import traceback, pdb
        # You are NOT in interactive mode; so, print the exception...
        traceback.print_exception(type, value, tb)
        print
        # ...then start the debugger in post-mortem mode
        pdb.pm()
sys.excepthook = info
