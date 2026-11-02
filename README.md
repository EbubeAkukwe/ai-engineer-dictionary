# AI Engineer Dictionary

**Understand AI. Build AI.**

An open-source, community-maintained A–Z reference to the concepts, tools,
algorithms, architectures, and systems used in modern AI engineering.

## What belongs here?

The dictionary covers AI fundamentals, machine learning, deep learning,
LLM engineering, AI agents, data and retrieval systems, MLOps, infrastructure, robotics, and related software engineering concepts.

Entries use a layered teaching format: simple explanation first, then
technical depth, practical examples, and further reading.

## Project structure

```text
dictionary/   Dictionary entries written in Quarto Markdown
notebooks/    Jupyter notebooks for practical demonstrations
vocabulary/   Master A–Z vocabulary and CSV index
assets/       Website styles and static assets
scripts/      Validation and maintenance scripts
.github/      Contribution templates and automation
```

## Run locally

1. Install [Quarto](https://quarto.org/docs/get-started/).
2. Install Python 3 and Jupyter support:

   ```bash
   python -m pip install jupyter numpy
   ```

3. Clone the repository:

   ```bash
   git clone https://github.com/YOUR-USERNAME/ai-engineer-dictionary.git
   cd ai-engineer-dictionary
   ```

4. Preview the website:

   ```bash
   quarto preview
   ```

5. Render the static website:

   ```bash
   quarto render
   ```

The generated website is written to `_site/`.

## Contributing

Read [CONTRIBUTING.md](CONTRIBUTING.md) or the website's
[contribution guide](contribute.qmd). New terms should use
[`dictionary/TEMPLATE.qmd`](dictionary/TEMPLATE.qmd).

## Project Progress

- [x] Establish project scope and editorial format
- [x] Create initial Quarto website scaffold
- [x] Add example A entries
- [x] Add an example Jupyter notebook
- [x] Draft the A–Z master vocabulary (343 proposed terms)
- [ ] Editorially review and approve the vocabulary
- [ ] Add entry validation and duplicate detection
- [ ] Add GitHub issue and pull-request templates
- [ ] Enable automated GitHub Pages deployment
- [ ] Publish the first public release

## Licensing

- Code and project tooling: [MIT](LICENSE-CODE).
- Original educational content: [CC BY 4.0](LICENSE-CONTENT).

Third-party material remains subject to its own license and attribution terms.
