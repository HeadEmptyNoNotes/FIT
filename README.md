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

## Why?
Keeping tickets as simple markdown files, moved between directories representing ticket status, keeps a human's focus on the repository. <br />
The tools that the developer uses to handle their code are also the tools that they use to manage tickets, reducing mental overhead and making it more likely that they'll properly maintain them.  <br />
Issues transcend the host's platform and are replicated perfectly wherever the project is hosted or mirrored. <br />

## NAQ

Nobody Asked these Questions but it seems like a good idea to answer them

Q: I use Trello/Github Issues/Whatever, why would I use this? <br />
A: Decompose your tasks into FIT tickets, and let your main board be big-picture.

Q: My org wont' sign off on a different issue tracker, how do I use FIT? <br />
A: put fit/ into .gitignore, or put your board into another folder

Q: Is this a shitpost? <br />
A: Nope, this was born out of intense frustration

Q: This doesn't fit my usecase <br />
A: 👍

## Agents

FIT was designed for people to benefit people, but feel free to point your agent at this file. 
