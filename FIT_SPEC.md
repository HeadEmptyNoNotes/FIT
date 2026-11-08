# Fit Spec

## Basic

A basic FIT system is very simple.

Structure: Somewhere, for example in a directory called "fit" in a repo, are four directories "open", "in_progress", "backlog", and "closed"

Tickets: Tickets are markdown files in one of the four afformentioned directories, or a subdirectory inside of one.
Ticket order is determined by sorting the filenames ascending. Metadata is frontmatter, if needed.

That is the extent of the basic system. 

## Strict

The strict FIT system is the basic system, with restrictions and specific rules. The system is
intended to make the FIT system more suited to using collaboratively, automating, and checking programatically. 
It is entirely optional. Any variation of this spec is valid, as long as all contributors/coolaborates agree.

### Board

A fit board is a directory called "fit" consisting of the following child directories (listed in sort order):

- in_progress
- open
- backlog
- closed

These directories may contain subdirectories. These subdirectories may be additional, more granular statuses,
or directories specific to a particular overall ticket. If both are desired, directories specific to
a project should be inside directories denoting status.

By convention, the "fit" directory lives at the root of a repository using FIT.

This specification document may live at the root of the board directory.

### Tickets

A ticket is a markdown file within one of the aforementioned folders.

Ticket order is determined by sorting the tickets by filename ascending.

A ticket is named according to following template: {two-digit ticket priority (0 high)}-{dash-seperated-short-name}.md

A ticket name should be shorter then 80 characters.

A ticket may contain a frontmatter YAML header with arbitrary relevant information.
Any metadata must be immediately relevant to the reader of the ticket. 
A ticket without frontmatter is still a valid ticket.

The first line of a ticket should be one to three sentences describing the issue.

Any additional sections must be preceeded by a sub-heading, and each additional section should have a single purpose and be kept short. 

### Lifecycle

A ticket is created in "open" or "backlog". It is moved to "in_progress" while it is being worked on. A ticket is moved to "closed" when it is finished. 

A ticket may only be moved to "in_progress" if there are no tickets in "in_progress". If multiple tickets are in "in_progress", 
those tickets should be moved to other statuses until only one ticket remains in "in_progress". Git branches are the
prefered way of handling the case where multiple tickets are being worked on simultanously. 

Tickets in "closed" may be archived by being moved out of the "closed" directory.

A ticket is not required to correspond to one git commit.

### Git

A /fit directory may be included in .gitignore.

If a FIT directory is hidden via .gitignore, it may be its own git repository or a branch of the repository into which it is currently embedded.
If it is tracked by a branch of the parent repository, the branch should be named "fit"

When a ticket is closed:

If the ticket is tracked by the same repository+branch that is tracking the work that was done, it should be included in
the commit that finishes the work.

If the ticket is tracked by a different repository/branch, it may record the git commit that
resolved the work, and the date that the work was completed, in the ticket's frontmatter. Neither are required.
