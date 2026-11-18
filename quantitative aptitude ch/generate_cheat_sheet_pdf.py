import os
import sys
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, KeepTogether, HRFlowable
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.pdfgen import canvas

class NumberedCanvas(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        super(NumberedCanvas, self).__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_page_decorations(num_pages)
            super(NumberedCanvas, self).showPage()
        super(NumberedCanvas, self).save()

    def draw_page_decorations(self, page_count):
        self.saveState()
        self.setFont("Helvetica-Bold", 8)
        self.setFillColor(colors.HexColor("#1A365D")) # Navy
        
        # Header (Top)
        self.drawString(36, 810, "IBPS RRB PO SCALE-I (PRELIMS) — QUANTITATIVE APTITUDE SPEED CHEAT SHEET")
        self.setFont("Helvetica", 8)
        self.setFillColor(colors.HexColor("#718096"))
        self.drawRightString(559, 810, "Candidate: Hitendrasinh Solanki | Exam: 21 Nov 2026")
        self.setStrokeColor(colors.HexColor("#CBD5E0"))
        self.setLineWidth(0.75)
        self.line(36, 804, 559, 804)
        
        # Footer (Bottom)
        self.line(36, 40, 559, 40)
        self.setFont("Helvetica-Bold", 8)
        self.setFillColor(colors.HexColor("#2B6CB0"))
        self.drawString(36, 28, "TARGET: 35+/40 MARKS IN 20 MINUTES | SPEED & ZERO-PEN ACCURACY DOSSIER")
        self.setFont("Helvetica-Bold", 8)
        self.setFillColor(colors.HexColor("#1A365D"))
        self.drawRightString(559, 28, f"Page {self._pageNumber} of {page_count}")
        self.restoreState()

def build_pdf():
    pdf_filename = "quantitative aptitude ch/IBPS_RRB_PO_Quant_Ultimate_Cheat_Sheet.pdf"
    doc = SimpleDocTemplate(
        pdf_filename,
        pagesize=A4,
        leftMargin=36,
        rightMargin=36,
        topMargin=46,
        bottomMargin=48
    )

    styles = getSampleStyleSheet()
    
    # Custom Palette
    NAVY = colors.HexColor("#1A365D")
    BLUE = colors.HexColor("#2B6CB0")
    LIGHT_BLUE = colors.HexColor("#EBF8FF")
    DARK_GRAY = colors.HexColor("#2D3748")
    BORDER_COLOR = colors.HexColor("#CBD5E0")
    LIGHT_RED = colors.HexColor("#FFF5F5")
    GOLD_ACCENT = colors.HexColor("#744210")
    LIGHT_GOLD = colors.HexColor("#FEFCBF")

    # Typography Styles
    title_style = ParagraphStyle(
        'DocTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=16,
        leading=20,
        textColor=NAVY,
        alignment=1, # Center
        spaceAfter=3
    )
    
    subtitle_style = ParagraphStyle(
        'DocSubTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=9.5,
        leading=13,
        textColor=BLUE,
        alignment=1,
        spaceAfter=8
    )
    
    module_header_style = ParagraphStyle(
        'ModuleHeader',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=11,
        leading=14,
        textColor=colors.white,
        spaceAfter=0
    )
    
    trick_title_style = ParagraphStyle(
        'TrickTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=9.5,
        leading=12,
        textColor=NAVY
    )
    
    body_style = ParagraphStyle(
        'BodyDark',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8,
        leading=11,
        textColor=DARK_GRAY
    )
    
    bold_label_style = ParagraphStyle(
        'BoldLabel',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=8.5,
        leading=11.5,
        textColor=NAVY
    )
    
    example_style = ParagraphStyle(
        'ExampleText',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8,
        leading=11,
        textColor=colors.HexColor("#1A202C")
    )

    story = []

    # Title Block
    banner_data = [
        [Paragraph("IBPS RRB PO PRELIMS QUANTITATIVE APTITUDE", title_style)],
        [Paragraph("ULTIMATE SPEED CHEAT SHEET, FORMULAE & IDENTIFICATION GUIDE", subtitle_style)],
        [Paragraph("<b>Candidate:</b> Hitendrasinh Solanki | <b>Target:</b> 35+/40 Marks (21 Nov 2026) | <b>Scope:</b> Ch 1 to 12 & 20", ParagraphStyle('Meta', parent=body_style, alignment=1, fontSize=8, textColor=DARK_GRAY))]
    ]
    banner_table = Table(banner_data, colWidths=[523])
    banner_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), LIGHT_BLUE),
        ('BOX', (0,0), (-1,-1), 1.5, BLUE),
        ('TOPPADDING', (0,0), (-1,-1), 6),
        ('BOTTOMPADDING', (0,0), (-1,-1), 6),
        ('LEFTPADDING', (0,0), (-1,-1), 10),
        ('RIGHTPADDING', (0,0), (-1,-1), 10),
    ]))
    story.append(banner_table)
    story.append(Spacer(1, 8))

    def make_module_header(title_text):
        t = Table([[Paragraph(f"<b>{title_text}</b>", module_header_style)]], colWidths=[523])
        t.setStyle(TableStyle([
            ('BACKGROUND', (0,0), (-1,-1), NAVY),
            ('TOPPADDING', (0,0), (-1,-1), 4),
            ('BOTTOMPADDING', (0,0), (-1,-1), 4),
            ('LEFTPADDING', (0,0), (-1,-1), 8),
        ]))
        return t

    def make_trick_box(trick_num, trick_name, when_to_use, shortcut_rule, example_q, example_sol, trap_warn=None):
        content = [
            [Paragraph(f"<b>TRICK {trick_num}: {trick_name.upper()}</b>", trick_title_style)],
            [Paragraph(f"<b>🎯 How to Identify in Exam:</b> {when_to_use}", body_style)],
            [Paragraph(f"<b>⚡ Speed Shortcut & Rule:</b> <font color='#2B6CB0'><b>{shortcut_rule}</b></font>", body_style)],
            [Paragraph(f"<b>📝 Real Exam Example:</b><br/><b>[Problem]:</b> {example_q}<br/><b>[Speed Solution]:</b> {example_sol}", example_style)]
        ]
        if trap_warn:
            content.append([Paragraph(f"<b>⚠️ Trap to Avoid:</b> <font color='#9B2C2C'>{trap_warn}</font>", body_style)])

        t = Table(content, colWidths=[523])
        t_style = [
            ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#EDF2F7")),
            ('BACKGROUND', (0,1), (-1,-1), colors.white),
            ('BOX', (0,0), (-1,-1), 1, BORDER_COLOR),
            ('LINEBELOW', (0,0), (-1,0), 0.75, colors.HexColor("#CBD5E0")),
            ('TOPPADDING', (0,0), (-1,-1), 3),
            ('BOTTOMPADDING', (0,0), (-1,-1), 3),
            ('LEFTPADDING', (0,0), (-1,-1), 8),
            ('RIGHTPADDING', (0,0), (-1,-1), 8),
        ]
        if trap_warn:
            t_style.append(('BACKGROUND', (0, len(content)-1), (-1, len(content)-1), LIGHT_RED))
        t.setStyle(TableStyle(t_style))
        return t

    # =========================================================================
    # MODULE 1: SPEED MATH & RAPID APPROXIMATION (CH 1 & 2)
    # =========================================================================
    story.append(make_module_header("MODULE 1: SPEED MATH & RAPID APPROXIMATION (CH 1 & 2) — 5 MARKS"))
    story.append(Spacer(1, 5))

    story.append(make_trick_box(
        "1.1", "VBODMAS Left-to-Right Priority Law",
        "Equations containing consecutive division and multiplication without enclosing brackets.",
        "Divide and Multiply have equal precedence. Solve strictly <b>LEFT TO RIGHT</b>! Never jump ahead to multiply first.",
        "What approximate value replaces (?): <b>256 ÷ 16 × 4 = ?</b>",
        "Step 1: (256 ÷ 16) = 16. Step 2: 16 × 4 = <b>64</b>.",
        "Multiplying 16 × 4 = 64 first, then doing 256 ÷ 64 = 4. This is an immediate -0.25 penalty!"
    ))
    story.append(Spacer(1, 5))

    story.append(make_trick_box(
        "1.2", "Whole Minus Mixed Fraction 3-Second Hack",
        "Subtracting any mixed fraction A (b/c) from a whole integer N (e.g. 25 - 6 3/8).",
        "<b>N - A (b/c) = (N - A - 1) [ (c - b) / c ]</b>. (Add 1 to the integer part, subtract from N, numerator becomes denominator minus numerator).",
        "Evaluate <b>25 - 6 3/8</b> in 2 seconds without pen.",
        "Subtract 7 from 25: 25 - 7 = <b>18</b>. Fraction: (8 - 3)/8 = <b>5/8</b>. Final Answer: <b>18 5/8</b>!",
        "Converting 6 3/8 into 51/8, finding LCM with 25/1, and subtracting wastes 45 valuable seconds."
    ))
    story.append(Spacer(1, 5))

    story.append(make_trick_box(
        "1.3", "Benchmark Percentage-Fraction Swap Rule",
        "Percentages with decimals like 37.5%, 62.5%, 87.5%, 16.66%, 83.33%, 14.28%, 12.5%.",
        "<b>A% of B = B% of A</b>. Always replace benchmark percentages with exact fractions:<br/>"
        "• 12.5% = 1/8 | 37.5% = 3/8 | 62.5% = 5/8 | 87.5% = 7/8<br/>"
        "• 16.66% = 1/6 | 33.33% = 1/3 | 66.66% = 2/3 | 83.33% = 5/6<br/>"
        "• 14.28% = 1/7 | 28.57% = 2/7 | 9.09% = 1/11",
        "Find <b>64% of 875</b>.",
        "Swap using A% of B = B% of A: 87.5% of 640 = <b>(7/8) × 640 = 7 × 80 = 560</b>!",
        "Multiplying 64 × 875 and dividing by 100 causes severe calculation fatigue and arithmetic slips."
    ))
    story.append(Spacer(1, 5))

    story.append(make_trick_box(
        "1.4", "5-Second Square Root Hack (Tens Benchmark + Unit Ending)",
        "Estimating square roots of 4-digit numbers in approximation (e.g., √1024, √3249).",
        "1. Bracket between base tens: 30² = 900, 40² = 1600, 50² = 2500, 60² = 3600.<br/>"
        "2. Match unit digit endings: 1 → 1/9, 4 → 2/8, 5 → 5, 6 → 4/6, 9 → 3/7.<br/>"
        "3. Choose the option closer to the lower or upper base ten square.",
        "Find approx value of <b>√1024</b>.",
        "Lies between 30² (900) and 40² (1600). Ends in 4 → last digit is 2 or 8 (32 or 38). 1024 is much closer to 900 than 1600 → <b>32</b>!",
        "Do not use manual division square root algorithms in bank exams."
    ))
    story.append(Spacer(1, 5))

    story.append(make_trick_box(
        "1.5", "Difference of Squares Algebraic Shortcut",
        "Expressions of the form (A.98)² - (B.95)² in rapid approximation.",
        "Use <b>a² - b² = (a - b)(a + b)</b> instead of squaring both numbers separately.",
        "Find approx value of <b>(17.98)² - (13.95)²</b>.",
        "Round to 18² - 14². (18 - 14)(18 + 14) = <b>4 × 32 = 128</b>!",
        "Squaring 18² = 324 and 14² = 196 and subtracting takes twice the time."
    ))
    story.append(Spacer(1, 8))

    # =========================================================================
    # MODULE 2: QUADRATIC EQUATIONS & INEQUALITIES (CH 4)
    # =========================================================================
    story.append(make_module_header("MODULE 2: QUADRATIC EQUATIONS & INEQUALITIES (CH 4) — 5 MARKS"))
    story.append(Spacer(1, 5))

    story.append(make_trick_box(
        "2.1", "The 2-Second Instant CND Hack (The Free Mark)",
        "Both quadratic equations have a <b>NEGATIVE constant term (- c)</b> at the end.",
        "If the constant term in BOTH equations is negative (-), the answer is <b>ALWAYS [E] x = y or Relationship Cannot Be Established (CND)</b>. Zero factoring needed!",
        "<b>I.</b> x² + 2x - 35 = 0 &nbsp;&nbsp;|&nbsp;&nbsp; <b>II.</b> y² - 4y - 45 = 0",
        "Both equations end with minus (-35 and -45). Mark <b>[E] CND</b> in 2 seconds!",
        "Solving factors for both equations when both end in negative constants wastes 2 minutes."
    ))
    story.append(Spacer(1, 5))

    story.append(make_trick_box(
        "2.2", "Universal Root Sign Table & Sign Jump Shortcut",
        "Every quadratic equation ax² + bx + c = 0.",
        "Determine the signs of the roots directly from equation signs:<br/>"
        "• Equation <b>(-, +)</b> → Roots are <b>(+, +)</b> [Both Positive]<br/>"
        "• Equation <b>(+, +)</b> → Roots are <b>(-, -)</b> [Both Negative]<br/>"
        "• Equation <b>(+, -)</b> → Roots are <b>(-, +)</b> [Larger root is Negative]<br/>"
        "• Equation <b>(-, -)</b> → Roots are <b>(+, -)</b> [Larger root is Positive]<br/>"
        "<b>SIGN JUMP:</b> If Eq I is (-, +) and Eq II is (+, +) → (+, +) > (-, -) → <b>x > y instantly</b>!",
        "<b>I.</b> x² - 11x + 30 = 0 &nbsp;&nbsp;|&nbsp;&nbsp; <b>II.</b> y² + 15y + 56 = 0",
        "Eq I has (-, +) → Roots are (+5, +6). Eq II has (+, +) → Roots are (-7, -8). Positive is always greater than negative → <b>x > y</b>!",
        "Forgetting that (+, +) equation yields (-,-) roots."
    ))
    story.append(Spacer(1, 5))

    story.append(make_trick_box(
        "2.3", "Square vs Square Root Trap",
        "Pair of equations where one is x² = N and the other is y = √N.",
        "• <b>x² = N</b> has TWO roots: <b>+√N and -√N</b>.<br/>"
        "• <b>y = √N</b> has ONLY ONE root: <b>+√N</b> (principal square root is always non-negative).<br/>"
        "• Comparing {+√N, -√N} with {+√N} always yields <b>x ≤ y</b>!",
        "<b>I.</b> x² = 196 &nbsp;&nbsp;|&nbsp;&nbsp; <b>II.</b> y = √196",
        "Roots: x = {+14, -14}. Root: y = {+14}. Since +14 = +14 and -14 < +14, final relation is <b>x ≤ y</b> (Option [D]).",
        "Candidates assume √196 is ±14, which leads them to incorrectly choose [E] CND or [A] x > y!"
    ))
    story.append(Spacer(1, 5))

    story.append(make_trick_box(
        "2.4", "Coefficient Balancing Multiplication Hack",
        "Quadratic equations with leading coefficients a₁ ≠ a₂ (e.g. 2x² vs 3y²).",
        "Do NOT divide roots by coefficients (creates difficult decimal comparisons). Instead, <b>cross-multiply the roots</b>: Multiply Eq I roots by a₂, and Eq II roots by a₁!",
        "<b>I.</b> 2x² - 7x + 6 = 0 &nbsp;&nbsp;|&nbsp;&nbsp; <b>II.</b> 3y² - 11y + 10 = 0",
        "Eq I factors: 3, 4. Eq II factors: 5, 6.<br/>"
        "Multiply Eq I factors by 3: {9, 12}. Multiply Eq II factors by 2: {10, 12}.<br/>"
        "Comparing: 9 < 10, 12; but 12 > 10. Overlap → <b>[E] CND</b>!",
        "Dividing 3/2 = 1.5, 4/2 = 2.0, 5/3 = 1.66, 6/3 = 2.0 causes comparison confusion."
    ))
    story.append(Spacer(1, 8))

    # =========================================================================
    # MODULE 3: NUMBER SERIES & TWO-SERIES PATTERNS (CH 3 & 12)
    # =========================================================================
    story.append(make_module_header("MODULE 3: NUMBER SERIES & TWO-SERIES PATTERNS (CH 3 & 12) — 5 MARKS"))
    story.append(Spacer(1, 5))

    story.append(make_trick_box(
        "3.1", "3-Second Visual Scan Flowchart",
        "Recognizing series type in the first 3 seconds before writing any numbers.",
        "• <b>Slow / Steady Rise:</b> Difference Series (+n², +n³, primes, or D₂ step-ladder).<br/>"
        "• <b>Explosive Growth:</b> Multiplication Series (×1+1, ×2+2, ×3+3...).<br/>"
        "• <b>Second Number Halves:</b> Decimal Series (×0.5 + 0.5, ×1 + 1, ×2 + 2...).<br/>"
        "• <b>Up-Down-Up-Down:</b> Alternating Series (skip one number).",
        "Identify and solve: <b>12, 13, 28, 87, 352, ?</b>",
        "Growth is explosive: 12×1+1=13, 13×2+2=28, 28×3+3=87, 87×4+4=352. Next is <b>352 × 5 + 5 = 1765</b>!",
        "Trying difference methods on multiplication series wastes 2 minutes."
    ))
    story.append(Spacer(1, 5))

    story.append(make_trick_box(
        "3.2", "Wrong Number 'Two Bad Gaps' Law",
        "Identifying the wrong number in a difference/addition series.",
        "A single wrong number in a series ruins <b>TWO adjacent gaps</b>. The number located exactly at the junction of the two bad gaps is <b>ALWAYS the wrong number</b>!",
        "Find the wrong number in: <b>6, 12, 20, 30, 41, 56</b>",
        "Gaps: +6, +8, +10, +11, +15. The pattern of consecutive even differences (+6, +8, +10, +12, +14) is ruined at +11 and +15. The junction number is <b>41</b> (it should be 30 + 12 = 42).",
        "Do not guess options. The junction of the two ruined differences is always the answer."
    ))
    story.append(Spacer(1, 5))

    story.append(make_trick_box(
        "3.3", "Parallel Shift Shortcut (Two-Series Patterns — Ch 12)",
        "Two-Series questions where Series II starts with a new number but follows the exact same difference/step pattern as Series I.",
        "<b>Shift = Start of Series II - Start of Series I</b>.<br/>"
        "<b>Term_n(Series II) = Term_n(Series I) + Shift</b>.<br/>"
        "Valid for all difference, square, cube, prime, and alternating patterns! (Not valid for pure multiplication).",
        "Series I: 14, 22, 38, 70, 134, 262.<br/>Series II: 25, a, b, c, d, e. Find the value of <b>(b)</b>.",
        "Shift = 25 - 14 = <b>+11</b>. (b) is at Position 3.<br/>"
        "Position 3 of Series I is 38. Therefore, <b>b = 38 + 11 = 49</b>! (Solved in 2 seconds!).",
        "Candidates calculate 'a' (Position 2) and select option [A] forgetting the question asked for 'b'!"
    ))
    story.append(Spacer(1, 8))

    # =========================================================================
    # MODULE 4: DATA INTERPRETATION SPEED HACKS (CH 9)
    # =========================================================================
    story.append(make_module_header("MODULE 4: DATA INTERPRETATION SPEED HACKS (CH 9) — 15 MARKS"))
    story.append(Spacer(1, 5))

    story.append(make_trick_box(
        "4.1", "The 'THAN' Denominator Reference Law",
        "Any question asking 'X is what % MORE than Y?' or 'X is what % LESS than Y?'.",
        "<b>% More / Less = [ (Difference between X and Y) / (Value right after 'THAN') ] × 100</b>.<br/>"
        "The denominator is ALWAYS the reference base appearing directly after the word <b>'THAN'</b>!",
        "Total accounts in Surat = 2,400. Total accounts in Gandhinagar = 1,200. Total accounts in Surat are what percent more than Gandhinagar?",
        "Difference = 2400 - 1200 = 1200. Value after 'THAN' is Gandhinagar (1200).<br/>"
        "% More = <b>(1200 / 1200) × 100 = 100%</b>!",
        "Putting Surat (2400) in the denominator gives 50%, which is wrong."
    ))
    story.append(Spacer(1, 5))

    story.append(make_trick_box(
        "4.2", "Pie Chart Direct Degree Ratio & Scale Shortcut",
        "Finding ratios or percentages between slices in the same pie chart.",
        "1. Full Circle = 360° = 100% → 36° = 10% → 18° = 5%.<br/>"
        "2. <b>RATIO OF SLICES:</b> NEVER convert degrees to actual candidates! Take the ratio of degrees directly.<br/>"
        "3. <b>SCALE FACTOR:</b> Total value / 360 = Value per 1°.",
        "In a pie chart of 3,600 candidates, Engineering is 54° and Others is 36°. Find ratio of Engineering to Others.",
        "Do NOT find actual counts! Take ratio of degrees: <b>54° : 36° = 3 : 2</b> (Option [B])!",
        "Misreading category names (e.g. taking Arts 72° instead of Others 36°)."
    ))
    story.append(Spacer(1, 5))

    story.append(make_trick_box(
        "4.3", "Line & Bar Graph Month-Wise Gap Summation",
        "Finding total difference between two companies/groups over multiple periods.",
        "Do NOT sum each group's numbers separately! Calculate the <b>individual period gaps</b> directly and sum the small gaps.",
        "Company P and Q production over 4 months: Jan (35 vs 45), Feb (40 vs 50), Mar (55 vs 60), Apr (65 vs 70). Find total difference across all months.",
        "Calculate gaps directly: Jan (+10) + Feb (+10) + Mar (+5) + Apr (+5) = <b>30</b>! (Done in 5 seconds).",
        "Adding 35+40+55+65 = 195, and 45+50+60+70 = 225, then subtracting 225 - 195 = 30 takes 3x more time."
    ))
    story.append(Spacer(1, 8))

    # =========================================================================
    # MODULE 5: CORE ARITHMETIC 10-SECOND FORMULAS (CH 5 TO 8, 20)
    # =========================================================================
    story.append(make_module_header("MODULE 5: CORE ARITHMETIC 10-SECOND FORMULAS (CH 5 TO 8, 20) — 10 MARKS"))
    story.append(Spacer(1, 5))

    story.append(make_trick_box(
        "5.1", "Ages Ratio-Unit Invariance Rule",
        "Age word problems where ratios are given at two different times.",
        "The age difference between two persons NEVER changes. If unit differences are equal, <b>1 Unit = Number of elapsed years</b>.",
        "Ratio of ages of A and B is 4:5. Six years hence, it becomes 5:6. Find A's present age.",
        "Unit increase: 5 - 4 = 1 unit, 6 - 5 = 1 unit. 1 Unit = 6 years.<br/>"
        "A's present age = 4 units = <b>4 × 6 = 24 years</b>!",
        "Setting up algebraic equations 5(4x + 6) = 4(5x + 6) is slow."
    ))
    story.append(Spacer(1, 5))

    story.append(make_trick_box(
        "5.2", "Price-Consumption Fraction Ladder",
        "Commodity price changes by X%, find % reduction in consumption to keep expenditure constant.",
        "• If price increases by <b>+1/n</b>, consumption must decrease by <b>-1/(n+1)</b>.<br/>"
        "• If price decreases by <b>-1/n</b>, consumption must increase by <b>+1/(n-1)</b>.",
        "If price of sugar increases by 25%, by what % must consumption drop to keep expenditure unchanged?",
        "Price increases by 25% = +1/4. Consumption must decrease by -1/(4 + 1) = -1/5 = <b>20%</b>!",
        "Candidates assume if price increases by 25%, consumption drops by 25%."
    ))
    story.append(Spacer(1, 5))

    story.append(make_trick_box(
        "5.3", "Dynamic Average Group Shift",
        "Average of a group changes when a new person joins or leaves.",
        "<b>New Person's Value = Old Average + (New Total Headcount × Increase in Average)</b>.",
        "Average weight of 24 students is 45 kg. When teacher is included, average weight increases by 1 kg. Find teacher's weight.",
        "Teacher's weight = 45 + (25 × 1) = 45 + 25 = <b>70 kg</b>!",
        "Calculating 25 × 46 = 1150 and 24 × 45 = 1080 and subtracting 1150 - 1080 takes 4x longer."
    ))
    story.append(Spacer(1, 5))

    story.append(make_trick_box(
        "5.4", "Loss-to-Profit Jump Rule",
        "Selling price increase of ₹K shifts outcome from L% loss to P% profit.",
        "Total percentage gap = <b>(L + P)%</b>. Then: <b>(L + P)% of CP = ₹K → CP = [ K / (L + P) ] × 100</b>.",
        "Shopkeeper shifts from 15% loss to 15% profit when selling price is increased by ₹450. Find Cost Price.",
        "Percentage Jump = 15% + 15% = 30%. 30% of CP = ₹450 → 1% = 15 → <b>CP (100%) = ₹1,500</b>!",
        "Subtracting 15% - 15% = 0% instead of adding the opposite directional shift."
    ))
    story.append(Spacer(1, 5))

    story.append(make_trick_box(
        "5.5", "Compound Interest Doubling Power Rule",
        "Sum doubles (or triples) in T years under Compound Interest.",
        "CI grows exponentially by powers: <b>Multiple = (Base)^k → Time = k × T</b>.<br/>"
        "If it doubles (2¹) in T years, it becomes 4 times (2²) in 2T years, and 8 times (2³) in 3T years.",
        "A sum at CI doubles itself in 4 years. In how many years will it become 8 times?",
        "8 = 2³. Power is 3. Required Time = <b>3 × 4 = 12 years</b> (Option [C])!",
        "Assuming CI grows linearly like SI: 4 + 4 = 8 years. In 8 years it only becomes 4 times!"
    ))
    story.append(Spacer(1, 5))

    story.append(make_trick_box(
        "5.6", "Time & Work LCM Chocolate Method",
        "Two or more individuals completing work at different rates, joining/leaving.",
        "1. Total Work = LCM of individual days.<br/>"
        "2. Efficiency = Total Work / Days.<br/>"
        "3. Remaining Days = Remaining Work / Active Efficiency.",
        "A completes work in 12 days, B in 18 days. They work together for 4 days, then A leaves. In how many days will B finish remaining work?",
        "Total Work = LCM(12, 18) = 36 chocolates. A = 3, B = 2 chocs/day.<br/>"
        "Together in 4 days = 4 × (3 + 2) = 20 chocolates. Remaining = 36 - 20 = 16.<br/>"
        "B finishes in 16 / 2 = <b>8 days</b>!",
        "Using fractions 1/12 + 1/18 leads to fraction arithmetic errors."
    ))
    story.append(Spacer(1, 5))

    story.append(make_trick_box(
        "5.7", "Speed 18-Table & Train Crossing Platform",
        "Train speed conversions and platform crossing problems.",
        "• Speed Conversion Table (Multiples of 18):<br/>"
        "  18 km/h = 5 m/s | 36 km/h = 10 m/s | 54 km/h = 15 m/s | 72 km/h = 20 m/s | 90 km/h = 25 m/s.<br/>"
        "• Crossing Platform: <b>Total Distance = Length of Train + Length of Platform</b>.",
        "A train 180 m long running at 54 km/h crosses a platform in 24 seconds. Find length of platform.",
        "Speed = 54 km/h = 15 m/s. Total distance in 24s = 15 × 24 = 360 m.<br/>"
        "Platform length = 360 - 180 = <b>180 m</b>!",
        "Forgetting to subtract train length from total distance."
    ))
    story.append(Spacer(1, 5))

    story.append(make_trick_box(
        "5.8", "Boats & Streams Speed Formulas",
        "Boat moving downstream (with current) and upstream (against current).",
        "• Downstream Speed D = Distance / Time. Upstream Speed U = Distance / Time.<br/>"
        "• <b>Boat Speed in Still Water (u) = (D + U) / 2</b>.<br/>"
        "• <b>Stream Speed (v) = (D - U) / 2</b>.",
        "Boat travels 36 km downstream in 3h (D = 12 km/h) and 24 km upstream in 4h (U = 6 km/h). Find stream speed.",
        "Stream speed v = (12 - 6) / 2 = 6 / 2 = <b>3 km/h</b> (Option [C])!",
        "Confusing boat speed formula (add) with stream speed formula (subtract)."
    ))
    story.append(Spacer(1, 5))

    story.append(make_trick_box(
        "5.9", "7-44-154 Circle Scaling Benchmark (Mensuration 2D)",
        "Circle radius, circumference, and area calculations.",
        "Benchmark Circle with Radius r = 7 cm:<br/>"
        "• Circumference = 44 cm | Area = 154 cm².<br/>"
        "If radius is multiplied by k:<br/>"
        "• Circumference becomes <b>44 × k</b> | Area becomes <b>154 × k²</b>.",
        "Circumference of a circle is 88 cm. Find its area.",
        "Circumference = 88 = 44 × 2 → scaling factor k = 2 (radius = 14 cm).<br/>"
        "Area = 154 × k² = 154 × 4 = <b>616 cm²</b>!",
        "Applying full πr² formula and computing 22/7 × 14 × 14 takes twice as long."
    ))
    story.append(Spacer(1, 5))

    story.append(make_trick_box(
        "5.10", "Fast Combinations (nC₂) & 'Neither/None' Probability",
        "Drawing 2 balls/cards/items from an urn without replacement.",
        "• <b>nC₂ = n(n - 1) / 2</b> (e.g. 12C₂ = 66, 8C₂ = 28, 10C₂ = 45).<br/>"
        "• For 'neither is X', select both items directly from the remaining non-X items: <b>P = (Non-X)C₂ / Total C₂</b>.",
        "A bag has 6 Red, 4 Blue, 2 Green balls (12 total). Two balls drawn. Probability neither is Blue?",
        "Total outcomes = 12C₂ = (12 × 11)/2 = 66.<br/>"
        "Non-blue balls = 6 Red + 2 Green = 8 balls. Favorable = 8C₂ = (8 × 7)/2 = 28.<br/>"
        "Probability = 28 / 66 = <b>14 / 33</b>!",
        "Calculating P(1st ball not blue) × P(2nd ball not blue) is prone to fraction simplification errors."
    ))
    story.append(Spacer(1, 10))

    # Exam Strategy Checklist
    checklist_data = [
        [Paragraph("<b>🏆 HITENDRASINH'S 3 GOLDEN LAWS FOR 21 NOV 2026 EXAM ROOM</b>", ParagraphStyle('CheckTitle', parent=bold_label_style, fontSize=9, textColor=NAVY, alignment=1))],
        [Paragraph("<b>1. The 20-Second Drop Law:</b> If a question's pattern or method does not click in 20 seconds, SKIP IMMEDIATELY! Do not spend 3 minutes and then skip.", body_style)],
        [Paragraph("<b>2. Zero Tukka Law:</b> Never make a blind guess! Every guess costs -0.25 marks. Skipping preserves your hard-earned positive score.", body_style)],
        [Paragraph("<b>3. Final Click Verification:</b> Before clicking [A]-[E], take 1 deep breath and double check the exact question (e.g. 'A or B?', 'Engineering or Others?').", body_style)],
    ]
    checklist_table = Table(checklist_data, colWidths=[523])
    checklist_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), LIGHT_GOLD),
        ('BOX', (0,0), (-1,-1), 1.5, GOLD_ACCENT),
        ('TOPPADDING', (0,0), (-1,-1), 5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
        ('LEFTPADDING', (0,0), (-1,-1), 8),
        ('RIGHTPADDING', (0,0), (-1,-1), 8),
    ]))
    story.append(checklist_table)

    doc.build(story, canvasmaker=NumberedCanvas)
    print(f"PDF successfully built: {pdf_filename}")

if __name__ == '__main__':
    build_pdf()
