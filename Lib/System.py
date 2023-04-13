"""System

A professional yet usable programming framework.
"""

# RequirerDataPolicy:
# The RequirerDataPolicy class is used to define the dependencies of System's classes.
# Legacy.Os:
# - abc
# - sys ✅
# - stat ✅
# - _collections_abc
# - nt
# - posix
# - posixpath
# ...
# Branding.User.Interface.DarkDetect:
# - typing
# - subprocess
# - ctypes
# - sys ✅
# - os ✅
# - pathlib
# - Foundation (😕) 
# - PyObjCTools

class Legacy:
    """System.Legacy
    
    Foundation class for the purpose of providing legacy Python modules for more.. refined use."""
    
    class _stat:
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
            """Return the portion of the file's mode that can be set b`y
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
            
    import sys as _sys;
#    from Legacy import pathlib as _path;
#    from Legacy import zipimport as _zip;
#    from Legacy import csv as _csv;
#    from Legacy import turtle as _turtle;
#    from Legacy import socket as _socket;
#    from Legacy import random as _random;
    from Legacy import subprocess as _process;
    import time as _time;
    
import Fluid;

GenericAlias = type(list[int])
Null = type[None] # Make sure Null is a type
Object = object # Make references to Object PascalCase to make code more readable

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
    
    def SlashInPaths():
        """System.Branding.SlashInPaths()
        
        Detect whether the computer uses backslashes or forwardslashes in paths.
        Returns True if there are forwardslashes, False if backslashes.
        """
        return "/" in Fluid.Location
    
    if SlashInPaths() is not True:
        Slash = "\\" # Windows
        
    else:
        Slash = "/" # Unix/Others
        
    class Computer:
        """System.Branding.Computer"""
        # Name = Legacy._socket.gethostname()
        Interpreter = Legacy._sys.platform
        # Register = Legacy._os.name
        class Platform:
            __copyright__ = """
                Inspired by Python's default Platform module.

                Copyright (c) 1999-2000, Marc-Andre Lemburg; mailto:mal@lemburg.com
                Copyright (c) 2000-2010, eGenix.com Software GmbH; mailto:info@egenix.com
                Permission to use, copy, modify, and distribute this software and its
                documentation for any purpose and without fee or royalty is hereby granted,
                provided that the above copyright notice appear in all copies and that
                both that copyright notice and this permission notice appear in
                supporting documentation or portions thereof, including modifications,
                that you make.
                EGENIX.COM SOFTWARE GMBH DISCLAIMS ALL WARRANTIES WITH REGARD TO
                THIS SOFTWARE, INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY AND
                FITNESS, IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY SPECIAL,
                INDIRECT OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING
                FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT,
                NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR IN CONNECTION
                WITH THE USE OR PERFORMANCE OF THIS SOFTWARE !
            """
            
            class Data:
                def macOSVersion():
                    DataSource = "/System/Library/CoreServices/SystemVersion.plist"

                    try:
                        import plistlib as PListLib;
                    except ImportError:
                        return Null

                    with open("/System/Library/CoreServices/SystemVersion.plist", "rb") as Data:
                        PList = PListLib.load(Data)
                    
                    Release = PList['ProductVersion']
                    Info = ("", "", "")
                    # Machine = os.uname().machine
                    # if Variables.Search(Machine, ("ppc", "Power Macintosh")):
                    #     Machine = 'PowerPC'

                    return Release, Info# , Machine
                
            def macOSVersion(Release="", Info=("", "", ""), Machine=""):
                if Info is not Null:
                    return Info

                # If that also doesn't work return the default values
                return Release, Info, Machine

    Model = Computer
    class User:
        """System.Branding.User"""
        # Login = Legacy._os.getlogin()
        # UserName = f"{Login}@{Legacy._socket.gethostname()}"
        class Interface:
            def DarkDetect():
                #-----------------------------------------------------------------------------
                #  Inspired by DarkDetect by Alberto Sottile (https://github.com/albertosottile/darkdetect)
                #  Copyright (C) 2019 Alberto Sottile
                #
                #  Distributed under the terms of the 3-clause BSD License.
                #-----------------------------------------------------------------------------
                
                def IsmacOSVersionSupported():
                    sysver = platform.mac_ver()[0] #typically 10.14.2 or 12.3
                    major = int(sysver.split('.')[0])
                    if major < 10:
                        return False
                    elif major >= 11:
                        return True
                    else:
                        minor = int(sysver.split('.')[1])
                        if minor < 14:
                            return False
                        else:
                            return True
                

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
        def __init__(self, String: str):
            self.String = String

        def __str__(self):
            return self.String
        
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

    def Execute(ExecuteScript, ScriptTimeOut = Null, Language: str = "fl", IncludeFoundation = []):
        """System.Processing.Execute()
    
        Foundation method for the purpose of executing Python code from a string."""
        if Language == "fl":
            if IncludeFoundation is not Null:
#               try:
                return exec(str(ExecuteScript), IncludeFoundation)
#               except NameError: # NameError is for when the person includes a Foundation module such as 'System' without using the 'IncludeFoundation' parameter.
#                   if Variables.Search(ExecuteScript, "System") is True:
#                       return exec(ExecuteScript, {"System.Console":Console})
            else:
                return exec(str(ExecuteScript))
            
        elif Language == "shell":
            if ScriptTimeOut is not Null:
                return Legacy._process.call(ExecuteScript, timeout = ScriptTimeOut)
            else:
                return Legacy._process.call(ExecuteScript)
        
        else:
            raise NotImplementedError
        
    def Halt(HaltTime: float): # type: ignore
        """System.Processing.Halt"""
        Legacy._time.sleep(HaltTime)

    #class Task(Object):
        #if Branding.Computer.Interpreter is 
        #def __init__(This, Task: str, Task):

class Chronology:
    """System.Chronology
    
    Foundation class for obtaining the current date and time, as well as other details.
    """
    class Time():
        """System.Chronology.Time
        
        Return the current time in the specified time zone.
        """
        def __init__(self, TimeZone = "Local", Form: str = "DateTime"):
            self.TimeZone = TimeZone
            self.Form = Form
            self.DataSource = Null
            
            if TimeZone == "UCT":
                self.DataSource = Legacy._time.gmtime()
                
            elif TimeZone == "Local":
                self.DataSource = Legacy._time.localtime()
                
            else:
                raise NotImplementedError("The specified time zone is not supported.")
            
            self.Year = self.DataSource.tm_year
            self.Month = self.DataSource.tm_mon
            self.Day = self.DataSource.tm_mday
            self.WeekDay = self.DataSource.tm_wday
            self.Hour = self.DataSource.tm_hour
            
            if self.DataSource.tm_isdst == 1:
                self.DaylightSavings = True
                
            elif self.DataSource.tm_isdst == 0:
                self.DaylightSavings = False
                
            else:
                raise ValueError("Daylight savings time could not be determined.")
        
        def __str__(self):
            """System.Chronology.Time.__str__
            
            Return the time in the specified time zone in ISO 8601 format.
            
            📝 Form argument should be either "Date", "DateTime", "Week" or "Ordinal". See https://wikipedia.org/wiki/ISO_8601 for more information.
            """
            
            if self.Form == "Date" or "DateTime" or "Week" or "WeekWeekDay" or "Ordinal":
                if self.TimeZone == "UCT":
                    if self.Form == "Date":
                        return f"{self.DataSource.tm_year}-{self.DataSource.tm_mon}-{self.DataSource.tm_mday}"
                    
                    elif self.Form == "DateTime":
                        return f"{self.DataSource.tm_year}-{self.DataSource.tm_mon}-{self.DataSource.tm_mday}T{self.DataSource.tm_hour}:{self.DataSource.tm_min}:{self.DataSource.tm_sec}Z"
                    
                    elif self.Form == "Week":
                        return f"{self.DataSource.tm_year}-W{self.DataSource.tm_wday}"
                    
                    elif self.Form == "WeekWeekDay":
                        return f"{self.DataSource.tm_year}-W{self.DataSource.tm_wday}-{self.DataSource.tm_wday}"
                    
                    elif self.Form == "Ordinal":
                        return f"{self.DataSource.tm_year}-{self.DataSource.tm_yday}"
                
                elif self.TimeZone == "Local":
                    if self.Form == "Date":
                        return f"{self.DataSource.tm_year}-{self.DataSource.tm_mon}-{self.DataSource.tm_mday}"
                    
                    elif self.Form == "DateTime":
                        return f"{self.DataSource.tm_year}-{self.DataSource.tm_mon}-{self.DataSource.tm_mday}T{self.DataSource.tm_hour}:{self.DataSource.tm_min}:{self.DataSource.tm_sec}"
                    
                    elif self.Form == "Week":
                        return f"{self.DataSource.tm_year}-W{self.DataSource.tm_wday}"
                    
                    elif self.Form == "Ordinal":
                        return f"{self.DataSource.tm_year}-{self.DataSource.tm_yday}"
                
                else:
                    raise NotImplementedError("The specified time zone is not supported.")
                
            else:
                raise Fluid.Exception.ArgumentError("The specified format is not supported.")
            
        def Minute(self, WithSeconds = False):
            """System.Chronology.Time.Minute
            
            Returns the time with the minute or seconds.
            """
            if self.TimeZone == "UCT":
                if WithSeconds is True:
                    return f"{self.DataSource.tm_hour}:{self.DataSource.tm_min}:{self.DataSource.tm_sec}"
                else:
                    return f"{self.DataSource.tm_hour}:{self.DataSource.tm_min}"
            
            elif self.TimeZone == "Local":
                if WithSeconds is True:
                    return f"{self.DataSource.tm_hour}:{self.DataSource.tm_min}:{self.DataSource.tm_sec}"
                else:
                    return f"{self.DataSource.tm_hour}:{self.DataSource.tm_min}"
            
            else:
                raise NotImplementedError("The specified time zone is not supported.")
            
class Console:
    """System.Console

    Foundation class for the purpose of displaying plain text on the console, particularly for debugging or logging.
    Also comes with an advanced logger to format logs neatly in the console.
    Not recommended for actual text display as part of a GUI application; use only for logging purposes.
    """

    def WriteLine(Text: any): # type: ignore
        return print(Text)

    def Write(Text: any): # type: ignore
        return print(Text, end="")
    
    class Log():
        """System.Console.Log
        
        Very advanced version of System.Console.WriteLine() that formats logs neatly in the console.
        """
        
        def __init__(self, Log: str = "", LogType: str = "INFO", LogTimeZone: str = "Local"):
            
            self.Log = Log
            self.LogType = LogType
            self.LogTimeZone = LogTimeZone

            self.LogDate = Chronology.Time(self.LogTimeZone, "DateTime")

            self.LogType = self.LogType.upper()

            self.LogDate = f"[{self.LogDate}]"
            
            self.ValidLogTypes = ["INFO", "WARNING", "ERROR", "DEBUG", "FATAL"]
            
            if self.LogType not in self.ValidLogTypes:
                raise Fluid.Exception.ArgumentError("The specified log type is not supported.")
            
            self.Log = f"{self.LogDate} |{self.LogType[0:1]}| {self.Log}"
            
            print(self.Log)
            
        def __str__(self):
            return self.Log

class Explore:
    """System.Explore

    Foundation class for the purpose of allowing the developer to read, write and make new files on the end-user's computer.
    """
    
    def __init__(self, FileName: str, Auto: bool = True, AutoValue: str = "", FileEncoding = "utf-8"):
        self.FileName = FileName
        self.Auto = Auto
        self.AutoValue = AutoValue
        self.FileEncoding = FileEncoding
        self.GetWorkingDirectory = Fluid.Location
        
    def __str__(self):
        raise Fluid.Exception.ArgumentError("You must use a function inside the System.Explore class in order to explore your computer.")
    
    def IsFile(self):
        """System.Explore.IsFile()

        Foundation method for the purpose of a allowing the developer to check if a file exists on the end-user's computer.
        """
        
        try:
            open(self.FileName, "r", encoding = self.FileEncoding)
            return True
            
        except FileNotFoundError:
            return False
        
        except:
            raise RuntimeError("An unknown error has occurred.")

    def Read(self): # type: ignore
        """System.Explore.Read()

        Foundation method for the purpose of a allowing the developer to read files on the end-user's computer.
        """
        if self.Auto is not False:
            return str(open(self.FileName, "r", encoding = self.FileEncoding).read())
        else:
            return open(self.FileName, "r", encoding = self.FileEncoding)

    def Write(self): # type: ignore   
        """System.Explore.Write()

        Foundation method for the purpose of a allowing the developer to write files on the end-user's computer.
        """
        if self.Auto == False:
            return open(self.FileName, "w", encoding = self.FileEncoding)
        else:
            return open(self.FileName, "w", encoding = self.FileEncoding).write(self.AutoValue)

    def Append(self): # type: ignore
        """System.Explore.Append()

        Foundation method for the purpose of a allowing the developer to append to files on the end-user's computer.
        """
        if self.Auto == False:
            return open(self.FileName, "a", encoding = self.FileEncoding)
        else:
            return open(self.FileName, "a", encoding = self.FileEncoding).write(self.AutoValue)

    def Create(self): # type: ignore
        """System.Explore.Create()

        Foundation method for the purpose of a allowing the developer to create files on the end-user's computer.
        """
        return open(self.FileName, "x", encoding = self.FileEncoding)

    def Access(self): # type: ignore
        """System.Explore.Access()

        Foundation method for the purpose of a allowing the developer to access files completely on the end-user's computer.
        """
        return open(self.FileName, "r+", encoding = self.FileEncoding)

class Packaging:
    """System.Packaging
    
    An advanced Foundation class enabling the developer to properly package their application.
    """
    
    class License():
        """System.Packaging.License
        
        Foundation class object which defines a license and its metadata.
        """
        
        def __init__(self, Name: str, CopyrightHolder: str, Contents: str = "", Year = Chronology.Time().Year):
            self.Name = Name
            self.CopyrightHolder = CopyrightHolder
            self.Year = Year
            
            if Contents != Null:
                self.Contents = Contents
                
        def __str__(self):
            if self.Contents != "":
                return f"{self.Name}\n\n{self.Contents}"
            
            elif self.Contents == "":
                # TODO: Add more licenses.
                
                if self.Name == "MIT":
                    return f"{self.Name}\n\nCopyright {self.Year} {self.CopyrightHolder}\n\nPermission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the \"Software\"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:\n\nThe above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.\n\nTHE SOFTWARE IS PROVIDED \"AS IS\", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE."
                
                elif self.Name == "Apache 2.0":
                    return f"{self.Name}\n\nLicensed under the Apache License, Version 2.0 (the \"License\"); you may not use this file except in compliance with the License. You may obtain a copy of the License at\n\nhttp://www.apache.org/licenses/LICENSE-2.0\n\nUnless required by applicable law or agreed to in writing, software distributed under the License is distributed on an \"AS IS\" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License."
                
                elif self.Name == "GPL 3.0":
                    return f"{self.Name}\n\nThis program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.\n\nThis program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.\n\nYou should have received a copy of the GNU General Public License along with this program. If not, see http://www.gnu.org/licenses/."

                elif self.Name == "LGPL 3.0":
                    return f"{self.Name}\n\nThis library is free software; you can redistribute it and/or modify it under the terms of the GNU Lesser General Public License as published by the Free Software Foundation; either version 3 of the License, or (at your option) any later version.\n\nThis library is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU Lesser General Public License for more details.\n\nYou should have received a copy of the GNU Lesser General Public License along with this library. If not, see http://www.gnu.org/licenses/."
                
                elif self.Name == "AGPL 3.0":
                    return f"{self.Name}\n\nThis program is free software: you can redistribute it and/or modify it under the terms of the GNU Affero General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.\n\nThis program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU Affero General Public License for more details.\n\nYou should have received a copy of the GNU Affero General Public License along with this program. If not, see http://www.gnu.org/licenses/."
                
                elif self.Name == "MPL 2.0":
                    return f"{self.Name}\n\nThis Source Code Form is subject to the terms of the Mozilla Public License, v. 2.0. If a copy of the MPL was not distributed with this file, You can obtain one at http://mozilla.org/MPL/2.0/."
                
                elif self.Name == "Unlicense":
                    return f"{self.Name}\n\nThis is free and unencumbered software released into the public domain.\n\nAnyone is free to copy, modify, publish, use, compile, sell, or\n\nDistribute this software, either in source code form or as a compiled\n\nbinary, for any purpose, commercial or non-commercial, and by any\n\nmeans.\n\nIn jurisdictions that recognize copyright laws, the author or authors\n\nof this software dedicate any and all copyright interest in the\n\nsoftware to the public domain. We make this dedication for the benefit\n\nof the public at large and to the detriment of our heirs and\n\nsuccessors. We intend this dedication to be an overt act of\n\nrelinquishment in perpetuity of all present and future rights to this\n\nsoftware under copyright law.\n\nTHE SOFTWARE IS PROVIDED \"AS IS\", WITHOUT WARRANTY OF ANY KIND,\n\nEXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF\n\nMERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.\n\nIN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR\n\nOTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,\n\nARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR\n\nOTHER DEALINGS IN THE SOFTWARE.\n\nFor more information, please refer to <http://unlicense.org/>"
                
                elif self.Name == "CC0 1.0":
                    return f"""{self.Name}\n\nCREATIVE COMMONS CORPORATION IS NOT A LAW FIRM AND DOES NOT PROVIDE LEGAL SERVICES. DISTRIBUTION OF THIS DOCUMENT DOES NOT CREATE AN ATTORNEY-CLIENT RELATIONSHIP. CREATIVE COMMONS PROVIDES THIS INFORMATION ON AN "AS-IS" BASIS. CREATIVE COMMONS MAKES NO WARRANTIES REGARDING THE USE OF THIS DOCUMENT OR THE INFORMATION OR WORKS PROVIDED HEREUNDER, AND DISCLAIMS LIABILITY FOR DAMAGES RESULTING FROM THE USE OF THIS DOCUMENT OR THE INFORMATION OR WORKS PROVIDED HEREUNDER.
