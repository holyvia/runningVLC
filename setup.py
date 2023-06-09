import sys
from cx_Freeze import Executable,setup

templates = "./templates"
build_exe_options = {
    "packages": [ "bottle_websocket", "eel"],
    # "packages": ["bottle_websocket", "eel"],
    "include_files": [(templates, "templates")],
    
}

setup(
    name="MyApp",
    version="0.1",
    description="My App Description",
    options={"build_exe": build_exe_options},
    executables=[Executable("main.py")],
)