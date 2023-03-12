"""System

A professional yet usable programming framework.
"""

# RequirerDataPolicy:
# Legacy.Os:
# - abc
# - sys ✅
# - stat ✅
# - _collections_abc
# - nt
# - posix
# - posixpath
# ...
# Legacy.DarkDetect:
# - typing
# - subprocess
# - ctypes
# - sys ✅
# - os ✅
# - pathlib

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

    class Os:
        r"""OS routines for NT or Posix depending on what system we're on.

        This exports:
          - all functions from posix or nt, e.g. unlink, stat, etc.
          - os.path is either posixpath or ntpath
          - os.name is either 'posix' or 'nt'
          - os.curdir is a string representing the current directory (always '.')
          - os.pardir is a string representing the parent directory (always '..')
          - os.sep is the (or a most common) pathname separator ('/' or '\\')
          - os.extsep is the extension separator (always '.')
          - os.altsep is the alternate pathname separator (None or '/')
          - os.pathsep is the component separator used in $PATH etc
          - os.linesep is the line separator in text files ('\r' or '\n' or '\r\n')
          - os.defpath is the default search path for executables
          - os.devnull is the file path of the null device ('/dev/null', etc.)

        Programs that import and use 'os' stand a better chance of being
        portable between different platforms.  Of course, they must then
        only use functions that are defined by all platforms (e.g., unlink
        and opendir), and leave all pathname manipulation to os.path
        (e.g., split and join).
        """

        #'
        import abc
        import sys
        import stat as st

        from _collections_abc import _check_methods

        GenericAlias = type(list[int])

        _names = sys.builtin_module_names

        # Note:  more names are added to __all__ later.
        __all__ = ["altsep", "curdir", "pardir", "sep", "pathsep", "linesep",
                   "defpath", "name", "path", "devnull", "SEEK_SET", "SEEK_CUR",
                   "SEEK_END", "fsencode", "fsdecode", "get_exec_path", "fdopen",
                   "extsep"]

        def _exists(name):
            return name in globals()

        def _get_exports_list(module):
            try:
                return list(module.__all__)
            except AttributeError:
                return [n for n in dir(module) if n[0] != '_']

        # Any new dependencies of the os module and/or changes in path separator
        # requires updating importlib as well.
        if 'posix' in _names:
            name = 'posix'
            linesep = '\n'
            import posix
            try:
                from posix import _exit
                __all__.append('_exit')
            except ImportError:
                pass
            import posixpath as path

            try:
                from posix import _have_functions
            except ImportError:
                pass

            import posix
            __all__.extend(_get_exports_list(posix))
            del posix

        elif 'nt' in _names:
            name = 'nt'
            linesep = '\r\n'
            import nt
            try:
                from nt import _exit
                __all__.append('_exit')
            except ImportError:
                pass
            import ntpath as path

            import nt
            __all__.extend(_get_exports_list(nt))
            del nt

            try:
                from nt import _have_functions
            except ImportError:
                pass

        else:
            raise ImportError('no os specific module found')

        sys.modules['os.path'] = path
        from os.path import (curdir, pardir, sep, pathsep, defpath, extsep, altsep,
            devnull)

        del _names


        if _exists("_have_functions"):
            _globals = globals()
            def _add(str, fn):
                if (fn in _globals) and (str in _have_functions):
                    _set.add(_globals[fn])

            _set = set()
            _add("HAVE_FACCESSAT",  "access")
            _add("HAVE_FCHMODAT",   "chmod")
            _add("HAVE_FCHOWNAT",   "chown")
            _add("HAVE_FSTATAT",    "stat")
            _add("HAVE_FUTIMESAT",  "utime")
            _add("HAVE_LINKAT",     "link")
            _add("HAVE_MKDIRAT",    "mkdir")
            _add("HAVE_MKFIFOAT",   "mkfifo")
            _add("HAVE_MKNODAT",    "mknod")
            _add("HAVE_OPENAT",     "open")
            _add("HAVE_READLINKAT", "readlink")
            _add("HAVE_RENAMEAT",   "rename")
            _add("HAVE_SYMLINKAT",  "symlink")
            _add("HAVE_UNLINKAT",   "unlink")
            _add("HAVE_UNLINKAT",   "rmdir")
            _add("HAVE_UTIMENSAT",  "utime")
            supports_dir_fd = _set

            _set = set()
            _add("HAVE_FACCESSAT",  "access")
            supports_effective_ids = _set

            _set = set()
            _add("HAVE_FCHDIR",     "chdir")
            _add("HAVE_FCHMOD",     "chmod")
            _add("HAVE_FCHOWN",     "chown")
            _add("HAVE_FDOPENDIR",  "listdir")
            _add("HAVE_FDOPENDIR",  "scandir")
            _add("HAVE_FEXECVE",    "execve")
            _set.add(stat) # fstat always works
            _add("HAVE_FTRUNCATE",  "truncate")
            _add("HAVE_FUTIMENS",   "utime")
            _add("HAVE_FUTIMES",    "utime")
            _add("HAVE_FPATHCONF",  "pathconf")
            if _exists("statvfs") and _exists("fstatvfs"): # mac os x10.3
                _add("HAVE_FSTATVFS", "statvfs")
            supports_fd = _set

            _set = set()
            _add("HAVE_FACCESSAT",  "access")
            # Some platforms don't support lchmod().  Often the function exists
            # anyway, as a stub that always returns ENOSUP or perhaps EOPNOTSUPP.
            # (No, I don't know why that's a good design.)  ./configure will detect
            # this and reject it--so HAVE_LCHMOD still won't be defined on such
            # platforms.  This is Very Helpful.
            #
            # However, sometimes platforms without a working lchmod() *do* have
            # fchmodat().  (Examples: Linux kernel 3.2 with glibc 2.15,
            # OpenIndiana 3.x.)  And fchmodat() has a flag that theoretically makes
            # it behave like lchmod().  So in theory it would be a suitable
            # replacement for lchmod().  But when lchmod() doesn't work, fchmodat()'s
            # flag doesn't work *either*.  Sadly ./configure isn't sophisticated
            # enough to detect this condition--it only determines whether or not
            # fchmodat() minimally works.
            #
            # Therefore we simply ignore fchmodat() when deciding whether or not
            # os.chmod supports follow_symlinks.  Just checking lchmod() is
            # sufficient.  After all--if you have a working fchmodat(), your
            # lchmod() almost certainly works too.
            #
            # _add("HAVE_FCHMODAT",   "chmod")
            _add("HAVE_FCHOWNAT",   "chown")
            _add("HAVE_FSTATAT",    "stat")
            _add("HAVE_LCHFLAGS",   "chflags")
            _add("HAVE_LCHMOD",     "chmod")
            if _exists("lchown"): # mac os x10.3
                _add("HAVE_LCHOWN", "chown")
            _add("HAVE_LINKAT",     "link")
            _add("HAVE_LUTIMES",    "utime")
            _add("HAVE_LSTAT",      "stat")
            _add("HAVE_FSTATAT",    "stat")
            _add("HAVE_UTIMENSAT",  "utime")
            _add("MS_WINDOWS",      "stat")
            supports_follow_symlinks = _set

            del _set
            del _have_functions
            del _globals
            del _add


        # Python uses fixed values for the SEEK_ constants; they are mapped
        # to native constants if necessary in posixmodule.c
        # Other possible SEEK values are directly imported from posixmodule.c
        SEEK_SET = 0
        SEEK_CUR = 1
        SEEK_END = 2

        # Super directory utilities.
        # (Inspired by Eric Raymond; the doc strings are mostly his)

        def makedirs(name, mode=0o777, exist_ok=False):
            """makedirs(name [, mode=0o777][, exist_ok=False])

            Super-mkdir; create a leaf directory and all intermediate ones.  Works like
            mkdir, except that any intermediate path segment (not just the rightmost)
            will be created if it does not exist. If the target directory already
            exists, raise an OSError if exist_ok is False. Otherwise no exception is
            raised.  This is recursive.

            """
            head, tail = path.split(name)
            if not tail:
                head, tail = path.split(head)
            if head and tail and not path.exists(head):
                try:
                    makedirs(head, exist_ok=exist_ok)
                except FileExistsError:
                    # Defeats race condition when another thread created the path
                    pass
                cdir = curdir
                if isinstance(tail, bytes):
                    cdir = bytes(curdir, 'ASCII')
                if tail == cdir:           # xxx/newdir/. exists if xxx/newdir exists
                    return
            try:
                mkdir(name, mode)
            except OSError:
                # Cannot rely on checking for EEXIST, since the operating system
                # could give priority to other errors like EACCES or EROFS
                if not exist_ok or not path.isdir(name):
                    raise

        def removedirs(name):
            """removedirs(name)

            Super-rmdir; remove a leaf directory and all empty intermediate
            ones.  Works like rmdir except that, if the leaf directory is
            successfully removed, directories corresponding to rightmost path
            segments will be pruned away until either the whole path is
            consumed or an error occurs.  Errors during this latter phase are
            ignored -- they generally mean that a directory was not empty.

            """
            rmdir(name)
            head, tail = path.split(name)
            if not tail:
                head, tail = path.split(head)
            while head and tail:
                try:
                    rmdir(head)
                except OSError:
                    break
                head, tail = path.split(head)

        def renames(old, new):
            """renames(old, new)

            Super-rename; create directories as necessary and delete any left
            empty.  Works like rename, except creation of any intermediate
            directories needed to make the new pathname good is attempted
            first.  After the rename, directories corresponding to rightmost
            path segments of the old name will be pruned until either the
            whole path is consumed or a nonempty directory is found.

            Note: this function can fail with the new directory structure made
            if you lack permissions needed to unlink the leaf directory or
            file.

            """
            head, tail = path.split(new)
            if head and tail and not path.exists(head):
                makedirs(head)
            rename(old, new)
            head, tail = path.split(old)
            if head and tail:
                try:
                    removedirs(head)
                except OSError:
                    pass

        __all__.extend(["makedirs", "removedirs", "renames"])

        def walk(top, topdown=True, onerror=None, followlinks=False):
            """Directory tree generator.

            For each directory in the directory tree rooted at top (including top
            itself, but excluding '.' and '..'), yields a 3-tuple

                dirpath, dirnames, filenames

            dirpath is a string, the path to the directory.  dirnames is a list of
            the names of the subdirectories in dirpath (excluding '.' and '..').
            filenames is a list of the names of the non-directory files in dirpath.
            Note that the names in the lists are just names, with no path components.
            To get a full path (which begins with top) to a file or directory in
            dirpath, do os.path.join(dirpath, name).

            If optional arg 'topdown' is true or not specified, the triple for a
            directory is generated before the triples for any of its subdirectories
            (directories are generated top down).  If topdown is false, the triple
            for a directory is generated after the triples for all of its
            subdirectories (directories are generated bottom up).

            When topdown is true, the caller can modify the dirnames list in-place
            (e.g., via del or slice assignment), and walk will only recurse into the
            subdirectories whose names remain in dirnames; this can be used to prune the
            search, or to impose a specific order of visiting.  Modifying dirnames when
            topdown is false has no effect on the behavior of os.walk(), since the
            directories in dirnames have already been generated by the time dirnames
            itself is generated. No matter the value of topdown, the list of
            subdirectories is retrieved before the tuples for the directory and its
            subdirectories are generated.

            By default errors from the os.scandir() call are ignored.  If
            optional arg 'onerror' is specified, it should be a function; it
            will be called with one argument, an OSError instance.  It can
            report the error to continue with the walk, or raise the exception
            to abort the walk.  Note that the filename is available as the
            filename attribute of the exception object.

            By default, os.walk does not follow symbolic links to subdirectories on
            systems that support them.  In order to get this functionality, set the
            optional argument 'followlinks' to true.

            Caution:  if you pass a relative pathname for top, don't change the
            current working directory between resumptions of walk.  walk never
            changes the current directory, and assumes that the client doesn't
            either.

            Example:

            import os
            from os.path import join, getsize
            for root, dirs, files in os.walk('python/Lib/email'):
                print(root, "consumes ")
                print(sum(getsize(join(root, name)) for name in files), end=" ")
                print("bytes in", len(files), "non-directory files")
                if 'CVS' in dirs:
                    dirs.remove('CVS')  # don't visit CVS directories

            """
            sys.audit("os.walk", top, topdown, onerror, followlinks)
            return _walk(fspath(top), topdown, onerror, followlinks)

        def _walk(top, topdown, onerror, followlinks):
            dirs = []
            nondirs = []
            walk_dirs = []

            # We may not have read permission for top, in which case we can't
            # get a list of the files the directory contains.  os.walk
            # always suppressed the exception then, rather than blow up for a
            # minor reason when (say) a thousand readable directories are still
            # left to visit.  That logic is copied here.
            try:
                # Note that scandir is global in this module due
                # to earlier import-*.
                scandir_it = scandir(top)
            except OSError as error:
                if onerror is not None:
                    onerror(error)
                return

            with scandir_it:
                while True:
                    try:
                        try:
                            entry = next(scandir_it)
                        except StopIteration:
                            break
                    except OSError as error:
                        if onerror is not None:
                            onerror(error)
                        return

                    try:
                        is_dir = entry.is_dir()
                    except OSError:
                        # If is_dir() raises an OSError, consider that the entry is not
                        # a directory, same behaviour than os.path.isdir().
                        is_dir = False

                    if is_dir:
                        dirs.append(entry.name)
                    else:
                        nondirs.append(entry.name)

                    if not topdown and is_dir:
                        # Bottom-up: recurse into sub-directory, but exclude symlinks to
                        # directories if followlinks is False
                        if followlinks:
                            walk_into = True
                        else:
                            try:
                                is_symlink = entry.is_symlink()
                            except OSError:
                                # If is_symlink() raises an OSError, consider that the
                                # entry is not a symbolic link, same behaviour than
                                # os.path.islink().
                                is_symlink = False
                            walk_into = not is_symlink

                        if walk_into:
                            walk_dirs.append(entry.path)

            # Yield before recursion if going top down
            if topdown:
                yield top, dirs, nondirs

                # Recurse into sub-directories
                islink, join = path.islink, path.join
                for dirname in dirs:
                    new_path = join(top, dirname)
                    # Issue #23605: os.path.islink() is used instead of caching
                    # entry.is_symlink() result during the loop on os.scandir() because
                    # the caller can replace the directory entry during the "yield"
                    # above.
                    if followlinks or not islink(new_path):
                        yield from _walk(new_path, topdown, onerror, followlinks)
            else:
                # Recurse into sub-directories
                for new_path in walk_dirs:
                    yield from _walk(new_path, topdown, onerror, followlinks)
                # Yield after recursion if going bottom up
                yield top, dirs, nondirs

        __all__.append("walk")

        if {open, stat} <= supports_dir_fd and {scandir, stat} <= supports_fd:

            def fwalk(top=".", topdown=True, onerror=None, *, follow_symlinks=False, dir_fd=None):
                """Directory tree generator.

                This behaves exactly like walk(), except that it yields a 4-tuple

                    dirpath, dirnames, filenames, dirfd

                `dirpath`, `dirnames` and `filenames` are identical to walk() output,
                and `dirfd` is a file descriptor referring to the directory `dirpath`.

                The advantage of fwalk() over walk() is that it's safe against symlink
                races (when follow_symlinks is False).

                If dir_fd is not None, it should be a file descriptor open to a directory,
                  and top should be relative; top will then be relative to that directory.
                  (dir_fd is always supported for fwalk.)

                Caution:
                Since fwalk() yields file descriptors, those are only valid until the
                next iteration step, so you should dup() them if you want to keep them
                for a longer period.

                Example:

                import os
                for root, dirs, files, rootfd in os.fwalk('python/Lib/email'):
                    print(root, "consumes", end="")
                    print(sum(os.stat(name, dir_fd=rootfd).st_size for name in files),
                          end="")
                    print("bytes in", len(files), "non-directory files")
                    if 'CVS' in dirs:
                        dirs.remove('CVS')  # don't visit CVS directories
                """
                sys.audit("os.fwalk", top, topdown, onerror, follow_symlinks, dir_fd)
                top = fspath(top)
                # Note: To guard against symlink races, we use the standard
                # lstat()/open()/fstat() trick.
                if not follow_symlinks:
                    orig_st = stat(top, follow_symlinks=False, dir_fd=dir_fd)
                topfd = open(top, O_RDONLY, dir_fd=dir_fd)
                try:
                    if (follow_symlinks or (st.S_ISDIR(orig_st.st_mode) and
                                            path.samestat(orig_st, stat(topfd)))):
                        yield from _fwalk(topfd, top, isinstance(top, bytes),
                                          topdown, onerror, follow_symlinks)
                finally:
                    close(topfd)

            def _fwalk(topfd, toppath, isbytes, topdown, onerror, follow_symlinks):
                # Note: This uses O(depth of the directory tree) file descriptors: if
                # necessary, it can be adapted to only require O(1) FDs, see issue
                # #13734.

                scandir_it = scandir(topfd)
                dirs = []
                nondirs = []
                entries = None if topdown or follow_symlinks else []
                for entry in scandir_it:
                    name = entry.name
                    if isbytes:
                        name = fsencode(name)
                    try:
                        if entry.is_dir():
                            dirs.append(name)
                            if entries is not None:
                                entries.append(entry)
                        else:
                            nondirs.append(name)
                    except OSError:
                        try:
                            # Add dangling symlinks, ignore disappeared files
                            if entry.is_symlink():
                                nondirs.append(name)
                        except OSError:
                            pass

                if topdown:
                    yield toppath, dirs, nondirs, topfd

                for name in dirs if entries is None else zip(dirs, entries):
                    try:
                        if not follow_symlinks:
                            if topdown:
                                orig_st = stat(name, dir_fd=topfd, follow_symlinks=False)
                            else:
                                assert entries is not None
                                name, entry = name
                                orig_st = entry.stat(follow_symlinks=False)
                        dirfd = open(name, O_RDONLY, dir_fd=topfd)
                    except OSError as err:
                        if onerror is not None:
                            onerror(err)
                        continue
                    try:
                        if follow_symlinks or path.samestat(orig_st, stat(dirfd)):
                            dirpath = path.join(toppath, name)
                            yield from _fwalk(dirfd, dirpath, isbytes,
                                              topdown, onerror, follow_symlinks)
                    finally:
                        close(dirfd)

                if not topdown:
                    yield toppath, dirs, nondirs, topfd

            __all__.append("fwalk")

        def execl(file, *args):
            """execl(file, *args)

            Execute the executable file with argument list args, replacing the
            current process. """
            execv(file, args)

        def execle(file, *args):
            """execle(file, *args, env)

            Execute the executable file with argument list args and
            environment env, replacing the current process. """
            env = args[-1]
            execve(file, args[:-1], env)

        def execlp(file, *args):
            """execlp(file, *args)

            Execute the executable file (which is searched for along $PATH)
            with argument list args, replacing the current process. """
            execvp(file, args)

        def execlpe(file, *args):
            """execlpe(file, *args, env)

            Execute the executable file (which is searched for along $PATH)
            with argument list args and environment env, replacing the current
            process. """
            env = args[-1]
            execvpe(file, args[:-1], env)

        def execvp(file, args):
            """execvp(file, args)

            Execute the executable file (which is searched for along $PATH)
            with argument list args, replacing the current process.
            args may be a list or tuple of strings. """
            _execvpe(file, args)

        def execvpe(file, args, env):
            """execvpe(file, args, env)

            Execute the executable file (which is searched for along $PATH)
            with argument list args and environment env, replacing the
            current process.
            args may be a list or tuple of strings. """
            _execvpe(file, args, env)

        __all__.extend(["execl","execle","execlp","execlpe","execvp","execvpe"])

        def _execvpe(file, args, env=None):
            if env is not None:
                exec_func = execve
                argrest = (args, env)
            else:
                exec_func = execv
                argrest = (args,)
                env = environ

            if path.dirname(file):
                exec_func(file, *argrest)
                return
            saved_exc = None
            path_list = get_exec_path(env)
            if name != 'nt':
                file = fsencode(file)
                path_list = map(fsencode, path_list)
            for dir in path_list:
                fullname = path.join(dir, file)
                try:
                    exec_func(fullname, *argrest)
                except (FileNotFoundError, NotADirectoryError) as e:
                    last_exc = e
                except OSError as e:
                    last_exc = e
                    if saved_exc is None:
                        saved_exc = e
            if saved_exc is not None:
                raise saved_exc
            raise last_exc


        def get_exec_path(env=None):
            """Returns the sequence of directories that will be searched for the
            named executable (similar to a shell) when launching a process.

            *env* must be an environment variable dict or None.  If *env* is None,
            os.environ will be used.
            """
            # Use a local import instead of a global import to limit the number of
            # modules loaded at startup: the os module is always loaded at startup by
            # Python. It may also avoid a bootstrap issue.
            import warnings

            if env is None:
                env = environ

            # {b'PATH': ...}.get('PATH') and {'PATH': ...}.get(b'PATH') emit a
            # BytesWarning when using python -b or python -bb: ignore the warning
            with warnings.catch_warnings():
                warnings.simplefilter("ignore", BytesWarning)

                try:
                    path_list = env.get('PATH')
                except TypeError:
                    path_list = None

                if supports_bytes_environ:
                    try:
                        path_listb = env[b'PATH']
                    except (KeyError, TypeError):
                        pass
                    else:
                        if path_list is not None:
                            raise ValueError(
                                "env cannot contain 'PATH' and b'PATH' keys")
                        path_list = path_listb

                    if path_list is not None and isinstance(path_list, bytes):
                        path_list = fsdecode(path_list)

            if path_list is None:
                path_list = defpath
            return path_list.split(pathsep)


        # Change environ to automatically call putenv() and unsetenv()
        from _collections_abc import MutableMapping, Mapping

        class _Environ(MutableMapping):
            def __init__(self, data, encodekey, decodekey, encodevalue, decodevalue):
                self.encodekey = encodekey
                self.decodekey = decodekey
                self.encodevalue = encodevalue
                self.decodevalue = decodevalue
                self._data = data

            def __getitem__(self, key):
                try:
                    value = self._data[self.encodekey(key)]
                except KeyError:
                    # raise KeyError with the original key value
                    raise KeyError(key) from None
                return self.decodevalue(value)

            def __setitem__(self, key, value):
                key = self.encodekey(key)
                value = self.encodevalue(value)
                putenv(key, value)
                self._data[key] = value

            def __delitem__(self, key):
                encodedkey = self.encodekey(key)
                unsetenv(encodedkey)
                try:
                    del self._data[encodedkey]
                except KeyError:
                    # raise KeyError with the original key value
                    raise KeyError(key) from None

            def __iter__(self):
                # list() from dict object is an atomic operation
                keys = list(self._data)
                for key in keys:
                    yield self.decodekey(key)

            def __len__(self):
                return len(self._data)

            def __repr__(self):
                formatted_items = ", ".join(
                    f"{self.decodekey(key)!r}: {self.decodevalue(value)!r}"
                    for key, value in self._data.items()
                )
                return f"environ({{{formatted_items}}})"

            def copy(self):
                return dict(self)

            def setdefault(self, key, value):
                if key not in self:
                    self[key] = value
                return self[key]

            def __ior__(self, other):
                self.update(other)
                return self

            def __or__(self, other):
                if not isinstance(other, Mapping):
                    return NotImplemented
                new = dict(self)
                new.update(other)
                return new

            def __ror__(self, other):
                if not isinstance(other, Mapping):
                    return NotImplemented
                new = dict(other)
                new.update(self)
                return new

        def _createenviron():
            if name == 'nt':
                # Where Env Var Names Must Be UPPERCASE
                def check_str(value):
                    if not isinstance(value, str):
                        raise TypeError("str expected, not %s" % type(value).__name__)
                    return value
                encode = check_str
                decode = str
                def encodekey(key):
                    return encode(key).upper()
                data = {}
                for key, value in environ.items():
                    data[encodekey(key)] = value
            else:
                # Where Env Var Names Can Be Mixed Case
                encoding = sys.getfilesystemencoding()
                def encode(value):
                    if not isinstance(value, str):
                        raise TypeError("str expected, not %s" % type(value).__name__)
                    return value.encode(encoding, 'surrogateescape')
                def decode(value):
                    return value.decode(encoding, 'surrogateescape')
                encodekey = encode
                data = environ
            return _Environ(data,
                encodekey, decode,
                encode, decode)

        # unicode environ
        environ = _createenviron()
        del _createenviron


        def getenv(key, default=None):
            """Get an environment variable, return None if it doesn't exist.
            The optional second argument can specify an alternate default.
            key, default and the result are str."""
            return environ.get(key, default)

        supports_bytes_environ = (name != 'nt')
        __all__.extend(("getenv", "supports_bytes_environ"))

        if supports_bytes_environ:
            def _check_bytes(value):
                if not isinstance(value, bytes):
                    raise TypeError("bytes expected, not %s" % type(value).__name__)
                return value

            # bytes environ
            environb = _Environ(environ._data,
                _check_bytes, bytes,
                _check_bytes, bytes)
            del _check_bytes

            def getenvb(key, default=None):
                """Get an environment variable, return None if it doesn't exist.
                The optional second argument can specify an alternate default.
                key, default and the result are bytes."""
                return environb.get(key, default)

            __all__.extend(("environb", "getenvb"))

        def _fscodec():
            encoding = sys.getfilesystemencoding()
            errors = sys.getfilesystemencodeerrors()

            def fsencode(filename):
                """Encode filename (an os.PathLike, bytes, or str) to the filesystem
                encoding with 'surrogateescape' error handler, return bytes unchanged.
                On Windows, use 'strict' error handler if the file system encoding is
                'mbcs' (which is the default encoding).
                """
                filename = fspath(filename)  # Does type-checking of `filename`.
                if isinstance(filename, str):
                    return filename.encode(encoding, errors)
                else:
                    return filename

            def fsdecode(filename):
                """Decode filename (an os.PathLike, bytes, or str) from the filesystem
                encoding with 'surrogateescape' error handler, return str unchanged. On
                Windows, use 'strict' error handler if the file system encoding is
                'mbcs' (which is the default encoding).
                """
                filename = fspath(filename)  # Does type-checking of `filename`.
                if isinstance(filename, bytes):
                    return filename.decode(encoding, errors)
                else:
                    return filename

            return fsencode, fsdecode

        fsencode, fsdecode = _fscodec()
        del _fscodec

        # Supply spawn*() (probably only for Unix)
        if _exists("fork") and not _exists("spawnv") and _exists("execv"):

            P_WAIT = 0
            P_NOWAIT = P_NOWAITO = 1

            __all__.extend(["P_WAIT", "P_NOWAIT", "P_NOWAITO"])

            # XXX Should we support P_DETACH?  I suppose it could fork()**2
            # and close the std I/O streams.  Also, P_OVERLAY is the same
            # as execv*()?

            def _spawnvef(mode, file, args, env, func):
                # Internal helper; func is the exec*() function to use
                if not isinstance(args, (tuple, list)):
                    raise TypeError('argv must be a tuple or a list')
                if not args or not args[0]:
                    raise ValueError('argv first element cannot be empty')
                pid = fork()
                if not pid:
                    # Child
                    try:
                        if env is None:
                            func(file, args)
                        else:
                            func(file, args, env)
                    except:
                        _exit(127)
                else:
                    # Parent
                    if mode == P_NOWAIT:
                        return pid # Caller is responsible for waiting!
                    while 1:
                        wpid, sts = waitpid(pid, 0)
                        if WIFSTOPPED(sts):
                            continue

                        return waitstatus_to_exitcode(sts)

            def spawnv(mode, file, args):
                """spawnv(mode, file, args) -> integer

        Execute file with arguments from args in a subprocess.
        If mode == P_NOWAIT return the pid of the process.
        If mode == P_WAIT return the process's exit code if it exits normally;
        otherwise return -SIG, where SIG is the signal that killed it. """
                return _spawnvef(mode, file, args, None, execv)

            def spawnve(mode, file, args, env):
                """spawnve(mode, file, args, env) -> integer

        Execute file with arguments from args in a subprocess with the
        specified environment.
        If mode == P_NOWAIT return the pid of the process.
        If mode == P_WAIT return the process's exit code if it exits normally;
        otherwise return -SIG, where SIG is the signal that killed it. """
                return _spawnvef(mode, file, args, env, execve)

            # Note: spawnvp[e] isn't currently supported on Windows

            def spawnvp(mode, file, args):
                """spawnvp(mode, file, args) -> integer

        Execute file (which is looked for along $PATH) with arguments from
        args in a subprocess.
        If mode == P_NOWAIT return the pid of the process.
        If mode == P_WAIT return the process's exit code if it exits normally;
        otherwise return -SIG, where SIG is the signal that killed it. """
                return _spawnvef(mode, file, args, None, execvp)

            def spawnvpe(mode, file, args, env):
                """spawnvpe(mode, file, args, env) -> integer

        Execute file (which is looked for along $PATH) with arguments from
        args in a subprocess with the supplied environment.
        If mode == P_NOWAIT return the pid of the process.
        If mode == P_WAIT return the process's exit code if it exits normally;
        otherwise return -SIG, where SIG is the signal that killed it. """
                return _spawnvef(mode, file, args, env, execvpe)


            __all__.extend(["spawnv", "spawnve", "spawnvp", "spawnvpe"])


        if _exists("spawnv"):
            # These aren't supplied by the basic Windows code
            # but can be easily implemented in Python

            def spawnl(mode, file, *args):
                """spawnl(mode, file, *args) -> integer

        Execute file with arguments from args in a subprocess.
        If mode == P_NOWAIT return the pid of the process.
        If mode == P_WAIT return the process's exit code if it exits normally;
        otherwise return -SIG, where SIG is the signal that killed it. """
                return spawnv(mode, file, args)

            def spawnle(mode, file, *args):
                """spawnle(mode, file, *args, env) -> integer

        Execute file with arguments from args in a subprocess with the
        supplied environment.
        If mode == P_NOWAIT return the pid of the process.
        If mode == P_WAIT return the process's exit code if it exits normally;
        otherwise return -SIG, where SIG is the signal that killed it. """
                env = args[-1]
                return spawnve(mode, file, args[:-1], env)


            __all__.extend(["spawnl", "spawnle"])


        if _exists("spawnvp"):
            # At the moment, Windows doesn't implement spawnvp[e],
            # so it won't have spawnlp[e] either.
            def spawnlp(mode, file, *args):
                """spawnlp(mode, file, *args) -> integer

        Execute file (which is looked for along $PATH) with arguments from
        args in a subprocess with the supplied environment.
        If mode == P_NOWAIT return the pid of the process.
        If mode == P_WAIT return the process's exit code if it exits normally;
        otherwise return -SIG, where SIG is the signal that killed it. """
                return spawnvp(mode, file, args)

            def spawnlpe(mode, file, *args):
                """spawnlpe(mode, file, *args, env) -> integer

        Execute file (which is looked for along $PATH) with arguments from
        args in a subprocess with the supplied environment.
        If mode == P_NOWAIT return the pid of the process.
        If mode == P_WAIT return the process's exit code if it exits normally;
        otherwise return -SIG, where SIG is the signal that killed it. """
                env = args[-1]
                return spawnvpe(mode, file, args[:-1], env)


            __all__.extend(["spawnlp", "spawnlpe"])

        # VxWorks has no user space shell provided. As a result, running
        # command in a shell can't be supported.
        if sys.platform != 'vxworks':
            # Supply os.popen()
            def popen(cmd, mode="r", buffering=-1):
                if not isinstance(cmd, str):
                    raise TypeError("invalid cmd type (%s, expected string)" % type(cmd))
                if mode not in ("r", "w"):
                    raise ValueError("invalid mode %r" % mode)
                if buffering == 0 or buffering is None:
                    raise ValueError("popen() does not support unbuffered streams")
                import subprocess
                if mode == "r":
                    proc = subprocess.Popen(cmd,
                                            shell=True, text=True,
                                            stdout=subprocess.PIPE,
                                            bufsize=buffering)
                    return _wrap_close(proc.stdout, proc)
                else:
                    proc = subprocess.Popen(cmd,
                                            shell=True, text=True,
                                            stdin=subprocess.PIPE,
                                            bufsize=buffering)
                    return _wrap_close(proc.stdin, proc)

            # Helper for popen() -- a proxy for a file whose close waits for the process
            class _wrap_close:
                def __init__(self, stream, proc):
                    self._stream = stream
                    self._proc = proc
                def close(self):
                    self._stream.close()
                    returncode = self._proc.wait()
                    if returncode == 0:
                        return None
                    if name == 'nt':
                        return returncode
                    else:
                        return returncode << 8  # Shift left to match old behavior
                def __enter__(self):
                    return self
                def __exit__(self, *args):
                    self.close()
                def __getattr__(self, name):
                    return getattr(self._stream, name)
                def __iter__(self):
                    return iter(self._stream)

            __all__.append("popen")

        # Supply os.fdopen()
        def fdopen(fd, mode="r", buffering=-1, encoding=None, *args, **kwargs):
            if not isinstance(fd, int):
                raise TypeError("invalid fd type (%s, expected integer)" % type(fd))
            import io
            if "b" not in mode:
                encoding = io.text_encoding(encoding)
            return io.open(fd, mode, buffering, encoding, *args, **kwargs)


        # For testing purposes, make sure the function is available when the C
        # implementation exists.
        def _fspath(path):
            """Return the path representation of a path-like object.

            If str or bytes is passed in, it is returned unchanged. Otherwise the
            os.PathLike interface is used to get the path representation. If the
            path representation is not str or bytes, TypeError is raised. If the
            provided path is not str, bytes, or os.PathLike, TypeError is raised.
            """
            if isinstance(path, (str, bytes)):
                return path

            # Work from the object's type to match method resolution of other magic
            # methods.
            path_type = type(path)
            try:
                path_repr = path_type.__fspath__(path)
            except AttributeError:
                if hasattr(path_type, '__fspath__'):
                    raise
                else:
                    raise TypeError("expected str, bytes or os.PathLike object, "
                                    "not " + path_type.__name__)
            if isinstance(path_repr, (str, bytes)):
                return path_repr
            else:
                raise TypeError("expected {}.__fspath__() to return str or bytes, "
                                "not {}".format(path_type.__name__,
                                                type(path_repr).__name__))

        # If there is no C implementation, make the pure Python version the
        # implementation as transparently as possible.
        if not _exists('fspath'):
            fspath = _fspath
            fspath.__name__ = "fspath"


        class PathLike(abc.ABC):

            """Abstract base class for implementing the file system path protocol."""

            @abc.abstractmethod
            def __fspath__(self):
                """Return the file system path representation of the object."""
                raise NotImplementedError

            @classmethod
            def __subclasshook__(cls, subclass):
                if cls is PathLike:
                    return _check_methods(subclass, '__fspath__')
                return NotImplemented

            __class_getitem__ = classmethod(GenericAlias)


        if name == 'nt':
            class _AddedDllDirectory:
                def __init__(self, path, cookie, remove_dll_directory):
                    self.path = path
                    self._cookie = cookie
                    self._remove_dll_directory = remove_dll_directory
                def close(self):
                    self._remove_dll_directory(self._cookie)
                    self.path = None
                def __enter__(self):
                    return self
                def __exit__(self, *args):
                    self.close()
                def __repr__(self):
                    if self.path:
                        return "<AddedDllDirectory({!r})>".format(self.path)
                    return "<AddedDllDirectory()>"

            def add_dll_directory(path):
                """Add a path to the DLL search path.

                This search path is used when resolving dependencies for imported
                extension modules (the module itself is resolved through sys.path),
                and also by ctypes.

                Remove the directory by calling close() on the returned object or
                using it in a with statement.
                """
                import nt
                cookie = nt._add_dll_directory(path)
                return _AddedDllDirectory(
                    path,
                    cookie,
                    nt._remove_dll_directory
                )
    class DarkDetect:
        #-----------------------------------------------------------------------------
        #  Copyright (C) 2019 Alberto Sottile
        #
        #  Distributed under the terms of the 3-clause BSD License.
        #-----------------------------------------------------------------------------
        
        def _dummy():
            #-----------------------------------------------------------------------------
            #  Copyright (C) 2019 Alberto Sottile
            #
            #  Distributed under the terms of the 3-clause BSD License.
            #-----------------------------------------------------------------------------

            import typing

            def theme():
                return None
        
            def isDark():
                return None
    
            def isLight():
                return None

            def listener(callback: typing.Callable[[str], None]) -> None:
                raise NotImplementedError()
            
        def __init__():
            #-----------------------------------------------------------------------------
            #  Copyright (C) 2019 Alberto Sottile
            #
            #  Distributed under the terms of the 3-clause BSD License.
            #-----------------------------------------------------------------------------

            __version__ = '0.8.0'

            import sys
            import platform

            def macos_supported_version():
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

            if sys.platform == "darwin":
                #-----------------------------------------------------------------------------
                #  Copyright (C) 2019 Alberto Sottile
                #
                #  Distributed under the terms of the 3-clause BSD License.
                #-----------------------------------------------------------------------------

                import ctypes
                import ctypes.util
                import subprocess
                import sys
                from pathlib import Path
                from typing import Callable

                try:
                    from Foundation import NSObject, NSKeyValueObservingOptionNew, NSKeyValueChangeNewKey, NSUserDefaults
                    from PyObjCTools import AppHelper
                    _can_listen = True
                except ModuleNotFoundError:
                    _can_listen = False


                try:
                    # macOS Big Sur+ use "a built-in dynamic linker cache of all system-provided libraries"
                    appkit = ctypes.cdll.LoadLibrary('AppKit.framework/AppKit')
                    objc = ctypes.cdll.LoadLibrary('libobjc.dylib')
                except OSError:
                    # revert to full path for older OS versions and hardened programs
                    appkit = ctypes.cdll.LoadLibrary(ctypes.util.find_library('AppKit'))
                    objc = ctypes.cdll.LoadLibrary(ctypes.util.find_library('objc'))

                void_p = ctypes.c_void_p
                ull = ctypes.c_uint64

                objc.objc_getClass.restype = void_p
                objc.sel_registerName.restype = void_p

                # See https://docs.python.org/3/library/ctypes.html#function-prototypes for arguments description
                MSGPROTOTYPE = ctypes.CFUNCTYPE(void_p, void_p, void_p, void_p)
                msg = MSGPROTOTYPE(('objc_msgSend', objc), ((1 ,'', None), (1, '', None), (1, '', None)))

                def _utf8(s):
                    if not isinstance(s, bytes):
                        s = s.encode('utf8')
                    return s

                def n(name):
                    return objc.sel_registerName(_utf8(name))

                def C(classname):
                    return objc.objc_getClass(_utf8(classname))

                def theme():
                    NSAutoreleasePool = objc.objc_getClass('NSAutoreleasePool')
                    pool = msg(NSAutoreleasePool, n('alloc'))
                    pool = msg(pool, n('init'))

                    NSUserDefaults = C('NSUserDefaults')
                    stdUserDef = msg(NSUserDefaults, n('standardUserDefaults'))

                    NSString = C('NSString')

                    key = msg(NSString, n("stringWithUTF8String:"), _utf8('AppleInterfaceStyle'))
                    appearanceNS = msg(stdUserDef, n('stringForKey:'), void_p(key))
                    appearanceC = msg(appearanceNS, n('UTF8String'))

                    if appearanceC is not None:
                        out = ctypes.string_at(appearanceC)
                    else:
                        out = None

                    msg(pool, n('release'))

                    if out is not None:
                        return out.decode('utf-8')
                    else:
                        return 'Light'

                def isDark():
                    return theme() == 'Dark'

                def isLight():
                    return theme() == 'Light'


                def _listen_child():
                    """
                    Run by a child process, install an observer and print theme on change
                    """
                    import signal
                    signal.signal(signal.SIGINT, signal.SIG_IGN)

                    OBSERVED_KEY = "AppleInterfaceStyle"

                    class Observer(NSObject):
                        def observeValueForKeyPath_ofObject_change_context_(
                            self, path, object, changeDescription, context
                        ):
                            result = changeDescription[NSKeyValueChangeNewKey]
                            try:
                                print(f"{'Light' if result is None else result}", flush=True)
                            except IOError:
                                os._exit(1)

                    observer = Observer.new()  # Keep a reference alive after installing
                    defaults = NSUserDefaults.standardUserDefaults()
                    defaults.addObserver_forKeyPath_options_context_(
                        observer, OBSERVED_KEY, NSKeyValueObservingOptionNew, 0
                    )

                    AppHelper.runConsoleEventLoop()


                def listener(callback: Callable[[str], None]) -> None:
                    if not _can_listen:
                        raise NotImplementedError()
                    with subprocess.Popen(
                        (sys.executable, "-c", "import _mac_detect as m; m._listen_child()"),
                        stdout=subprocess.PIPE,
                        universal_newlines=True,
                        cwd=Path(__file__).parent,
                    ) as p:
                        for line in p.stdout:
                            callback(line.strip())
                    
            elif sys.platform == "win32" and platform.release().isdigit() and int(platform.release()) >= 10:
                # Checks if running Windows 10 version 10.0.14393 (Anniversary Update) OR HIGHER. The getwindowsversion method returns a tuple.
                # The third item is the build number that we can use to check if the user has a new enough version of Windows.
                winver = int(platform.version().split('.')[2])
            elif sys.platform == "linux":
                from ._linux_detect import *
            else:
                

            del sys, platform
            
        def __main__():
            #-----------------------------------------------------------------------------
            #  Copyright (C) 2019 Alberto Sottile
            #
            #  Distributed under the terms of the 3-clause BSD License.
            #-----------------------------------------------------------------------------

            import darkdetect

            print('Current theme: {}'.format(darkdetect.theme()))
            
    import sys as _sys;
    from Legacy import pathlib as _path;
    from Legacy import zipimport as _zip;
    from Legacy import csv as _csv;
    from Legacy import turtle as _turtle;
    from Legacy import socket as _socket;
    from Legacy import random as _random;
    from Legacy import subprocess as _process;
    import time as _time;

GenericAlias = type(list[int])
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
