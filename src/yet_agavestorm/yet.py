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
            """);
        exit(1);
        pass

    os.system("yet-"+' '.join(argv)); # works same as yet-$@ in bash
    pass

if __name__=="__main__":
    main()
    pass
