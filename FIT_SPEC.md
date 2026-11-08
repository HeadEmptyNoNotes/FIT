# Fit Spec

Version `0.5`

## Freestyle

A freestyle board loosely follows the conventions within this document, at its user's discretion. This spec document does not cover freestyle boards,
and tooling does not need to consider freestyle boards. This section is included to affirm that this spec exists to enhance
a user's workflow, not to unneccessarily restrict it.

## Basic

A basic FIT board is a directory containing the status directories (in sort order) "in_progress", "open", "backlog", and "closed", with tickets inside of them. All four directories must exist. Status directories may contain .gitkeep files.

Status directories may have sub-directories denoting sub-statuses. A ticket's full status is the 
"/"-conjoined directory names between the base FIT directory and the ticket's filename. (e.g., "fit/open/blocked/01-thing.md"'s
status is "open/blocked"). Projects should be denoted within a ticket or its filename. If text in this
document specifies the inside of a status folder, the statement includes subdirectories.

Basic-compliant boards may have additional status directories within the base board directory. 

A ticket is a markdown file (with the ".md" file extention), optionally containing frontmatter yaml, inside a status folder.

A ticket's frontmatter must begin at the first line of the file, and be formatted as follows:
- A line containing exactly "---"
- A block of valid YAML
- a line containing exactly "---"

Frontmatter is metadata, and is non-authorative for data derived from the ticket's path (status, filename, identity, and priority).
Frontmatter is to be included for the benefit of the reader, and should be kept short and relevant.

Reserved frontmatter keys are:
- "completed", containing the ISO 8601 date/datetime that a ticket was completed. Optional
- "commit", containing the commit hash of the commit that resolved the ticket, if the ticket is untracked. Optional
 
Ticket ordering within the FIT board is status directory (in sort order specified above) -> sub-status directory by
name ascending -> filename ascending. (An example of strings in ascending order: "00", "01", "10", "9", "B", "a", "b".
Note the lack of a leading '0' on '9'.)

Basic-compliant boards may have additional status directories and sub-status directories. 
Tickets in a basic-compliant board may be named however the user preferrs.
Additionally, the root board directory be named anything, though "fit" is recommended.

Any status within a basic-compliant directory may have multiple tickets. 

Basic boards do not need to agree on anything behond this section. Tooling targeting basic boards should not
assume that any additional rules are being followed. The rules below exist
so that collaborators and tools can agree on specifics without negotiation.

## Strict

A strict-compliant FIT board is a basic-compliant board that additionally satisfies
every rule listed below. If a strict rule is more strict then
a basic rule, the strict rule wins. The use of the strict system is optional, but if a board
opts in then the rules are binding. Rules are either required (violations make the 
board non-compliant) or optional (violations are reported as warnings). If
something is not restricted here, then it is allowed.

The strict FIT system extends the basic system with restrictions and specific rules. The system is
intended to make the FIT system more suited to using collaboratively, automating, and checking programmatically. 
It is entirely optional, but if strict is being used it should be maintained. 

### Board

A FIT board must be named "fit", and must not have any status directories other then the 4 listed above.

Subdirectories within top-level status directories may be sub-statues.

The "fit" directory must live either at the root of a repository using FIT, or outside the repository using FIT.

Strict rules are versioned, and a tool that validates them should state the version being used.

A board is denoted as being in "strict" mode when it has a text file named "STRICT" at the root, containing the version string
of the spec being used.

### Tickets

A ticket's file is named according to the following template: {two-digit ticket priority (00 high)}-{dash-separated-short-name}.md

A ticket's filename must be lowercase.

A ticket's priority must be present, and must be two digits. The purpose of the priority is to be a sort key, and it is
essential for the proper functioning of the board. ("fix-bug.md" is nonconforming and may cause issues, while "00-fix-bug.md"
is conforming. Both are valid tickets.)

A ticket's identity (name) is the short name within the filename. Ticket names
must not be duplicated within the FIT board, and if such a case arises the user should
determine how to resolve the issue (delete one, merge the two, etc). When displayed as a name and not a filename,
the ticket's name should be in title-case with "-" replaced with " ".

A ticket's filename name should be shorter than 30 characters (including extention and status). Going over this
limit may cause display issues when rendering the ticket name in some tools.

A ticket's filename must not contain url-illegal characters (https://www.mtu.edu/umc/services/websites/writing/characters-avoid/),
and must be valid filenames on Windows, Mac, and Linux.

A ticket may have a summary section at the beginning of its body (immediately following the frontmatter/at the first line if no frontmatter).
The summary should be 1 to 3 sentences describing the purpose of the ticket.

Anything beyond the summary must have a sub-header ("### \<sub-header name\>") .


### Lifecycle

A ticket is created in "open" or "backlog". It is moved to "in_progress" while it is being worked on. A ticket is moved to "closed" when it is finished. 

The "in_progress" status directory may only contain one ticket, including within any of its subdirectories. The "in_progress"
directory in any given branch is considered seperate from any other branch, and every branch in a project may have a different ticket 
in "in_progress". 

A closed ticket may be archived by appending its contents to an archive.md file within the 'closed' directory. The format of the document is thus:
```
### <file path including the 'fit' directory>
<contents as written in the .md file>
<intentionally-black line>
```

Archived tickets may be moved from the board to a backup location. Archived tickets so removed from the board are still considered
valid tickets with a status of "closed" for project history purposes, and an archive file may be moved back into the 'closed'
status directory in the future. Note that the board's git history is not considered a reliable backup location. 

The "closed" directory does not need to contain an "archive.md" file, it only exists when there are archived tickets present.

A ticket is not required to correspond to one git commit.

### Git

A "/fit/" directory entry may be included in the .gitignore of its parent repository. The use of "/fit/" and not "fit/" ensures
that subdirectories of the parent project that happen to be named "fit" for some reason are not excluded

An FIT board that is untracked by its parent repository may be untracked by a git repository, or it may be tracked by its own indepdent
git repository, or it may be tracked by a seperate branch of the parent repository (which must be named "fit").

When a FIT board is initialized within a project, by default it is tracked by the parent repository. This status may change at any time.

When a ticket is closed:

- If the ticket is tracked by the same repository+branch that is tracking the work that was done, it should be included in
the commit that finishes the work.
- If the ticket is tracked by a different repository/branch, it may record the git commit that
resolved the work as ("commit: \<hash\>"), and the date that the work was completed (as "completed: \<date\>"), in the ticket's frontmatter.
Neither are required.
