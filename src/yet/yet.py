#!/usr/bin/env python
import os, sys;

def main():
    argv = sys.argv;
    argv.pop(0); # remove first element, pointing to script itself
    if len(argv) == 0 :
        print("""
    Usage:
        yet create %taskname%   - create new task, return taskId and filename
        # yet list                - show current tasks
        yet list heap           - show tasks from heap
        yet list cur            - show tasks for current date
        yet pick %taskId%       - move tsak from heap to current date
        yet lastid              - show last insert id
        yet open %taskId%       - open task in kate (parallel kate filename.md)
        yet reset               - move not finished tasks back to heap
        yet archive             - move done tasks from cur to archive with date
        yet scope               - change/reset scope ( current context and project ) affects avironment variables yet_CONTEXT, yet_PROJECT
        yet drop                - Use with care! completely remove task with specific id
        yet git %attributes%    - run git on ./yet folder
        
    Environmant variables:
        YET_CONTEXT             - set context
        YET_PROJECT             - set project
        YET                     - short version for setting both project and context
        YET_HOME                - working folder name inside AppData/home (~/.yet_agavestorm is default value for Linux)
        
        Examples:
            YET_PROJECT=myproj yet create task decription
                                 - will create task with project parameter set to `myproj`
            YET_CONTEXT=personal yet list cur
                                 - will show only tasks in `personal` scope
            YET=context:personal - equivalent for`YET_CONTEXT=personal
            YET=context:personal,project:myproj
                                 - equivalent for `YET_CONTEXT=personal YET_PROJECT=myproj yet ...`
            YET=p:proj,c:context - equivalent for `YET=context:personal,project:myproj` parameter order does not matter
            
        Priorities:
            YET_CONTEXT, YET_PROJECT - high
            YET                      - middle
            scope.yaml               - low
            """);
        exit(1);
        pass

    os.system("yet-"+' '.join(argv)); # works same as yet-$@ in bash
    pass

if __name__=="__main__":
    main()
    pass
