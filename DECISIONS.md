# Decision log

Your methods section, in your own words.
About one to two pages in total.

Answer these as you go, not the night before it is due.
Each answer is easier to write while the decision is still fresh, and prompt 1 only works if you write it before you see your own-corpus numbers.
Specifics beat polish: a short, honest answer with a number in it is worth more than a long vague one.

Each prompt ends with a marker line.
Replace that line with your answer.
`uv run p2 check` reports a marker as unfinished work, and `uv run p2 check --final` fails while any marker is left, so a finished log is part of being done.

Please do not let the agent write these for you.
These answers are about what you chose and what you knew, and the agent cannot know that.
Prompt 3 in particular only works in your own words.

---

## 1. Why this corpus, and what you expected

Why did you pick the corpus you used in stage 2, and why does it belong to a field or a question you care about?
Then say what you expected before you measured anything: which of `bm25`, `dense`, `hybrid` and `rerank` do you think will win on it, and which will do worst, and why?

Commit this answer before your first `uv run p2 score` on the own corpus.
Git history then shows that the expectation came first, which is what lets it be wrong in a way that teaches you something.
If you were surprised later, say so in prompt 4 or in EVAL.md; do not come back and rewrite this one.

I chose my corpus because I regularly follow the NBA and am fairly knowledgeable about its history. I wanted to base this project around a topic I was already familiar with. The Wikipedia biography leads provided consistent, accessible information about players, making it relatively straightforward to judge which documents were relevant to each query across the 300-document corpus. I did not have a specific prediction about which of BM25, Dense, Hybrid, or Rerank would perform best, nor did I document any expectations before scoring. I learned more about how these systems work as I progressed through the project.

---

## 2. A fork in the road

Name one real design choice where you could have gone two ways: the chunk size, the embedding model, how the two systems are fused, how many documents the reranker sees, a sentence in `prompts/answer.txt`, how you cleaned the corpus.

Say which you picked, what the alternative was, and what you gave up by not taking it.
If you measured both, give both numbers.
If you rejected the alternative without measuring it, say why that was a fair call, and what it cost you in time, tokens or complexity.

"There was no alternative" is not an answer.
Find the fork.

I chose to test 100-word chunks instead of 300-word chunks (the project baseline) because I wanted to see if smaller chunks would help Dense focus on specific details about a player rather than representing an entire biography in one embedding. In the end, the change increased MRR@10 by only 0.036, with a 95% confidence interval of [-0.101, +0.180], meaning the difference was not distinguishable on this gold set. Therefore, I kept the original 300-word Dense configuration.

---

## 3. Where you overruled the agent

One time Claude suggested, wrote or claimed something and you did not take it.
It might be a relevance judgment you disagreed with, a retriever it called finished when a run file showed otherwise, a number it summarized wrongly, or a license it said was fine.

What did it do?
How did you notice?
What did you do instead?

If it genuinely never happened, say so plainly, and then say what you would have had to check in order to notice.
Being honest here costs you far less than a story you cannot defend when you record your video.

After creating my 10 handwritten queries, I had Claude generate the remaining 20. I made sure to review each query to see whether it made sense and could be answered using the biography leads. I came across four queries (q12, q13, q21, and q29) that were unclear or difficult to answer using the available documents. Instead of accepting them, I asked Claude to revise these queries so that I could make more consistent relevance judgments later.

---

## 4. A number you do not trust

Pick one number in `EVAL.md` that you do not fully trust, and say why.
It could be a mean over a small query class, a difference whose interval includes zero, a verified share of 100%, a score on a gold set you wrote yourself, or a result you got only once.

What would have to be true for you to trust it?
Did you do anything to test it, and what did that show?

Going back to the Dense MRR@10 result from reducing the chunk size from 300 to 100 words, the score increased by 0.036, but the 95% confidence interval for the difference was [-0.101, +0.180]. I mostly trust the calculated result, but I am cautious about concluding that shorter chunks improve retrieval because I only had 30 judged queries, with some improving and others worsening. I tested the two chunk sizes on my own corpus, but a larger or separate evaluation set would help me understand whether shorter chunks consistently improve performance.

---

## 5. What is still wrong

One thing in your system, your corpus or your gold set that is not right, not finished, or that you do not fully understand.

What would you do next, and how would you find out whether it matters?
Name the file, the query or the document where someone could look.

There were two queries (q10 and q25), one written by me and the other by Claude, for which Rerank failed to retrieve any relevant documents, even though those documents existed in my corpus. The relevant documents for q10 were at Hybrid ranks 97 and 116, while those for q25 were at ranks 86 and 109. Since Rerank only considers Hybrid's top 20 documents, it never had the opportunity to rank the correct ones. One possible improvement would be changing the wording of these queries to better match the documents, such as using "undrafted" instead of "never picked." I don't know whether this would improve performance, so I would test the rewritten queries and compare their retrieval results with the originals.
