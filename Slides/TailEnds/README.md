# TailEnds

Slides pulled out of the main `slides_X.X.md` decks: still worth keeping, not part of the lecture as given.

Each file is a small Slidev deck of its own:

```bash
cd IAA/Slides
slidev TailEnds/slides_2.1-tailends.md
```

Figure paths from here are `../Figures/`.

## Hide vs TailEnds

Slidev can skip a slide without moving it: put this in that slide's frontmatter.

```yaml
---
hide: true
---
```

(`disabled: true` is the same flag.) Hidden slides stay in the markdown, drop out of the show, and still show up as skipped in the overview. Use that for a one-off skip. Use this folder when the slide should leave the main file.
