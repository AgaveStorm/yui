# CHANGELOG

## [2023-02-20]
 - Macos and windows changes for yui open
 - error handling for random string instead of taskId

## [2023-02-15]
### Added
 - list-archives command

## [2023-02-13]
### Fixed
 - Yaml dependency problem, etc
 - No linux colors in windows console (will be just white)

## [2023-02-12]
### Fixed
 - Default folder on windows was %userfolder%/yui, should be %userfolder%/AppData/Local, fixed. 

## [2023-02-05]
### Added
 - check if git exist, disable automatic commits if not, display warning

## [2023-02-04]
### Added
 - pick range of items like so: `pick 141,142,143..154`

## [2023-02-03]
### Added
 - Hint for next possible commands under the list of tasks, different for cur and heap

## [2023-02-02]
### Added
 - Order numbers ( "No." column on the left )
 - pick/reset/open/drop tasks by order number ( by id still works, and it is default behaviour )
    as for order number is different for `list heap` and `list cur` you need to prefix order number with container name, example: `open cur3`
 - table title in bottom-right corner
