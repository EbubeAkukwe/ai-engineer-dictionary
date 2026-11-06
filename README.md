# AI Engineer Dictionary

**Understand AI. Build AI.**

An open-source, community-maintained A–Z reference to the concepts, tools,
algorithms, architectures, and systems used in modern AI engineering.

The project aims to make AI engineering concepts easier to learn and apply
through concise, layered explanations, practical examples, and links to
authoritative references.

## What belongs here?

The dictionary covers AI fundamentals, machine learning, deep learning,
LLM engineering, AI agents, data and retrieval systems, MLOps, infrastructure,
robotics, and related software engineering concepts. The maintained vocabulary
currently contains 347 unique terms; the live count can grow as reviewed
contributions are accepted.

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
   git clone https://github.com/EbubeAkukwe/ai-engineer-dictionary.git
   cd ai-engineer-dictionary
   ```

4. Preview the website:

   ```bash
   quarto preview
   ```

5. Render the static website:

   ```bash
   quarto render --output-dir _site
   ```

The generated website is written to `_site/`.

To run the entry metadata and duplicate check:

```bash
python scripts/validate_entries.py
```

## Contributing

Read [CONTRIBUTING.md](CONTRIBUTING.md) or the website's
[contribution guide](contribute.qmd). New terms should use
[`dictionary/TEMPLATE.qmd`](dictionary/TEMPLATE.qmd).
Use the [GitHub issue forms](https://github.com/EbubeAkukwe/ai-engineer-dictionary/issues/new/choose)
to report a bug, propose terminology, or suggest a definition improvement.

## Navigation

Browse entries from the [dictionary index](dictionary/index.qmd), the
[A–Z page](dictionary/letters.qmd), or the letter sections in the website
sidebar. Individual letter folders contain their own index and `.qmd` entries.
The [master vocabulary](vocabulary/MASTER_VOCABULARY.md) and
[CSV vocabulary](vocabulary/master_vocabulary.csv) track the canonical terms.

## Project Progress

- [x] Establish project scope and editorial format
- [x] Create initial Quarto website scaffold
- [x] Add example A entries
- [x] Add an example Jupyter notebook
- [x] Create and maintain the curated A–Z master vocabulary (347 current terms)
- [x] Add entry validation and duplicate detection
- [x] Add GitHub issue and pull-request templates
- [x] Prepare automated Vercel deployment configuration
- [ ] Publish the first public release

## Licensing

- Code and project tooling: [MIT](LICENSE-CODE).
- Original educational content: [CC BY 4.0](LICENSE-CONTENT).

Third-party material remains subject to its own license and attribution terms.
