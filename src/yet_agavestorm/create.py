#!/usr/bin/env python
import os, sys, glob, yaml, subprocess, datetime
from yet_agavestorm import tsklib
from pathlib import Path

def main():
    argv = sys.argv;
    argv.pop(0); # remove first element, pointing to script itself
    if len(argv) == 0 :
        print("""
        Usage:
            yet create %taskname%   - create new task
        Example:
            yet create do this and do that
            """)
        exit(1);
        pass;
    tasknameArr = argv
    taskname = '_'.join( tasknameArr )
    taskDatetime = datetime.datetime.today()
    id = str( int( tsklib.getLastId() )+1 )
    path = tsklib.tskpath + "/heap/new"
    filename = taskDatetime.strftime("%Y-%m-%d_%H.%M.%S_%z_")+taskname+"."+id+".md"
    os.makedirs(path, exist_ok=True)

    scope = tsklib.getScope()

    Path( path + "/" + filename ).write_text("""---
    name: """+" ".join(tasknameArr)+"""
    created: """+taskDatetime.strftime("%Y-%m-%d %H:%M:%S %z")+"""
    context: """+scope["context"]+"""
    project: """+scope["project"]+"""
    filename:  """+filename+"""
    status: new
    id: """+id+"""
    ---
    """, encoding='utf-8')

    tsklib.gitAddCommitTask("created "+id);
    pass

if __name__=="__main__":
    main()
    pass
