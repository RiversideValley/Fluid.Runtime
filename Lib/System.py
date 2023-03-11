"""System

A professional yet usable programming framework.
"""

class Legacy:
    """System.Legacy
    
    Foundation class for the purpose of providing legacy Python modules for more.. refined use."""
    class Stat:
        """Constants/functions for interpreting results of os.stat() and os.lstat().

        Suggested usage: from stat import *
        """

        # Indices for stat struct members in the tuple returned by os.stat()

        ST_MODE  = 0
        ST_INO   = 1
        ST_DEV   = 2
        ST_NLINK = 3
        ST_UID   = 4
        ST_GID   = 5
        ST_SIZE  = 6
        ST_ATIME = 7
        ST_MTIME = 8
        ST_CTIME = 9

        # Extract bits from the mode

        def S_IMODE(mode):
            """Return the portion of the file's mode that can be set by
            os.chmod().
            """
            return mode & 0o7777

        def S_IFMT(mode):
            """Return the portion of the file's mode that describes the
            file type.
            """
            return mode & 0o170000

        # Constants used as S_IFMT() for various file types
        # (not all are implemented on all systems)

        S_IFDIR  = 0o040000  # directory
        S_IFCHR  = 0o020000  # character device
        S_IFBLK  = 0o060000  # block device
        S_IFREG  = 0o100000  # regular file
        S_IFIFO  = 0o010000  # fifo (named pipe)
        S_IFLNK  = 0o120000  # symbolic link
        S_IFSOCK = 0o140000  # socket file
        # Fallbacks for uncommon platform-specific constants
        S_IFDOOR = 0
        S_IFPORT = 0
        S_IFWHT = 0

        # Functions to test for each file type

        def S_ISDIR(mode):
            """Return True if mode is from a directory."""
            return S_IFMT(mode) == S_IFDIR

        def S_ISCHR(mode):
            """Return True if mode is from a character special device file."""
            return S_IFMT(mode) == S_IFCHR

        def S_ISBLK(mode):
            """Return True if mode is from a block special device file."""
            return S_IFMT(mode) == S_IFBLK

        def S_ISREG(mode):
            """Return True if mode is from a regular file."""
            return S_IFMT(mode) == S_IFREG

        def S_ISFIFO(mode):
            """Return True if mode is from a FIFO (named pipe)."""
            return S_IFMT(mode) == S_IFIFO

        def S_ISLNK(mode):
            """Return True if mode is from a symbolic link."""
            return S_IFMT(mode) == S_IFLNK

        def S_ISSOCK(mode):
            """Return True if mode is from a socket."""
            return S_IFMT(mode) == S_IFSOCK

        def S_ISDOOR(mode):
            """Return True if mode is from a door."""
            return False

        def S_ISPORT(mode):
            """Return True if mode is from an event port."""
            return False

        def S_ISWHT(mode):
            """Return True if mode is from a whiteout."""
            return False

        # Names for permission bits

        S_ISUID = 0o4000  # set UID bit
        S_ISGID = 0o2000  # set GID bit
        S_ENFMT = S_ISGID # file locking enforcement
        S_ISVTX = 0o1000  # sticky bit
        S_IREAD = 0o0400  # Unix V7 synonym for S_IRUSR
        S_IWRITE = 0o0200 # Unix V7 synonym for S_IWUSR
        S_IEXEC = 0o0100  # Unix V7 synonym for S_IXUSR
        S_IRWXU = 0o0700  # mask for owner permissions
        S_IRUSR = 0o0400  # read by owner
        S_IWUSR = 0o0200  # write by owner
        S_IXUSR = 0o0100  # execute by owner
        S_IRWXG = 0o0070  # mask for group permissions
        S_IRGRP = 0o0040  # read by group
        S_IWGRP = 0o0020  # write by group
        S_IXGRP = 0o0010  # execute by group
        S_IRWXO = 0o0007  # mask for others (not in group) permissions
        S_IROTH = 0o0004  # read by others
        S_IWOTH = 0o0002  # write by others
        S_IXOTH = 0o0001  # execute by others

        # Names for file flags

        UF_NODUMP    = 0x00000001  # do not dump file
        UF_IMMUTABLE = 0x00000002  # file may not be changed
        UF_APPEND    = 0x00000004  # file may only be appended to
        UF_OPAQUE    = 0x00000008  # directory is opaque when viewed through a union stack
        UF_NOUNLINK  = 0x00000010  # file may not be renamed or deleted
        UF_COMPRESSED = 0x00000020 # OS X: file is hfs-compressed
        UF_HIDDEN    = 0x00008000  # OS X: file should not be displayed
        SF_ARCHIVED  = 0x00010000  # file may be archived
        SF_IMMUTABLE = 0x00020000  # file may not be changed
        SF_APPEND    = 0x00040000  # file may only be appended to
        SF_NOUNLINK  = 0x00100000  # file may not be renamed or deleted
        SF_SNAPSHOT  = 0x00200000  # file is a snapshot file


        _filemode_table = (
            ((S_IFLNK,         "l"),
             (S_IFSOCK,        "s"),  # Must appear before IFREG and IFDIR as IFSOCK == IFREG | IFDIR
             (S_IFREG,         "-"),
             (S_IFBLK,         "b"),
             (S_IFDIR,         "d"),
             (S_IFCHR,         "c"),
             (S_IFIFO,         "p")),
        
            ((S_IRUSR,         "r"),),
            ((S_IWUSR,         "w"),),
            ((S_IXUSR|S_ISUID, "s"),
             (S_ISUID,         "S"),
             (S_IXUSR,         "x")),

            ((S_IRGRP,         "r"),),
            ((S_IWGRP,         "w"),),
            ((S_IXGRP|S_ISGID, "s"),
             (S_ISGID,         "S"),
             (S_IXGRP,         "x")),
        
            ((S_IROTH,         "r"),),
            ((S_IWOTH,         "w"),),
            ((S_IXOTH|S_ISVTX, "t"),
             (S_ISVTX,         "T"),
             (S_IXOTH,         "x"))
        )

        def filemode(mode):
            """Convert a file's mode to a string of the form '-rwxrwxrwx'."""
            perm = []
            for table in _filemode_table:
                for bit, char in table:
                    if mode & bit == bit:
                        perm.append(char)
                        break
                else:
                    perm.append("-")
            return "".join(perm)


        # Windows FILE_ATTRIBUTE constants for interpreting os.stat()'s
        # "st_file_attributes" member

        FILE_ATTRIBUTE_ARCHIVE = 32
        FILE_ATTRIBUTE_COMPRESSED = 2048
        FILE_ATTRIBUTE_DEVICE = 64
        FILE_ATTRIBUTE_DIRECTORY = 16
        FILE_ATTRIBUTE_ENCRYPTED = 16384
        FILE_ATTRIBUTE_HIDDEN = 2
        FILE_ATTRIBUTE_INTEGRITY_STREAM = 32768
        FILE_ATTRIBUTE_NORMAL = 128
        FILE_ATTRIBUTE_NOT_CONTENT_INDEXED = 8192
        FILE_ATTRIBUTE_NO_SCRUB_DATA = 131072
        FILE_ATTRIBUTE_OFFLINE = 4096
        FILE_ATTRIBUTE_READONLY = 1
        FILE_ATTRIBUTE_REPARSE_POINT = 1024
        FILE_ATTRIBUTE_SPARSE_FILE = 512
        FILE_ATTRIBUTE_SYSTEM = 4
        FILE_ATTRIBUTE_TEMPORARY = 256
        FILE_ATTRIBUTE_VIRTUAL = 65536


        # If available, use C implementation
        try:
            from _stat import *
        except ImportError:
            pass

    from Legacy import os as _os;
    import sys as _sys;
    from Legacy import pathlib as _path;
    from Legacy import zipimport as _zip;
    from Legacy import csv as _csv;
    from Legacy import turtle as _turtle;
    from Legacy import socket as _socket;
    from Legacy import random as _random;
    from Legacy import subprocess as _process;
    import time as _time;

