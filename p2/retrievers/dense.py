"""Dense retrieval: embed every chunk once with bge-small-en-v1.5, embed the query, and rank chunks by cosine similarity.

Every vector has length 1 (p2/embed.py scales them), so a dot product is the cosine similarity.
ChunkScorer lifts the chunk scores to documents, a document scoring its best chunk.
"""

from p2 import embed
from p2.retrievers import ChunkScorer

NEEDS_CLAUDE = False


class Dense(ChunkScorer):
    model = embed.BGE

    def __init__(self, corpus, cfg):
        super().__init__(corpus, cfg)
        self.embedder = embed.load(self.model)
        self.vectors = embed.doc_vectors(self.embedder, [c.text for c in self.chunks], cfg.root)

    def score_chunks(self, text):
        query = self.embedder.encode([text])[0]
        return self.vectors @ query


def build(corpus, cfg):
    return Dense(corpus, cfg)
