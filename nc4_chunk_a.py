import json

OUTPUT_FILE = 'nc4_quiz_wk20_29.html'

# ── SAFE JSON ──────────────────────────────────────────────────────────────────
def safe_json(obj):
    s = json.dumps(obj, ensure_ascii=False)
    s = s.replace('&', r'\u0026').replace('<', r'\u003c').replace('>', r'\u003e')
    return s

# ── DATA ───────────────────────────────────────────────────────────────────────

TOPICS = {
    20: "Comparing & Ordering Fractions",
    21: "Adding Fractions (Like Denominators)",
    22: "Subtracting Fractions & Mixed Numbers",
    23: "Multiplying Fractions by Whole Numbers",
    24: "Decimals — Tenths & Hundredths",
    25: "Comparing Decimals",
    26: "Adding & Subtracting Decimals",
    27: "Fraction-Decimal Relationships",
    28: "Customary Measurement",
    29: "Metric Measurement",
}

TOPIC_INTROS = {
    20: {
        "desc": "Imagine you and your friend each get a pizza cut into 8 equal slices. You get 5 slices and your friend gets 3 — you definitely have more! That is basically how comparing fractions works. When the bottom numbers match, the bigger top number wins. When the top numbers match, the smaller bottom number means bigger pieces (and more fraction overall). You can also ask yourself: is it more or less than half?",
        "examples": [
            {"label": "🍕 Same-sized slices!", "problem": "Which is more: 3/8 of a pizza or 5/8?", "solution": "Both pizzas are cut into 8 slices, so just compare the top: 5 > 3. You get more with 5/8!"},
            {"label": "🍫 Same number of pieces!", "problem": "Which is bigger: 2/5 or 2/9?", "solution": "Both have 2 pieces, but a pizza cut into 5 slices has bigger pieces than one cut into 9. So 2/5 > 2/9!"},
            {"label": "🎯 More or less than half?", "problem": "Is 3/7 more than 1/2?", "solution": "Half of 7 is 3.5, and 3 is less than 3.5, so 3/7 is just under half. 3/7 < 1/2!"},
        ],
    },
    21: {
        "desc": "Adding fractions is actually super easy when the bottom numbers are the same! Just add the top numbers and keep the bottom number exactly as it is. Think of it like eating slices from the same pizza — if you eat 2 slices and then 3 more slices, you ate 5 slices total. The pizza did not magically get 16 slices! The one golden rule: NEVER add the bottom numbers together!",
        "examples": [
            {"label": "🍕 More pizza please!", "problem": "2/8 + 3/8 = ?", "solution": "Add the top numbers: 2 + 3 = 5. Keep the bottom the same: 5/8. Easy peasy!"},
            {"label": "🎉 More than a whole!", "problem": "3/5 + 4/5 = ?", "solution": "3 + 4 = 7, so you get 7/5. That is more than 1 whole! 7 divided by 5 = 1 remainder 2, so the answer is 1 and 2/5."},
            {"label": "🥧 Pie time!", "problem": "Ana ate 1/6 of a pie at lunch, then 3/6 more at dinner. How much total?", "solution": "1/6 + 3/6 = 4/6 of the whole pie. Ana really loves pie!"},
        ],
    },
    22: {
        "desc": "Subtracting fractions with the same bottom number is just as easy as adding them! You only touch the top numbers — subtract one from the other and keep the bottom number unchanged. For mixed numbers like 2 and 3/4, just subtract the whole number parts separately and the fraction parts separately. It is like eating some of your snack and figuring out what is left!",
        "examples": [
            {"label": "🍎 How much is left?", "problem": "5/8 - 2/8 = ?", "solution": "Subtract the top numbers: 5 - 2 = 3. Keep the bottom: 3/8 is left!"},
            {"label": "🧱 Building a project!", "problem": "3 and 4/6 minus 1 and 2/6 = ?", "solution": "Subtract the whole numbers: 3 - 1 = 2. Subtract the fractions: 4/6 - 2/6 = 2/6. Answer: 2 and 2/6!"},
            {"label": "🪵 Cutting wood!", "problem": "A board is 7/8 foot long. You cut off 3/8 foot. How much is left?", "solution": "7/8 - 3/8 = 4/8, which simplifies to 1/2 foot. Nice cut!"},
        ],
    },
    23: {
        "desc": "What if you need the same fraction multiple times? Just multiply! To multiply a fraction by a whole number, multiply the top number by the whole number and keep the bottom number the same. It is the same as adding the fraction over and over — for example, 3 times 2/5 is the same as 2/5 + 2/5 + 2/5. If your answer is bigger than 1, you can convert it to a mixed number!",
        "examples": [
            {"label": "🧁 Baking time!", "problem": "3 x 2/5 = ?", "solution": "Multiply the top: 3 x 2 = 6. Keep the bottom: 6/5. That is more than 1! 6 divided by 5 = 1 remainder 1, so the answer is 1 and 1/5."},
            {"label": "🏃 Running laps!", "problem": "4 x 3/8 = ?", "solution": "4 x 3 = 12, so 12/8. Simplify: 12 divided by 8 = 1 remainder 4, so 1 and 4/8 = 1 and 1/2 miles. Great run!"},
            {"label": "🍪 Cookie factory!", "problem": "A recipe uses 2/3 cup of sugar. You are making 5 batches. How much sugar?", "solution": "5 x 2/3 = 10/3 = 3 and 1/3 cups of sugar. Better grab a big measuring cup!"},
        ],
    },
    24: {
        "desc": "Decimals are just fractions in disguise! The dot (called the decimal point) splits whole numbers from parts. The first spot after the dot is the tenths place — like cutting something into 10 equal pieces. The second spot is the hundredths place — like cutting into 100 tiny pieces. You see decimals all the time: prices at stores, your height, sports scores, and more!",
        "examples": [
            {"label": "💰 At the store!", "problem": "Write 0.7 as a fraction", "solution": "0.7 = 7/10. It means 7 out of 10 equal parts — like 70 cents out of a dollar!"},
            {"label": "📏 Getting precise!", "problem": "Write 0.43 as a fraction", "solution": "0.43 = 43/100. That is 43 out of 100 tiny pieces — called hundredths!"},
            {"label": "↔️ Flip it around!", "problem": "Write 3/10 as a decimal", "solution": "3/10 means 3 tenths. Put the 3 in the tenths spot after the dot: 0.3. Done!"},
        ],
    },
    25: {
        "desc": "Comparing decimals is just like comparing whole numbers — start from the left and go digit by digit! Here is a sneaky trick that trips a lot of people up: 0.5 and 0.50 are EXACTLY the same number. Adding a zero at the end of a decimal does not change anything, just like $0.50 and $0.5 are both 50 cents. When in doubt, think of decimals as money — it makes comparing way easier!",
        "examples": [
            {"label": "🛒 Which costs more?", "problem": "Which is more: $0.38 or $0.40?", "solution": "Think of it as cents: 38 cents vs 40 cents. $0.40 is more — even though it has fewer digits, 40 > 38!"},
            {"label": "🎮 Trick question!", "problem": "Is 0.60 the same as 0.6?", "solution": "Yes, they are equal! Adding a zero at the end does not change the value. Both equal 60 hundredths."},
            {"label": "🏁 Race results!", "problem": "Put in order from least to greatest: 0.57, 0.7, 0.75", "solution": "Think: 57, 70, 75 hundredths. So the order is: 0.57, 0.7, 0.75!"},
        ],
    },
    26: {
        "desc": "Adding and subtracting decimals is the same as regular addition and subtraction — you just have to line up the decimal points first! Think of the decimal point like an anchor that keeps everything in the right spot. You can add zeros to fill in empty spots (0.4 becomes 0.40). You already do this math every day when you count money!",
        "examples": [
            {"label": "🛍️ Shopping total!", "problem": "2.4 + 1.35 = ?", "solution": "Write 2.4 as 2.40 (add a zero helper). Now line up: 2.40 + 1.35 = 3.75. That is it!"},
            {"label": "💸 Making change!", "problem": "You have $5.00 and spend $2.38. How much is left?", "solution": "5.00 - 2.38 = $2.62 change. Line up the decimal points and subtract just like normal!"},
            {"label": "📚 School supply run!", "problem": "A book costs $4.75 and a pen costs $1.50. What is the total?", "solution": "$4.75 + $1.50 = $6.25. You are basically a human calculator!"},
        ],
    },
    27: {
        "desc": "Fractions and decimals are two different ways of saying the exact same thing — like how half and 0.5 mean exactly the same amount! To turn a fraction into a decimal, just divide the top number by the bottom number. A few super useful ones to memorize: 1/2 = 0.5, 1/4 = 0.25, 3/4 = 0.75, 1/5 = 0.2. Once you know these, you can switch between fractions and decimals like a pro!",
        "examples": [
            {"label": "🧩 Switching it up!", "problem": "What decimal equals 3/4?", "solution": "Divide the top by the bottom: 3 divided by 4 = 0.75. So 3/4 and 0.75 are exactly the same thing!"},
            {"label": "🔄 Going backwards!", "problem": "Write 0.6 as a fraction in simplest form", "solution": "0.6 = 6/10. Then simplify: divide top and bottom by 2 to get 3/5. Same value, simpler look!"},
            {"label": "🏆 Which is bigger?", "problem": "Is 1/4 or 0.3 bigger?", "solution": "Turn 1/4 into a decimal: 1 divided by 4 = 0.25. Now compare: 0.25 vs 0.30. So 0.3 wins!"},
        ],
    },
    28: {
        "desc": "In the United States we use special units to measure things — inches and feet for length, ounces and pounds for weight, cups and gallons for liquids. The key is knowing how to switch between them! To go from a big unit to a smaller one, multiply. To go from a small unit to a bigger one, divide. The big ones to know: 12 inches = 1 foot, 3 feet = 1 yard, 16 ounces = 1 pound, and 4 quarts = 1 gallon!",
        "examples": [
            {"label": "📏 How tall is that?", "problem": "How many inches are in 3 feet?", "solution": "1 foot = 12 inches, so 3 feet = 3 x 12 = 36 inches. That is about as tall as a 3-year-old!"},
            {"label": "🛒 At the grocery store!", "problem": "A recipe needs 2 pounds of flour. How many ounces is that?", "solution": "1 pound = 16 ounces, so 2 pounds = 2 x 16 = 32 ounces. That is a lot of flour!"},
            {"label": "🥤 Juice for everyone!", "problem": "How many quarts are in 2 gallons?", "solution": "1 gallon = 4 quarts, so 2 gallons = 2 x 4 = 8 quarts. Enough juice for a party!"},
        ],
    },
    29: {
        "desc": "The metric system is genius because everything is based on 10s, 100s, and 1000s — just like our number system! Scientists and most countries around the world use it. Once you learn the prefixes, converting is a breeze: kilo means 1000 of something, centi means 1/100, and milli means 1/1000. So a kilometer is 1000 meters, and a milliliter is 1/1000 of a liter. Just multiply or divide by 10, 100, or 1000!",
        "examples": [
            {"label": "📐 In the classroom!", "problem": "A desk is 150 cm wide. How many meters is that?", "solution": "100 cm = 1 m, so 150 divided by 100 = 1.5 meters. About the length of a guitar!"},
            {"label": "⚖️ Weighing things!", "problem": "A bag of apples weighs 2.5 kg. How many grams is that?", "solution": "1 kg = 1000 g, so 2.5 x 1000 = 2,500 grams. Those are some heavy apples!"},
            {"label": "🧃 Juice box math!", "problem": "A water bottle holds 500 mL. How many liters is that?", "solution": "1000 mL = 1 L, so 500 divided by 1000 = 0.5 L. That is half a liter!"},
        ],
    },
}

