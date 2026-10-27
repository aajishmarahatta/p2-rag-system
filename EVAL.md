# Evaluation report

This is the report on what you built and what the numbers let you claim.
Two kinds of text live here.

The tables between a `p2:begin` comment line and its matching `p2:end` comment line are written by `uv run p2 score` from your committed run files and answers files.
Please do not edit anything between those two lines, because `uv run p2 check` recomputes them and fails when they differ.
A table that says no runs or answers exist yet is waiting for data; run `uv run p2 score` after you commit the files it needs.

Everything else is yours.
Each prompt ends with a marker line that you replace with your own writing; `uv run p2 check --final` fails while one is left.
Write what you measured, including what did not work.
What I read for is whether each claim matches its interval, not whether the result is good news.

Words used below: recall@10, MRR@10 and nDCG@10 are the three scores, each averaged over the queries of a set; step 7 of stage 1 in the README defines them, and lecture 14 goes deeper.
A paired interval is the 95% interval of the mean difference between two systems on the same queries, found by resampling the queries 10,000 times.
When an interval includes zero, the gold set cannot tell the two systems apart, and the right words are "not distinguishable on this gold set".
The minimum detectable difference is the smallest gap this many queries could reliably show, so a difference below it is invisible to this gold set, not absent.

---

## 1. Stage 1 - the shared corpus (30 CFR Chapter I)

### What you built

For each of `dense`, `hybrid` and `rerank`, one or two sentences: the embedding model, how documents were chunked, what was fused and how, how many candidates the reranker saw, and anything you changed from the 12 and 13 lab code.

Dense uses the BGE-small-en-v1.5 embedding model. Each document is split into 300-word chunks that overlap by 50 words, and every chunk and the query are turned into vectors. The vectors are normalized to length 1, so a dot product between two of them is their cosine similarity. A document is ranked by its highest-scoring chunk.

Hybrid combines BM25 and Dense with reciprocal rank fusion (RRF) with K = 60. Each document gets the sum of 1 / (60 + rank) over the rankings it appears in, so only ranks count, not the BM25 scores or the cosine similarities.

Rerank takes Hybrid's top 20 candidates and asks Claude Sonnet, in one call per query, to put them in order, best first. Each candidate is shown as a numbered passage of at most its first 600 characters. If the reply is not each of the numbers 1 to 20 once, the query keeps Hybrid's order.

The code of Hybrid and Rerank says it follows the rrf() and rerank_one() functions of the lab 13 code, and the constants match the lab 13 `pipeline.py`: K = 60, 20 candidates, 600 characters per passage. I am not claiming any change from the labs beyond what the code shows, and I did not compare the rest of the lab code line by line.

### Practice queries (20)

Scores per system.

<!-- p2:begin shared-practice -->
| System | Recall@10 | MRR@10 | nDCG@10 |
| --- | ---: | ---: | ---: |
| bm25 | 0.625 | 0.507 | 0.518 |
| dense | 0.558 | 0.562 | 0.480 |
| hybrid | 0.592 | 0.471 | 0.443 |
| rerank | 0.758 | 0.800 | 0.759 |

20 judged queries; nDCG uses binary labels; a random ranking of the 2,484 documents would get recall@10 near 0.004.
<!-- p2:end shared-practice -->

The same scores per query class.

<!-- p2:begin shared-practice-classes -->
| System | Metric | identifier (n=7) | paraphrase (n=7) | mixed (n=6) |
| --- | --- | ---: | ---: | ---: |
| bm25 | Recall@10 | 1.000 | 0.000 | 0.917 |
| bm25 | MRR@10 | 0.810 | 0.000 | 0.746 |
| bm25 | nDCG@10 | 0.857 | 0.000 | 0.728 |
| dense | Recall@10 | 0.214 | 0.595 | 0.917 |
| dense | MRR@10 | 0.333 | 0.714 | 0.653 |
| dense | nDCG@10 | 0.211 | 0.593 | 0.661 |
| hybrid | Recall@10 | 0.500 | 0.405 | 0.917 |
| hybrid | MRR@10 | 0.514 | 0.152 | 0.792 |
| hybrid | nDCG@10 | 0.397 | 0.202 | 0.779 |
| rerank | Recall@10 | 0.714 | 0.595 | 1.000 |
| rerank | MRR@10 | 0.714 | 0.714 | 1.000 |
| rerank | nDCG@10 | 0.697 | 0.626 | 0.987 |
<!-- p2:end shared-practice-classes -->

Differences between every pair of systems, each with its paired interval and the minimum detectable difference.

<!-- p2:begin shared-practice-pairs -->
| Comparison | Metric | Mean difference | 95% interval | MDD | Reading |
| --- | --- | ---: | ---: | ---: | --- |
| dense minus bm25 | Recall@10 | -0.067 | [-0.350, +0.225] | 0.415 | not distinguishable |
| dense minus bm25 | MRR@10 | +0.055 | [-0.225, +0.343] | 0.412 | not distinguishable |
| dense minus bm25 | nDCG@10 | -0.039 | [-0.302, +0.231] | 0.385 | not distinguishable |
| hybrid minus bm25 | Recall@10 | -0.033 | [-0.250, +0.192] | 0.324 | not distinguishable |
| hybrid minus bm25 | MRR@10 | -0.037 | [-0.178, +0.083] | 0.192 | not distinguishable |
| hybrid minus bm25 | nDCG@10 | -0.075 | [-0.238, +0.075] | 0.228 | not distinguishable |
| hybrid minus dense | Recall@10 | +0.033 | [-0.125, +0.192] | 0.231 | not distinguishable |
| hybrid minus dense | MRR@10 | -0.092 | [-0.306, +0.109] | 0.301 | not distinguishable |
| hybrid minus dense | nDCG@10 | -0.036 | [-0.200, +0.113] | 0.227 | not distinguishable |
| rerank minus bm25 | Recall@10 | +0.133 | [-0.100, +0.358] | 0.340 | not distinguishable |
| rerank minus bm25 | MRR@10 | +0.293 | [+0.043, +0.533] | 0.353 | rerank higher |
| rerank minus bm25 | nDCG@10 | +0.240 | [+0.011, +0.457] | 0.325 | rerank higher |
| rerank minus dense | Recall@10 | +0.200 | [+0.050, +0.367] | 0.224 | rerank higher |
| rerank minus dense | MRR@10 | +0.237 | [+0.083, +0.408] | 0.239 | rerank higher |
| rerank minus dense | nDCG@10 | +0.279 | [+0.141, +0.433] | 0.214 | rerank higher |
| rerank minus hybrid | Recall@10 | +0.167 | [+0.058, +0.292] | 0.166 | rerank higher |
| rerank minus hybrid | MRR@10 | +0.329 | [+0.164, +0.504] | 0.247 | rerank higher |
| rerank minus hybrid | nDCG@10 | +0.316 | [+0.191, +0.444] | 0.184 | rerank higher |

The interval is a paired bootstrap (10,000 resamples of the queries); MDD is the smallest difference this many queries detect 80% of the time.
<!-- p2:end shared-practice-pairs -->

