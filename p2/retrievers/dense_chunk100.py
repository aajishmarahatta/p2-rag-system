"""Ablation of dense: the same retriever with chunks of 100 words instead of the 300 of p2.toml.

Only chunk_words changes; chunk_overlap stays at p2.toml's 50 and every other setting is the same.
"""

from p2.retrievers import dense

NEEDS_CLAUDE = False
BASE = "dense"
CHUNK_WORDS = 100


def build(corpus, cfg):
    return dense.build(corpus, cfg.replace(chunk_words=CHUNK_WORDS))
