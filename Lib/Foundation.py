"""Foundation

A fast, fully-fledged package manager for the Fluid framework.
"""

from System import Processing, Branding, Explore, Console, Legacy, Null;

from Fluid import Location as LibLocation, Extension as Fl, Exception;

def Install(ApplicationPublisher = "", ApplicationName = "", ApplicationGitIdentifier = "main", ApplicationHasSubmodules: bool = False):
    """Foundation.Install()
    
    The base of connection with the outside world.
    Download packages today from GitHub and alike! You can even download non-Fluid projects. (🤔 Why you would do this we have no idea.)
    Coming soon: install Foundation packages from Git repositories not from GitHub!
    """
    
    # Print the variable ApplicationPublisher

    GitPublisher = ApplicationPublisher
    GitName = ApplicationName
    RequireDotPostActionHelper = False
    SplitApplicationName = ""

    SpecialPublisherList = ["RiversideValley", "Riverside"]

    for str in SpecialPublisherList:
        if ApplicationPublisher is str:
            # Special
            if GitPublisher == "RiversideValley":
                ApplicationPublisher = "Riverside"

            elif GitPublisher == "Riverside":
                GitPublisher = "RiversideValley"
                # raise RuntimeError("Illegal Fluid Foundation publisher; github publisher 43607 ('Riverside') is blocked.")

    if "." in GitPublisher:
        # Very problematic.
        
        raise Exception.FrameworkArchitectureError("An error occured due to the way the Python and C-based Fluid backends were built which contradicts the code of the Fluid Runtime.")

    elif "." in GitName:
        # Very problematic.
        # However, this is very important to make work as most Riverside Valley repos contain dots in them.

        RequireDotPostActionHelper = True
        SplitApplicationName = ApplicationName.split(".")
        
    elif "Fluid." in GitName and "RiversideValley" is GitPublisher:
        # Special repository.
        
        FluidSpecialRepo = True
        ApplicationName = ApplicationName.removeprefix("Fluid.")

    # TODO: Implement ability to install non-GitHub sourced Foundation packages.
    GitRepoUrl = f"https://github.com/{GitPublisher}/{ApplicationName}.git" # In order to implement the 'Install from non-GitHub repos' task, this url must be edited.

    try:
        if Branding.SlashInPaths is not True:
            Slash = "\\"
        else:
            Slash = "/"
            
        PackageLocation = f"{LibLocation}{Slash}{ApplicationPublisher}{Slash}{ApplicationName}"

        if ApplicationHasSubmodules:
            Processing.Execute(f"git clone {GitRepoUrl} {PackageLocation} --recurse-submodules", Language="shell")

        elif ApplicationHasSubmodules is not True:
            Processing.Execute(f"git clone {GitRepoUrl} {PackageLocation}", Language="shell")

        else:
            raise Exception.FoundationCloneError("Error with submodules")
        
        Processing.Execute(f"cd {PackageLocation}", Language="shell")
        Processing.Execute(f"git checkout -q {ApplicationGitIdentifier}", Language="shell")

    except:
        raise Exception.FoundationCloneError("There was a problem cloning the Foundation package")

    # Post clone actions 🎉

    if RequireDotPostActionHelper is True:
        # 🤔 How to do this...
        # I've got to thank GitHub Copilot for this one, without it, I might not have fixed this issue.

        # if GitPublisher is SpecialPublisherList[1]:
            # Fix only if the provider is Riverside Valley Corporation.

        #     raise NotImplementedError

        # else:
        #     raise NotImplementedError("\nThe package you are attempting to install appears to contain illegal characters, and is not yet supported by the Fluid Runtime. Try renaming your Git repository.\nOtherwise, there is a temporary fix: https://github.com/RiversideValley/Fluid.Runtime/wiki/Classes.Foundation#-if-you-have-a-package-with-a-dot--in-its-name-the-foundation-will-fail-to-install-the-package-this-is-due-to-the-nature-of-the-python-and-c-based-libraries-the-fluid-runtime-depends-on-which-contain-a-restriction-causing-the-code-to-fail-we-are-still-locating-the-root-of-this-restriction-but-it-will-be-fixed-at-some-point-meanwhile-you-can-create-an-issue-and-we-will-implement-the-workaround-for-your-package")

        Console.WriteLine("\nThe package you are attempting to install appears to contain illegal characters.\nNot to worry, the Fluid Helper will solve the problem for you. We will run some checks and tests on your machine; ignore console output if there is any.\n")
        
        HelperFile = f"{LibLocation}{Slash}{ApplicationPublisher}{Slash}{SplitApplicationName[0]}.{Fl}"
        
        try:
            Explore(HelperFile, True).Read()
            
        except FileNotFoundError:
            # Create the file.
            Explore(HelperFile, True).Create()

        for str in SplitApplicationName:
            for line in Explore.Read(HelperFile, Auto=True):
                if line.startswith("class"):
                    pass
                
                elif line.startswith("    ") and "class" not in line:
                    # Fix!
                    
                    Explore(HelperFile, True, f"class {SplitApplicationName[1]}:\n    ").Append()
                    
                else:
                    raise Exception.FoundationCloneError("There was a problem reading the package's helper contents.")
            #try:
            #    Explore.Append(f"{LibLocation}{Slash}{ApplicationPublisher}{Slash}{SplitApplicationName[0]}.{Fl}", Auto=True, AutoValue=f"class {SplitApplicationName[1]}:\n    ")
            #except:
            #    pass