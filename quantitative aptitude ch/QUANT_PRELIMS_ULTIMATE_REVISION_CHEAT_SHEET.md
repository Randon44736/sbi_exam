# ⚡ QUANT PRELIMS ULTIMATE SPEED CHEAT SHEET & RULES DOSSIER
**Candidate:** Hitendrasinh Solanki | **Target:** IBPS RRB PO 2026 Prelims (Target: 35+/40 in 20 Mins)  
**Scope:** Complete Formulae, Zero-Pen Shortcuts & Traps for Chapters 1 to 12 & 20 (પ્રિલિમ્સ ગણિતનું સંપૂર્ણ રિવિઝન)

---

## 🏛️ SECTION 1: SPEED MATH CORE (0 TO 6 MINUTES — 15 MARKS)

### 1. Rapid Approximation & BODMAS (પ્રકરણ ૧ & ૨)
* **VBODMAS Order & Left-to-Right Law:**
  * Operations: Brackets inside-out `( )` $\to$ `{ }` $\to$ `[ ]`, then `Of` (multiplication with priority over division!).
  * Divide & Multiply: Equal priority $\implies$ Solve **strictly LEFT TO RIGHT**!
    * *Trap:* $256 \div 16 \times 4 = (256 \div 16) \times 4 = 16 \times 4 = 64$ (NOT $256 \div 64 = 4$!).
  * Add & Subtract: In $-A + B$, think of cash: $64 - 36 + 12 = 28 + 12 = 40$ (Do not add $36+12=48$!).
* **Mixed Fractions Separation Rule:**
  * Never convert to improper fractions! Separate whole numbers and fractions:
    $$A \frac{b}{c} + D \frac{e}{f} - G \frac{h}{k} = (A + D - G) + \left(\frac{b}{c} + \frac{e}{f} - \frac{h}{k}\right)$$
* **The "Whole Minus Mixed Fraction" 3-Second Hack:**
  * $$N - A \frac{b}{c} = (N - A - \mathbf{1}) \frac{c - b}{c}$$
  * *Example:* $25 - 6 \frac{3}{8} = (25 - 7) \frac{8 - 3}{8} = 18 \frac{5}{8}$! (Zero pen needed!).
* **Benchmark Percentage Fraction Swaps:**
  * $50\% = \frac{1}{2} \quad | \quad 25\% = \frac{1}{4} \quad | \quad 20\% = \frac{1}{5} \quad | \quad 10\% = \frac{1}{10}$
  * $37.5\% = \frac{3}{8} \quad | \quad 62.5\% = \frac{5}{8} \quad | \quad 87.5\% = \frac{7}{8}$
  * $66.66\% = \frac{2}{3} \quad | \quad 83.33\% = \frac{5}{6} \quad | \quad 14.28\% = \frac{1}{7} \quad | \quad 28.57\% = \frac{2}{7}$
  * *The Swap Rule:* $A\% \text{ of } B = B\% \text{ of } A$ (e.g. $64\% \text{ of } 875 = 87.5\% \text{ of } 640 = \frac{7}{8} \times 640 = 560$).
* **5-Second Square Root Method (Benchmark Tens + Unit Digit):**
  * Tens: $20^2=400, 30^2=900, 40^2=1600, 50^2=2500, 60^2=3600, 70^2=4900$.
  * Unit digit endings: $1 \to 1 \text{ or } 9 \quad | \quad 4 \to 2 \text{ or } 8 \quad | \quad 5 \to 5 \quad | \quad 6 \to 4 \text{ or } 6 \quad | \quad 9 \to 3 \text{ or } 7$.
  * *Example:* $\sqrt{1024}$ lies between 900 ($30^2$) and 1600 ($40^2$), ends in 4 $\implies 32$ or $38$. Close to 900 $\implies \mathbf{32}$!

---

### 2. Quadratic Equations & Inequalities (પ્રકરણ ૪)
* **The 2-Second Instant CND Hack (The Free Mark!):**
  * If the constant term ($c$) in **BOTH** equations is **NEGATIVE** ($-$), the answer is **ALWAYS [E] CND** without solving!
  * *Example:* $x^2 + 2x - 35 = 0$ and $y^2 - 4y - 45 = 0 \implies$ Both end in minus $\implies$ **Instant [E] CND**!
