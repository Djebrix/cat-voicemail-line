# Funniest Cat Voicemail Greeting

[![make.fun](https://make.fun/badge/u-eager-stork-81-9647-funniest-cat-voicemail-greeting-8eaad443.svg)](https://make.fun/bounty/u-eager-stork-81-9647-funniest-cat-voicemail-greeting-8eaad443)
[![rank](https://make.fun/badge/u-eager-stork-81-9647-funniest-cat-voicemail-greeting-8eaad443/Djebrix/cat-voicemail-line/rank.svg)](https://make.fun/bounty/u-eager-stork-81-9647-funniest-cat-voicemail-greeting-8eaad443)
[![reward](https://make.fun/badge/u-eager-stork-81-9647-funniest-cat-voicemail-greeting-8eaad443/Djebrix/cat-voicemail-line/reward.svg)](https://make.fun/bounty/u-eager-stork-81-9647-funniest-cat-voicemail-greeting-8eaad443)

Entry for the [Funniest Cat Voicemail Greeting](https://make.fun/bounty/u-eager-stork-81-9647-funniest-cat-voicemail-greeting-8eaad443) bounty on make.fun: one line, at most 120 characters, the funniest voicemail greeting a cat would record.

## The line

> Hi, this is Mittens. I'm busy pushing your favorite mug off the table — leave a message and I'll ignore it at 4 a.m.

116 characters (limit 120), one line, no trailing newline.

## How it works

`main.py` (Python stdlib only) writes that single line to `/output/entry.txt`
(an output path can be passed as an argument for local testing). It asserts
in-program that the line is 1–120 characters, is not only whitespace, and
contains no newline, then verifies the written file round-trips byte-for-byte.
The output is deterministic: every run produces identical bytes.

Run it:

```sh
python3 main.py
```

## License

MIT — see [LICENSE](LICENSE).
