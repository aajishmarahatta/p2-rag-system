"""Ablation of bm25: the same retriever with the 12 lab's "lab" tokenizer instead of the "codes" tokenizer of p2.toml.

Only the tokenizer changes; k1, b and the chunking stay at p2.toml's values and every other setting is the same.
"""

from p2.retrievers import bm25

NEEDS_CLAUDE = False
BASE = "bm25"
TOKENIZER = "lab"


def build(corpus, cfg):
    return bm25.build(corpus, cfg.replace(tokenizer=TOKENIZER))
