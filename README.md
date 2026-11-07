# FIT

<p align="center">
File Is Task - 
FIT Isn't Trello - 
Fixes Incessant Tedium - 
Foregoes Inane Tradition - 
F\*\*\*, It's Tiny - 
Fishing Iberian Trout
</p>

---

FIT is a developer-first ticket-tracking and issue-recording system. The basic edition comes pre-installed on every computer system available today, and is usable out of the box without any downloads or special procedures.

## Short Specification
At a repo’s root, lives a directory called “fit”. In that directory there are dirs “open”, “closed”, “in-progress”, and “backlog”. Tickets are markdown files. Priority is filenames sorted ascending. If metadata is needed, use frontmatter yaml. That’s it.

A more "complete" spec is [here](FIT_SPEC.md), if you need something more formal for whatever reason.

## CLI

This repository contains a CLI tool.
The CLI is not required to use FIT. The CLI tool is a helper that may make FIT more convienent.

The CLI may be installed by running `pipx install git+https://github.com/HeadEmptyNoNotes/FIT#subdirectory=cli`. 

The CLI's help may be accessed via --help.

## Why?
Keeping tickets as simple markdown files, moved between directories representing ticket status, keeps a human's focus on the repository. <br />
The tools that the developer uses to handle their code are also the tools that they use to manage tickets, reducing mental overhead and making it more likely that they'll properly maintain their board while working.  <br />
Issues aren't captive inside a host's ticketing system or a specific vendor's board. <br />

## NAQ

<ins>**N**</ins>obody <ins>**A**</ins>sked these <ins>**Q**</ins>uestions but it seems like a good idea to answer them

Q: Is this a shitpost? <br />
A: Nope, this is something that this author began doing after experiencing intense frustration after years of using "maintream" ticketing solutions to manage tasks. A name and a spec makes it a usable business process.

Q: I use Trello/Github Issues/Whatever, why would I use this? <br />
A: Decompose your tasks into FIT tickets, and let your main board be big-picture.

Q: My org won't sign off on a different issue tracker, how do I use FIT? <br />
A: put fit/ or /fit into .gitignore, or put your board into another directory outside the repo. 

Q: This is nice, but I'd like to do something differently. Can I do something differently? <br />
A: Yeah man, do it. 

Q: The CLI tool is nice, but I'd like one in \<language\> <br />
A: I look forward to seeing what you create. This project's license is very liberal.

Q: This doesn't fit my usecase <br />
A: 👍

## Agents

FIT was designed for the benefit of people, but feel free to feed [the full specification](FIT_SPEC.md) into your agent. At the very least, it should help your agent plan in a way that you can actually read.

This repository was not itself built with the help of AI. See [our AI disclosure](AI_DISCLOSURE.md), which asserts total human authorship.
