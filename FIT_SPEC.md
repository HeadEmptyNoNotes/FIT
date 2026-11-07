# Full Fit Spec

## Board

A fit board is a directory ("fit" by convention, but it could be named anything) consisting of the following child directories:

- open
- closed
- in_progress
- backlog

These directories may contain subdirectories. These subdirectories may be additional, more granular statuses, or directories specific to a particular overall ticket. If both are desired, directories specific to a project should be inside directories denoting status.

By convention, the "fit" directory lives at the root of a repository using FIT.

This specification document may live at the root of the board directory.

## Tickets

A ticket is a markdown file within one of the aforementioned folders.

Ticket order is determined by sorting the tickets by filename ascending.

A ticket may be named anything. By convention, the name format is a two-digit number representing ticket priority (ie multiple tickets may use the same number), followed by an all-lowercase name that is meaningful when viewed from a file tree, with words separated via hyphen-minus. eg: 03-fix-typo-in-readme.md

A ticket may contain a frontmatter YAML header with arbitrary relevant information. It should *not* contain extraneous or frivolous information that is not immediately relevant to a reader. A ticket without frontmatter is a valid ticket.

The body of a ticket should be short, ideally no more then ~250 characters (3 lines long at 80 characters a line).

## Lifecycle

A ticket is created in "open" or "backlog". It is moved to "in_progress" while it is being worked on. A ticket is moved to "closed" when it is finished. 

To archive closed tickets, either zip the "closed" directory or compile all of the tickets into a single markdown file. 

A ticket is not required to correspond to one git commit. A ticket that has just been closed should not contain the git commit hash of the commit that closed it.

## Git

A fit/ directory may be included in .gitignore. In this case, it is recommend that the time of completion is recorded, though it is not mandatory.