Statement of Purpose
The laws of most jurisdictions throughout the world automatically confer exclusive Copyright and Related Rights (defined below) upon the creator and subsequent owner(s) (each and all, an "owner") of an original work of authorship and/or a database (each, a "Work").

Certain owners wish to permanently relinquish those rights to a Work for the purpose of contributing to a commons of creative, cultural and scientific works ("Commons") that the public can reliably and without fear of later claims of infringement build upon, modify, incorporate in other works, reuse and redistribute as freely as possible in any form whatsoever and for any purposes, including without limitation commercial purposes. These owners may contribute to the Commons to promote the ideal of a free culture and the further production of creative, cultural and scientific works, or to gain reputation or greater distribution for their Work in part through the use and efforts of others.

For these and/or other purposes and motivations, and without any expectation of additional consideration or compensation, the person associating CC0 with a Work (the "Affirmer"), to the extent that he or she is an owner of Copyright and Related Rights in the Work, voluntarily elects to apply CC0 to the Work and publicly distribute the Work under its terms, with knowledge of his or her Copyright and Related Rights in the Work and the meaning and intended legal effect of CC0 on those rights.

1. Copyright and Related Rights. A Work made available under CC0 may be protected by copyright and related or neighboring rights ("Copyright and Related Rights"). Copyright and Related Rights include, but are not limited to, the following:

