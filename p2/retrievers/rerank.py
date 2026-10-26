"""Rerank: Claude reorders the top 20 of hybrid, as in the 13 lab's rerank_one().

One claude -p call per query shows the 20 candidates as numbered passages (each cut to its first 600
characters) and asks for the best order of all 20 numbers. A reply that is not each number once, or no
reply at all, keeps hybrid's order for that query and prints a warning. The candidates below the top 20
keep hybrid's order underneath. A document's score is 1 / its final rank, so the order is the run's order.
search ranks documents and search_chunks ranks chunks, which `p2 answer --system rerank` needs.
"""

from p2 import claude, retrievers

NEEDS_CLAUDE = True
CANDIDATES = 20
PASSAGE_CHARS = 600
PROMPT = """Below are {n} passages from the US federal mine safety and health regulations (30 CFR Chapter I), numbered 1 to {n}, and a search query.
Order the passages from the most useful for answering the query to the least useful.
Reply with all {n} passage numbers, each exactly once, best first.

Query: {query}

{passages}"""


def schema(n):
    """The reply must be {"order": [n numbers]}, each between 1 and n."""
    numbers = {"type": "integer", "minimum": 1, "maximum": n}
    return {
        "type": "object",
        "properties": {"order": {"type": "array", "items": numbers, "minItems": n, "maxItems": n}},
        "required": ["order"],
    }


class Rerank:
    def __init__(self, corpus, cfg):
        self.cfg = cfg
        self.model = cfg.model
        self.first = retrievers.build("hybrid", corpus, cfg)
        self.doc_texts = {docid: doc.text for docid, doc in corpus.docs.items()}
        self.chunk_texts = corpus.chunk_texts(cfg.chunk_words, cfg.chunk_overlap)

    def rerank(self, query, hits, texts, k):
        """hits: hybrid's (id, score) pairs, best first. Returns the k best ids of the new order as (id, 1 / rank)."""
        ids = [i for i, _ in hits]
        candidates = ids[:CANDIDATES]
        n = len(candidates)
        passages = "\n\n".join(f"[{number}] {texts[i][:PASSAGE_CHARS]}" for number, i in enumerate(candidates, 1))
        prompt = PROMPT.format(n=n, query=query, passages=passages)
        reply = claude.call(prompt, schema(n), model=self.cfg.model, cache_dir=claude.cache_folder(self.cfg))
        order = reply.output.get("order") if reply.output else None
        if reply.error or not isinstance(order, list) or sorted(order) != list(range(1, n + 1)):
            problem = reply.error or f"reply was not each of 1 to {n} once: {order}"
            print(f"  WARNING: {problem}; kept hybrid's order for this query", flush=True)
        else:
            candidates = [candidates[number - 1] for number in order]
        ids = candidates + ids[n:]
        return [(i, 1 / rank) for rank, i in enumerate(ids[:k], 1)]

    def search(self, text, k):
        hits = self.first.search(text, max(k, CANDIDATES))
        return self.rerank(text, hits, self.doc_texts, k)

    def search_chunks(self, text, k):
        hits = self.first.search_chunks(text, max(k, CANDIDATES))
        return self.rerank(text, hits, self.chunk_texts, k)


def build(corpus, cfg):
    return Rerank(corpus, cfg)
