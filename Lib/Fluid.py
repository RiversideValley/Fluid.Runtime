from System import Branding;

Location = __file__.removesuffix(f"{Branding.Slash}Fluid.py")
Extension = "py" # Change this when support added for Fluid's own file extension.

try:
    from Riverside import Runtime;
    
except ImportError:
    pass

try:
    from Riverside import UI;
    
except ImportError:
    pass

class Exception:
    class Maloote(Exception):
        """Fluid.Exception.Maloote
        
        Inexplicable error; use for easter eggs in applications.
        Also impossible to solve error. (an unrecoverable fatal error)
        """
        ...

    class ArgumentError(Exception):
        """Fluid.Exception.ArgumentError
        
        There was a problem processing the function or class's request arguments.
        """
        ...
        
    class FoundationCloneError(Exception):
        """Fluid.Exception.FoundationCloneError
        
        There was a problem cloning the Foundation package.
        """
        
    class FrameworkArchitectureError(Exception):
        """Fluid.Exception.FrameworkArchitectureError
        
        An error occured due to the way the Python and C-based Fluid backends were built which contradicts the code of the Fluid Runtime."""
    