the right to reproduce, adapt, distribute, perform, display, communicate, and translate a Work;
moral rights retained by the original author(s) and/or performer(s);
publicity and privacy rights pertaining to a person's image or likeness depicted in a Work;
rights protecting against unfair competition in regards to a Work, subject to the limitations in paragraph 4(a), below;
rights protecting the extraction, dissemination, use and reuse of data in a Work;
database rights (such as those arising under Directive 96/9/EC of the European Parliament and of the Council of 11 March 1996 on the legal protection of databases, and under any national implementation thereof, including any amended or successor version of such directive); and
other similar, equivalent or corresponding rights throughout the world based on applicable law or treaty, and any national implementations thereof.
2. Waiver. To the greatest extent permitted by, but not in contravention of, applicable law, Affirmer hereby overtly, fully, permanently, irrevocably and unconditionally waives, abandons, and surrenders all of Affirmer's Copyright and Related Rights and associated claims and causes of action, whether now known or unknown (including existing as well as future claims and causes of action), in the Work (i) in all territories worldwide, (ii) for the maximum duration provided by applicable law or treaty (including future time extensions), (iii) in any current or future medium and for any number of copies, and (iv) for any purpose whatsoever, including without limitation commercial, advertising or promotional purposes (the "Waiver"). Affirmer makes the Waiver for the benefit of each member of the public at large and to the detriment of Affirmer's heirs and successors, fully intending that such Waiver shall not be subject to revocation, rescission, cancellation, termination, or any other legal or equitable action to disrupt the quiet enjoyment of the Work by the public as contemplated by Affirmer's express Statement of Purpose.