* **The Universal Sign Table (Root Signs from Equation Signs):**
  * Equation has $(-, +) \implies$ Roots are **$(+, +)$** (Both Positive).
  * Equation has $(+, +) \implies$ Roots are **$(-, -)$** (Both Negative).
  * Equation has $(+, -) \implies$ Roots are **$(-, +)$** (Larger root is Negative).
  * Equation has $(-, -) \implies$ Roots are **$(+, -)$** (Larger root is Positive).
  * *Sign Rule Jump:* If Eq I is $(-, +)$ and Eq II is $(+, +) \implies (+, +) > (-, -) \implies \mathbf{x > y}$ instantly!
* **Square vs Square Root Trap:**
  * $x^2 = 196 \implies x = +14, -14$ (Two roots!).
  * $y = \sqrt{196} \implies y = +14$ (Principal root is only positive!).
  * Comparison: $\{+14, -14\}$ vs $\{+14\} \implies \mathbf{x \le y}$!
* **Negative Comparison Rule:**
  * In negative numbers, smaller looking number is NUMERICALLY LARGER: $-5 > -9$.

---

### 3. Number Series & Two-Series Hacks (પ્રકરણ ૩ & ૧૨)
* **The 3-Second Visual Scan Flowchart:**
  * Slow/Steady Growth $\implies$ **Difference Series** (Squares $+n^2$, Cubes $+n^3$, Primes, or $D_2$).
  * Explosive Growth $\implies$ **Multiplication Series** ($\times n, \times n + k$).
  * 2nd Number drops to ~half $\implies$ **Decimal Series** ($\times 0.5 + k$).
  * Zig-Zag Up & Down $\implies$ **Alternating Series** (Skip 1 number).
  * Terms add previous terms $\implies$ **Fibonacci Series** ($A + B = C$).
* **The Parallel Shift Shortcut (Zero-Pen 2-Second Hack):**
  * In Two-Series where pattern is additive/difference-based:
    $$\text{Shift} = \text{Start of Series II} - \text{Start of Series I}$$
    $$\text{Term}_n(\text{Series II}) = \text{Term}_n(\text{Series I}) + \text{Shift}$$
  * *Note:* Works on differences, squares, cubes, primes, alternating. Does NOT work on multiplication!
* **Wrong Number "Two Bad Gaps" Law:**
  * A single wrong number ruins **TWO adjacent gaps**. The number at the junction of the two bad gaps is **ALWAYS the wrong number**!

---

## 🧭 SECTION 2: DATA INTERPRETATION SPEED HACKS (6 TO 14 MINUTES — 15 MARKS)

### 4. Universal DI Calculations (પ્રકરણ ૯)
* **Ratio Calculations:** Cancel trailing zeros immediately before writing (e.g., $1500 : 800 \to 15 : 8$).
* **Percentage Comparison ("X is what % MORE / LESS than Y"):**
  $$\text{Percentage More / Less} = \left(\frac{\text{Difference}}{\text{Value after 'THAN'}}\right) \times 100$$
  * *Golden Rule:* The denominator is ALWAYS the reference value appearing right after the word **"THAN"**!
* **Pie Chart Degree Shortcut:**
  * Full Circle $= 360^\circ = 100\% \implies 36^\circ = 10\% \implies 18^\circ = 5\%$.
  * *Ratio of Slices in Same Pie:* NEVER calculate real values! Use degrees directly: $54^\circ : 36^\circ = 3 : 2$.
* **Line & Bar Graph Gap Summation:**
  * When asked for total difference between Company P and Q over 4 months:
  * Sum the individual month-wise gaps directly instead of calculating two large sums!

---

## 🧩 SECTION 3: ARITHMETIC 10-SECOND FORMULAS (14 TO 20 MINUTES — 10 MARKS)

### 5. Ratio, Ages, Averages & Percentages (પ્રકરણ ૫)
* **Ages Ratio-Unit Trick:** Age difference NEVER changes with time!
  * Present 4:5 $\to$ 6 yrs later 5:6 $\implies 1 \text{ unit} = 6 \text{ yrs} \implies A = 4 \times 6 = 24 \text{ yrs}$.
* **Price-Consumption Fraction Ladder:**
  * If price increases by $+\frac{1}{n}$, consumption must drop by $-\frac{1}{n+1}$ to keep expenditure constant.
  * Price $+25\% \left(+\frac{1}{4}\right) \implies$ Usage drops by $-\frac{1}{5} = \mathbf{20\%}$.