The 40 test queries have no answer key in this repo.
Your test run files are scored by the course and the score comes back to you as feedback, so nothing goes here for them.

### What the intervals let you claim

Which differences are distinguishable from zero and which are not?
What is the minimum detectable difference at 20 queries, and what does that say about any gap smaller than it?
Which claim from lecture 12 or 13 did your numbers support, and which did they leave open?

On the 20 practice queries, Rerank is the only system with differences from other systems that are distinguishable from zero. Rerank minus BM25 is higher on MRR@10 (+0.293, interval [+0.043, +0.533]) and nDCG@10 (+0.240, [+0.011, +0.457]). Rerank minus Dense is higher on all three metrics: Recall@10 +0.200 [+0.050, +0.367], MRR@10 +0.237 [+0.083, +0.408] and nDCG@10 +0.279 [+0.141, +0.433]. Rerank minus Hybrid is also higher on all three: Recall@10 +0.167 [+0.058, +0.292], MRR@10 +0.329 [+0.164, +0.504] and nDCG@10 +0.316 [+0.191, +0.444]. The BM25 intervals for MRR@10 and nDCG@10 have lower ends close to zero, so that evidence is weaker than the evidence against Dense and Hybrid. Rerank minus BM25 on Recall@10 (+0.133, [-0.100, +0.358]) is not distinguishable on this gold set.

Every comparison among BM25, Dense and Hybrid, on all three metrics, has an interval that includes zero, so those are not distinguishable on this gold set. For example, Dense minus BM25 on MRR@10 is +0.055 [-0.225, +0.343] and Hybrid minus BM25 on MRR@10 is -0.037 [-0.178, +0.083]. This does not mean they are equal. The minimum detectable difference (MDD) for these pairs is between 0.192 and 0.415. The MDD is the size of difference that 20 queries would detect about 80% of the time (roughly 80% power), so a smaller difference is detected less reliably, though it is not impossible to detect. The observed gaps are all smaller than the MDD, so 20 queries would be unlikely to show them reliably even if they are real. The scores on the three systems should not be ranked by their averages.

The per-query-class table shows the pattern behind this, but its classes have only 6 or 7 queries each and no intervals, so I read it as descriptive only. On paraphrase queries BM25 scored 0.000 on all three metrics, while Dense scored MRR@10 0.714 and Rerank 0.714. On identifier queries BM25 scored Recall@10 1.000 and MRR@10 0.810, while Dense scored 0.214 and 0.333 and Rerank 0.714 and 0.714. This fits the lecture claim that no retrieval method wins across all query types: keyword search was strongest on identifiers and failed on paraphrases, and the embedding search was the other way around. Rerank did not win every cell either, because BM25's mean on identifier queries is higher than Rerank's. My numbers support the claim as a pattern, but they do not prove it for a single pair of systems, because the pairwise intervals among BM25, Dense and Hybrid include zero.

---

## 2. Stage 1 - cited answers on the 12 shared questions

<!-- p2:begin answers -->
| Label | System | Verified (in) | 95% interval | not_found (in) | Declined (out) | 95% interval | Quotes found |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| rerank | rerank | 8 of 8 (100%) | [0.676, 1.000] | 0 of 8 (0%) | 4 of 4 (100%) | [0.510, 1.000] | 11 of 11 |
<!-- p2:end answers -->

Which system answered, and why that one?
What did you change in `prompts/answer.txt`, if anything, and did the verified share or the declined share move?

Then read three in-corpus answers that `uv run p2 verify` passed.
For each one, open the cited chunk and say whether the quote really supports the claim next to it.
The check proves a quote is a real piece of the chunk and cannot prove that it supports the claim, so this reading is the part only you can do.

I used Rerank to answer the 12 shared questions, because it had the strongest shared retrieval performance, especially on MRR@10 (0.800) and nDCG@10 (0.759). I did not change `prompts/answer.txt` from its original version, so there is no before-and-after prompt comparison and no way to say whether the prompt moved the verified or declined share.

All 8 answerable questions passed verification, all 4 unanswerable questions were correctly declined, and all 11 cited quotations were found in their chunks. With so few questions, these shares are less certain than 100% sounds. The Wilson 95% interval for 8 of 8 verified is [0.676, 1.000], and for 4 of 4 declined it is [0.510, 1.000], so the true rate could still be well below 100%. Automated verification only checks that a quotation is present in the cited chunk. It does not check that the claim next to it is logically supported by the quotation, which is why I read answers myself below.

Manual review of cited answers. I personally reviewed three in-corpus answers, a01, a04 and a07, and one additional out-of-corpus refusal, a10. These are the only answers I reviewed by hand.

a01 - fully supported. The question was "Within how many minutes must a mine operator call MSHA after an accident that kills a miner?" I compared the generated answer against 30 CFR 50.10, "Immediate notification." The answer correctly says a mine operator must contact MSHA immediately and within 15 minutes once the operator knows or should know that an accident involving a death has occurred. It also correctly gives the toll-free telephone number, 1-800-746-1553. Both generated claims are directly supported by the cited document, cfr30-50.10#0. The first claim accurately reflects the immediate notification requirement, the 15-minute deadline and the telephone number. The second claim correctly identifies a death at the mine as one of the accidents requiring notification, as specified in subsection (a). The wording of the claims closely matches the regulation, and I found no unsupported additions.

a04 - supported. The question was "How often must an underground metal or nonmetal mine hold evacuation drills?" I compared both generated claims against 30 CFR 57.4361. The answer correctly says evacuation drills must occur at least once every six months, as subsection (a) requires. It also correctly says drills must occur for each shift outside shift changes and involve everyone underground, as subsection (b)(1) requires. Both claims are directly supported by their citations, with no unsupported additions.

a07 - supported. The question was "How high must berms or guardrails be on the banks of roadways at metal and nonmetal mines?" I compared the answer against both 30 CFR 56.9300 and 57.9300. Subsection (b) of both regulations says berms or guardrails must be at least mid-axle height of the largest self-propelled mobile equipment that usually travels the roadway, so both citations support the answer. I also noticed that subsection (d) has exceptions for certain infrequently traveled elevated roadways when specific safeguards are present. The answer does not mention these exceptions, but its stated height requirement is correct for situations where berms or guardrails are required.

a10 - appropriate refusal. The question was "At what depth does OSHA require a construction trench to have a protective system such as shoring or a trench box?" The system returned not_found with no claims. I searched the shared corpus myself with `grep -il "trench" corpora/shared/docs/*.md`, `grep -il "shoring" corpora/shared/docs/*.md` and `grep -il "trench box" corpora/shared/docs/*.md`. All three returned no results. This supports the refusal, because the shared corpus covers federal mine-safety regulations and not OSHA construction-trenching requirements. The system avoided answering from unsupported outside knowledge.

Overall: a01 is fully supported, a04 is supported, and a07 is supported with a relevant exception that the answer does not mention, so all three in-corpus answers were supported by their cited evidence. a10 was appropriately declined. `p2 verify` confirmed that the cited quotations exist in their referenced chunks. My manual review additionally checked whether the evidence supports the claims.

---

## 3. Stage 2 - your corpus and your gold set

