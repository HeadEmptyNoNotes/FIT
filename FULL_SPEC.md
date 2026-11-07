# Full Fit Spec

## Board

A fit board is a directory ("fit" by convention, but it could be named anything) consisting of the following child directories:

- open
- closed
- in_progress
- backlog

These directories main contain subdirectories. These subdirectories may be additional, more granular statuses, or directories specific to a particular overall ticket. If both are desired, directories specific to a project should be inside directories denoting status.

## Tickets

A ticket is a markdown file within one of the aforementioned folders, either at their root or within another subfolder.

Ticket order is determined by sorting the tickets by filename ascending.

A ticket may be named anything, though by convention is named with a two-digit number representing ticket priority (ie multiple tickets may use the same number), followed by a name that is meaningful when viewed from a file tree, with words separated via underscore.

A ticket may contain a frontmatter YAML header with arbitrary relevant information. It should *not* contain extraneous or frivolous information that is not immediately relevant to a reader.

The body of a ticket should be short, ideally no more then 5 lines long given 80-character lines.

## Lifecycle

A ticket is created in "open" or "backlog". It is moved to "in_progress" while it is being worked on. A ticket is moved to "closed" when it is finished. 

To archive closed tickets, either zip the "closed" directory or compile all of the tickets into a single markdown file. 

A ticket is not required to correspond to one git commit. 
