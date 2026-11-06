# Contributing

Thanks for helping improve the AI Engineer Dictionary.

## Choose a contribution path

- Use the **New terminology proposal** issue form to suggest a term before
  writing an entry.
- Use the **Definition improvement** form to propose a correction to an
  existing entry.
- Use the **Bug report** form for website, content, or navigation problems.

Search the [live dictionary](https://ai-engineer-dictionary.vercel.app/), the
master vocabulary, and the CSV before proposing a new term. Wait for
maintainers to review a proposed term before adding it.

## Make a change

1. Fork the repository and create a focused branch.
2. Use `dictionary/TEMPLATE.qmd` for a new entry. Follow its metadata and
   required sections; write explanations in your own words.
3. Keep the term's page, letter index, A–Z index, sidebar, and vocabulary
   sources in sync when adding or renaming an approved term.
4. Cite reliable sources for non-obvious claims. Add a notebook only when code
   or an experiment materially improves understanding.
5. Run the existing entry and duplicate check:

   ```bash
   python scripts/validate_entries.py
   ```

6. Render the site and inspect changed pages and links:

   ```bash
   quarto render --output-dir _site
   ```

7. Open a pull request with a concise summary, sources, and the completed
   validation checklist.

Keep pull requests focused. One term or a small, related group of terms per
pull request is easier to review.

Never commit API keys, passwords, private datasets, or other secrets.
