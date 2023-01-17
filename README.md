# Yet - personal task manager
Git based personal task manager.
100% command line.

## 4 dummies
 0. `yet` without arguments will display help

Workflow:
 1. Add task to the heap `yet create task name or short descriprion`
    1. Show tasks in heap `yet list heap`
 2. Pick the task to current day schedule `yet pick %taskId%` 
    1. Show tasks for current day `yet list cur`
 3. Open task in text editor  `yet open %taskId%`
    1. Task file is just md file with yaml header
    2. Adjust status in header
    3. Write any notes below
    4. Save
 4. When you done working, or before next day
    1. Move unfinished tasks back to heap `yet reset all`
    2. Archive tasks with status *done*  `yet archive today`
 5. View archive for specific date `yet list 2023-01-11`
 6. Run manual git command on task list `yet git %git_command% %git_command_args%`
 7. Adjust visible scope with `yet scope`
 
## How it works
 1. There is git repository behind the scenes. So you have history and you can sync tasks using any git server. History, branches, etc.
    1. Create/pick/reset/archive commands will invoke `git add` + `git commit` commands automatically.
 2. Task data stored in plain text files.
    1. Format markdown(.md) with yaml header.
    2. You work with single task using plain text editor, like kate
 3. yet tool is used to organize and navigate .md files
 
## The method
### Step 1: Write it down and forget. 
Once you spot new task or idea - you just add it to the heap, and continue with your current work. So you stay focused.
```
yet create
```
*Heap* is the most chaotic, unorganised, unsorted, *backlog* you can imagine.
Do not waste your time on details, just stock pile it in the heap as is.

Imagine that you are working with paper stickers and you have a big box of chaotic notes written on stickers - that's the heap.
```
yet list heap
```
Will show you tasks in the heap in form of table
```
 id | context  | project    | name                                                                   | status
----|----------|------------|------------------------------------------------------------------------|-------
 7  | personal | yet        | show creation date column in task list                                 | new   
 15 | personal | yet        | sanitize slashes in task filename                                      | new
```
First column is *taskId* you will need it to manipulate the task

### Step 2: pick the task into daily plan
Pick all tasks you are planning to work with today. 
```
yet pick %taskId%
```
Will pick the task
```
yet list cur
```
Will display tasks for current day.

If you made a mistake, you can return the task back to heap
```
yet reset %taskId%
```

### Step 3: open the task in text editor
```
yet open %taskId%
```
### Step 4: change status to *work*
Adjust yaml header, simple replace `status: new` with `status: work`.

You can use any custom statuses, but buildin - *new*, *work*, *done* will be highlighted in `yet list` output.

### Step 5: Make notes while you are working on the task
As for it's just .md file, you can make any notes behind yaml header.

### Note: you can work with as many tasks at once as you want
That's just plain text files, after all.

### Step 6: change task status to *done*
In yaml header, replace `status: work` with `status: work`.

### Step 7: check your progress
```
yet list cur
```
Will get more green lines while you complete the tasks.

### Step 8: Cleanup workspace
```
yet reset all
```
Will return unfinished tasks back to the heap
```
yet archive today
```
Will move only *done* tasks to archive folder with current day. You can also use "yesterday" or specify date as "YYYY-MM-DD", or anything else recognized by php `strtotime()` function.

To view archived tasks use:
```
yet list YYYY-MM-DD
```

### Step 9: apply git
All git commands are mapped with `yet git`.

Most used:
    - `yet git log` history of changes in tasks
    - `yet git remote add origin %link%` link your task list with remote repository
    - `yet git push` save local changes to remote repository
    - `yet git pull` load fresh changes from remote repository
    
## Todo
Markdown with yaml header can be easily parsed, so it's a subject for creting extensions for *yet*. 
Also, tasks can be accessed/synced using git remotes. That's potential for multiple clients (mobile, gui etc).

