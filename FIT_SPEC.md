---
version: "0.5"
---
# Fit Spec

## Freestyle

The specs presented within this document are provided in order to provide formal procedures and definitions for those who
would benefit from them. The basic idea explained in this repository's readme is all that is needed for a human to effectively use FIT,
and these rules do not need to be adopted or even read if they are not needed. A FIT board that does not adhere to 
any any rules beyond that which the user feels appropriate.

This document will make no attempt to further define a Freestyle FIT board, and tooling is not required to function
on freestyle FIT boards. This definition exists to clarify the purpose of this document, and to give humans
reading this document an escape hatch.

## Basic

A basic FIT board is a directory containing the status directories (in sort order) "in_progress", "open", "backlog", and "closed", with tickets inside of them. All four directories must exist. Status directories may contain non-.md files if relevant, such as .gitkeep and archive.txt

Status directories may have sub-directories denoting sub-statuses. A ticket's full status is the 
"/"-conjoined directory names between the base FIT directory and the ticket's filename. (e.g., "fit/open/blocked/01-thing.md"'s
status is "open/blocked"). 

Basic-compliant boards may have additional status directories within the base board directory. 

A ticket is a markdown file (with the ".md" file extention), optionally containing frontmatter yaml, inside a status folder.
All such markdown files are valid tickets that may be acted upon.

A ticket's frontmatter must begin at the first line of the file, and be formatted as follows:
- A line containing exactly "---"
- A block of valid YAML
- a line containing exactly "---"

Frontmatter is metadata, and is non-authorative for data derived from the ticket's path (status, filename, identity, and priority).
Frontmatter is to be included for the benefit of the reader, and should be kept short and relevant. Any frontmatter key may
be used, but the following keys should be used as described.

Defined frontmatter keys are:
- "completed", containing the ISO 8601 date/datetime that a ticket was completed. Optional
- "commit", containing the commit hash of the commit that resolved the ticket, if the ticket is untracked. Optional
- "project", describing the name of the project to which the ticket belongs
 
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

Status directories may only contain .md files, with the exception of ".gitkeep", image files linked by
.md files, and "fit/closed/archive.txt"

A board is denoted as being in "strict" mode when it has a text file named "STRICT" at the root, containing the version string
of the spec being used. The version string is noted in the frontmatter at the top of the file, and includes the double-quotes on either side.
Note that the version string is not semver-compliant, may contain additional words such as "draft", and each version is independent to any other.
If the "STRICT" file is not present at the root, it is not in "strict" mode.

### Tickets

Any markdown file is a valid ticket and may be acted upon. Only tickets conforming to the rules in this
section are compliant tickets, and are guaranteed to work with tooling and between collaborators.

A ticket has the following properties, encoded in the file path:
- Name: Also called "short name", this is the identity of the ticket. Should be a curt summary of the issue. Must not be duplicated within the board. Archived tickets do not count towards uniqueness, purely because it would be impractical to enforce.
- Priority: A double-digit number between 00 and 99, used to sort the ticket. Changing the priority does not change the ticket's identity.
- Status: The ticket's parent directory (after "fit/"), this determines where in the ticket's lifecycle its at
- Filename: A combination of Priority and Name, in lowercase

A ticket's filename is formatted as follows: {priority}-{dash-seperated-short-name}.md

A ticket's priority must be present, and must be two digits. The purpose of the priority is to be a sort key, and it is
essential for the proper functioning of the board. ("fix-bug.md" is nonconforming and may cause issues, while "00-fix-bug.md"
is conforming.)

A ticket's identity (name) is the short name within the filename. Ticket names
must not be duplicated within the FIT board, and if such a case arises the user should
determine how to resolve the issue (delete one, merge the two, etc). When displayed as a name and not a filename,
the ticket's name should be in title-case with "-" replaced with " ".

A ticket's short name should be shorter than 30 characters.

A ticket's filename must not contain url-illegal characters (https://www.mtu.edu/umc/services/websites/writing/characters-avoid/),
and must be valid filenames on Windows, Mac, and Linux.

A ticket may have a summary section at the beginning of its body (immediately following the frontmatter/at the first line if no frontmatter).
The summary should be 1 to 3 sentences describing the purpose of the ticket.

A ticket may have sub-sections following the summary section. Each sub-section must begin with a level-3 header, and must 
encapsulate one concept (left up to the writer's discretion). 

Anything beyond the summary must have a level-3 sub-header


### Lifecycle

A ticket is created in "open" or "backlog". It is moved to "in_progress" while it is being worked on. A ticket is moved to "closed" when it is finished. 

The "in_progress" status directory may only contain one ticket, including within any of its subdirectories. The "in_progress"
directory in any given branch is considered seperate from any other branch, and every branch in a project may have a different ticket 
in "in_progress". 

A closed ticket may be archived by appending its contents to an archive.txt file within the 'closed' directory, and then deleting the
ticket file. The format of the document is thus:
````
### <file path including the 'fit' directory>
```
<contents as written in the .md file>
```
````

An archived ticket ceases to be an actionable ticket, and exists for backup and history purposes. An archived ticket may be 
reconstructed

Archived tickets may be moved from the board to a backup location. Archived tickets so removed from the board are no longer
actionable tickets while they are , and an archive file may be moved back into the 'closed'
status directory in the future. Note that the board's git history is not considered a reliable backup location. 

The "closed" directory does not need to contain an "archive.txt" file, it only exists when there are archived tickets present.

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
