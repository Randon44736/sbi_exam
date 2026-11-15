import os
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.pdfgen import canvas
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, KeepTogether, PageBreak
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
import fitz

class NumberedCanvas(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_header_footer(self._pageNumber, num_pages)
            super().showPage()
        super().save()

    def draw_header_footer(self, page_num, total_pages):
        self.saveState()
        self.setFont("Helvetica", 8)
        self.setFillColor(colors.HexColor("#64748b"))
        # Header
        self.drawString(40, 815, "IBPS CRP RRBs-XV Prelims 2026 | Candidate: Hitendrasinh Solanki | Exam Date: 21 Nov 2026")
        actual_page = 48 + page_num
        self.drawRightString(555, 815, f"Page {actual_page} of 52")
        self.setStrokeColor(colors.HexColor("#e2e8f0"))
        self.setLineWidth(0.5)
        self.line(40, 808, 555, 808)
        # Footer
        self.line(40, 32, 555, 32)
        self.drawString(40, 22, "IBPS CRP RRBs-XV Officer Scale-I Preparation System | Booklet 1: Quantitative Aptitude Expanded Handbook")
        self.drawRightString(555, 22, "Confidential Exam Prep")
        self.restoreState()

def build_expansion_pdf():
    pdf_filename = "expansion_pages.pdf"
    doc = SimpleDocTemplate(
        pdf_filename,
        pagesize=A4,
        leftMargin=40,
        rightMargin=40,
        topMargin=45,
        bottomMargin=45
    )

    styles = getSampleStyleSheet()
    
    # Custom styles
    title_banner = ParagraphStyle(
        'TitleBanner',
        fontName='Helvetica-Bold',
        fontSize=12,
        leading=15,
        textColor=colors.white,
        alignment=1
    )
    
    sec_header = ParagraphStyle(
        'SecHeader',
        fontName='Helvetica-Bold',
        fontSize=10,
        leading=13,
        textColor=colors.HexColor("#0f172a")
    )
    
    body_txt = ParagraphStyle(
        'BodyTxt',
        fontName='Helvetica',
        fontSize=8,
        leading=11,
        textColor=colors.HexColor("#1e293b")
    )

    body_bold = ParagraphStyle(
        'BodyBold',
        fontName='Helvetica-Bold',
        fontSize=8,
        leading=11,
        textColor=colors.HexColor("#0f172a")
    )

    small_txt = ParagraphStyle(
        'SmallTxt',
        fontName='Helvetica',
        fontSize=7.5,
        leading=9.5,
        textColor=colors.HexColor("#334155")
    )

    table_header = ParagraphStyle(
        'TableHeader',
        fontName='Helvetica-Bold',
        fontSize=7.5,
        leading=9.5,
        textColor=colors.HexColor("#0f172a"),
        alignment=1
    )

    story = []

    # =========================================================================
    # PAGE 49: MASTER EXPANDED SYLLABUS DIRECTORY (CHAPTERS 1 TO 21)
    # =========================================================================
    banner_table = Table(
        [[Paragraph("MASTER EXPANDED SYLLABUS DIRECTORY (21 COMPLETE CHAPTERS)", title_banner)]],
        colWidths=[515]
    )
    banner_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#0b2545")),
        ('TOPPADDING', (0,0), (-1,-1), 7),
        ('BOTTOMPADDING', (0,0), (-1,-1), 7),
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
    ]))
    story.append(banner_table)
    story.append(Spacer(1, 8))

    intro_p = Paragraph(
        "<b>OFFICIAL SYLLABUS ARCHITECTURE & EXAM MAPPING:</b> To guarantee selection in IBPS RRB PO Scale-I (Officer Scale-I), "
        "the quantitative preparation is organized into 21 targeted chapters divided into <b>Phase I (Prelims Speed Core: 40 Qs / 20 Min)</b> "
        "and <b>Phase II (Mains Analytical Mastery: 40 Qs / 50 Marks)</b>. Chapters 1–10 establish foundational speed shortcuts, while "
        "Chapters 11–21 deliver advanced arithmetic, modern data interpretation, and complete mathematical coverage.",
        body_txt
    )
    story.append(intro_p)
    story.append(Spacer(1, 6))

    # Master Syllabus Table
    headers = [
        Paragraph("<b>Ch</b>", table_header),
        Paragraph("<b>Chapter Title & Core Focus</b>", table_header),
        Paragraph("<b>Module Category</b>", table_header),
        Paragraph("<b>Exam Tier</b>", table_header),
        Paragraph("<b>Weightage</b>", table_header)
    ]
    
    syllabus_data = [headers]
    rows = [
        ("1", "BODMAS, Fractions, Decimals & Exact Calculation", "Speed Math Foundation", "Prelims", "2-3 Qs"),
        ("2", "Simplification & Rapid Approximation Techniques", "Speed Math (Rapid Scoring)", "Prelims", "5 Qs"),
        ("3", "Missing and Wrong Number Series", "Pattern Recognition", "Prelims/Mains", "5 Qs"),
        ("4", "Quadratic Equations & 4-Way Root Comparison", "Algebraic Inequality", "Prelims", "5 Qs"),
        ("5", "Percentage, Ratio-Proportion, Average & Ages", "Core Arithmetic Base", "Prelims/Mains", "3-4 Qs"),
        ("6", "Profit, Loss, Discount, Simple & Compound Interest", "Commercial Banking Math", "Prelims/Mains", "3-4 Qs"),
        ("7", "Time & Work, Pipes, Speed, Distance, Trains & Boats", "Work & Motion Mechanics", "Prelims/Mains", "4-5 Qs"),
        ("8", "Mixture & Alligation, LCM & HCF, Mensuration 2D/3D", "Applied Arithmetic & Shapes", "Prelims/Mains", "3-4 Qs"),
        ("9", "Data Interpretation (Table, Bar, Line, Pie & Caselet)", "Data Analysis (35% Paper)", "Prelims/Mains", "10-15 Qs"),
        ("10", "Quantity Comparison (Q1 vs Q2) & Data Sufficiency", "Analytical Evaluation", "Prelims/Mains", "5 Qs"),
        ("11", "Number System: Divisibility, Remainders & Factorials", "Number Theory & Properties", "Prelims/Mains", "1-2 Qs"),
        ("12", "Advanced Number Series (Multi-tier, Prime, Alternate)", "Complex Pattern Analysis", "Prelims/Mains", "5 Qs (Mains)"),
        ("13", "Advanced Calculation (Surds, Indices, 1-50 Squares)", "High-Speed Calculation", "Prelims/Mains", "Speed Core"),
        ("14", "Advanced Percentage & Proportion (Elections, Partner)", "Multi-variable Arithmetic", "Prelims/Mains", "2-3 Qs"),
        ("15", "Advanced Average & Ages (Weighted Avg, Replacement)", "Dynamic Group Analysis", "Prelims/Mains", "2 Qs"),
        ("16", "Advanced Time & Work (Men-Women-Children, Wages)", "Efficiency Variation", "Prelims/Mains", "2-3 Qs"),
        ("17", "Advanced Speed, Distance & Motion (Races, Relative)", "Multi-object Kinetics", "Prelims/Mains", "2-3 Qs"),
        ("18", "Advanced Mensuration & Geometry (Recasting, Solids)", "3D Geometric Calculus", "Prelims/Mains", "2 Qs"),
        ("19", "Advanced Data Interpretation (Missing Variables, Radar)", "Complex Multi-graph DI", "Mains Priority", "15-20 Qs"),
        ("20", "Probability and Permutation & Combination (P&C)", "Combinatorics & Chance", "Prelims/Mains", "2-3 Qs"),
        ("21", "Basic Trigonometry & Heights/Distances (Optional)", "Geometric Measurements", "Specialized", "1 Q (Opt)")
    ]

    for ch_num, title, cat, tier, weight in rows:
        syllabus_data.append([
            Paragraph(f"<b>{ch_num}</b>", table_header),
            Paragraph(f"<b>{title}</b>", small_txt),
            Paragraph(cat, small_txt),
            Paragraph(f"<b>{tier}</b>", small_txt),
            Paragraph(weight, small_txt)
        ])

    s_table = Table(syllabus_data, colWidths=[22, 220, 125, 78, 70])
    s_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#f1f5f9")),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor("#cbd5e1")),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('TOPPADDING', (0,0), (-1,-1), 2.2),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2.2),
        ('ALIGN', (0,0), (0,-1), 'CENTER'),
        ('ALIGN', (3,0), (-1,-1), 'CENTER'),
    ]))
    story.append(s_table)
    story.append(PageBreak())

    # =========================================================================
    # PAGE 50: CHAPTER 11: NUMBER SYSTEM (PART 1: DIVISIBILITY, PRIMES, FACTORS)
    # =========================================================================
    ch11_banner = Table(
        [[Paragraph("CHAPTER 11: NUMBER SYSTEM (DIVISIBILITY, PRIMES & FACTORS) — PART 1", title_banner)]],
        colWidths=[515]
    )
    ch11_banner.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#0b2545")),
        ('TOPPADDING', (0,0), (-1,-1), 7),
        ('BOTTOMPADDING', (0,0), (-1,-1), 7),
    ]))
    story.append(ch11_banner)
    story.append(Spacer(1, 7))

    # Core Theory Box
    th_box = [
        [Paragraph("<b>1. Classification of Numbers & Foundational Properties</b>", sec_header)],
        [Paragraph(
            "• <b>Natural Numbers (N):</b> {1, 2, 3, ...} | <b>Whole Numbers (W):</b> {0, 1, 2, 3, ...}<br/>"
            "• <b>Integers (Z):</b> {..., -3, -2, -1, 0, 1, 2, 3, ...}<br/>"
            "• <b>Prime Numbers:</b> Natural numbers > 1 having exactly 2 distinct factors (1 and itself). "
            "First 10 primes: <b>2, 3, 5, 7, 11, 13, 17, 19, 23, 29</b>. (Note: <b>2 is the ONLY even prime!</b> 1 is neither prime nor composite).<br/>"
            "• <b>Co-prime Numbers:</b> Two numbers whose HCF is 1 (e.g., 8 and 15 are coprime, even though neither is prime).<br/>"
            "• <b>Twin Primes:</b> Prime pairs with a difference of 2: (3, 5), (5, 7), (11, 13), (17, 19), (29, 31).",
            body_txt
        )]
    ]
    t1 = Table(th_box, colWidths=[515])
    t1.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#f8fafc")),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor("#cbd5e1")),
        ('TOPPADDING', (0,0), (-1,-1), 5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
    ]))
    story.append(t1)
    story.append(Spacer(1, 7))

    # Divisibility Rules Table
    div_header = [
        Paragraph("<b>Divisor</b>", table_header),
        Paragraph("<b>Mathematical Divisibility Condition & Verification Rule</b>", table_header),
        Paragraph("<b>Rapid Exam Shortcut / Example</b>", table_header)
    ]
    div_rows = [
        ("2, 4, 8, 16", "Last 1, 2, 3, 4 digits divisible by 2, 4, 8, 16 (2ⁿ rule).", "74,832 -> 32 div by 4 (Yes); 832 div by 8 (Yes!)."),
        ("3 and 9", "Sum of all digits is divisible by 3 or 9.", "54,828 -> Sum=27 -> div by 9 and 3 cleanly."),
        ("5 and 10", "Last digit ends in 0 or 5 (for 5); ends in 0 (for 10).", "Instant visual scan in 1 second."),
        ("6", "Number is divisible by BOTH 2 (even) AND 3 (digit sum).", "63,216: Even and sum=18 (div by 3) -> Divisible!"),
        ("7", "Double the last digit and subtract from the remaining truncated number.", "343: 34 - (2x3) = 28 -> 28 is div by 7. (Yes!)."),
        ("11", "<b>Difference between Sum of Odd-Place Digits and Sum of Even-Place Digits is 0 or multiple of 11.</b>", "91,828: Odd=(9+8+8)=25; Even=(1+2)=3. Diff=22 -> Divisible by 11!"),
        ("12, 72, 88", "<b>Co-prime Product Rule:</b> Divisible by 3 & 4 (for 12); 8 & 9 (for 72); 8 & 11 (for 88).", "<b>Super High Yield in IBPS PO missing-digit questions!</b>")
    ]
    div_data = [div_header]
    for d, c, ex in div_rows:
        div_data.append([Paragraph(f"<b>{d}</b>", body_bold), Paragraph(c, small_txt), Paragraph(ex, small_txt)])
    
    t_div = Table(div_data, colWidths=[65, 260, 190])
    t_div.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#f1f5f9")),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor("#cbd5e1")),
        ('TOPPADDING', (0,0), (-1,-1), 3),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3),
        ('ALIGN', (0,0), (0,-1), 'CENTER'),
    ]))
    story.append(t_div)
    story.append(Spacer(1, 7))

    # Factors & Multiples
    fact_box = [
        [Paragraph("<b>2. Total Number of Factors & Prime Factorization Formula</b>", sec_header)],
        [Paragraph(
            "Every composite integer N can be uniquely prime-factored as: <b>N = p<sub>1</sub><sup>a</sup> &times; p<sub>2</sub><sup>b</sup> &times; p<sub>3</sub><sup>c</sup> ...</b><br/>"
            "• <b>Total Factors:</b> <b>Total = (a + 1)(b + 1)(c + 1)...</b><br/>"
            "  <i>Example:</i> Find total factors of 72. Prime factorize: 72 = 2<sup>3</sup> &times; 3<sup>2</sup>.<br/>"
            "  Total factors = (3 + 1)(2 + 1) = 4 &times; 3 = <b>12 factors</b>.<br/>"
            "• <b>Sum of Factors:</b> Sum = [(p<sub>1</sub><sup>a+1</sup> - 1)/(p<sub>1</sub> - 1)] &times; [(p<sub>2</sub><sup>b+1</sup> - 1)/(p<sub>2</sub> - 1)]...<br/>"
            "• <b>Number of Prime Factors:</b> Simply add the exponents: a + b + c = 3 + 2 = 5 prime factors.",
            body_txt
        )]
    ]
    t2 = Table(fact_box, colWidths=[515])
    t2.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#f0fdf4")),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor("#86efac")),
        ('TOPPADDING', (0,0), (-1,-1), 5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
    ]))
    story.append(t2)
    story.append(PageBreak())

    # =========================================================================
    # PAGE 51: CHAPTER 11: NUMBER SYSTEM (PART 2: REMAINDERS, UNIT DIGITS, ZEROS)
    # =========================================================================
    story.append(Table(
        [[Paragraph("CHAPTER 11: NUMBER SYSTEM — PART 2: REMAINDERS, CYCLICITY & FACTORIALS", title_banner)]],
        colWidths=[515],
        style=[('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#0b2545")), ('TOPPADDING', (0,0), (-1,-1), 7), ('BOTTOMPADDING', (0,0), (-1,-1), 7)]
    ))
    story.append(Spacer(1, 7))

    # Remainder Theorem
    rem_box = [
        [Paragraph("<b>1. Remainder Theorem & Negative Remainder Arithmetic</b>", sec_header)],
        [Paragraph(
            "• <b>Distributive Remainder Law:</b> Rem[(A + B) / M] = (Rem[A/M] + Rem[B/M]) mod M; "
            "Rem[(A &times; B) / M] = (Rem[A/M] &times; Rem[B/M]) mod M.<br/>"
            "• <b>Negative Remainder Shortcut:</b> Dividing 14 by 15 leaves +14 or a negative remainder of <b>-1</b>.<br/>"
            "  <i>Power Example:</i> Find remainder of 14<sup>99</sup> &divide; 15.<br/>"
            "  Treat 14 as (-1) mod 15. Then (-1)<sup>99</sup> = -1. Final positive remainder = 15 - 1 = <b>14</b>! (Solved in 3 seconds!).<br/>"
            "• <b>Algebraic Identity Law:</b> (a<sup>n</sup> + b<sup>n</sup>) is always divisible by (a + b) when n is ODD. "
            "(a<sup>n</sup> - b<sup>n</sup>) is always divisible by (a - b) for all n, and divisible by (a + b) when n is EVEN.",
            body_txt
        )]
    ]
    t_rem = Table(rem_box, colWidths=[515])
    t_rem.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#f8fafc")),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor("#cbd5e1")),
        ('TOPPADDING', (0,0), (-1,-1), 5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
    ]))
    story.append(t_rem)
    story.append(Spacer(1, 7))

    # Unit Digit Cyclicity
    cyc_header = [
        Paragraph("<b>Last Digit Base</b>", table_header),
        Paragraph("<b>Cyclicity Pattern & Periodicity</b>", table_header),
        Paragraph("<b>Fast Resolution Algorithm (Power mod 4)</b>", table_header)
    ]
    cyc_rows = [
        ("0, 1, 5, 6", "Period = 1. Always ends in the exact same digit for any positive power.", "5<sup>100</sup> ends in 5; 6<sup>45</sup> ends in 6; 1<sup>99</sup> ends in 1."),
        ("4 and 9", "Period = 2. 4^(odd)=4, 4^(even)=6. 9^(odd)=9, 9^(even)=1.", "4<sup>42</sup>: Power 42 is even -> ends in 6! 9<sup>33</sup>: Power odd -> ends in 9!"),
        ("2, 3, 7, 8", "<b>Period = 4.</b> Divide power by 4. The remainder r gives the effective power (if r=0, use power 4).",
         "Find unit digit of 7<sup>67</sup>: 67 &divide; 4 = Remainder 3.<br/>Effective power = 7<sup>3</sup> = 343 -> <b>Unit digit is 3!</b>")
    ]
    cyc_data = [cyc_header]
    for b, c, al in cyc_rows:
        cyc_data.append([Paragraph(f"<b>{b}</b>", body_bold), Paragraph(c, small_txt), Paragraph(al, small_txt)])
    
    t_cyc = Table(cyc_data, colWidths=[80, 215, 220])
    t_cyc.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#f1f5f9")),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor("#cbd5e1")),
        ('TOPPADDING', (0,0), (-1,-1), 3),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3),
        ('ALIGN', (0,0), (0,-1), 'CENTER'),
    ]))
    story.append(t_cyc)
    story.append(Spacer(1, 7))

    # Factorials & Trailing Zeros
    fact_zero_box = [
        [Paragraph("<b>3. Trailing Zeros in Factorials (Legendre's Formula)</b>", sec_header)],
        [Paragraph(
            "• <b>Mechanism:</b> A trailing zero is created by every 2 &times; 5 pair. In any factorial N!, 2s are plentiful, so "
            "the number of trailing zeros equals the <b>highest power of 5</b> dividing N!.<br/>"
            "• <b>Formula:</b> <b>Number of Trailing Zeros = [N/5] + [N/25] + [N/125] + [N/625] + ...</b> (where [ ] is integer division).<br/>"
            "• <i>Standard Banking Example:</i> Find trailing zeros in 100!.<br/>"
            "  [100/5] = 20; [100/25] = 4; [100/125] = 0.<br/>"
            "  Total trailing zeros = 20 + 4 = <b>24 zeros</b>.",
            body_txt
        )]
    ]
    t_fz = Table(fact_zero_box, colWidths=[515])
    t_fz.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#f0fdf4")),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor("#86efac")),
        ('TOPPADDING', (0,0), (-1,-1), 5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
    ]))
    story.append(t_fz)
    story.append(PageBreak())

    # =========================================================================
    # PAGE 52: CHAPTER 11: WORKED EXAMPLES & FORMULA REVISION SHEET
    # =========================================================================
    story.append(Table(
        [[Paragraph("CHAPTER 11: WORKED PYQ PATTERNS & FORMULA REVISION SHEET", title_banner)]],
        colWidths=[515],
        style=[('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#0b2545")), ('TOPPADDING', (0,0), (-1,-1), 7), ('BOTTOMPADDING', (0,0), (-1,-1), 7)]
    ))
    story.append(Spacer(1, 7))

    # Worked Examples Box
    ex_box = [
        [Paragraph("<b>Verified Previous-Year Exam Models & Step-by-Step Solutions</b>", sec_header)],
        [Paragraph(
            "<b>Model 1 (IBPS PO 72-Divisibility Trap):</b> If the 7-digit number 54x32y4 is divisible by 72, find the value of (x + y).<br/>"
            "• <i>Step 1:</i> 72 = 8 &times; 9 (coprime). For divisibility by 8, last 3 digits '2y4' must be divisible by 8. Testing even digits: 224/8=28 (Yes, y=2) or 264/8=33 (y=6).<br/>"
            "• <i>Step 2:</i> For divisibility by 9, sum of digits (5+4+x+3+2+y+4) = 18 + x + y must be divisible by 9. Hence x + y = 9.<br/>"
            "<b>Answer: x + y = 9</b> (Takes 15 seconds!).<br/><br/>"
            "<b>Model 2 (Unit Digit Product):</b> Find the unit digit of (23<sup>45</sup> &times; 46<sup>78</sup> &times; 77<sup>43</sup>).<br/>"
            "• 3<sup>45</sup>: 45 mod 4 = 1 -> 3<sup>1</sup> = 3. | 6<sup>78</sup>: Powers of 6 always end in 6. | 7<sup>43</sup>: 43 mod 4 = 3 -> 7<sup>3</sup> = 343 (ends in 3).<br/>"
            "• Combined unit digit = 3 &times; 6 &times; 3 = 54 -> <b>Unit digit = 4</b>.<br/><br/>"
            "<b>Model 3 (Consecutive Numbers Sum):</b> The sum of 5 consecutive even numbers is 180. Find the largest number.<br/>"
            "• Shortcut: Average = 180 &divide; 5 = 36 (this is the middle, 3rd number!).<br/>"
            "• The numbers are: 32, 34, <b>36</b>, 38, 40 -> <b>Largest number = 40</b>.",
            body_txt
        )]
    ]
    t_ex = Table(ex_box, colWidths=[515])
    t_ex.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#f8fafc")),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor("#cbd5e1")),
        ('TOPPADDING', (0,0), (-1,-1), 5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
    ]))
    story.append(t_ex)
    story.append(Spacer(1, 7))

    # Formula Cheat Sheet
    rev_header = [
        Paragraph("<b>Formula / Concept</b>", table_header),
        Paragraph("<b>Exact Mathematical Formulation & Speed Clue</b>", table_header)
    ]
    rev_rows = [
        ("Divisibility by 11", "Sum(Odd places) - Sum(Even places) = 0 or multiple of 11."),
        ("Total Factors of N", "N = p<sub>1</sub><sup>a</sup> p<sub>2</sub><sup>b</sup> p<sub>3</sub><sup>c</sup> -> Total Factors = (a + 1)(b + 1)(c + 1)."),
        ("Unit Digit Cyclicity", "Powers of 2, 3, 7, 8 have cyclicity 4. Divide power by 4, use remainder r (r=0 -> 4)."),
        ("Trailing Zeros in N!", "Zeros = [N/5] + [N/25] + [N/125] + ... (powers of 5 count)."),
        ("Sum of First N Numbers", "Sum = n(n + 1) / 2. Sum of first n odd numbers = n<sup>2</sup>. Sum of first n even numbers = n(n + 1)."),
        ("Remainder of Powers", "Use negative remainders: (M - 1)<sup>n</sup> mod M = (-1)<sup>n</sup> mod M.")
    ]
    rev_data = [rev_header]
    for f, c in rev_rows:
        rev_data.append([Paragraph(f"<b>{f}</b>", body_bold), Paragraph(c, small_txt)])
    
    t_rev = Table(rev_data, colWidths=[140, 375])
    t_rev.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#f1f5f9")),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor("#cbd5e1")),
        ('TOPPADDING', (0,0), (-1,-1), 3),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3),
    ]))
    story.append(t_rev)

    # Build PDF
    doc.build(story, canvasmaker=NumberedCanvas)
    print("Expansion pages generated successfully!")

if __name__ == "__main__":
    build_expansion_pdf()
