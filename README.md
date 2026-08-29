<p align="center">
  <img src="assets/logo.png" alt="AnimeBench logo" width="160">
</p>

<h1 align="center">AnimeBench</h1>

AnimeBench is a Python benchmark for measuring detailed anime knowledge in AI models. It focuses on specific, non-surface-level questions that are difficult to answer through guessing alone.

The initial public dataset will contain **50 questions** (10 per title) across:

- [*My Hero Academia*](https://myanimelist.net/anime/31964/Boku_no_Hero_Academia)
- [*Re:Zero − Starting Life in Another World*](https://myanimelist.net/anime/31240/Re_Zero_kara_Hajimeru_Isekai_Seikatsu)
- [*Attack on Titan*](https://myanimelist.net/anime/16498/Shingeki_no_Kyojin)
- [*Made in Abyss*](https://myanimelist.net/anime/34599/Made_in_Abyss)
- [*Jujutsu Kaisen*](https://myanimelist.net/anime/40748/Jujutsu_Kaisen)

All questions, reference answers, rubrics, and sources will be publicly available and versioned.

## Benchmark design

AnimeBench uses **free-form answers only**, limited to 100 words. This tests recall without revealing possible answers.

Questions may cover the anime adaptation or its primary published source: manga for four selected titles and the light novel for *Re:Zero*. Every question must label the exact source and cutoff; web novels, spin-offs, and other secondary canon are excluded.

Questions are authored as YAML files in `data/questions/`. Each question defines:

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

The Python package and placeholder CLI are scaffolded. The 10-question *My Hero Academia* set is complete; the other four title sets remain. Model runner, judge integration, and scoring have not been built yet.

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

1. Define the source cutoff for each title.
2. Draft and source 10 questions per title.
3. Human-review each reference answer and rubric.
4. Define the dataset schema before implementing model or judge integrations.

## License

MIT © 2026 bzzimmy