### The corpus

What is it, where did it come from, how many documents and how many megabytes, and what is the license basis for publishing it?
Name the one or two documents you were least sure about and what you decided.
Say which of the allowed sources in the brief it comes from.

My own corpus has 300 documents, each the lead section of an English Wikipedia article about an NBA All-Star player (from Category:NBA All-Stars). I collected them on October 26, 2026 through the MediaWiki API, and the `source` column of `manifest.tsv` links every document to the exact article revision I copied. The text totals about 0.33 MB (334,840 bytes). The selection rule was fixed before I evaluated any query: all valid biography pages in the category, from which 300 were picked with a seeded random sample (seed 498).

The source is Wikipedia, which the brief lists among the allowed sources as CC BY-SA text with attribution. The manifest lists all 300 documents as `cc-by-sa-4.0`. `corpora/own/NOTICE.md` gives the attribution and the license, and `LICENSES.md` reports 300 documents ok, with no flags and no failures.

There was no document I was unsure about including. I did not identify any specific NBA biography that I doubted.

### The gold set

How many queries, how many with origin `hand` and how many with origin `claude`, and which query classes did you use and why?
How did you decide that a document is relevant: write your relevance rule in two or three sentences, the way the brief does for the shared corpus.
How did you find candidates (the systems' top 10, a keyword search, reading), and did you read every document before you labeled it?
Your labels are binary (`rel` 1) unless you say otherwise: if you use graded labels, declare the scale here, for example 2 means the document answers the query fully and 1 means it helps.

The gold set has 30 judged queries, 10 with origin `hand` (I wrote them) and 20 with origin `claude` (drafted by Claude). It uses three query classes with 10 queries each: identifier, mixed and paraphrase. It has 97 binary relevance judgments (`rel` 1), with no graded scale.

My relevance rule is that a document is relevant when the information in its biography lead supports an answer to the query. I made all the final relevance judgments myself, for both the hand and the claude queries.

I found candidate documents by pooling the top 10 of BM25, Dense and Hybrid for each query, plus keyword searches for terms related to the query. The candidates were shown to me without retrieval scores or rankings, so what I judged did not depend on which system returned a document first.

The 97 judgments are the relevant documents I found among those candidates. They are not necessarily an exhaustive judgment of all 300 documents for every query, so a document I never saw as a candidate counts as not relevant, and the recall scores may be slightly too high or too low because of that.

Yes, I read the full biography lead of every candidate document that was shown to me before I made my relevance judgments.

---

## 4. Stage 2 - results on your corpus

Scores per system on your gold set.

<!-- p2:begin own -->
| System | Recall@10 | MRR@10 | nDCG@10 |
| --- | ---: | ---: | ---: |
| bm25 | 0.734 | 0.769 | 0.676 |
| dense | 0.447 | 0.448 | 0.375 |
| hybrid | 0.629 | 0.693 | 0.553 |
| rerank | 0.735 | 0.878 | 0.731 |
| ablation/dense_chunk100 | 0.467 | 0.484 | 0.382 |

30 judged queries; nDCG uses binary labels; a random ranking of the 300 documents would get recall@10 near 0.033.
<!-- p2:end own -->

The same scores per query class.

<!-- p2:begin own-classes -->
| System | Metric | mixed (n=10) | identifier (n=10) | paraphrase (n=10) |
| --- | --- | ---: | ---: | ---: |
| bm25 | Recall@10 | 0.752 | 0.975 | 0.475 |
| bm25 | MRR@10 | 0.808 | 0.933 | 0.567 |
| bm25 | nDCG@10 | 0.691 | 0.948 | 0.388 |
| dense | Recall@10 | 0.443 | 0.583 | 0.315 |
| dense | MRR@10 | 0.353 | 0.613 | 0.378 |
| dense | nDCG@10 | 0.304 | 0.566 | 0.255 |
| hybrid | Recall@10 | 0.620 | 0.773 | 0.495 |
| hybrid | MRR@10 | 0.703 | 0.850 | 0.525 |
| hybrid | nDCG@10 | 0.539 | 0.744 | 0.377 |
| rerank | Recall@10 | 0.773 | 0.902 | 0.530 |
| rerank | MRR@10 | 0.950 | 0.933 | 0.750 |
| rerank | nDCG@10 | 0.809 | 0.839 | 0.544 |
| ablation/dense_chunk100 | Recall@10 | 0.337 | 0.770 | 0.294 |
| ablation/dense_chunk100 | MRR@10 | 0.430 | 0.607 | 0.414 |
| ablation/dense_chunk100 | nDCG@10 | 0.292 | 0.578 | 0.277 |
<!-- p2:end own-classes -->

The same scores for the queries you wrote yourself (`hand`) and the ones a model drafted (`claude`), with the difference between the two groups and its interval.
Once both groups have queries, the table also says whether `bm25`'s lead over `dense` differs between them, and what share of each query's content words its best relevant document contains, which is stretch option 6.

<!-- p2:begin own-origins -->
| System | Metric | hand (n=10) | claude (n=20) | hand minus claude | 95% interval | Reading |
| --- | --- | ---: | ---: | ---: | ---: | --- |
| bm25 | Recall@10 | 0.742 | 0.730 | +0.012 | [-0.241, +0.244] | not distinguishable |
| bm25 | MRR@10 | 0.675 | 0.817 | -0.142 | [-0.400, +0.117] | not distinguishable |
| bm25 | nDCG@10 | 0.642 | 0.693 | -0.051 | [-0.302, +0.187] | not distinguishable |
| dense | Recall@10 | 0.617 | 0.363 | +0.254 | [-0.031, +0.525] | not distinguishable |
| dense | MRR@10 | 0.417 | 0.463 | -0.046 | [-0.352, +0.273] | not distinguishable |
| dense | nDCG@10 | 0.455 | 0.335 | +0.120 | [-0.155, +0.401] | not distinguishable |
| hybrid | Recall@10 | 0.742 | 0.573 | +0.169 | [-0.079, +0.398] | not distinguishable |
| hybrid | MRR@10 | 0.595 | 0.742 | -0.147 | [-0.443, +0.150] | not distinguishable |
| hybrid | nDCG@10 | 0.577 | 0.542 | +0.035 | [-0.207, +0.274] | not distinguishable |
| rerank | Recall@10 | 0.875 | 0.665 | +0.210 | [-0.035, +0.414] | not distinguishable |
| rerank | MRR@10 | 0.850 | 0.892 | -0.042 | [-0.292, +0.175] | not distinguishable |
| rerank | nDCG@10 | 0.840 | 0.676 | +0.165 | [-0.072, +0.356] | not distinguishable |
| ablation/dense_chunk100 | Recall@10 | 0.542 | 0.430 | +0.112 | [-0.200, +0.413] | not distinguishable |
| ablation/dense_chunk100 | MRR@10 | 0.464 | 0.493 | -0.029 | [-0.339, +0.293] | not distinguishable |
| ablation/dense_chunk100 | nDCG@10 | 0.440 | 0.353 | +0.087 | [-0.182, +0.364] | not distinguishable |

The hand and claude queries are different queries, so the interval of hand minus claude comes from resampling the queries within each group (10,000 times), not from pairing them.

Do model-written queries favor keyword search? bm25's lead over dense (bm25 minus dense, per query) on the claude queries and on the hand queries, and claude minus hand:

| Metric | Lead on claude | Lead on hand | Claude minus hand | 95% interval | Reading |
| --- | ---: | ---: | ---: | ---: | --- |
| Recall@10 | +0.367 | +0.125 | +0.242 | [-0.041, +0.501] | not distinguishable |
| MRR@10 | +0.353 | +0.258 | +0.096 | [-0.200, +0.386] | not distinguishable |
| nDCG@10 | +0.358 | +0.187 | +0.171 | [-0.096, +0.434] | not distinguishable |

Mean content-word overlap, the share of a query's content words found in its best relevant document: hand 0.73 (10 queries), claude 0.80 (20 queries).

Stretch option 6 asks for at least 20 judged queries of each origin; here there are 10 hand and 20 claude.
<!-- p2:end own-origins -->

Differences between every pair of systems.

<!-- p2:begin own-pairs -->
| Comparison | Metric | Mean difference | 95% interval | MDD | Reading |
| --- | --- | ---: | ---: | ---: | --- |
| dense minus bm25 | Recall@10 | -0.287 | [-0.446, -0.140] | 0.223 | bm25 higher |
| dense minus bm25 | MRR@10 | -0.321 | [-0.492, -0.158] | 0.243 | bm25 higher |
| dense minus bm25 | nDCG@10 | -0.301 | [-0.462, -0.152] | 0.226 | bm25 higher |
| hybrid minus bm25 | Recall@10 | -0.105 | [-0.219, -0.001] | 0.160 | bm25 higher |
| hybrid minus bm25 | MRR@10 | -0.077 | [-0.208, +0.048] | 0.187 | not distinguishable |
| hybrid minus bm25 | nDCG@10 | -0.122 | [-0.241, -0.015] | 0.165 | bm25 higher |
| hybrid minus dense | Recall@10 | +0.182 | [+0.089, +0.291] | 0.148 | hybrid higher |
| hybrid minus dense | MRR@10 | +0.245 | [+0.139, +0.363] | 0.163 | hybrid higher |
| hybrid minus dense | nDCG@10 | +0.178 | [+0.111, +0.254] | 0.103 | hybrid higher |
| rerank minus bm25 | Recall@10 | +0.001 | [-0.087, +0.089] | 0.127 | not distinguishable |
| rerank minus bm25 | MRR@10 | +0.108 | [-0.006, +0.225] | 0.171 | not distinguishable |
| rerank minus bm25 | nDCG@10 | +0.055 | [-0.050, +0.158] | 0.154 | not distinguishable |
| rerank minus dense | Recall@10 | +0.288 | [+0.178, +0.410] | 0.169 | rerank higher |
| rerank minus dense | MRR@10 | +0.430 | [+0.287, +0.577] | 0.209 | rerank higher |
| rerank minus dense | nDCG@10 | +0.356 | [+0.248, +0.468] | 0.158 | rerank higher |
| rerank minus hybrid | Recall@10 | +0.106 | [+0.031, +0.187] | 0.115 | rerank higher |
| rerank minus hybrid | MRR@10 | +0.185 | [+0.077, +0.304] | 0.166 | rerank higher |
| rerank minus hybrid | nDCG@10 | +0.177 | [+0.098, +0.266] | 0.122 | rerank higher |
| ablation/dense_chunk100 minus bm25 | Recall@10 | -0.267 | [-0.415, -0.126] | 0.213 | bm25 higher |
| ablation/dense_chunk100 minus bm25 | MRR@10 | -0.286 | [-0.457, -0.113] | 0.254 | bm25 higher |
| ablation/dense_chunk100 minus bm25 | nDCG@10 | -0.294 | [-0.443, -0.147] | 0.220 | bm25 higher |
| ablation/dense_chunk100 minus dense | Recall@10 | +0.020 | [-0.094, +0.130] | 0.164 | not distinguishable |
| ablation/dense_chunk100 minus dense | MRR@10 | +0.036 | [-0.101, +0.180] | 0.204 | not distinguishable |
| ablation/dense_chunk100 minus dense | nDCG@10 | +0.007 | [-0.093, +0.110] | 0.147 | not distinguishable |
| ablation/dense_chunk100 minus hybrid | Recall@10 | -0.162 | [-0.299, -0.030] | 0.196 | hybrid higher |
| ablation/dense_chunk100 minus hybrid | MRR@10 | -0.209 | [-0.329, -0.084] | 0.182 | hybrid higher |
| ablation/dense_chunk100 minus hybrid | nDCG@10 | -0.171 | [-0.272, -0.067] | 0.152 | hybrid higher |
| ablation/dense_chunk100 minus rerank | Recall@10 | -0.268 | [-0.391, -0.148] | 0.178 | rerank higher |
| ablation/dense_chunk100 minus rerank | MRR@10 | -0.394 | [-0.540, -0.256] | 0.207 | rerank higher |
| ablation/dense_chunk100 minus rerank | nDCG@10 | -0.349 | [-0.469, -0.229] | 0.174 | rerank higher |

The interval is a paired bootstrap (10,000 resamples of the queries); MDD is the smallest difference this many queries detect 80% of the time.
<!-- p2:end own-pairs -->

Which differences are distinguishable and which are not, at your gold-set size?
Do the `hand` queries and the `claude` queries tell the same story?
Did your prediction in `DECISIONS.md` prompt 1 hold?

On my 30 queries, BM25 scored Recall@10 0.734, MRR@10 0.769 and nDCG@10 0.676. Dense scored 0.447, 0.448 and 0.375, Hybrid 0.629, 0.693 and 0.553, and Rerank 0.735, 0.878 and 0.731.

These differences have a paired 95% interval that excludes zero:
- Dense is below BM25 on all three metrics: Recall@10 -0.287 [-0.446, -0.140], MRR@10 -0.321 [-0.492, -0.158] and nDCG@10 -0.301 [-0.462, -0.152].
- Hybrid is below BM25 on Recall@10 (-0.105 [-0.219, -0.001]) and nDCG@10 (-0.122 [-0.241, -0.015]). The Recall@10 interval ends at -0.001, so that one only just excludes zero.
- Hybrid is above Dense on all three: Recall@10 +0.182 [+0.089, +0.291], MRR@10 +0.245 [+0.139, +0.363] and nDCG@10 +0.178 [+0.111, +0.254].
- Rerank is above Dense on all three: Recall@10 +0.288 [+0.178, +0.410], MRR@10 +0.430 [+0.287, +0.577] and nDCG@10 +0.356 [+0.248, +0.468].
- Rerank is above Hybrid on all three: Recall@10 +0.106 [+0.031, +0.187], MRR@10 +0.185 [+0.077, +0.304] and nDCG@10 +0.177 [+0.098, +0.266].

These are not distinguishable on this gold set, because their intervals include zero: Hybrid minus BM25 on MRR@10 (-0.077 [-0.208, +0.048]), and Rerank minus BM25 on Recall@10 (+0.001 [-0.087, +0.089]), MRR@10 (+0.108 [-0.006, +0.225]) and nDCG@10 (+0.055 [-0.050, +0.158]).

Rerank has the highest mean MRR@10 (0.878 against BM25's 0.769), but that does not show that it beats BM25. The difference is +0.108 with the interval [-0.006, +0.225], which includes zero, and it is smaller than the minimum detectable difference (MDD) of 0.171 for that pair. The MDD is the size of difference that 30 queries would detect about 80% of the time (roughly 80% power), so a difference of +0.108 would be detected less reliably than that, though it is not impossible to detect. So the gold set does not distinguish Rerank from BM25. This does not mean they are equal, only that the evidence is too weak to say which is better.

BM25 is clearly better than Dense on this corpus, with every Dense minus BM25 interval below zero. The per-class table shows BM25's mean above Dense's in all three classes (MRR@10: mixed 0.808 against 0.353, identifier 0.933 against 0.613, paraphrase 0.567 against 0.378), but those class means have 10 queries each and no intervals. One possible reason is that my queries share many words with their relevant documents (mean content-word overlap 0.73 for hand queries and 0.80 for claude queries), which helps keyword search. I did not test this, so it is a guess. Hybrid and Rerank are both clearly better than Dense, and Rerank is also clearly better than Hybrid.

Hand against claude queries: all 15 intervals for hand minus claude include zero, so none of the differences between my 10 hand queries and the 20 claude queries is distinguishable on this gold set. For example, BM25 MRR@10 is 0.675 on hand and 0.817 on claude (-0.142 [-0.400, +0.117]), and Dense Recall@10 is 0.617 on hand and 0.363 on claude (+0.254 [-0.031, +0.525]). The extra comparison of BM25's lead over Dense on claude queries against hand queries is also not distinguishable (for example MRR@10 +0.096 [-0.200, +0.386]). With only 10 hand queries, a real difference between the two groups could be hidden.

What 30 queries can and cannot show: the MDD for pairs among the four systems runs from 0.103 to 0.243. That is the size of difference these 30 queries would detect about 80% of the time, so a smaller gap is detected less reliably, though it is not impossible to detect. I can say that Dense is worse than BM25, and that Rerank and Hybrid are better than Dense. I cannot say which of BM25 and Rerank is better, and this gold set does not distinguish whether Hybrid is below BM25 on MRR@10. Per-class and per-origin groups have only 10 or 20 queries and the intervals for them are wide.

My `DECISIONS.md` prompt 1 was not committed before I scored my own corpus, so there is no recorded prediction made before the measurement to compare with these results.

I did not have a clear prediction beforehand about whether BM25, Dense, Hybrid or Rerank would do best or worst on my corpus, and I did not commit a prediction in `DECISIONS.md` before running the own-corpus evaluation. So I cannot compare these results with a ranking of the systems that I made in advance.

---

## 5. The ablation

Change one thing and keep everything else the same.
Write your hypothesis here before you run it, in one sentence with a direction: "I expect X to raise MRR@10 on my corpus because Y."
The run file for it lives in `runs/own/ablation/`.

I expect Dense MRR@10 to decrease when reducing the chunk from 300 to 100 words because shorter chunks may focus the embedding on fewer facts instead of representing an entire biography lead at once.

<!-- p2:begin own-ablation -->
| Comparison | Metric | Mean difference | 95% interval | MDD | Reading |
| --- | --- | ---: | ---: | ---: | --- |
| ablation/dense_chunk100 minus bm25 | Recall@10 | -0.267 | [-0.415, -0.126] | 0.213 | bm25 higher |
| ablation/dense_chunk100 minus bm25 | MRR@10 | -0.286 | [-0.457, -0.113] | 0.254 | bm25 higher |
| ablation/dense_chunk100 minus bm25 | nDCG@10 | -0.294 | [-0.443, -0.147] | 0.220 | bm25 higher |
| ablation/dense_chunk100 minus dense | Recall@10 | +0.020 | [-0.094, +0.130] | 0.164 | not distinguishable |
| ablation/dense_chunk100 minus dense | MRR@10 | +0.036 | [-0.101, +0.180] | 0.204 | not distinguishable |
| ablation/dense_chunk100 minus dense | nDCG@10 | +0.007 | [-0.093, +0.110] | 0.147 | not distinguishable |
| ablation/dense_chunk100 minus hybrid | Recall@10 | -0.162 | [-0.299, -0.030] | 0.196 | hybrid higher |
| ablation/dense_chunk100 minus hybrid | MRR@10 | -0.209 | [-0.329, -0.084] | 0.182 | hybrid higher |
| ablation/dense_chunk100 minus hybrid | nDCG@10 | -0.171 | [-0.272, -0.067] | 0.152 | hybrid higher |
| ablation/dense_chunk100 minus rerank | Recall@10 | -0.268 | [-0.391, -0.148] | 0.178 | rerank higher |
| ablation/dense_chunk100 minus rerank | MRR@10 | -0.394 | [-0.540, -0.256] | 0.207 | rerank higher |
| ablation/dense_chunk100 minus rerank | nDCG@10 | -0.349 | [-0.469, -0.229] | 0.174 | rerank higher |

The interval is a paired bootstrap (10,000 resamples of the queries); MDD is the smallest difference this many queries detect 80% of the time.
<!-- p2:end own-ablation -->

The queries your ablation helped and hurt, against the system it varies, by reciprocal rank.
`p2 score` finds that system from a line such as `BASE = "bm25"` in your variant's file, or else from its name: `bm25_lab` varies `bm25`.

<!-- p2:begin own-ablation-queries -->
ablation/dense_chunk100 against dense (BASE = "dense" in p2/retrievers/dense_chunk100.py): it helped 10 queries, hurt 9 and left 11 unchanged.

| Query | Class | Origin | dense RR | ablation/dense_chunk100 RR | Change | Effect |
| --- | --- | --- | ---: | ---: | ---: | --- |
| q04 | mixed | hand | 0.125 | 1.000 | +0.875 | helped |
| q11 | identifier | claude | 0.125 | 1.000 | +0.875 | helped |
| q23 | mixed | claude | 0.167 | 1.000 | +0.833 | helped |
| q27 | paraphrase | claude | 0.500 | 1.000 | +0.500 | helped |
| q30 | paraphrase | claude | 0.500 | 1.000 | +0.500 | helped |
| q09 | paraphrase | hand | 0.250 | 0.500 | +0.250 | helped |
| q12 | identifier | claude | 0.000 | 0.200 | +0.200 | helped |
| q13 | identifier | claude | 0.000 | 0.143 | +0.143 | helped |
| q14 | identifier | claude | 0.000 | 0.111 | +0.111 | helped |
| q19 | mixed | claude | 0.000 | 0.100 | +0.100 | helped |
| q15 | identifier | claude | 1.000 | 0.111 | -0.889 | hurt |
| q07 | identifier | hand | 1.000 | 0.500 | -0.500 | hurt |
| q18 | mixed | claude | 1.000 | 0.500 | -0.500 | hurt |
| q28 | paraphrase | claude | 1.000 | 0.500 | -0.500 | hurt |
| q26 | paraphrase | claude | 0.333 | 0.000 | -0.333 | hurt |
| q24 | mixed | claude | 0.500 | 0.200 | -0.300 | hurt |
| q21 | mixed | claude | 0.143 | 0.000 | -0.143 | hurt |
| q01 | mixed | hand | 0.100 | 0.000 | -0.100 | hurt |
| q06 | paraphrase | hand | 0.200 | 0.143 | -0.057 | hurt |

RR is the reciprocal rank of the first relevant document in the top 10 (0 when none is there), the per-query value behind MRR@10; the queries at the top of each list are the ones to read.
<!-- p2:end own-ablation-queries -->

What did you change, what happened, and does the interval support the claim you want to make?
If the result is not distinguishable, say what size of effect your gold set could have seen.
Read the queries at the top of each list in the second table, and say whether your change explains them.

The one change is the chunk size of Dense: the baseline Dense uses 300-word chunks, and the ablation (`p2/retrievers/dense_chunk100.py`) uses 100-word chunks. The chunk overlap stayed at 50 words and every other setting is the same as Dense. My hypothesis, written and committed before I ran it, predicted that Dense MRR@10 would decrease.

The result went the other way, but not by enough to show anything. Dense MRR@10 was 0.448 and the 100-word version scored 0.484, a difference of +0.036 with the interval [-0.101, +0.180], and an MDD of 0.204. Recall@10 changed by +0.020 [-0.094, +0.130] (MDD 0.164) and nDCG@10 by +0.007 [-0.093, +0.110] (MDD 0.147). All three intervals include zero, so the change is not distinguishable on this gold set. The predicted decrease was not supported by the observed mean, because the mean moved the other way, but I cannot claim an increase either. The MDDs of 0.147 to 0.204 are the sizes of difference that 30 queries would detect about 80% of the time, so an effect as small as the observed +0.036 on MRR@10 would be detected much less reliably. The 100-word Dense is also still clearly below BM25 (MRR@10 -0.286 [-0.457, -0.113]), so this change did not close the gap.

A limitation of the design is that I kept the overlap fixed at 50 words. With 300-word chunks the overlap is about 17% of a chunk, and with 100-word chunks it is 50%. So the ablation changed the relative overlap as well as the chunk size, and I cannot separate the two effects.

The change helped 10 queries, hurt 9 and left 11 unchanged, which fits a result with no clear direction. In the per-query table, the first relevant document moved as follows (rank in the top 10 for Dense with 300-word chunks, then for the 100-word version):
- q04 ("Which players won an NCAA national championship while playing for UConn?"): Kemba Walker from rank 8 to 1. The other relevant document, Richard Hamilton, was not in the top 10 before and is at rank 7 afterwards.
- q11 ("Winners of the John R. Wooden Award for the top men's college player"): Sean Elliott from rank 8 to 1. Tim Duncan and Danny Ainge were not in the top 10 before and are at ranks 7 and 9 afterwards.
- q15 ("Played for the Harlem Globetrotters before reaching the NBA"): Wilt Chamberlain from rank 1 to 9.
- q07 ("Which Canadian players have won NBA MVP?"): Shai Gilgeous-Alexander from rank 1 to 2.

These are possible explanations, not demonstrated causes, because I did not inspect the similarity scores of individual chunks.
- q04: Kemba Walker moved from rank 8 to 1. Shorter chunks may have helped the embedding focus on the information about his UConn championship.
- q11: Sean Elliott moved from rank 8 to 1. Shorter chunks may have emphasized the Wooden Award information rather than his entire career.
- q15: Wilt Chamberlain moved from rank 1 to 9. Shorter chunks may have lost some broader context, although the relevant Globetrotters sentence appears in chunks under both settings.
- q07: Shai Gilgeous-Alexander moved from rank 1 to 2, and Kawhi Leonard moved above him. Leonard's lead refers to Finals MVP, not to a Canadian winning the NBA MVP, so this looks like a loose match to part of the query, but I have not checked it against the chunk scores.

Two queries moving up and two moving down fits the overall finding that the ablation was not distinguishable from baseline Dense on this gold set. My hypothesis (shorter chunks focus the embedding on fewer facts) is a possible reading of q04 and q11 and does not fit q15, but with 10 queries helped and 9 hurt, I cannot say that chunk size explains any of these changes.

---

## 6. Failure analysis

Pick the queries where your best system on your own corpus failed: the relevant document is missing from the top 10, or sits far below the top.
Take at least five, and read what the system returned next to what was relevant.
Then sort the failures by cause, for example a vocabulary mismatch, near-duplicate documents, a chunk that cut the answer in half, a query that is ambiguous, or a label that was wrong, because sometimes the gold set is what failed.

| qid | what the best system returned | what was relevant | cause | what you would try |
|---|---|---|---|---|
| q10 "Which players have a son who also played in the NBA?" | Top 10 had none of the 2 relevant documents. It began with Wes Unseld, Devin Booker and Kobe Bryant. Unseld's lead says "His son, Wes Unseld Jr., is currently an assistant coach"; the Booker and Bryant leads say they are the "son of" a player. | `glenn-robinson` ("the father of Glenn Robinson III, who ... has also played in the NBA") and `tim-hardaway` ("the father of NBA player Tim Hardaway Jr."). Hybrid ranked them 97 and 116, outside the 20 candidates Rerank can reorder. | Possible: the relevant leads say "father of" and not "son", and the query asks about a relationship that the returned leads state in the other direction. Not tested. | A top-50 pool would not be enough, because Hybrid ranked the relevant documents 97 and 116. A future experiment could test a much wider pool (more than 116 candidates, which costs far more Claude input per query), or improve the first-stage retrieval, for example by rewriting the query. I do not know that either would work. |
| q25 "Was never picked in the NBA draft but still reached the league" | Top 10 had none of the 2 relevant documents. It began with Moses Malone, Gus Johnson and DeAndre Jordan; their leads say they were "selected" in a draft (Malone in the 1974 ABA draft, Johnson in 1963, Jordan in 2008). | `fred-vanvleet` ("After going undrafted in the 2016 NBA draft") and `john-starks` ("He was undrafted in the 1988 NBA draft"). Hybrid ranked them 86 and 109, outside the 20 candidates. | Possible: the returned leads share the words "NBA draft" with the query but state the opposite, while the relevant leads say "undrafted" and not "never picked". Not tested. | As for q10, a top-50 pool would not reach Hybrid ranks 86 and 109, so I would test either a much wider pool (more than 109 candidates) or a query rewritten to use "undrafted", compared separately. I do not know that either would work. |
| q12 "Won the NBA Three-Point Contest" | Both relevant documents were in the top 10, at ranks 3 (`peja-stojakovic`) and 6 (`karl-anthony-towns`), so this is a low first-relevant rank (reciprocal rank 0.333), not a miss. Ranks 1 and 2 were Larry Bird and Stephen Curry; my text search found no "contest" or "shootout" in the leads of Bird, Curry or Klay Thompson. | `karl-anthony-towns` ("the first center to win the NBA Three-Point Contest in 2022") and `peja-stojakovic` ("won the NBA Three-Point Contest two times"). Both sentences start after character 1,000 of the document, beyond the first 600 characters that Rerank sees. | Possible: Rerank could not see the contest sentences and ranked on the three-point shooting wording in the first 600 characters. Not tested. | Show Rerank the part of each lead that best matches the query, or 1,200 characters, and see whether ranks 1 and 2 change. |
| q27 "Players who also acted in movies or on television" | Partial recall: 1 of 7 relevant documents in the top 10 (`dennis-rodman`, rank 1). Others returned included Baron Davis (his lead says "television host") and Bill Walton ("television sportscaster"), which I did not judge relevant, and Julius Erving and Wilt Chamberlain, whose leads contain none of the acting or television words I searched for. | 7 relevant, 6 missing: `elgin-baylor` (Hybrid rank 15), `kyrie-irving` (25), `shaquille-o-neal` (30), `kevin-garnett` (48), `lamelo-ball` (236), `amar-e-stoudemire` (247). The evidence for each starts after character 1,489, beyond the first 600 characters Rerank sees. Only Baylor was within the top 20 candidates. | Possible: the evidence sits late in the lead, and for five of the six the documents never reached Rerank's 20 candidates. Not tested. | A top-50 pool would reach four of the six missing documents (Hybrid ranks 15, 25, 30 and 48) but not `lamelo-ball` (236) or `amar-e-stoudemire` (247), so I would test a top-50 pool together with the longer view from q12 and check which relevant documents enter the top 10. I do not know that either would work. |
| q29 "Played club basketball in the Italian league" | Partial recall: 1 of 7 relevant documents in the top 10 (`manu-ginobili`, rank 1). Peja Stojakovic was rank 2; his lead mentions an Italian newspaper (Gazzetta dello Sport), not playing in Italy. My search found no Italian words in the Deni Avdija or Dirk Nowitzki leads. | 7 relevant, 6 missing: `dominique-wilkins` (Hybrid rank 9, Italian clubs after character 1,197, beyond the 600), and `norm-nixon`, `bob-mcadoo`, `antonio-davis`, `sidney-wicks` and `dan-roundfield` (Hybrid ranks 107 to 179, outside the 20 candidates). Example: "He also played with Scavolini Pesaro in Italy." | Possible: five relevant documents never reached Rerank's candidates, and the sixth had its Italian text beyond the 600 characters Rerank sees. The relevant leads state Italy in passing, in one clause. Not tested. | A top-50 pool would not reach the five documents at Hybrid ranks 107 to 179. The longer view from q12 is the test that fits `dominique-wilkins` (Hybrid rank 9), and the other five would need a much wider pool or better first-stage retrieval. I do not know that any of these would work. |

For all five queries, what I can show from the files is limited to where the relevant documents sat and what the leads say. For q10 and q25, and for most of the missing relevant documents of q27 and q29, Hybrid ranked the relevant lead between 86 and 247, so Rerank, which only reorders Hybrid's top 20, never had them to move. For q12, q27 and q29, the sentence that makes a lead relevant often starts after the first 600 characters that Rerank is shown. The pattern is therefore that the relevant evidence was often outside the candidate pool or outside the part of the lead that Rerank sees, and in q10 and q25 the query wording differed from the lead wording ("son" and "father of", "never picked" and "undrafted"). I did not test any of these causes, so they are possible explanations and not established. I did not find evidence in what I looked at that a relevance judgment was wrong, but I only looked at the sentences my keyword searches found, not every full lead.

---

## 7. Cross-corpus comparison

The two tables to compare are the shared-corpus scores in section 1 and your own-corpus scores in section 4, with their intervals.
If you want them side by side, copy the rows you need into a table here and say that you copied them.

Did the winner change between the shared corpus and yours?
Why, or why not: what is different about the two collections (document length, vocabulary, identifiers, near-duplicates, how the queries were written), and which of your explanations did you test and which are guesses?
Say what 20 queries on one side and your gold-set size on the other cannot support.

Observed in the evaluation:
- Rerank has the highest mean MRR@10 on both corpora (0.800 on the 20 shared practice queries and 0.878 on my 30 queries).
- On the shared corpus, Rerank is distinguishably better than BM25 on MRR@10 (+0.293 [+0.043, +0.533]) and nDCG@10 (+0.240 [+0.011, +0.457]), and not distinguishable on Recall@10 (+0.133 [-0.100, +0.358]).
- On my corpus, Rerank is not distinguishable from BM25 on any of the three metrics: Recall@10 +0.001 [-0.087, +0.089], MRR@10 +0.108 [-0.006, +0.225] and nDCG@10 +0.055 [-0.050, +0.158]. So the winner by mean did not change, but the evidence that it beats BM25 holds only on the shared corpus.
- BM25 is distinguishably better than Dense on my corpus (for example MRR@10 -0.321 [-0.492, -0.158] for Dense minus BM25), while on the shared corpus BM25 and Dense are not distinguishable (Recall@10 -0.067 [-0.350, +0.225], MRR@10 +0.055 [-0.225, +0.343], nDCG@10 -0.039 [-0.302, +0.231]).
- The query classes behave differently across corpora, though these class means have 6 to 10 queries each and no intervals. On the shared paraphrase queries BM25 scored MRR@10 0.000, and on mine 0.567. On identifier queries BM25 scored 0.810 on the shared corpus and 0.933 on mine. Dense scored MRR@10 0.714 on shared paraphrase queries and 0.378 on mine, and 0.333 on shared identifier queries against 0.613 on mine.

What differs between the collections: the shared corpus has 2,484 regulation sections with repeated technical wording and overlapping requirements, and the shared queries came with the course. My corpus has 300 NBA All-Star biography leads with a median length of 148 words, and my queries are 10 written by hand and 20 proposed by Claude. The mean content-word overlap between a query and its best relevant document is 0.73 for my hand queries and 0.80 for my claude queries. I did not compute that overlap for the shared queries, so I cannot compare it across corpora.

Tested explanations:
- Chunk size, which relates to document length: the 100-word ablation of Dense was not distinguishable from the 300-word baseline (MRR@10 +0.036 [-0.101, +0.180]), so it gives no evidence that chunk size explains Dense's weakness on my corpus.
- How the queries were written: every hand-minus-claude interval includes zero, including the check of whether BM25's lead over Dense differs between the two groups (MRR@10 +0.096 [-0.200, +0.386]). That is no evidence that model-written queries explain BM25's lead, but with 10 hand queries it cannot rule it out either.

Untested possible explanations, which are guesses:
- Vocabulary: my queries share many words with their relevant leads, which may help keyword search, and the shared paraphrase queries share few.
- Identifiers: names and award titles in my corpus may suit BM25.
- Document length: the shared sections are short and my leads are longer, which may change how well one embedding represents a document.
- Near-duplicates: the shared corpus repeats rules across parts, which may make relevant documents compete with each other. I did not measure any near-duplicate effect.
- In the failure analysis, the relevant evidence was often outside Rerank's 20 candidates or after the first 600 characters it sees, which may limit Rerank more on my corpus than on the short shared sections. I did not test this.

Limits of this comparison: the two corpora have different documents and different queries, so the difference between corpora is not paired and I have no interval for it. 20 queries on the shared corpus (MDD about 0.17 to 0.42) and 30 on mine (MDD about 0.10 to 0.24) detect a difference of that size about 80% of the time and miss smaller ones more often, and each query class has only 6 to 10 queries. I can describe what changed between the two corpora, but I cannot say what caused it.

---

## 8. Stretch

498E: the stretch is one of the six options in the brief's "One stretch" section, and that section says what earns the 25 points for each.
It is optional, so `uv run p2 check --final` never waits on this section.
598E: the rider is your stretch, so write "rider" below and put its results in section 9; the other options add no points, because the project is capped at 150.

Whichever option you chose, write these five things:

1. The option's name.
2. What you did, and the files that hold it.
3. The table `p2 score` wrote for it, by name: one of the three below, `own-ablation` and `own-ablation-queries` in section 5 for a second ablation, `own-origins` in section 4 for the hand and claude queries, or `repeats` in section 9 for the rider.
4. What its interval lets you claim, and what it does not.
5. One thing you would do next, and what result would tell you it worked.

For a second ablation, write its hypothesis here before you run it, and commit it, so your history shows that it came first.
For the hand and claude queries, do the same with your prediction before you score.

### Claim-level faithfulness check (option 2)

Claude's verdicts from `p2 judge` against your own verdicts in the calibration file.

<!-- p2:begin stretch-judge -->
_No judged answers yet (stretch option 2): `uv run p2 judge answers/shared/LABEL.json` writes them, your own verdicts go in answers/shared/LABEL.calibration.tsv, and then `uv run p2 score` fills this table._
<!-- p2:end stretch-judge -->

### Cost and latency (option 3)

The Claude calls, tokens and seconds in every trace you committed, and what a cheaper system or answers file saves against what it loses.

<!-- p2:begin stretch-cost -->
Every trace in traces/ that records a Claude call:

| Trace | System | Spans | Claude calls | Saved | Input tokens | Output tokens | Seconds | Input per span | Output per span | Seconds per span |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| traces/answers-rerank.jsonl | rerank | 12 | 24 | 4 | 151,774 | 4,189 | 118.6 | 12,648 | 349 | 9.9 |
| traces/own-own-rerank.jsonl | rerank | 30 | 30 | 2 | 243,936 | 5,932 | 131.9 | 8,131 | 198 | 4.4 |
| traces/shared-practice-rerank.jsonl | rerank | 20 | 20 | 2 | 155,182 | 2,038 | 88.6 | 7,759 | 102 | 4.4 |
| traces/shared-test-rerank.jsonl | rerank | 40 | 40 | 0 | 327,181 | 4,536 | 176.0 | 8,180 | 113 | 4.4 |

A span is one query of a run, one question of an answers file, or one claim of a judged file. A saved reply costs nothing now, so it counts the tokens and the seconds of the call that made it.

Every pair of systems on the same queries where at least one calls Claude, the one with fewer Claude input tokens per query first:

| Cheaper minus dearer | Queries | MRR@10 difference | 95% interval | Input tokens saved per query | Seconds saved per query | Reading |
| --- | ---: | ---: | ---: | ---: | ---: | --- |
| shared practice: bm25 minus rerank | 20 | -0.293 | [-0.533, -0.043] | 7,759 | 4.4 | rerank higher |
| shared practice: dense minus rerank | 20 | -0.237 | [-0.408, -0.083] | 7,759 | 4.4 | rerank higher |
| shared practice: hybrid minus rerank | 20 | -0.329 | [-0.504, -0.164] | 7,759 | 4.4 | rerank higher |
| own: bm25 minus rerank | 30 | -0.108 | [-0.225, +0.006] | 8,131 | 4.4 | not distinguishable |
| own: dense minus rerank | 30 | -0.430 | [-0.577, -0.287] | 8,131 | 4.4 | rerank higher |
| own: hybrid minus rerank | 30 | -0.185 | [-0.304, -0.077] | 8,131 | 4.4 | rerank higher |

The difference is the cheaper system's score minus the dearer one's, with its paired interval; the savings count Claude calls only, so a system that makes none saves all of the other's.

Systems that do not call Claude, from traces/retrieval/ on the machine that last ran `p2 score` (git ignores that folder, so `p2 check` does not compare this part):

| Trace | System | Queries | Seconds | Milliseconds per query |
| --- | --- | ---: | ---: | ---: |
| traces/retrieval/own-own-ablation-dense_chunk100.jsonl | dense_chunk100 | 30 | 0.13 | 4.2 |
| traces/retrieval/own-own-bm25.jsonl | bm25 | 30 | 0.01 | 0.3 |
| traces/retrieval/own-own-dense.jsonl | dense | 30 | 0.12 | 3.9 |
| traces/retrieval/own-own-hybrid.jsonl | hybrid | 30 | 0.14 | 4.5 |
| traces/retrieval/shared-practice-bm25.jsonl | bm25 | 20 | 0.03 | 1.6 |
| traces/retrieval/shared-practice-dense.jsonl | dense | 20 | 0.13 | 6.6 |
| traces/retrieval/shared-practice-hybrid.jsonl | hybrid | 20 | 0.22 | 10.9 |
| traces/retrieval/shared-test-bm25.jsonl | bm25 | 40 | 0.07 | 1.8 |
| traces/retrieval/shared-test-dense.jsonl | dense | 40 | 0.51 | 12.6 |
| traces/retrieval/shared-test-hybrid.jsonl | hybrid | 40 | 0.44 | 11.1 |
<!-- p2:end stretch-cost -->

### The grep agent (option 5)

Your stretch run on some of your own queries against the four systems on the same queries.

<!-- p2:begin stretch-agent -->
_No stretch runs yet (stretch option 5): `uv run p2 run --corpus own --queries eval/own/agent.queries.tsv --system agent --stretch` writes one to runs/own/stretch/, then `uv run p2 score` fills this table._
<!-- p2:end stretch-agent -->

### Your stretch

Write the five things here.

---

## 9. 598E only - repeats and the pre-registered claim

498E students can leave this section as it is; nothing checks it.
598E students replace each line that starts with "598E: write", and `uv run p2 check --final` counts those lines as work still to do until they are gone.

### Repeats on the shared corpus

Three runs of the reranker on the practice queries, and three answers files, with their run-to-run spread and Wilson intervals.

<!-- p2:begin repeats -->
_No repeated runs or answers files yet (598E: `p2 run ... --repeat 3` and `p2 answer ... --repeat 3`)._
<!-- p2:end repeats -->

Does the reranker's gain over its first stage survive the run-to-run variation?
Write what the spread is, how it compares with the gain, and what the Wilson intervals on the verified share and the declined share say about 8 and 4 questions.

598E: write the repeats result here.

### The pre-registered claim

The claim, the smallest effect, the gold-set size and the test are in `PREREG.md`, committed before your own gold-set judgments.
Here, say whether you followed the plan, what the interval turned out to be, and what that means.
The outcome section of `PREREG.md` holds the short version.

598E: write the claim and its outcome here.