Null = type[None]
Object = object

class Branding:
    """System.Branding
    
    Get computer details, interpreter details and other variables."""

    # Windows, Microsoft
    Windows = "win32"
    Win = Windows
    Microsoft = Windows
    MSDOS = Windows
    # Cygwin
    Cygwin = "cygwin"
    # macOS, Apple
    macOS = "darwin"
    MacOS = macOS
    Apple = macOS
    Darwin = macOS
    OSX = macOS
    macOSX = macOS
    # Unix
    Unix = macOS or "linux"
    # Linux, Unix
    Linux = "linux"
    # AIX, IBM
    Aix = "aix"
    # Emscripten, WebAssembly
    Emscripten = "emscripten"
    # WebAssembly
    WebAssembly = "wasi"
    WebAssembleySystemInterface = WebAssembly
    Web = WebAssembly
    class Computer:
        """System.Branding.Computer"""
        Name = Legacy._socket.gethostname()
        Interpreter = Legacy._sys.platform
        Register = Legacy._os.name

    Model = Computer
    class User:
        """System.Branding.User"""
        Login = Legacy._os.getlogin()
        UserName = f"{Login}@{Legacy._socket.gethostname()}"

class Variables:
    def Environment(EnvironmentVariable: str):
        return Legacy._os.environ[EnvironmentVariable] 
    class Convert:
        def String(ToVariable):
            return str(ToVariable)
    
        def Integer(ToVariable):
            return int(ToVariable)

        def Float(ToVariable):
            return float(ToVariable)
        
        def Boolean(ToVariable):
            return bool(ToVariable)
        
    class String(Object):
        def __init__(This, String: str):
            This.String = String

        def __str__(This):
            return This.String
        
        def Convert(ToVariable):
            return str(ToVariable)
        
    def Search(Index, Key, MatchFullWord: bool = True):
        if MatchFullWord == False:
            return (" " + str(Key) + " ") in (" " + str(Index) + " ")
        else:
            return str(Key) in str(Index)
        
