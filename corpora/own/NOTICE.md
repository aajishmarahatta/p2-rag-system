# Notice for the own corpus

This corpus holds 300 documents. Each one is a modified, plain-text copy of the lead section of an English Wikipedia article about an NBA player.

- **Source:** English Wikipedia (https://en.wikipedia.org), articles in Category:NBA All-Stars.
- **Retrieved:** October 26, 2026.
- **License:** the text is available under the Creative Commons Attribution-ShareAlike 4.0 International license (CC BY-SA 4.0), https://creativecommons.org/licenses/by-sa/4.0/. These modified copies are shared under the same license.
- **Attribution:** the `source` column of `manifest.tsv` gives, for every document, the permanent link to the exact revision of the article that was copied. The history page of each article lists its authors. The `notes` column records the page id and revision id.
- **Changes made:** only the lead section of each article (the text before its first heading) was kept, as plain text from the MediaWiki TextExtracts API. The rest of the article, its formatting, images, tables, infobox and references are not included. `p2 ingest` then normalized whitespace and wrote each file as a title line followed by the text.