QUESTIONS = [
    # ── Week 20: Comparing & Ordering Fractions ───────────────────────────────
    {"week": 20, "id": "W20Q1",  "question": "Compare the fractions: 2/5 and 3/5. Which is GREATER?",                   "options": ["2/5", "3/5", "They are equal", "Cannot compare"],         "answer": 1},
    {"week": 20, "id": "W20Q2",  "question": "Which fraction is SMALLER: 1/3 or 1/7?",                                  "options": ["1/3", "1/7", "They are equal", "Need more info"],          "answer": 1},
    {"week": 20, "id": "W20Q3",  "question": "Place in order from LEAST to GREATEST: 1/4, 1/8, 1/2",                   "options": ["1/8, 1/4, 1/2", "1/2, 1/4, 1/8", "1/4, 1/8, 1/2", "1/8, 1/2, 1/4"], "answer": 0},
    {"week": 20, "id": "W20Q4",  "question": "Compare: 3/4 and 2/4. Which is GREATER?",                                 "options": ["2/4", "3/4", "They are equal", "Cannot tell"],             "answer": 1},
    {"week": 20, "id": "W20Q5",  "question": "Is 2/6 less than 1/2?",                                                   "options": ["Yes", "No", "They are equal", "Cannot compare"],           "answer": 0},
    {"week": 20, "id": "W20Q6",  "question": "Which group is in order from LEAST to GREATEST? 2/8, 4/8, 6/8",          "options": ["6/8, 4/8, 2/8", "2/8, 4/8, 6/8", "4/8, 2/8, 6/8", "Cannot order"], "answer": 1},
    {"week": 20, "id": "W20Q7",  "question": "Compare: 3/6 and 3/9. Which is GREATER?",                                 "options": ["3/9", "3/6", "They are equal", "Cannot determine"],        "answer": 1},
    {"week": 20, "id": "W20Q8",  "question": "Is 4/5 greater than 1/2?",                                                "options": ["Yes", "No", "They are equal", "Need more info"],           "answer": 0},
    {"week": 20, "id": "W20Q9",  "question": "Place in order from GREATEST to LEAST: 1/6, 1/3, 1/2",                   "options": ["1/6, 1/3, 1/2", "1/2, 1/3, 1/6", "1/3, 1/6, 1/2", "1/3, 1/2, 1/6"], "answer": 1},
    {"week": 20, "id": "W20Q10", "question": "Which fraction is closest to 1? 3/4, 2/3, or 4/5?",                       "options": ["3/4", "2/3", "4/5", "They are equal"],                     "answer": 2},
    {"week": 20, "id": "W20Q11", "question": "Compare: 5/8 and 5/10. Which is GREATER?",                                "options": ["5/10", "5/8", "They are equal", "Cannot tell"],            "answer": 1},
    {"week": 20, "id": "W20Q12", "question": "Is 2/3 greater than 1/2?",                                                "options": ["Yes", "No", "They are equal", "Cannot determine"],         "answer": 0},
    {"week": 20, "id": "W20Q13", "question": "Order from LEAST to GREATEST: 5/6, 3/6, 1/6",                             "options": ["5/6, 3/6, 1/6", "1/6, 3/6, 5/6", "3/6, 1/6, 5/6", "1/6, 5/6, 3/6"], "answer": 1},
    {"week": 20, "id": "W20Q14", "question": "Which fraction is GREATER: 4/7 or 3/7?",                                  "options": ["3/7", "4/7", "They are equal", "Need more data"],          "answer": 1},
    {"week": 20, "id": "W20Q15", "question": "Compare: 2/5 and 2/3. Which is SMALLER?",                                 "options": ["2/3", "2/5", "They are equal", "Cannot compare"],          "answer": 1},
    {"week": 20, "id": "W20Q16", "question": "Is 1/4 less than 1/2?",                                                   "options": ["Yes", "No", "They are equal", "Cannot tell"],              "answer": 0},
    {"week": 20, "id": "W20Q17", "question": "Order from GREATEST to LEAST: 2/5, 2/8, 2/3",                             "options": ["2/3, 2/5, 2/8", "2/8, 2/5, 2/3", "2/5, 2/3, 2/8", "Cannot order"], "answer": 0},
    {"week": 20, "id": "W20Q18", "question": "Which is closest to 1/2: 3/8 or 5/8?",                                   "options": ["3/8", "5/8", "Both equally close", "Cannot determine"],    "answer": 2},
    {"week": 20, "id": "W20Q19", "question": "Compare: 1/6 and 1/8. Which is GREATER?",                                 "options": ["1/8", "1/6", "They are equal", "Need more info"],          "answer": 1},
    {"week": 20, "id": "W20Q20", "question": "Is 6/8 equal to 3/4?",                                                    "options": ["Yes", "No", "Cannot determine", "Need more data"],         "answer": 0},

    # ── Week 21: Adding Fractions (Like Denominators) ─────────────────────────
    {"week": 21, "id": "W21Q1",  "question": "1/4 + 2/4 = ?",    "options": ["3/8", "3/4", "1/2", "2/3"],           "answer": 1},
    {"week": 21, "id": "W21Q2",  "question": "2/6 + 3/6 = ?",    "options": ["5/12", "5/6", "1/2", "6/6"],         "answer": 1},
    {"week": 21, "id": "W21Q3",  "question": "1/8 + 3/8 = ?",    "options": ["4/8", "4/16", "1/2", "3/8"],         "answer": 2},
    {"week": 21, "id": "W21Q4",  "question": "3/5 + 1/5 = ?",    "options": ["4/5", "4/10", "3/5", "2/5"],         "answer": 0},
    {"week": 21, "id": "W21Q5",  "question": "2/8 + 4/8 = ?",    "options": ["6/16", "6/8", "3/4", "1/2"],         "answer": 2},
    {"week": 21, "id": "W21Q6",  "question": "1/3 + 2/3 = ?",    "options": ["3/6", "2/3", "1", "1/3"],            "answer": 2},
    {"week": 21, "id": "W21Q7",  "question": "4/10 + 3/10 = ?",  "options": ["7/20", "7/10", "1/2", "3/10"],       "answer": 1},
    {"week": 21, "id": "W21Q8",  "question": "2/5 + 2/5 = ?",    "options": ["4/5", "2/5", "4/10", "1"],           "answer": 0},
    {"week": 21, "id": "W21Q9",  "question": "3/8 + 4/8 = ?",    "options": ["7/16", "7/8", "1 3/8", "1 2/8"],     "answer": 1},
    {"week": 21, "id": "W21Q10", "question": "1/6 + 4/6 = ?",    "options": ["5/6", "5/12", "1/2", "1"],           "answer": 0},
    {"week": 21, "id": "W21Q11", "question": "2/3 + 1/3 = ?",    "options": ["3/3", "1", "2/3", "1 1/3"],          "answer": 1},
    {"week": 21, "id": "W21Q12", "question": "3/10 + 5/10 = ?",  "options": ["8/20", "8/10", "4/5", "1/2"],        "answer": 2},
    {"week": 21, "id": "W21Q13", "question": "1/4 + 3/4 = ?",    "options": ["4/4", "1", "1/2", "3/4"],            "answer": 1},
    {"week": 21, "id": "W21Q14", "question": "5/12 + 4/12 = ?",  "options": ["9/24", "9/12", "3/4", "1 1/12"],     "answer": 2},
    {"week": 21, "id": "W21Q15", "question": "2/7 + 3/7 = ?",    "options": ["5/7", "5/14", "1/2", "3/7"],         "answer": 0},
    {"week": 21, "id": "W21Q16", "question": "1/5 + 3/5 = ?",    "options": ["4/5", "4/10", "3/5", "1"],           "answer": 0},
    {"week": 21, "id": "W21Q17", "question": "4/9 + 3/9 = ?",    "options": ["7/18", "7/9", "1 2/9", "1 1/9"],     "answer": 1},
    {"week": 21, "id": "W21Q18", "question": "2/8 + 5/8 = ?",    "options": ["7/16", "7/8", "1 1/8", "1 2/8"],     "answer": 1},
    {"week": 21, "id": "W21Q19", "question": "1/2 + 1/2 = ?",    "options": ["2/4", "1", "1/2", "1/4"],            "answer": 1},
    {"week": 21, "id": "W21Q20", "question": "3/6 + 2/6 = ?",    "options": ["5/6", "5/12", "1/2", "1"],           "answer": 0},

    # ── Week 22: Subtracting Fractions & Mixed Numbers ────────────────────────
    {"week": 22, "id": "W22Q1",  "question": "3/4 - 1/4 = ?",          "options": ["2/4", "1/2", "2/8", "1/3"],              "answer": 1},
    {"week": 22, "id": "W22Q2",  "question": "5/6 - 2/6 = ?",          "options": ["3/6", "1/2", "2/6", "1/3"],              "answer": 1},
    {"week": 22, "id": "W22Q3",  "question": "7/8 - 3/8 = ?",          "options": ["4/8", "1/2", "3/8", "1/4"],              "answer": 1},
    {"week": 22, "id": "W22Q4",  "question": "4/5 - 2/5 = ?",          "options": ["2/5", "2/10", "1/5", "3/5"],             "answer": 0},
    {"week": 22, "id": "W22Q5",  "question": "6/10 - 3/10 = ?",        "options": ["3/10", "1/2", "3/20", "1/5"],            "answer": 0},
    {"week": 22, "id": "W22Q6",  "question": "5/8 - 2/8 = ?",          "options": ["3/8", "3/16", "2/8", "1/2"],             "answer": 0},
    {"week": 22, "id": "W22Q7",  "question": "4/6 - 1/6 = ?",          "options": ["3/6", "1/2", "2/6", "1/3"],              "answer": 1},
    {"week": 22, "id": "W22Q8",  "question": "9/10 - 4/10 = ?",        "options": ["5/10", "1/2", "4/10", "1/2"],            "answer": 1},
    {"week": 22, "id": "W22Q9",  "question": "2 3/4 - 1 1/4 = ?",      "options": ["1 2/4", "1 1/2", "1 1/4", "2/4"],        "answer": 1},
    {"week": 22, "id": "W22Q10", "question": "3 5/8 - 1 2/8 = ?",      "options": ["2 3/8", "2 4/8", "2 1/2", "2 2/8"],      "answer": 0},
    {"week": 22, "id": "W22Q11", "question": "1 - 3/8 = ?",             "options": ["5/8", "2/8", "1/2", "3/8"],              "answer": 0},
    {"week": 22, "id": "W22Q12", "question": "5/6 - 1/6 = ?",          "options": ["4/6", "2/3", "3/6", "1/2"],              "answer": 1},
    {"week": 22, "id": "W22Q13", "question": "4 2/5 - 2 1/5 = ?",      "options": ["2 1/5", "2 2/5", "1 1/5", "3/5"],        "answer": 0},
    {"week": 22, "id": "W22Q14", "question": "7/9 - 3/9 = ?",          "options": ["4/9", "3/9", "2/9", "1/3"],              "answer": 0},
    {"week": 22, "id": "W22Q15", "question": "1 1/2 - 3/4 = ?",        "options": ["3/4", "1/2", "1/4", "2/4"],              "answer": 0},
    {"week": 22, "id": "W22Q16", "question": "6/8 - 2/8 = ?",          "options": ["4/8", "1/2", "2/8", "3/4"],              "answer": 1},
    {"week": 22, "id": "W22Q17", "question": "3 7/10 - 1 4/10 = ?",    "options": ["2 3/10", "2 4/10", "2 1/10", "3/10"],    "answer": 0},
    {"week": 22, "id": "W22Q18", "question": "8/12 - 3/12 = ?",        "options": ["5/12", "4/12", "1/3", "1/2"],            "answer": 0},
    {"week": 22, "id": "W22Q19", "question": "2 1/3 - 1 2/3 = ?",      "options": ["2/3", "1/3", "1", "1 2/3"],              "answer": 0},
    {"week": 22, "id": "W22Q20", "question": "5/7 - 2/7 = ?",          "options": ["3/7", "2/7", "1/7", "1/3"],              "answer": 0},

    # ── Week 23: Multiplying Fractions by Whole Numbers ───────────────────────
    {"week": 23, "id": "W23Q1",  "question": "2 × 1/4 = ?",  "options": ["2/4", "1/2", "2/8", "1/4"],         "answer": 1},
    {"week": 23, "id": "W23Q2",  "question": "3 × 2/5 = ?",  "options": ["6/5", "1 1/5", "2/5", "3/5"],       "answer": 1},
    {"week": 23, "id": "W23Q3",  "question": "4 × 1/3 = ?",  "options": ["4/3", "1 1/3", "1/3", "1/4"],       "answer": 1},
    {"week": 23, "id": "W23Q4",  "question": "2 × 3/8 = ?",  "options": ["6/8", "3/4", "1 1/4", "1/2"],       "answer": 1},
    {"week": 23, "id": "W23Q5",  "question": "5 × 1/5 = ?",  "options": ["5/5", "1", "1/5", "2/5"],           "answer": 1},
    {"week": 23, "id": "W23Q6",  "question": "3 × 3/4 = ?",  "options": ["9/4", "2 1/4", "3/4", "1/2"],       "answer": 1},
    {"week": 23, "id": "W23Q7",  "question": "6 × 1/6 = ?",  "options": ["6/6", "1", "1/6", "6/36"],          "answer": 1},
    {"week": 23, "id": "W23Q8",  "question": "2 × 5/8 = ?",  "options": ["10/8", "1 2/8", "5/8", "1/4"],      "answer": 1},
    {"week": 23, "id": "W23Q9",  "question": "4 × 2/3 = ?",  "options": ["8/3", "2 2/3", "2/3", "1/2"],       "answer": 1},
    {"week": 23, "id": "W23Q10", "question": "3 × 1/2 = ?",  "options": ["3/2", "1 1/2", "1/2", "3/6"],       "answer": 1},
    {"week": 23, "id": "W23Q11", "question": "5 × 2/5 = ?",  "options": ["10/5", "2", "2/5", "1/5"],          "answer": 1},
    {"week": 23, "id": "W23Q12", "question": "2 × 4/7 = ?",  "options": ["8/7", "1 1/7", "4/7", "1/2"],       "answer": 1},
    {"week": 23, "id": "W23Q13", "question": "7 × 1/7 = ?",  "options": ["7/7", "1", "1/7", "7/49"],          "answer": 1},
    {"week": 23, "id": "W23Q14", "question": "3 × 5/6 = ?",  "options": ["15/6", "2 1/2", "5/6", "1/2"],      "answer": 1},
    {"week": 23, "id": "W23Q15", "question": "4 × 3/5 = ?",  "options": ["12/5", "2 2/5", "3/5", "1/2"],      "answer": 1},
    {"week": 23, "id": "W23Q16", "question": "2 × 2/5 = ?",  "options": ["4/5", "2/5", "1/5", "1/2"],         "answer": 0},
    {"week": 23, "id": "W23Q17", "question": "6 × 1/3 = ?",  "options": ["6/3", "2", "1/3", "1/2"],           "answer": 1},
    {"week": 23, "id": "W23Q18", "question": "3 × 4/8 = ?",  "options": ["12/8", "1 1/2", "4/8", "1/2"],      "answer": 1},
    {"week": 23, "id": "W23Q19", "question": "5 × 3/5 = ?",  "options": ["15/5", "3", "3/5", "1/2"],          "answer": 1},
    {"week": 23, "id": "W23Q20", "question": "4 × 1/8 = ?",  "options": ["4/8", "1/2", "1/8", "1/4"],         "answer": 1},

    # ── Week 24: Decimals — Tenths & Hundredths ───────────────────────────────
    {"week": 24, "id": "W24Q1",  "question": "What decimal equals 7/10?",           "options": ["0.07", "0.7", "7.0", "0.17"],          "answer": 1},
    {"week": 24, "id": "W24Q2",  "question": "What fraction equals 0.5?",           "options": ["5/10", "1/2", "5/100", "1/5"],         "answer": 0},
    {"week": 24, "id": "W24Q3",  "question": "0.43 = ?",                            "options": ["43/10", "43/100", "4/3", "4/10"],       "answer": 1},
    {"week": 24, "id": "W24Q4",  "question": "Write 3/10 as a decimal.",            "options": ["0.03", "0.3", "3.0", "0.13"],           "answer": 1},
    {"week": 24, "id": "W24Q5",  "question": "Which decimal equals 1/10?",          "options": ["0.1", "0.01", "1.0", "0.11"],           "answer": 0},
    {"week": 24, "id": "W24Q6",  "question": "What fraction equals 0.8?",           "options": ["8/10", "4/5", "8/100", "1/8"],          "answer": 0},
    {"week": 24, "id": "W24Q7",  "question": "25/100 = ?",                          "options": ["0.025", "2.5", "0.25", "25.0"],         "answer": 2},
    {"week": 24, "id": "W24Q8",  "question": "Write 0.6 as a fraction.",            "options": ["6/10", "3/5", "6/100", "1/6"],          "answer": 0},
    {"week": 24, "id": "W24Q9",  "question": "Which decimal equals 9/10?",          "options": ["0.9", "0.09", "9.0", "0.19"],           "answer": 0},
    {"week": 24, "id": "W24Q10", "question": "What fraction equals 0.37?",          "options": ["37/10", "37/100", "3/7", "3/10"],       "answer": 1},
    {"week": 24, "id": "W24Q11", "question": "0.2 = ?",                             "options": ["2/10", "1/5", "2/100", "1/2"],          "answer": 0},
    {"week": 24, "id": "W24Q12", "question": "Write 4/10 as a decimal.",            "options": ["0.04", "0.4", "4.0", "0.14"],           "answer": 1},
    {"week": 24, "id": "W24Q13", "question": "Which decimal equals 15/100?",        "options": ["0.015", "0.15", "1.5", "0.51"],         "answer": 1},
    {"week": 24, "id": "W24Q14", "question": "What decimal equals 6/10?",           "options": ["0.06", "0.6", "6.0", "0.16"],           "answer": 1},
    {"week": 24, "id": "W24Q15", "question": "Write 0.9 as a fraction.",            "options": ["9/10", "9/100", "1/9", "9/99"],         "answer": 0},
    {"week": 24, "id": "W24Q16", "question": "Which equals 0.03?",                  "options": ["3/10", "30/100", "3/100", "3/1000"],    "answer": 2},
    {"week": 24, "id": "W24Q17", "question": "What decimal equals 45/100?",         "options": ["0.045", "4.5", "0.45", "45.0"],         "answer": 2},
    {"week": 24, "id": "W24Q18", "question": "Write 0.08 as a fraction.",           "options": ["8/10", "8/100", "1/8", "8/80"],         "answer": 1},
    {"week": 24, "id": "W24Q19", "question": "Which decimal equals 2/10?",          "options": ["0.02", "0.2", "2.0", "0.12"],           "answer": 1},
    {"week": 24, "id": "W24Q20", "question": "What fraction equals 0.72?",          "options": ["72/10", "7/2", "72/100", "7/12"],       "answer": 2},

    # ── Week 25: Comparing Decimals ───────────────────────────────────────────
    {"week": 25, "id": "W25Q1",  "question": "Which decimal is GREATER: 0.4 or 0.38?",                                                               "options": ["0.38", "0.4", "They are equal", "Cannot be determined"],              "answer": 1},
    {"week": 25, "id": "W25Q2",  "question": "Marcus ran 1.45 miles on Monday and 1.5 miles on Tuesday. On which day did he run FARTHER?",            "options": ["Monday", "Tuesday", "Same distance", "Need more information"],        "answer": 1},
    {"week": 25, "id": "W25Q3",  "question": "Which symbol makes this true?  0.60  ___  0.6",                                                        "options": ["<", ">", "=", "cannot compare"],                                      "answer": 2},
    {"week": 25, "id": "W25Q4",  "question": "Order from LEAST to GREATEST:  0.75,  0.7,  0.57,  0.5",                                              "options": ["0.5, 0.57, 0.7, 0.75", "0.75, 0.7, 0.57, 0.5", "0.7, 0.75, 0.5, 0.57", "0.5, 0.7, 0.57, 0.75"], "answer": 0},
    {"week": 25, "id": "W25Q5",  "question": "A store sells orange juice for $1.89 and apple juice for $1.98. Which juice costs MORE?",               "options": ["Orange juice", "Apple juice", "They cost the same", "Cannot be determined"], "answer": 1},
    {"week": 25, "id": "W25Q6",  "question": "Which decimal is BETWEEN 0.5 and 0.8?",                                                               "options": ["0.82", "0.49", "0.63", "0.80"],                                       "answer": 2},
    {"week": 25, "id": "W25Q7",  "question": "Order from GREATEST to LEAST:  3.2,  3.15,  3.25,  3.18",                                             "options": ["3.25, 3.2, 3.18, 3.15", "3.15, 3.18, 3.2, 3.25", "3.2, 3.25, 3.18, 3.15", "3.25, 3.18, 3.2, 3.15"], "answer": 0},
    {"week": 25, "id": "W25Q8",  "question": "During a science experiment, Aisha measured 0.9 liters and Ben measured 0.85 liters. Who measured MORE?", "options": ["Ben", "Aisha", "They measured the same", "Need more data"],          "answer": 1},
    {"week": 25, "id": "W25Q9",  "question": "Which statement is TRUE?",                                                                              "options": ["0.3 > 0.35", "0.50 < 0.5", "0.08 < 0.1", "2.4 > 2.40"],             "answer": 2},
    {"week": 25, "id": "W25Q10", "question": "A bookstore sells pencils for $0.25, pens for $0.79, and erasers for $0.49. Which item costs the LEAST?", "options": ["Pens", "Erasers", "Pencils", "They cost the same"],                  "answer": 2},
    {"week": 25, "id": "W25Q11", "question": "Which decimal is CLOSEST to 1?",                                                                        "options": ["0.89", "0.9", "0.99", "0.98"],                                        "answer": 2},
    {"week": 25, "id": "W25Q12", "question": "In a relay race, Team A finished in 58.34 seconds and Team B finished in 58.3 seconds. Which team was FASTER (lower time)?", "options": ["Team A", "Team B", "Same time", "Cannot tell"], "answer": 1},
    {"week": 25, "id": "W25Q13", "question": "Which group is ordered correctly from LEAST to GREATEST?",                                              "options": ["0.45, 0.5, 0.54, 0.6", "0.5, 0.45, 0.54, 0.6", "0.6, 0.54, 0.5, 0.45", "0.45, 0.54, 0.5, 0.6"], "answer": 0},
    {"week": 25, "id": "W25Q14", "question": "Daily high temperatures: Mon 72.4 degrees F, Tue 72.8 degrees F, Wed 71.9 degrees F. On which day was it COOLEST?", "options": ["Monday", "Tuesday", "Wednesday", "Cannot tell"], "answer": 2},
    {"week": 25, "id": "W25Q15", "question": "Which decimal is NOT less than 0.5?",                                                                   "options": ["0.38", "0.49", "0.52", "0.09"],                                       "answer": 2},
    {"week": 25, "id": "W25Q16", "question": "A plant grew 0.6 cm on Monday and 0.58 cm on Tuesday. On which day did it grow MORE?",                  "options": ["Tuesday", "Monday", "Same amount", "Cannot determine"],               "answer": 1},
    {"week": 25, "id": "W25Q17", "question": "Jaylen's dog weighs 24.7 pounds and Sofia's dog weighs 24.70 pounds. Which dog is HEAVIER?",            "options": ["Jaylen's dog", "Sofia's dog", "They weigh the same", "Need more info"], "answer": 2},
    {"week": 25, "id": "W25Q18", "question": "Which number correctly completes: 0.4 > ___",                                                           "options": ["0.5", "0.40", "0.44", "0.38"],                                        "answer": 3},
    {"week": 25, "id": "W25Q19", "question": "Three students jumped: Ana jumped 1.28 m, Ben jumped 1.3 m, Cam jumped 1.25 m. Who jumped FARTHEST?",   "options": ["Ana", "Ben", "Cam", "They all jumped the same"],                       "answer": 1},
    {"week": 25, "id": "W25Q20", "question": "Which decimal fills the blank correctly on a number line?  0.35, ___, 0.5, 0.65",                       "options": ["0.30", "0.55", "0.42", "0.70"],                                       "answer": 2},

    # ── Week 26: Adding & Subtracting Decimals ────────────────────────────────
    {"week": 26, "id": "W26Q1",  "question": "3.4 + 2.1 = ?",                                                                                        "options": ["5.5", "5.41", "5.14", "54.1"],                                        "answer": 0},
    {"week": 26, "id": "W26Q2",  "question": "Maria bought a notebook for $2.45 and a pen for $1.30. How much did she spend in total?",                "options": ["$3.75", "$3.70", "$4.75", "$3.45"],                                    "answer": 0},
    {"week": 26, "id": "W26Q3",  "question": "7.00 - 3.85 = ?",                                                                                       "options": ["3.25", "4.25", "3.15", "4.15"],                                       "answer": 2},
    {"week": 26, "id": "W26Q4",  "question": "A piece of rope was 4.5 meters long. After cutting off 1.75 meters, how much is left?",                 "options": ["3.25 m", "2.75 m", "2.25 m", "3.75 m"],                               "answer": 1},
    {"week": 26, "id": "W26Q5",  "question": "0.8 + 0.45 = ?",                                                                                        "options": ["0.125", "0.85", "1.25", "1.85"],                                      "answer": 2},
    {"week": 26, "id": "W26Q6",  "question": "A store had $10.00 in the cash drawer. After a sale, $4.37 remained. How much was collected?",           "options": ["$5.63", "$6.63", "$5.37", "$14.37"],                                   "answer": 0},
    {"week": 26, "id": "W26Q7",  "question": "2.6 + 1.74 = ?",                                                                                        "options": ["3.34", "4.34", "3.44", "4.14"],                                       "answer": 1},
    {"week": 26, "id": "W26Q8",  "question": "Liam bought 3 items: $1.25, $0.79, and $2.50. What was his total?",                                     "options": ["$4.04", "$4.54", "$3.54", "$4.44"],                                    "answer": 1},
    {"week": 26, "id": "W26Q9",  "question": "8.3 - 2.65 = ?",                                                                                        "options": ["6.35", "5.65", "5.35", "6.65"],                                       "answer": 1},
    {"week": 26, "id": "W26Q10", "question": "A patient temperature was 98.6°F in the morning and 97.2°F in the evening. How much did it drop?",       "options": ["1.6°F", "1.4°F", "0.6°F", "2.4°F"],                                   "answer": 1},
    {"week": 26, "id": "W26Q11", "question": "0.45 + 0.55 = ?",                                                                                       "options": ["0.90", "1.00", "0.10", "1.10"],                                       "answer": 1},
    {"week": 26, "id": "W26Q12", "question": "In a two-lap race, Sara finished Lap 1 in 42.8 seconds and Lap 2 in 39.65 seconds. What was her TOTAL time?", "options": ["81.35 s", "82.45 s", "81.45 s", "82.35 s"],                    "answer": 1},
    {"week": 26, "id": "W26Q13", "question": "15.00 - 7.48 = ?",                                                                                      "options": ["8.62", "7.52", "7.62", "8.52"],                                       "answer": 1},
    {"week": 26, "id": "W26Q14", "question": "Tom had a $20 gift card. He spent $8.75 on a game and $4.50 on snacks. How much is LEFT?",               "options": ["$7.25", "$6.75", "$7.75", "$6.25"],                                    "answer": 1},
    {"week": 26, "id": "W26Q15", "question": "1.06 + 2.94 = ?",                                                                                       "options": ["3.90", "4.00", "3.00", "4.10"],                                       "answer": 1},
    {"week": 26, "id": "W26Q16", "question": "A fish tank had 6.8 liters of water. After adding 2.45 liters, how much water is in the tank?",          "options": ["9.25 L", "8.25 L", "9.35 L", "8.35 L"],                               "answer": 0},
    {"week": 26, "id": "W26Q17", "question": "Which sum is INCORRECT?",                                                                               "options": ["1.5 + 2.5 = 4.0", "3.2 + 1.8 = 5.0", "4.7 + 2.4 = 6.1", "0.6 + 0.8 = 1.4"], "answer": 2},
    {"week": 26, "id": "W26Q18", "question": "A runner completed 3 segments: 1.25 km, 0.8 km, and 1.45 km. What was the TOTAL distance?",             "options": ["3.40 km", "3.50 km", "2.50 km", "3.60 km"],                            "answer": 1},
    {"week": 26, "id": "W26Q19", "question": "A recipe needs 2.75 cups of flour. You have already added 1.3 cups. How much MORE is needed?",           "options": ["1.35 cups", "1.45 cups", "1.25 cups", "2.45 cups"],                    "answer": 1},
    {"week": 26, "id": "W26Q20", "question": "The snack booth collected $45.75 in the morning and $38.50 in the afternoon, and started with $10.00 in change. What was the TOTAL money at the end of the day?", "options": ["$84.25", "$94.25", "$84.50", "$94.00"], "answer": 1},

    # ── Week 27: Fraction-Decimal Relationships ───────────────────────────────
    {"week": 27, "id": "W27Q1",  "question": "What decimal equals 1/2?",                                                               "options": ["0.12", "0.21", "0.5", "0.25"],                               "answer": 2},
    {"week": 27, "id": "W27Q2",  "question": "What fraction in simplest form equals 0.25?",                                            "options": ["25/100", "1/4", "2/5", "1/25"],                              "answer": 1},
    {"week": 27, "id": "W27Q3",  "question": "Which decimal equals 3/4?",                                                              "options": ["0.34", "0.3", "0.75", "0.43"],                               "answer": 2},
    {"week": 27, "id": "W27Q4",  "question": "A pizza was cut into 5 equal slices. Jake ate 2 slices. What decimal represents the amount Jake ate?", "options": ["0.2", "0.25", "0.4", "0.5"],          "answer": 2},
    {"week": 27, "id": "W27Q5",  "question": "What fraction in simplest form equals 0.5?",                                             "options": ["5/10", "5/100", "1/2", "1/5"],                               "answer": 2},
    {"week": 27, "id": "W27Q6",  "question": "Which decimal equals 7/10?",                                                             "options": ["0.07", "7.0", "0.7", "0.17"],                                "answer": 2},
    {"week": 27, "id": "W27Q7",  "question": "A student got 3 out of 4 questions correct on a mini-quiz. What decimal represents the fraction correct?", "options": ["0.34", "3.4", "0.25", "0.75"],  "answer": 3},
    {"week": 27, "id": "W27Q8",  "question": "What fraction in simplest form equals 0.20?",                                            "options": ["20/100", "2/10", "1/5", "1/2"],                              "answer": 2},
    {"week": 27, "id": "W27Q9",  "question": "Which decimal equals 2/5?",                                                              "options": ["0.25", "0.4", "0.52", "0.45"],                               "answer": 1},
    {"week": 27, "id": "W27Q10", "question": "What fraction equals 0.75?",                                                             "options": ["7/5", "4/3", "3/4", "7/10"],                                 "answer": 2},
    {"week": 27, "id": "W27Q11", "question": "Which decimal equals 1/4?",                                                              "options": ["0.4", "0.14", "0.25", "2.5"],                                "answer": 2},
    {"week": 27, "id": "W27Q12", "question": "A ribbon is 0.6 meters long. What fraction in simplest form represents this length?",    "options": ["6/100", "3/10", "3/5", "6/5"],                               "answer": 2},
    {"week": 27, "id": "W27Q13", "question": "Which fraction equals 0.8?",                                                             "options": ["8/100", "1/8", "4/5", "8/5"],                                "answer": 2},
    {"week": 27, "id": "W27Q14", "question": "What decimal equals 9/100?",                                                             "options": ["0.9", "9.0", "0.09", "90.0"],                                "answer": 2},
    {"week": 27, "id": "W27Q15", "question": "A track is 400 meters. Sam ran 3/4 of the track. How many meters did Sam run?",          "options": ["300 m", "75 m", "304 m", "340 m"],                           "answer": 0},
    {"week": 27, "id": "W27Q16", "question": "What fraction in simplest form equals 0.04?",                                            "options": ["4/10", "1/25", "2/50", "4/100"],                             "answer": 1},
    {"week": 27, "id": "W27Q17", "question": "Which is GREATER: 3/4 or 0.7?",                                                         "options": ["0.7", "3/4", "They are equal", "Cannot compare fractions and decimals"], "answer": 1},
    {"week": 27, "id": "W27Q18", "question": "It rained 1/4 of days in January and 0.3 of days in February. Which month had GREATER fraction of rainy days?", "options": ["January", "February", "Same amount", "Cannot determine"], "answer": 1},
    {"week": 27, "id": "W27Q19", "question": "Place in order from LEAST to GREATEST:  1/2,  0.4,  3/4,  0.6",                         "options": ["0.4, 1/2, 0.6, 3/4", "1/2, 0.4, 3/4, 0.6", "3/4, 0.6, 1/2, 0.4", "0.4, 0.6, 1/2, 3/4"], "answer": 0},
    {"week": 27, "id": "W27Q20", "question": "Carlos scored 17 out of 20 on a test. What decimal represents his score?",               "options": ["0.17", "0.85", "1.7", "0.8"],                                "answer": 1},

    # ── Week 28: Customary Measurement ────────────────────────────────────────
    {"week": 28, "id": "W28Q1",  "question": "How many inches are in 1 foot?",                                                                        "options": ["10", "12", "16", "24"],                                               "answer": 1},
    {"week": 28, "id": "W28Q2",  "question": "A ribbon is 3 feet long. How many inches is that?",                                                     "options": ["30 inches", "36 inches", "3 inches", "39 inches"],                    "answer": 1},
    {"week": 28, "id": "W28Q3",  "question": "How many ounces are in 1 pound?",                                                                        "options": ["12", "10", "16", "20"],                                               "answer": 2},
    {"week": 28, "id": "W28Q4",  "question": "A recipe needs 2 pounds of flour. How many ounces of flour is that?",                                   "options": ["24 oz", "16 oz", "32 oz", "20 oz"],                                   "answer": 2},
    {"week": 28, "id": "W28Q5",  "question": "How many feet are in 1 yard?",                                                                           "options": ["12", "6", "4", "3"],                                                  "answer": 3},
    {"week": 28, "id": "W28Q6",  "question": "48 inches = ___ feet",                                                                                  "options": ["6", "4", "3", "5"],                                                   "answer": 1},
    {"week": 28, "id": "W28Q7",  "question": "How many quarts are in 1 gallon?",                                                                       "options": ["2", "3", "8", "4"],                                                   "answer": 3},
    {"week": 28, "id": "W28Q8",  "question": "A punch recipe calls for 2 gallons of juice. How many quarts is that?",                                 "options": ["6 quarts", "2 quarts", "8 quarts", "4 quarts"],                        "answer": 2},
    {"week": 28, "id": "W28Q9",  "question": "Mom buys a 5-pound bag of potatoes. How many ounces is that?",                                         "options": ["60 oz", "80 oz", "50 oz", "48 oz"],                                    "answer": 1},
    {"week": 28, "id": "W28Q10", "question": "A garden path is 15 feet long. How many yards is that?",                                                "options": ["45 yards", "30 yards", "12 yards", "5 yards"],                         "answer": 3},
    {"week": 28, "id": "W28Q11", "question": "How many cups are in 1 pint?",                                                                           "options": ["4", "3", "1", "2"],                                                   "answer": 3},
    {"week": 28, "id": "W28Q12", "question": "A family drank 3 quarts of lemonade. How many pints did they drink? (1 quart = 2 pints)",               "options": ["3 pints", "6 pints", "9 pints", "12 pints"],                           "answer": 1},
    {"week": 28, "id": "W28Q13", "question": "Jake needs 36 inches of string. The store sells string by the foot. How many feet should he buy?",      "options": ["4 feet", "3 feet", "36 feet", "2 feet"],                               "answer": 1},
    {"week": 28, "id": "W28Q14", "question": "Mia is 4 feet 6 inches tall. Her friend is 54 inches tall. Who is taller?",                            "options": ["Mia", "Her friend", "They are the same height", "Cannot determine"],   "answer": 2},
    {"week": 28, "id": "W28Q15", "question": "A dog weighs 48 ounces. How many pounds is that?",                                                      "options": ["4 pounds", "3 pounds", "6 pounds", "2 pounds"],                        "answer": 1},
    {"week": 28, "id": "W28Q16", "question": "How many pints are in 1 gallon?",                                                                        "options": ["4", "6", "8", "16"],                                                  "answer": 2},
    {"week": 28, "id": "W28Q17", "question": "A swimming pool holds 500 gallons. A hose fills 2 gallons per minute. How many minutes to fill 1/4 of the pool?", "options": ["62.5 minutes", "125 minutes", "250 minutes", "500 minutes"],  "answer": 0},
    {"week": 28, "id": "W28Q18", "question": "2 yards = ___ inches",                                                                                  "options": ["24 inches", "6 inches", "72 inches", "36 inches"],                    "answer": 2},
    {"week": 28, "id": "W28Q19", "question": "Rosa needs 12 cups of milk. She can only buy quarts. How many quarts should she buy? (1 quart = 4 cups)", "options": ["3 quarts", "4 quarts", "2 quarts", "6 quarts"],                    "answer": 0},
    {"week": 28, "id": "W28Q20", "question": "Pedro ran 1 mile on Monday, Wednesday, and Friday. If 1 mile = 5,280 feet, how many total feet did he run?", "options": ["5,280 feet", "10,560 feet", "15,840 feet", "52,800 feet"],      "answer": 2},

    # ── Week 29: Metric Measurement ───────────────────────────────────────────
    {"week": 29, "id": "W29Q1",  "question": "How many centimeters are in 1 meter?",                                                                  "options": ["10", "1,000", "100", "50"],                                           "answer": 2},
    {"week": 29, "id": "W29Q2",  "question": "A desk is 150 centimeters wide. How many meters is that?",                                              "options": ["0.15 m", "15 m", "1.5 m", "150 m"],                                   "answer": 2},
    {"week": 29, "id": "W29Q3",  "question": "How many meters are in 1 kilometer?",                                                                    "options": ["10", "100", "10,000", "1,000"],                                        "answer": 3},
    {"week": 29, "id": "W29Q4",  "question": "A school track is 400 meters. How many kilometers is that?",                                            "options": ["4 km", "40 km", "0.04 km", "0.4 km"],                                 "answer": 3},
    {"week": 29, "id": "W29Q5",  "question": "How many grams are in 1 kilogram?",                                                                      "options": ["10", "100", "1,000", "10,000"],                                        "answer": 2},
    {"week": 29, "id": "W29Q6",  "question": "A bag of apples weighs 2.5 kilograms. How many grams is that?",                                         "options": ["250 g", "25 g", "2,500 g", "25,000 g"],                                "answer": 2},
    {"week": 29, "id": "W29Q7",  "question": "How many milliliters are in 1 liter?",                                                                   "options": ["10", "100", "10,000", "1,000"],                                        "answer": 3},
    {"week": 29, "id": "W29Q8",  "question": "A water bottle holds 500 milliliters. How many liters is that?",                                        "options": ["5 L", "0.05 L", "50 L", "0.5 L"],                                     "answer": 3},
    {"week": 29, "id": "W29Q9",  "question": "How many millimeters are in 1 centimeter?",                                                              "options": ["100", "1,000", "10", "0.1"],                                          "answer": 2},
    {"week": 29, "id": "W29Q10", "question": "A pencil is 18 centimeters long. How many millimeters is that?",                                         "options": ["1.8 mm", "1,800 mm", "180 mm", "18 mm"],                               "answer": 2},
    {"week": 29, "id": "W29Q11", "question": "A trail is 3.5 kilometers long. How many meters is that?",                                              "options": ["35 m", "350 m", "3,500 m", "35,000 m"],                                "answer": 2},
    {"week": 29, "id": "W29Q12", "question": "A baby weighed 3,200 grams at birth. How many kilograms is that?",                                       "options": ["32 kg", "0.32 kg", "320 kg", "3.2 kg"],                                "answer": 3},
    {"week": 29, "id": "W29Q13", "question": "A recipe needs 250 mL of milk. You have a 1-liter carton. After using the milk, how many milliliters are LEFT?", "options": ["750 mL", "850 mL", "250 mL", "500 mL"],                      "answer": 0},
    {"week": 29, "id": "W29Q14", "question": "An Olympic swimming pool is 50 meters long. How many centimeters is that?",                             "options": ["500 cm", "5,000 cm", "50,000 cm", "5 cm"],                             "answer": 1},
    {"week": 29, "id": "W29Q15", "question": "4,500 grams = ___ kilograms",                                                                           "options": ["45 kg", "450 kg", "0.45 kg", "4.5 kg"],                                "answer": 3},
    {"week": 29, "id": "W29Q16", "question": "Maya is 135 cm tall. Her brother is 1.2 meters tall. Who is taller?",                                   "options": ["Brother", "Maya", "Same height", "Cannot determine"],                  "answer": 1},
    {"week": 29, "id": "W29Q17", "question": "A cyclist rode 2 km to school, 0.5 km to the store, and 1.5 km home. What was the TOTAL distance in meters?", "options": ["4,000 m", "400 m", "4 m", "40,000 m"],                         "answer": 0},
    {"week": 29, "id": "W29Q18", "question": "A juice box contains 200 mL. A full case has 24 juice boxes. How many liters are in the full case?",     "options": ["4.8 L", "48 L", "480 L", "0.48 L"],                                    "answer": 0},
    {"week": 29, "id": "W29Q19", "question": "Which measurement is the LONGEST?",                                                                      "options": ["300 cm", "0.003 km", "3,500 mm", "3 m"],                               "answer": 2},
    {"week": 29, "id": "W29Q20", "question": "A tank holds 8 liters of water. Each day, 750 mL evaporates. After 4 days, how many liters remain?",    "options": ["5 L", "5.5 L", "5.2 L", "4.5 L"],                                     "answer": 0},
]

# ── GENERATE ───────────────────────────────────────────────────────────────────
def generate():
    with open(OUTPUT_FILE, encoding='utf-8') as f:
        html = f.read()

    import re
    topics_json    = f'const TOPICS       = {safe_json(TOPICS)};'
    questions_json = f'const ALL_QUESTIONS = {safe_json(QUESTIONS)};'
    intros_json    = f'const TOPIC_INTROS = {safe_json(TOPIC_INTROS)};'

    html = re.sub(r'const TOPICS\s*=\s*\{[^;]+\};',
                  lambda _: topics_json, html)
    html = re.sub(r'const ALL_QUESTIONS\s*=\s*\[[^\]]*(?:\[[^\]]*\][^\]]*)*\];',
                  lambda _: questions_json, html, flags=re.DOTALL)
    html = re.sub(r'const TOPIC_INTROS\s*=\s*\{[^;]+\};',
                  lambda _: intros_json, html, flags=re.DOTALL)

    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        f.write(html)

    print(f"Generated {OUTPUT_FILE}")
    print(f"  {len(QUESTIONS)} questions across {len(TOPICS)} weeks")

if __name__ == '__main__':
    generate()