* **Average Dynamic Group Shift:**
  $$\text{New Person Weight/Age} = \text{Old Average} + (\text{New Total Count} \times \text{Increase in Average})$$
  * 24 students avg 45 kg, teacher added (+1 kg) $\implies 45 + (25 \times 1) = \mathbf{70 \text{ kg}}$.
* **Successive % Change (+x% then -x%):** Always a net loss of $-\left(\frac{x^2}{100}\right)\%$.

---

### 6. Commercial Math: P&L, Discount, SI & CI (પ્રકરણ ૬)
* **Loss-to-Profit Jump Rule:**
  * When shifting from $-L\%$ loss to $+P\%$ profit, ADD the two percentages to find the rupee gap:
  * $15\%$ loss to $15\%$ profit $= 30\%$ gap $= ₹450 \implies 1\% = 15 \implies \text{CP} (100\%) = ₹1,500$.
* **Equal Cost Price (CP) Trap:**
  * Two items BOUGHT for the same CP: One sold at $+10\%$, other at $-10\% \implies$ **Net is ₹0 (No Profit, No Loss)**!
* **CI Doubling Power Rule:** Money grows by powers: $1 \to 2^1 (T \text{ yrs}) \to 2^2 (2T \text{ yrs}) \to 2^3 (3T \text{ yrs})$.
  * Doubles in 4 yrs $\implies$ Becomes 8 times ($2^3$) in $3 \times 4 = \mathbf{12 \text{ yrs}}$.
* **2-Year CI vs SI Difference Formula:**
  $$\text{Diff} = P \times \left(\frac{R}{100}\right)^2 \quad \text{or} \quad R = 100 \times \sqrt{\frac{\text{Diff}}{P}}$$

---

### 7. Time & Work, Pipes, Speed, Boats (પ્રકરણ ૭)
* **Time & Work LCM Chocolate Method:**
  * Total Work = LCM of days. Efficiency = $\frac{\text{Total Work}}{\text{Days}}$.
  * $A=12 \text{ d}, B=18 \text{ d} \implies \text{Work}=36 \text{ units} \implies A=3, B=2 \implies A+B=5 \text{ units/day}$.
* **$M_1 D_1 = M_2 D_2$ Law:** Men $\times$ Days = Constant Work.
* **Speed Conversion 18-Table:**
  * $18 \text{ km/h} = 5 \text{ m/s} \quad | \quad 36 \text{ km/h} = 10 \text{ m/s} \quad | \quad 54 \text{ km/h} = 15 \text{ m/s} \quad | \quad 72 \text{ km/h} = 20 \text{ m/s}$.
* **Train Crossing Platform:** $\text{Total Distance} = \text{Train Length} + \text{Platform Length}$.
* **Boats & Streams Formulas:**
  * Downstream $D = u + v \quad | \quad$ Upstream $U = u - v$
  * Boat in still water: $u = \frac{D + U}{2} \quad | \quad$ Stream speed: $v = \frac{D - U}{2}$

---

### 8. Alligation, Mensuration 2D & Probability (પ્રકરણ ૮ & ૨૦)
* **Alligation Cross-Subtraction:**
  * $\frac{\text{Cheaper Quantity}}{\text{Dearer Quantity}} = \frac{\text{Dearer Price} - \text{Mean}}{\text{Mean} - \text{Cheaper Price}}$
* **Repeated Dilution Formula:** $\text{Liquid Left} = \text{Initial} \times \left(1 - \frac{x}{\text{Capacity}}\right)^n$.
* **7-44-154 Circle Scaling Benchmark:**
  * Radius $r = 7 \text{ cm} \implies \text{Circumference} = 44 \text{ cm} \implies \text{Area} = 154 \text{ cm}^2$.
  * If radius doubles ($r=14$): Circumference doubles ($88 \text{ cm}$), Area quadruples ($154 \times 4 = 616 \text{ cm}^2$).
* **Fast Combinations ($nC_2$):** $nC_2 = \frac{n(n-1)}{2}$ ($4C_2=6, 5C_2=10, 6C_2=15, 8C_2=28, 10C_2=45, 12C_2=66$).
* **"At Least One" Hack:** $P(\text{At least one}) = 1 - P(\text{None})$.
