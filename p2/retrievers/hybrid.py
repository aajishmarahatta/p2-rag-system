"""Hybrid retrieval: reciprocal rank fusion (RRF, K = 60) of bm25 and dense, as in the 13 lab's rrf().

Each item scores the sum of 1 / (K + rank) over the rankings it appears in; only the ranks count,
not the bm25 scores or the cosine similarities. Each system is asked for its full ranking, not its
top k, because an item that is 11th in both lists can belong in the fused top k.
search ranks documents and search_chunks ranks chunks, which `p2 answer` needs.
"""

from p2 import retrievers
from p2.runfile import order

NEEDS_CLAUDE = False
K = 60


def fuse(rankings, k):
    """The k best ids of the fused ranking, as (id, score); equal scores in id order."""
    scores = {}
    for ranking in rankings:
        for rank, (item, _score) in enumerate(ranking, 1):
            scores[item] = scores.get(item, 0.0) + 1 / (K + rank)
    return order(scores.items())[:k]


class Hybrid:
    def __init__(self, corpus, cfg):
        self.systems = [retrievers.build(name, corpus, cfg) for name in ("bm25", "dense")]
        self.n_docs = len(corpus.docs)
        self.n_chunks = len(self.systems[0].chunks)

    def search(self, text, k):
        return fuse([s.search(text, self.n_docs) for s in self.systems], k)

    def search_chunks(self, text, k):
        return fuse([s.search_chunks(text, self.n_chunks) for s in self.systems], k)


def build(corpus, cfg):
    return Hybrid(corpus, cfg)
