# FIT

File Is Task - 
FIT Isn't Trello - 
Fits In Tight - 
Fixes Incessant Tedium - 
Foregoes Inane Tradition - 
F\*\*\*, It's Tiny - 
Fishing Iberian Trout

---

FIT is a developer-first ticket-tracking and issue-recording system. The basic edition comes pre-installed on every computer system available today, and is usable out of the box without any downloads or special procedures.

## Specification
At a repo’s root, lives a directory called “fit”. In that directory there are dirs “open”, “closed”, “in-progress”, and “backlog”. Tickets are markdown files. Priority is filenames sorted ascending. If metadata is needed, use frontmatter yaml. That’s it.

## Additional Functionality
When you move a ticket into the “done” directory and commit it, by the magic of git you’ll be able to see when it was finished, and what commit finished it.

To reference a FIT ticket in a github issue, link to the file.

## Why?
Keeping tickets as simple markdown files, moved between directories representing ticket status, keeps a human's focus on the repository.
The tools that the developer uses to handle their code are also the tools that they use to manage tickets, reducing mental overhead and making it more likely that they'll properly maintain them. 
Issues transcend the host's platform and are replicated perfectly wherever the project is hosted or mirrored.