class Processing:
    """System.Processing
    
    Foundation class for the purpose of spawning, viewing and managing processes on the user's computer."""

    def Execute(ExecuteScript, ScriptTimeOut = Null, Language: str = "fl", IncludeFoundation = Null):
        """System.Execute()
    
        Foundation method for the purpose of executing Python code from a string."""
        if Language == "fl" or "py":
            if IncludeFoundation is not Null:
#               try:
                return exec(Variables.Convert.String(ExecuteScript), IncludeFoundation)
#               except NameError: # NameError is for when the person includes a Foundation module such as 'System' without using the 'IncludeFoundation' parameter.
#                   if Variables.Search(ExecuteScript, "System") is True:
#                       return exec(ExecuteScript, {"System.Console":Console})
            else:
                return exec(Variables.Convert.String(ExecuteScript))
        elif Language == "bash" or "cmd" or "command" or "cmd.exe" or "/bin/bash" or "pwsh" or "pwsh-core" or "powershell" or "shell" or "prompt" or "os.system()" or "system":
            return Legacy._process.call(ExecuteScript, timeout = ScriptTimeOut)
        else:
            raise NotImplementedError

    #class Task(Object):
        #if Branding.Computer.Interpreter is 
        #def __init__(This, Task: str, Task):



class Console:
    """System.Console

    Foundation class for the purpose of displaying plain text on the console, particularly for debugging or logging.
    Also comes with an advanced logger to format logs neatly in the console.
    Not recommended for actual text display as part of a GUI application; use only for logging purposes.
    """

    def WriteLine(Text: Null): # type: ignore
        return print(Variables.Convert.String(Text))

    def Write(Text: Null): # type: ignore
        return print(Variables.Convert.String(Text), end="")

class Chronology:
    def Time(TimeZone: str, WithSeconds=None):
        if TimeZone == "UCT":
            if WithSeconds == True:
                return Null # TODO: implement time with seconds
                return f"{Legacy._time.gmtime().tm_hour}:{Legacy._time.gmtime().tm_min}:{Legacy._time.gmtime().tm_sec}"
            else:
                return f"{Legacy._time.gmtime().tm_hour}:{Legacy._time.gmtime().tm_min}"

class Explore:
    """System.Explore

    Foundation class for the purpose of allowing the developer to read, write and make new files on the end-user's computer.
    """

    def Read(FileName: str, Auto: bool | Null, FileEncoding: str | Null):
        """System.Explore.Read()

        Foundation method for the purpose of a allowing the developer to read files on the end-user's computer.
        """
        if Auto == False:
            return open(FileName, "r", encoding = FileEncoding)
        else:
            return open(FileName, "r", encoding = FileEncoding).read()
    # type: ignore   
    def Write(FileName: str, Auto: bool | Null, AutoValue: str | Null, FileEncoding: Null):     
        """System.Explore.Write()

        Foundation method for the purpose of a allowing the developer to write files on the end-user's computer.
        """
        if Auto == False:
            return open(FileName, "w", encoding = FileEncoding)
        else:
            return open(FileName, "w", encoding = FileEncoding).write(Variables.String.Convert(AutoValue))

    def Append(FileName: str, Auto: bool | Null, AutoValue: Null, FileEncoding: Null):
        """System.Explore.Append()

        Foundation method for the purpose of a allowing the developer to append to files on the end-user's computer.
        """
        if Auto == False:
            return open(FileName, "a", encoding = FileEncoding)
        else:
            return open(FileName, "a", encoding = FileEncoding).write(AutoValue)

    def Create(FileName: str, FileEncoding: str | Null):
        """System.Explore.Create()

        Foundation method for the purpose of a allowing the developer to create files on the end-user's computer.
        """
        return open(FileName, "x", encoding = FileEncoding)

    def Access(FileName: str, FileEncoding: str | Null):
        """System.Explore.Access()

        Foundation method for the purpose of a allowing the developer to access files completely on the end-user's computer.
        """
        return open(FileName, "r+", encoding = FileEncoding)

class Packaging:
    """System.Packaging
    
    An advanced Foundation class enabling the developer to properly package their application.
    """
    class App(Object):
        """System.Packaging.Package"""
