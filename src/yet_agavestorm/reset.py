#!/usr/bin/env python
"""
move unfinished tasks back to heap
"""
import os, sys, glob, yaml, subprocess
from yet_agavestorm import tsklib

def main():
    argv = sys.argv;
    argv.pop(0); # remove first element, pointing to script itself
    if len(argv) != 1 :
        print("""
        Usage:
            yet reset %taskId%   - move single task back to heap
            yet reset all        - move all unfinished tasks back to heap
        Example:
            yet pick 3
            """)
        exit(1);
        pass;
    id = argv[0]
    pattern = "*."+id+".md"
    if id == "all":
        pattern = "*.md"
    files = tsklib.findTaskFiles(location="cur", pattern = pattern)
    if len(files) == 0:
        print("task with id="+id+" not found in cur")
        exit(1)
        pass

    for filename in files:
        task =  tsklib.loadYaml(filename) 
        if task["status"] == "done":
            continue
        pass
        targetPath = tsklib.tskpath() + "/heap/"+task["status"]
        os.makedirs(targetPath, exist_ok=True)
        print("moving " + task["filename"] + " back to heap .. ", end="")
        os.rename( filename, targetPath + "/" + task["filename"]);
        print("done")
    pass
    tsklib.gitAddCommitTask("reset "+id);
    pass

if __name__=="__main__":
    main()
    pass


