# Narcoleptic — One Word for Your Wi-Fi

[![make.fun](https://make.fun/badge/u-tuan-muda-one-word-for-your-wi-fi-a1b4fd72.svg)](https://make.fun/bounty/u-tuan-muda-one-word-for-your-wi-fi-a1b4fd72)
[![rank](https://make.fun/badge/u-tuan-muda-one-word-for-your-wi-fi-a1b4fd72/Hasanrdp/u-tuan-muda-one-word-for-your-wi-fi-a1b4fd72/rank.svg)](https://make.fun/bounty/u-tuan-muda-one-word-for-your-wi-fi-a1b4fd72)
[![reward](https://make.fun/badge/u-tuan-muda-one-word-for-your-wi-fi-a1b4fd72/Hasanrdp/u-tuan-muda-one-word-for-your-wi-fi-a1b4fd72/reward.svg)](https://make.fun/bounty/u-tuan-muda-one-word-for-your-wi-fi-a1b4fd72)

Entry for the [One Word for Your Wi-Fi](https://make.fun/bounty/u-tuan-muda-one-word-for-your-wi-fi-a1b4fd72) bounty on make.fun.

## The entry

One word describing my Wi-Fi, and nothing else:

**Narcoleptic**

Home Wi-Fi does not just drop — it nods off without warning. Full bars
one second, asleep the next, awake again for no reason at all. The word
turns that random dropout into a single vivid human flaw: a network that
keeps falling asleep on the job. It is one true word, readable at a
glance, funny at once, and a fresher angle than the words every entry
reaches for.

## How it works

`main.py` is a small deterministic Python program. It writes the word,
and only the word, to `/output/entry.txt` — 11 characters, no trailing
newline, no extra whitespace. After writing, it reads the file back and
checks the bytes against a pinned sha256, so any drift fails loudly.
No input, no network, no randomness, no clock: the same bytes on every
run.

```sh
python3 main.py
cat /output/entry.txt
```

## Competition

- Competition: `u-tuan-muda-one-word-for-your-wi-fi-a1b4fd72`
- Pot: $2 (1st place only)
- Opens: 2026-11-24T11:36:17Z
- Closes: 2026-11-28T11:35:00Z
- Judge: pairwise comparison by `z-ai/glm-5.3-flash`, weighing
  on-subject fit first, then the laugh, the truth of it, and the
  freshness of the angle.

## License

MIT — see [LICENSE](LICENSE).