3. Public License Fallback. Should any part of the Waiver for any reason be judged legally invalid or ineffective under applicable law, then the Waiver shall be preserved to the maximum extent permitted taking into account Affirmer's express Statement of Purpose. In addition, to the extent the Waiver is so judged Affirmer hereby grants to each affected person a royalty-free, non transferable, non sublicensable, non exclusive, irrevocable and unconditional license to exercise Affirmer's Copyright and Related Rights in the Work (i) in all territories worldwide, (ii) for the maximum duration provided by applicable law or treaty (including future time extensions), (iii) in any current or future medium and for any number of copies, and (iv) for any purpose whatsoever, including without limitation commercial, advertising or promotional purposes (the "License"). The License shall be deemed effective as of the date CC0 was applied by Affirmer to the Work. Should any part of the License for any reason be judged legally invalid or ineffective under applicable law, such partial invalidity or ineffectiveness shall not invalidate the remainder of the License, and in such case Affirmer hereby affirms that he or she will not (i) exercise any of his or her remaining Copyright and Related Rights in the Work or (ii) assert any associated claims and causes of action with respect to the Work, in either case contrary to Affirmer's express Statement of Purpose.

4. Limitations and Disclaimers.

No trademark or patent rights held by Affirmer are waived, abandoned, surrendered, licensed or otherwise affected by this document.
Affirmer offers the Work as-is and makes no representations or warranties of any kind concerning the Work, express, implied, statutory or otherwise, including without limitation warranties of title, merchantability, fitness for a particular purpose, non infringement, or the absence of latent or other defects, accuracy, or the present or absence of errors, whether or not discoverable, all to the greatest extent permissible under applicable law.
Affirmer disclaims responsibility for clearing rights of other persons that may apply to the Work or any use thereof, including without limitation any person's Copyright and Related Rights in the Work. Further, Affirmer disclaims responsibility for obtaining any necessary consents, permissions or other rights required for any use of the Work.
Affirmer understands and acknowledges that Creative Commons is not a party to this document and has no duty or obligation with respect to this CC0 or use of the Work."""
                
                else:
                    return f"{self.Name}"

    class App(Object):
        """System.Packaging.App
        
        Foundation class object which defines the application and its metadata.
        """
        
        def __init__(self, Name: str, Version: float, Author: str, Description: str, License: str, URL: str, Icon: str, OnGitHub: bool = False):
            """System.Packaging.App.__init__
            
            📝 We strongly recommend you use the System.Packaging.License() function to generate the license text. This will ensure that the license is always up to date.
            The Icon parameter should be a path to the icon file.
            """
            self.Name = Name
            self.Version = Version
            self.Author = Author
            self.Description = Description
            self.License = License
            self.URL = URL
            if OnGitHub:
                self.GitURL = f"https://github.com/{self.Author}/{self.Name}"
            self.Icon = Icon
