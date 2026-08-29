# AnimeBench

AnimeBench is a Python benchmark for measuring detailed anime knowledge in AI models. It focuses on specific, non-surface-level questions that are difficult to answer through guessing alone.

The initial dataset will contain **50 questions across five anime** (10 per title).

## Benchmark design

AnimeBench uses **free-form answers only**, limited to 100 words. This tests recall without revealing possible answers.

Each question should define:

- the title and canon source being tested (anime, manga, or another source);
- a source cutoff, such as an episode or chapter;
- a reference answer and grading rubric;
- required facts, acceptable variants, and important contradictions;
- provenance for author review.

Manga-only facts must be labeled as manga knowledge rather than described as events revealed in the anime.

## Evaluation

```text
question -> candidate model -> answer
question + rubric + reference answer + answer -> judge model -> score
```

A fixed secondary judge model will grade each answer:

- **2 — Correct:** includes the required facts without a major contradiction.
- **1 — Partial:** demonstrates relevant knowledge but misses an essential detail.
- **0 — Incorrect:** is unsupported, contradictory, or does not answer the question.

The judge should not receive the candidate model's identity. Judge model/version, prompt version, and settings should be recorded, and a human-reviewed sample should be used to check grading quality. Final scores are normalized to a percentage.

## Status

The Python package and placeholder CLI are scaffolded. The dataset, model runner, judge integration, and scoring implementation have not been built yet.

## Development

Requires Python 3.10 or newer.

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -e .
animebench
python -m unittest discover -s tests
```

## Next steps

1. Select five titles and define the allowed canon for each.
2. Draft and source 10 questions per title.
3. Human-review each reference answer and rubric.
4. Define the dataset schema before implementing model or judge integrations.

## License

MIT © 2026 bzzimmy
