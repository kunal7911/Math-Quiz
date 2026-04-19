# NC 4th Grade Adaptive Math Quiz

A self-contained, adaptive math quiz for NC 4th Grade students. No server, no login, no dependencies — just open the HTML file in any browser.

---

## Project Structure

```
nc4_chunk_a.py          # Python generator script — edit this to change questions/content
nc4_quiz_wk20_29.html   # Generated output — open this in a browser to play the quiz
README.md               # This file
```

---

## How It Works

The Python script (`nc4_chunk_a.py`) generates the entire quiz as a single self-contained HTML file. All questions, styles, and JavaScript logic are embedded in the output file — no external files or internet connection needed.

To regenerate the HTML after making changes to the Python script:

```bash
python3 nc4_chunk_a.py
```

This outputs `nc4_quiz_wk20_29.html` in the same directory.

---

## Covered Topics (Weeks 20–29)

| Week | Topic |
|------|-------|
| 20 | Comparing & Ordering Fractions |
| 21 | Adding Fractions (Like Denominators) |
| 22 | Subtracting Fractions & Mixed Numbers |
| 23 | Multiplying Fractions by Whole Numbers |
| 24 | Decimals — Tenths & Hundredths |
| 25 | Comparing Decimals |
| 26 | Adding & Subtracting Decimals |
| 27 | Fraction-Decimal Relationships |
| 28 | Customary Measurement |
| 29 | Metric Measurement |

20 questions per week × 10 weeks = **200 questions total**

---

## Quiz Features

- **Adaptive engine** — tracks weak topics using `localStorage` and serves more questions from areas where the student struggles
- **Topic intro screen** — kid-friendly explanation with worked examples before each week's quiz begins
- **Back button** — lets students go back and change an answer
- **Timer** — tracks time per question and total quiz time
- **Results breakdown** — shows score, time, per-topic performance, and a review of wrong answers
- **Dashboard** — shows mastery progress across all weeks and recent activity
- **Print mode** — generates a printable worksheet with optional answer key

---

## Data Structure in the Python Script

### TOPICS dict
```python
TOPICS = {
    20: "Comparing & Ordering Fractions",
    # ...
}
```

### TOPIC_INTROS dict
Each week has a `desc` (friendly paragraph for a 10-year-old) and a list of `examples`:
```python
TOPIC_INTROS = {
    20: {
        "desc": "Imagine you and your friend each get a pizza...",
        "examples": [
            {
                "label": "🍕 Same-sized slices!",
                "problem": "Which is more: 3/8 or 5/8?",
                "solution": "Both cut into 8 slices, so compare the top: 5 > 3. You get more with 5/8!"
            },
            # 2 more examples...
        ]
    },
    # weeks 21–29...
}
```

### QUESTIONS list
Each question uses this format:
```python
{
    "week": 21,
    "id": "W21Q1",
    "question": "1/4 + 2/4 = ?",
    "options": ["3/8", "3/4", "1/2", "2/3"],
    "answer": 1   # zero-based index into options[]
}
```

> **Important:** Always simplify fractions and convert improper fractions to mixed numbers in the `answer` index. For example, `4/8` should point to `1/2`, and `9/4` should point to `2 1/4`.

---

## Adding New Questions

1. Open `nc4_chunk_a.py`
2. Find the `QUESTIONS` list
3. Add new entries using the format above — make sure `"answer"` points to the **simplified/correct** option
4. Run `python3 nc4_chunk_a.py` to regenerate the HTML

---

## Adding New Weeks

1. Add the week number and topic name to `TOPICS`
2. Add a `TOPIC_INTROS` entry with a kid-friendly `desc` and 3 `examples`
3. Add 20 questions to `QUESTIONS` with `"week": <new_week_number>`
4. Run `python3 nc4_chunk_a.py`

---

## Publishing

The generated HTML is fully self-contained and can be hosted anywhere:

- **GitHub Pages** — upload to a repo and enable Pages (Settings → Pages → Deploy from branch)
  - Original quiz (weeks 20–24): `https://kunal7911.github.io/math-quiz`
  - Extended quiz (weeks 20–29): `https://kunal7911.github.io/math-quiz/nc4_quiz_wk20_29.html`
- **Netlify / Vercel** — drag and drop the HTML file
- **Local** — just double-click the HTML file

---

## Technical Notes

- All JavaScript uses `{{` and `}}` inside Python f-strings (to escape the curly braces)
- Python data is embedded into the HTML using a `safe_json()` function that escapes `<`, `>`, and `&` to prevent XSS issues
- Student mastery data is stored in `localStorage` under the key `mathquiz_mastery`
- Quiz results history is stored under `mathquiz_results`

---

## Requirements

- Python 3.x (only needed to regenerate the HTML — the quiz itself needs no Python)
- Any modern web browser to run the quiz
