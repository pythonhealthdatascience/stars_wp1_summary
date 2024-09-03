Using pandoc 2.9.2.1

* `-f` specifies input format
* `-t` specifies output format (if not provided, identifies from file)
* `-o` specifies an output file
* `-s` adds appropriate header and footer to create a standalone document

```
pandoc stars_checklist.md -f markdown_strict+pipe_tables -o stars_checklist.tex
```

```
pandoc stars_checklist.md -f markdown_strict+pipe_tables -o stars_checklist.tex -s
```