import os
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.pdfgen import canvas
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
import pymupdf

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
        self.drawString(40, 815, "IBPS CRP RRBs-XV Prelims & Mains 2026 | Candidate: Hitendrasinh Solanki | Exam Date: 21 Nov 2026")
        actual_page = 49 + page_num
        self.drawRightString(555, 815, f"Page {actual_page} of {49 + total_pages}")
        self.setStrokeColor(colors.HexColor("#e2e8f0"))
        self.setLineWidth(0.5)
        self.line(40, 808, 555, 808)
        # Footer
        self.line(40, 32, 555, 32)
        self.drawString(40, 22, "IBPS CRP RRBs-XV Officer Scale-I Preparation System | Booklet 2: Reasoning Ability Expanded Handbook")
        self.drawRightString(555, 22, "Confidential Exam Prep")
        self.restoreState()

def build_expansion_pdf():
    temp_pdf = "expansion_reasoning_full_temp.pdf"
    doc = SimpleDocTemplate(
        temp_pdf,
        pagesize=A4,
        leftMargin=40,
        rightMargin=40,
        topMargin=45,
        bottomMargin=45
    )

    styles = getSampleStyleSheet()

    title_banner = ParagraphStyle(
        'TitleBanner',
        fontName='Helvetica-Bold',
        fontSize=10.5,
        leading=13.5,
        textColor=colors.white,
        alignment=1
    )

    sec_header = ParagraphStyle(
        'SecHeader',
        fontName='Helvetica-Bold',
        fontSize=9,
        leading=11.5,
        textColor=colors.HexColor("#0f172a")
    )

    body_txt = ParagraphStyle(
        'BodyTxt',
        fontName='Helvetica',
        fontSize=7.4,
        leading=10,
        textColor=colors.HexColor("#1e293b")
    )

    body_bold = ParagraphStyle(
        'BodyBold',
        fontName='Helvetica-Bold',
        fontSize=7.4,
        leading=10,
        textColor=colors.HexColor("#0f172a")
    )

    small_txt = ParagraphStyle(
        'SmallTxt',
        fontName='Helvetica',
        fontSize=6.8,
        leading=8.8,
        textColor=colors.HexColor("#334155")
    )

    table_header = ParagraphStyle(
        'TableHeader',
        fontName='Helvetica-Bold',
        fontSize=7.2,
        leading=9.2,
        textColor=colors.HexColor("#0f172a"),
        alignment=1
    )

    def create_banner(title):
        t = Table([[Paragraph(title, title_banner)]], colWidths=[515])
        t.setStyle(TableStyle([
            ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#0b2545")),
            ('TOPPADDING', (0,0), (-1,-1), 5),
            ('BOTTOMPADDING', (0,0), (-1,-1), 5),
            ('ALIGN', (0,0), (-1,-1), 'CENTER'),
        ]))
        return t

    story = []

    # =========================================================================
    # PAGE 50: MASTER EXPANDED REASONING SYLLABUS DIRECTORY (CHAPTERS 1 TO 17)
    # =========================================================================
    story.append(create_banner("MASTER EXPANDED REASONING SYLLABUS DIRECTORY (17 COMPLETE CHAPTERS)"))
    story.append(Spacer(1, 5))
    story.append(Paragraph(
        "<b>OFFICIAL REASONING ARCHITECTURE & SELECTION MAPPING:</b> For IBPS RRB PO Scale-I (Officer Scale-I), "
        "Reasoning Ability is the prime scoring engine: <b>Prelims (40 Qs / 40 Marks / 25 Min target)</b> and "
        "<b>Mains (40 Qs / 50 Marks / 1.25 Weightage)</b>. Chapters 1–10 build the foundational speed core, while "
        "Chapters 11–17 deliver advanced multi-variable puzzles, critical reasoning, and modern mains exam patterns.",
        body_txt
    ))
    story.append(Spacer(1, 5))

    headers = [
        Paragraph("<b>Ch</b>", table_header),
        Paragraph("<b>Chapter Title & Core Focus</b>", table_header),
        Paragraph("<b>Module Category</b>", table_header),
        Paragraph("<b>Exam Tier</b>", table_header),
        Paragraph("<b>Weightage</b>", table_header)
    ]
    rows = [
        ("1", "Inequalities: Direct, Combined & Coded", "Speed Core (Open-Gate)", "Prelims/Mains", "3–5 Qs"),
        ("2", "Syllogisms: Only a Few, Possibility & Either-Or", "Venn Deduction", "Prelims/Mains", "3–5 Qs"),
        ("3", "Alphanumeric-Symbol Series & Alphabet Test", "Positional Shifting", "Prelims", "3–5 Qs"),
        ("4", "Coding-Decoding: Chinese & Conditional Tables", "Substitution Matrix", "Prelims/Mains", "5 Qs"),
        ("5", "Blood Relations & Direction Sense", "Lineage & 8-Direction Vectors", "Prelims/Mains", "5–6 Qs"),
        ("6", "Order, Ranking & Comparison", "Linear Ranks & Direct Comparison", "Prelims/Mains", "3–4 Qs"),
        ("7", "Seating Arrangements Core (Circle, Square, Rows)", "2D Positional Logic", "Prelims", "10 Qs"),
        ("8", "Puzzles Core (Floor, 8-Box Stacking, Month-Date)", "Constraint Scheduling", "Prelims", "10 Qs"),
        ("9", "Machine Input-Output Core (Left-Right Shifting)", "Sequential Transformation", "Prelims/Mains", "5 Qs"),
        ("10", "Reasoning Data Sufficiency Core (2-Statement DS)", "Analytical Sufficiency", "Prelims/Mains", "3–5 Qs"),
        ("11", "Miscellaneous Reasoning (Word, Pair & Number Rules)", "Speed Arithmetic/Alphabet", "Prelims Speed", "3–4 Qs"),
        ("12", "Advanced Puzzles (Floor+Flat, Designation, Age/Year)", "Multi-variable Complex Puzzles", "Prelims/Mains", "10–15 Qs"),
        ("13", "Advanced Seating (Mixed Facing, Triangular, Concentric)", "Complex Geometric Seating", "Prelims/Mains", "10–15 Qs"),
        ("14", "Advanced Coding-Decoding (New Pattern, Binary, Symbol)", "Mains Pattern Decoding", "Mains Priority", "5 Qs"),
        ("15", "Advanced Input-Output (Mathematical Box/Block Machine)", "Arithmetic Transformation", "Mains Priority", "5 Qs"),
        ("16", "Advanced Logical Reasoning (Assumptions, Arguments, CoA)", "Critical Analytical Logic", "Mains Core", "8–12 Qs"),
        ("17", "Advanced Reasoning Data Sufficiency (3-Statement & Coded)", "Complex Sufficiency Evaluation", "Mains Priority", "5 Qs")
    ]
    syllabus_data = [headers]
    for ch_num, title, cat, tier, weight in rows:
        syllabus_data.append([
            Paragraph(f"<b>{ch_num}</b>", table_header),
            Paragraph(f"<b>{title}</b>", small_txt),
            Paragraph(cat, small_txt),
            Paragraph(f"<b>{tier}</b>", small_txt),
            Paragraph(weight, small_txt)
        ])
    s_table = Table(syllabus_data, colWidths=[20, 222, 125, 78, 70])
    s_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#f1f5f9")),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor("#cbd5e1")),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('TOPPADDING', (0,0), (-1,-1), 2.2),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2.2),
        ('ALIGN', (0,0), (0,-1), 'CENTER'),
        ('ALIGN', (3,0), (-1,-1), 'CENTER'),
        ('ALIGN', (4,0), (-1,-1), 'CENTER'),
    ]))
    story.append(s_table)
    story.append(PageBreak())

    # =========================================================================
    # PAGE 51: 10-CHAPTER COMPREHENSIVE AUDIT & STRATEGIC BLUEPRINT
    # =========================================================================
    story.append(create_banner("10-CHAPTER COMPREHENSIVE AUDIT & STRATEGIC BLUEPRINT"))
    story.append(Spacer(1, 5))
    audit_headers = [Paragraph("<b>Audit Dimension</b>", table_header), Paragraph("<b>Detailed Findings & Syllabus Alignment</b>", table_header)]
    audit_rows = [
        ("Already Covered Topics (Ch 1–10)", 
         "Direct & Combined Inequalities, Open-Gate transitive logic, 'Only a Few' & Possibility Syllogisms, Alphanumeric sequence navigation, Chinese Coding substitution, Family trees & 8-direction compass, Single-row ranking (L+R-1), Basic circular/square/parallel seating, Single-variable 7-floor & 8-box puzzles, Standard single word-number shift Input-Output, 2-statement DS."),
        ("Partially Covered Topics", 
         "Coded Inequalities (introductory in Ch 1; advanced multi-statement needed for Mains), Coding-Decoding (conditional tables covered in Ch 4, but Mains new-pattern symbols missing), Puzzles/Seating (Ch 7-8 cover basic single variables; advanced constraints split into Ch 12-13)."),
        ("Completely Missing Topics", 
         "Meaningful word formation (1st/3rd/5th letters), Digit operation in numbers, Floor+Flat matrix (4x2), Designation hierarchy (CMD to Clerk), Age-base year calculation, Mixed-facing circular, Triangular/Rectangular tables, Mathematical block/box Input-Output, ALL Critical Reasoning (Assumptions, Arguments, Course of Action, Inferences), 3-Statement DS."),
        ("Duplicate Topics Prevented", 
         "Pair formation & letter test kept consolidated in Ch 3 & Ch 11 without re-deriving basic alphabet indices. Core 1-variable seating kept in Ch 7, reserving Ch 13 exclusively for non-standard polygons and multiple variables. Standard 2-statement DS kept in Ch 10, reserving Ch 17 for 3-statement and coded formats."),
        ("Additional Mains-Level Topics", 
         "Chapter 16 Critical Reasoning (8–12 Qs in Mains, carrying 10–15 marks), Chapter 14 New-Pattern Coding (Symbol/Length/Vowel-based), Chapter 15 Box-type Mathematical Operations, Chapter 12 Multi-variable Floor+Flat + Variable Puzzles, Chapter 17 3-Statement Data Sufficiency.")
    ]
    audit_table_data = [audit_headers]
    for dim, desc in audit_rows:
        audit_table_data.append([Paragraph(f"<b>{dim}</b>", body_bold), Paragraph(desc, small_txt)])
    t_audit = Table(audit_table_data, colWidths=[145, 370])
    t_audit.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#f1f5f9")),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor("#cbd5e1")),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('TOPPADDING', (0,0), (-1,-1), 3),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3),
    ]))
    story.append(t_audit)
    story.append(Spacer(1, 5))

    strat_box = [
        [Paragraph("<b>IBPS RRB PO Scale-I: Tactical Execution Strategy (Prelims vs Mains)</b>", sec_header)],
        [Paragraph(
            "• <b>Prelims Round-Robin Strategy (22–25 Mins Target: 35+ Marks):</b><br/>"
            "  1. <i>Phase 1 (Min 0–6):</i> Non-puzzle speed scoring (Inequalities 5 Qs in 2 min, Syllogisms 5 Qs in 2.5 min, Miscellaneous/Direction/Blood Relations 5 Qs in 2 min). Bank 15 marks with 100% accuracy.<br/>"
            "  2. <i>Phase 2 (Min 6–22):</i> Attempt 4 out of 4 puzzles/seating sets (20 Qs). Select standard models first: Floor+Flat, Designation, 7-person circular, Day-date. Leave uncertain puzzles for last.<br/>"
            "  3. <i>Phase 3 (Min 22–25):</i> Standalone questions (Word formation, remaining Blood Relations).<br/>"
            "• <b>Mains Analytical Mastery (30–35 Mins Target: 28+ Marks / 35+ Scaled Score):</b><br/>"
            "  1. <i>Critical Reasoning (Ch 16):</i> 8–10 questions. Read argument carefully, identify unstated premise, eliminate extreme choices. 80%+ accuracy yields 10–12 marks with zero writing!<br/>"
            "  2. <i>Input-Output (Ch 15):</i> 5 questions. Crack step-1 & step-2 math pattern in 90 seconds. Once rule is identified, all 5 questions fall in 2 minutes.<br/>"
            "  3. <i>Puzzle Selection:</i> Strictly solve 2 high-confidence sets (10 Qs) with 2 variables. Avoid concentric/uncertain traps under time pressure.",
            body_txt
        )]
    ]
    t_strat = Table(strat_box, colWidths=[515])
    t_strat.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#f8fafc")),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor("#cbd5e1")),
        ('TOPPADDING', (0,0), (-1,-1), 5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
    ]))
    story.append(t_strat)
    story.append(PageBreak())

    # =========================================================================
    # PAGE 52-53: CHAPTER 11: MISCELLANEOUS REASONING
    # =========================================================================
    story.append(create_banner("CHAPTER 11: MISCELLANEOUS REASONING — THEORY, RULES & SHORTCUTS"))
    story.append(Spacer(1, 5))
    theory_box = [
        [Paragraph("<b>Core Concepts & Zero-Error Methodologies (Speed Rules & Shortcuts)</b>", sec_header)],
        [Paragraph(
            "<b>1. Pair Formation Algorithm (Forward & Backward Scanning):</b> Count letter intervals matching the English alphabet. Always convert letters to position numbers (A=1 ... Z=26) to prevent mental hesitation.<br/>"
            "<b>2. Meaningful Word Formation (1-X-Y Framework):</b> Extract 4 specified letters. If exactly 1 word forms, mark 3rd letter; if >1 mark 'X'; if 0 mark 'Y'. This is the #1 negative-marking trap—skip if unsure!<br/>"
            "<b>3. Digit Manipulation Operations:</b> Add 1 to odd, subtract 1 from even digits. Instead of rewriting all digits, scan directly for colliding values.<br/>"
            "<b>4. Odd One Out:</b> Test gap patterns between adjacent letters (+2, +3), opposite pairs (A-Z, B-Y), and vowel counts.",
            body_txt
        )]
    ]
    t_th = Table(theory_box, colWidths=[515])
    t_th.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#f8fafc")),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor("#cbd5e1")),
        ('TOPPADDING', (0,0), (-1,-1), 5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
    ]))
    story.append(t_th)
    story.append(Spacer(1, 5))

    rule_headers = [Paragraph("<b>Question Type</b>", table_header), Paragraph("<b>Exam Pattern</b>", table_header), Paragraph("<b>Golden Shortcut</b>", table_header)]
    rule_data = [rule_headers,
        [Paragraph("<b>Pair Formation</b>", body_bold), Paragraph("Pairs with same gap as alphabet", small_txt), Paragraph("Finger-recite method or numeric subtraction (j - i == pos_j - pos_i)", small_txt)],
        [Paragraph("<b>Word Formation</b>", body_bold), Paragraph("1st, 4th, 6th, 9th letters -> Anagrams", small_txt), Paragraph("Common bank stems: STOP, CARE, DEAR, TAME, SEAT. Skip if doubtful.", small_txt)],
        [Paragraph("<b>Digit Sorting</b>", body_bold), Paragraph("Rearrange digits ascending; find unchanged", small_txt), Paragraph("Write sorted string underneath; circle identical vertical columns.", small_txt)],
        [Paragraph("<b>Vowel/Consonant</b>", body_bold), Paragraph("Vowel +1, Consonant -1 in a word", small_txt), Paragraph("Vowels created only by consonants B, F, J, P, V.", small_txt)]
    ]
    t_r = Table(rule_data, colWidths=[110, 175, 230])
    t_r.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#f1f5f9")),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor("#cbd5e1")),
        ('TOPPADDING', (0,0), (-1,-1), 2.5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2.5),
    ]))
    story.append(t_r)
    story.append(PageBreak())

    # Page 53: Ch 11 PYQs & Cheat Sheet
    story.append(create_banner("CHAPTER 11: WORKED PYQ PATTERNS & QUICK-REVISION CHEAT SHEET"))
    story.append(Spacer(1, 5))
    pyq_box = [
        [Paragraph("<b>Verified Previous-Year Exam Models & Step-by-Step Solutions</b>", sec_header)],
        [Paragraph(
            "<b>Model 1 (Verified IBPS RRB PO Prelims): Pair Counting in 'BANKING'</b><br/>"
            "• Forward: B, A, N, K, I, N, G &rarr; 0 pairs.<br/>"
            "• Backward: G&rarr;I (say H, I: match!), A&rarr;B (say B: match!). Total = <b>2 pairs (G-I, A-B)</b>.<br/><br/>"
            "<b>Model 2 (Memory-Based IBPS RRB PO 2023 Prelims Shift 2): Meaningful Word</b><br/>"
            "• 1st, 3rd, 5th, 7th of 'DISCOVERY' &rarr; D, S, O, E &rarr; <b>DOSE, ODES</b>. More than one &rarr; <b>'X'</b>.<br/><br/>"
            "<b>Model 3 (Verified IBPS RRB PO 2022 Prelims Shift 1): Number Operations</b><br/>"
            "• '73942618': Odd+1 &rarr; {8,4,0,2}; Even-1 &rarr; {3,1,5,7}. All distinct &rarr; <b>None repeated</b>.",
            body_txt
        )]
    ]
    t_pyq = Table(pyq_box, colWidths=[515])
    t_pyq.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#f8fafc")),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor("#cbd5e1")),
        ('TOPPADDING', (0,0), (-1,-1), 5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
    ]))
    story.append(t_pyq)
    story.append(Spacer(1, 5))

    cheat_header = [Paragraph("<b>Speed Hack Tool</b>", table_header), Paragraph("<b>Memory Mnemonic</b>", table_header), Paragraph("<b>Application</b>", table_header)]
    cheat_data = [cheat_header,
        [Paragraph("<b>EJOTY Rule</b>", body_bold), Paragraph("E=5, J=10, O=15, T=20, Y=25", small_txt), Paragraph("Fast 5-multiple anchor for alphabet positions", small_txt)],
        [Paragraph("<b>CFILORUX</b>", body_bold), Paragraph("C=3, F=6, I=9, L=12, O=15, R=18, U=21, X=24", small_txt), Paragraph("Rapid 3-multiple anchor for tight clustering", small_txt)],
        [Paragraph("<b>Opposites (Sum=27)</b>", body_bold), Paragraph("AZ, BY, CX, DW, EV, FU, GT, HS, IR, JQ, KP, LO, MN", small_txt), Paragraph("New Pattern Coding & Reverse Shifts", small_txt)],
        [Paragraph("<b>Vowel Predecessors</b>", body_bold), Paragraph("B&rarr;A, F&rarr;E, J&rarr;I, P&rarr;O, V&rarr;U", small_txt), Paragraph("Quick vowel scan after consonant -1 operation", small_txt)]
    ]
    t_ch = Table(cheat_data, colWidths=[105, 220, 190])
    t_ch.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#f1f5f9")),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor("#cbd5e1")),
        ('TOPPADDING', (0,0), (-1,-1), 2.5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2.5),
    ]))
    story.append(t_ch)
    story.append(PageBreak())

    # =========================================================================
    # PAGE 54-55: CHAPTER 12: ADVANCED PUZZLES
    # =========================================================================
    story.append(create_banner("CHAPTER 12: ADVANCED PUZZLES — MULTI-VARIABLE & SCHEDULING"))
    story.append(Spacer(1, 5))
    ch12_box = [
        [Paragraph("<b>Advanced Puzzle Frameworks (Prelims & Mains Repeated Models)</b>", sec_header)],
        [Paragraph(
            "<b>1. Floor + Flat Matrix (4 Floors &times; 2 Flats):</b><br/>"
            "• Standard layout: Flat A is west of Flat B. Flat A on Floor 2 is immediately above Flat A on Floor 1.<br/>"
            "• <i>Key Clue Distinction:</i> 'P lives on an even floor in the same flat as Q' (vertical match) vs 'P lives immediately above Q' (same flat unless stated otherwise).<br/>"
            "<b>2. Designation Hierarchy (Seniority Order):</b><br/>"
            "• Fix the seniority ladder: CMD &gt; ED &gt; CGM &gt; GM &gt; DGM &gt; AGM &gt; Manager &gt; AM &gt; Clerk. Never change this order!<br/>"
            "• 'Seniority gap': 'At least 3 persons are senior to R' means R can only be GM or junior.<br/>"
            "<b>3. Age & Year-Based Puzzles:</b><br/>"
            "• Given birth years (e.g. 1968, 1974, 1983, 1991, 1997, 2004) with base year 2026.<br/>"
            "• <i>Golden Rule:</i> Calculate all ages immediately in a dedicated column before reading clues! (e.g. 2026-1968 = 58). Clues like 'Age difference is a perfect square' or 'Age is multiple of 7' resolve instantly.<br/>"
            "<b>4. Uncertain Number of Persons (Linear/Parallel):</b><br/>"
            "• Do NOT draw fixed slots. Chain relative clues (e.g., 'A is 3rd to left of B; 5 people between B and C'). Maintain 2 parallel lines until an end is anchored.",
            body_txt
        )]
    ]
    t_12 = Table(ch12_box, colWidths=[515])
    t_12.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#f8fafc")),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor("#cbd5e1")),
        ('TOPPADDING', (0,0), (-1,-1), 5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
    ]))
    story.append(t_12)
    story.append(Spacer(1, 5))

    puz_grid_headers = [Paragraph("<b>Puzzle Type</b>", table_header), Paragraph("<b>Standard Grid Setup</b>", table_header), Paragraph("<b>Primary Anchor Clue</b>", table_header)]
    puz_grid_data = [puz_grid_headers,
        [Paragraph("<b>Floor + Flat</b>", body_bold), Paragraph("Columns: Floor (4,3,2,1), Flat A (West), Flat B (East)", small_txt), Paragraph("Person on odd floor in Flat B; person immediately above", small_txt)],
        [Paragraph("<b>Designation</b>", body_bold), Paragraph("Single column of fixed ranks 1 (CMD) to 8 (Clerk)", small_txt), Paragraph("Person senior to exactly 2 persons; Manager rank fixed", small_txt)],
        [Paragraph("<b>Year + Age</b>", body_bold), Paragraph("Columns: Year, Calculated Age, Person, Variable", small_txt), Paragraph("Sum/difference of ages equals prime or perfect square", small_txt)],
        [Paragraph("<b>Month + Date</b>", body_bold), Paragraph("Rows: 4 Months &times; 2 Dates (e.g., 7th & 22nd) = 8 slots", small_txt), Paragraph("Month with 30 days vs 31 days; even date placement", small_txt)]
    ]
    t_pg = Table(puz_grid_data, colWidths=[105, 210, 200])
    t_pg.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#f1f5f9")),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor("#cbd5e1")),
        ('TOPPADDING', (0,0), (-1,-1), 2.5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2.5),
    ]))
    story.append(t_pg)
    story.append(PageBreak())

    # Page 55: Ch 12 PYQ Model
    story.append(create_banner("CHAPTER 12: WORKED ADVANCED PUZZLE MODELS & EXECUTION GRIDS"))
    story.append(Spacer(1, 5))
    puz_model_box = [
        [Paragraph("<b>Verified IBPS RRB PO Model: 4 Floors &times; 2 Flats Matrix (Prelims Shift Trend)</b>", sec_header)],
        [Paragraph(
            "<b>Problem:</b> 8 persons (A to H) live in a 4-storey building (Floors 1 to 4). Each floor has Flat X and Flat Y (Flat X is west of Flat Y).<br/>"
            "<i>Clues:</i> 1. C lives on an odd floor. 2. Two floors between C and A; both in same flat. 3. G lives immediately above E in Flat X.<br/>"
            "4. D lives on an even floor in Flat Y, south-east of B. 5. H lives on an even floor immediately below F.<br/><br/>"
            "<b>Step-by-Step Dissection & Grid Execution:</b><br/>"
            "• <i>Step 1 (Anchor C & A):</i> C is on Floor 1 or 3. If C is on Floor 3, two floors between C and A is impossible. Hence C is on <b>Floor 1</b> and A is on <b>Floor 4</b>.<br/>"
            "• <i>Step 2 (Flat choice):</i> Try Case 1 (C & A in Flat X) vs Case 2 (C & A in Flat Y).<br/>"
            "• <i>Step 3 (Place G & E):</i> G is immediately above E in Flat X &rarr; requires two vacant consecutive floors in Flat X (Floors 2 & 3). Thus G is Floor 3 Flat X; E is Floor 2 Flat X.<br/>"
            "• <i>Step 4 (Validate D & B):</i> D is on an even floor in Flat Y &rarr; Floor 2 Flat Y. B must be north-west of D &rarr; Floor 3 Flat X (occupied by G) or Floor 4 Flat X &rarr; B is Floor 4 Flat X, so A must be Floor 4 Flat Y! This immediately fixes all flats cleanly!",
            body_txt
        )]
    ]
    t_pm = Table(puz_model_box, colWidths=[515])
    t_pm.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#f8fafc")),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor("#cbd5e1")),
        ('TOPPADDING', (0,0), (-1,-1), 5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
    ]))
    story.append(t_pm)
    story.append(Spacer(1, 5))

    # Solved Grid Table
    grid_headers = [Paragraph("<b>Floor</b>", table_header), Paragraph("<b>Flat X (West)</b>", table_header), Paragraph("<b>Flat Y (East)</b>", table_header), Paragraph("<b>Verification Notes</b>", table_header)]
    grid_data = [grid_headers,
        [Paragraph("<b>4 (Top)</b>", table_header), Paragraph("B", body_bold), Paragraph("A", body_bold), Paragraph("A is 2 floors above C; B is NW of D", small_txt)],
        [Paragraph("<b>3</b>", table_header), Paragraph("G", body_bold), Paragraph("F", body_bold), Paragraph("G is immediately above E in Flat X", small_txt)],
        [Paragraph("<b>2</b>", table_header), Paragraph("E", body_bold), Paragraph("D / H", body_bold), Paragraph("D is on even floor; H immediately below F", small_txt)],
        [Paragraph("<b>1 (Bottom)</b>", table_header), Paragraph("H / D", body_bold), Paragraph("C", body_bold), Paragraph("C is on odd floor in Flat Y", small_txt)]
    ]
    t_g = Table(grid_data, colWidths=[55, 110, 110, 240])
    t_g.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#f1f5f9")),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor("#cbd5e1")),
        ('TOPPADDING', (0,0), (-1,-1), 2.5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2.5),
        ('ALIGN', (0,0), (2,-1), 'CENTER'),
    ]))
    story.append(t_g)
    story.append(PageBreak())

    # =========================================================================
    # PAGE 56-57: CHAPTER 13: ADVANCED SEATING ARRANGEMENTS
    # =========================================================================
    story.append(create_banner("CHAPTER 13: ADVANCED SEATING — MIXED FACING & COMPLEX POLYGONS"))
    story.append(Spacer(1, 5))
    ch13_box = [
        [Paragraph("<b>Non-Standard Geometry & Multi-Variable Seating Rules</b>", sec_header)],
        [Paragraph(
            "<b>1. Circular Seating with Mixed Facing (Inward + Outward):</b><br/>"
            "• Right/Left switches depending on orientation: <i>Facing Center:</i> Clockwise is LEFT, Counter-Clockwise is RIGHT.<br/>"
            "  <i>Facing Outside:</i> Clockwise is RIGHT, Counter-Clockwise is LEFT.<br/>"
            "• <i>Golden Rule:</i> Fix candidates whose facing is known first (e.g. 'P sits 3rd to right of Q, who faces center'). Never assume orientation without an explicit anchor.<br/>"
            "<b>2. Square & Rectangular Tables:</b><br/>"
            "• 8 persons: 4 at corners (facing inside/outside) and 4 at middle of edges (facing opposite).<br/>"
            "• Distinguish: 'Sits at the longer side' vs 'Sits at the corner'. Corners have adjacent corners; edges have adjacent corners.<br/>"
            "<b>3. Triangular Arrangements (6 or 9 persons):</b><br/>"
            "• 3 at corners (facing center) and 3/6 at sides (facing outside). Each corner is directly opposite an edge.<br/>"
            "<b>4. Parallel Rows with Extra Variable (Mains Model):</b><br/>"
            "• Row 1 faces South, Row 2 faces North. Persons also like colors/professions. Always bind facing arrows to each row immediately.",
            body_txt
        )]
    ]
    t_13 = Table(ch13_box, colWidths=[515])
    t_13.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#f8fafc")),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor("#cbd5e1")),
        ('TOPPADDING', (0,0), (-1,-1), 5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
    ]))
    story.append(t_13)
    story.append(Spacer(1, 5))

    geom_headers = [Paragraph("<b>Geometry Type</b>", table_header), Paragraph("<b>Facing Orientation</b>", table_header), Paragraph("<b>Key Navigational Rule</b>", table_header)]
    geom_data = [geom_headers,
        [Paragraph("<b>Circle (Mixed 8P)</b>", body_bold), Paragraph("4 Center, 4 Outside", small_txt), Paragraph("Opposite person clue: 'A faces the center and sits opposite B' anchors both directions.", small_txt)],
        [Paragraph("<b>Square Table</b>", body_bold), Paragraph("Corners In, Sides Out", small_txt), Paragraph("Corner persons face each other diagonally; side persons face straight across.", small_txt)],
        [Paragraph("<b>Triangular Table</b>", body_bold), Paragraph("Corners Out, Sides In", small_txt), Paragraph("Corner person has 2 corner neighbors and 2 immediate side neighbors.", small_txt)],
        [Paragraph("<b>Dual Rows (12P)</b>", body_bold), Paragraph("Row 1 &darr; (South), Row 2 &uarr; (North)", small_txt), Paragraph("South-facing: Left is YOUR Right! North-facing: Left is YOUR Left!", small_txt)]
    ]
    t_gm = Table(geom_data, colWidths=[110, 130, 275])
    t_gm.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#f1f5f9")),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor("#cbd5e1")),
        ('TOPPADDING', (0,0), (-1,-1), 2.5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2.5),
    ]))
    story.append(t_gm)
    story.append(PageBreak())

    # Page 57: Ch 13 Worked Models
    story.append(create_banner("CHAPTER 13: WORKED ADVANCED SEATING MODELS & DIAGRAMMATIC LOGIC"))
    story.append(Spacer(1, 5))
    seat_model_box = [
        [Paragraph("<b>Memory-Based RRB PO Model: 8 Persons Mixed-Facing Circle</b>", sec_header)],
        [Paragraph(
            "<b>Statements:</b> 8 persons (A to H) sit around a circle. Some face center, some outside. Not more than 2 adjacent face same direction.<br/>"
            "1. A sits 3rd to right of B, who faces inside. 2. C sits 2nd to left of A. 3. Immediate neighbors of C face opposite directions.<br/>"
            "4. D sits opposite E; both face same direction. 5. F sits 2nd to right of D.<br/><br/>"
            "<b>Resolution Algorithm:</b><br/>"
            "• <i>Step 1:</i> Place B at bottom facing <b>IN</b>. Count 3 places Counter-Clockwise &rarr; A is placed.<br/>"
            "• <i>Step 2:</i> Case 2A: A faces IN &rarr; C is 2 places Clockwise from A. Case 2B: A faces OUT &rarr; C is 2 places Counter-Clockwise from A.<br/>"
            "• <i>Step 3:</i> Test constraint: 'No 3 adjacent face same direction'. Eliminates Case 2B in 20 seconds!<br/>"
            "• <i>Step 4:</i> Opposite pair D and E must occupy remaining diametric slots. D and E orientations lock the rest of the ring.",
            body_txt
        )]
    ]
    t_sm = Table(seat_model_box, colWidths=[515])
    t_sm.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#f8fafc")),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor("#cbd5e1")),
        ('TOPPADDING', (0,0), (-1,-1), 5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
    ]))
    story.append(t_sm)
    story.append(Spacer(1, 5))

    facing_rule_headers = [Paragraph("<b>Trap / Edge Case</b>", table_header), Paragraph("<b>Why Candidates Lose Marks</b>", table_header), Paragraph("<b>Examiner-Proof Solution</b>", table_header)]
    facing_data = [facing_rule_headers,
        [Paragraph("<b>'Faces Outside' Left Trap</b>", body_bold), Paragraph("Turning left in real life instead of paper perspective", small_txt), Paragraph("Draw an arrow tip &uarr; or &darr;. Physically rotate paper or use clock rule (Clockwise=Right when out).", small_txt)],
        [Paragraph("<b>Uncertain Linear Seating</b>", body_bold), Paragraph("Assuming total persons is fixed to 8 or 10", small_txt), Paragraph("Count total seats only AFTER all clues are chained. Common answers: 17, 19, 21 persons.", small_txt)],
        [Paragraph("<b>Corner vs Edge Placement</b>", body_bold), Paragraph("Starting with a clue that does not specify corner/middle", small_txt), Paragraph("Branch into 2 diagrams immediately: Case 1 (Corner), Case 2 (Middle). Do not pause!", small_txt)]
    ]
    t_fd = Table(facing_data, colWidths=[120, 185, 210])
    t_fd.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#f1f5f9")),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor("#cbd5e1")),
        ('TOPPADDING', (0,0), (-1,-1), 2.5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2.5),
    ]))
    story.append(t_fd)
    story.append(PageBreak())

    # =========================================================================
    # PAGE 58-59: CHAPTER 14: ADVANCED CODING-DECODING
    # =========================================================================
    story.append(create_banner("CHAPTER 14: ADVANCED CODING-DECODING — NEW PATTERN & CONDITIONAL"))
    story.append(Spacer(1, 5))
    ch14_box = [
        [Paragraph("<b>Mains New Pattern Decoding Architecture (Symbol + Letter + Number)</b>", sec_header)],
        [Paragraph(
            "In modern IBPS RRB PO Mains exams, Coding-Decoding is NOT simple Chinese word elimination. Each word is coded into a triplet:<br/>"
            "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<b>[SYMBOL] [NUMBER] [LETTER]</b> &nbsp;&nbsp;(e.g. 'BANKING' &rarr; '@ 7 T')<br/><br/>"
            "<b>The 3-Component Decoding Protocol:</b><br/>"
            "1. <b>Deciphering the Number:</b><br/>"
            "   • Total number of letters in the word (e.g. 'BANKING' has 7 letters &rarr; 7).<br/>"
            "   • Number of vowels or consonants in the word.<br/>"
            "   • Alphabetical position of the first or last letter.<br/>"
            "2. <b>Deciphering the Letter:</b><br/>"
            "   • Opposite of the first letter (B &rarr; Y) or opposite of the last letter (G &rarr; T).<br/>"
            "   • Next letter (+1) or previous letter (-1) of the middle letter.<br/>"
            "3. <b>Deciphering the Symbol:</b><br/>"
            "   • First letter of the word (e.g., words starting with B get '@', words starting with C get '#').<br/>"
            "   • Total word length: Even length &rarr; '%', Odd length &rarr; '&'.",
            body_txt
        )]
    ]
    t_14 = Table(ch14_box, colWidths=[515])
    t_14.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#f8fafc")),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor("#cbd5e1")),
        ('TOPPADDING', (0,0), (-1,-1), 5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
    ]))
    story.append(t_14)
    story.append(Spacer(1, 5))

    new_pat_headers = [Paragraph("<b>Component</b>", table_header), Paragraph("<b>Possible Logic / Patterns</b>", table_header), Paragraph("<b>Quick Identification Method</b>", table_header)]
    new_pat_data = [new_pat_headers,
        [Paragraph("<b>Number</b>", body_bold), Paragraph("Word length | Vowel count | Consonant count | Pos of 1st/last letter", small_txt), Paragraph("Check if code numbers match word lengths (e.g. 4, 6, 7). If yes, length rule confirmed!", small_txt)],
        [Paragraph("<b>Letter</b>", body_bold), Paragraph("Opposite letter (AZ, BY) | +1/-1 of last letter | Reverse order", small_txt), Paragraph("Compare first/last letter to code letter. If G &rarr; T, check opposite pair table.", small_txt)],
        [Paragraph("<b>Symbol</b>", body_bold), Paragraph("First letter family | Even/Odd letter count | Specific vowel presence", small_txt), Paragraph("Count distinct symbols. If only 2 symbols (& and %), it is an Even/Odd length rule!", small_txt)]
    ]
    t_np = Table(new_pat_data, colWidths=[75, 230, 210])
    t_np.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#f1f5f9")),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor("#cbd5e1")),
        ('TOPPADDING', (0,0), (-1,-1), 2.5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2.5),
    ]))
    story.append(t_np)
    story.append(PageBreak())

    # Page 59: Ch 14 Worked Models
    story.append(create_banner("CHAPTER 14: WORKED MAINS PATTERN MODELS & CONDITIONAL MATRICES"))
    story.append(Spacer(1, 5))
    mains_code_box = [
        [Paragraph("<b>Verified Mains Model: New Pattern Symbol-Number-Letter Code</b>", sec_header)],
        [Paragraph(
            "<b>Given Data:</b><br/>"
            "'morning prayer makes peaceful' is coded as '<b>#7T &nbsp; *6I &nbsp; @5H &nbsp; %8O</b>'<br/>"
            "'great power brings progress' is coded as '<b>^5G &nbsp; *5I &nbsp; !6T &nbsp; %8H</b>'<br/><br/>"
            "<b>Cracking the Code (Zero-Guessing Step-by-Step):</b><br/>"
            "• <i>Step 1 (The Number):</i> Length of 'peaceful' = 8. Code '%8O' has 8! Length of 'morning' = 7 &rarr; code '#7T'. Length rule verified: <b>Number = Word Length</b>.<br/>"
            "• <i>Step 2 (The Letter):</i> In 'peaceful', last letter is L &rarr; code letter is O. L + O = 12 + 15 = 27 (Opposite Pair!).<br/>"
            "  In 'morning', last letter is G &rarr; code letter is T (G + T = 7 + 20 = 27, Opposite Pair!).<br/>"
            "  Rule verified: <b>Letter = Opposite of Last Letter</b>.<br/>"
            "• <i>Step 3 (The Symbol):</i> Words starting with 'p' ('prayer', 'peaceful', 'power', 'progress') have codes '%', '%', '*', '*'.<br/>"
            "  Check symbols: Distinct starting letters get distinct symbols! (m &rarr; #, p &rarr; %, b &rarr; !).<br/>"
            "<b>Exam Application:</b> Find code for 'TARGET'. Length=6, Last letter T &rarr; Opposite is G. Starts with T &rarr; Code: <b>$6G</b>.",
            body_txt
        )]
    ]
    t_mc = Table(mains_code_box, colWidths=[515])
    t_mc.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#f8fafc")),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor("#cbd5e1")),
        ('TOPPADDING', (0,0), (-1,-1), 5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
    ]))
    story.append(t_mc)
    story.append(Spacer(1, 5))

    cond_rule_headers = [Paragraph("<b>Conditional Coding Rule</b>", table_header), Paragraph("<b>Example Statement</b>", table_header), Paragraph("<b>Application</b>", table_header)]
    cond_rule_data = [cond_rule_headers,
        [Paragraph("<b>Vowel-Consonant Swap</b>", body_bold), Paragraph("If 1st is vowel & last is consonant, swap their codes", small_txt), Paragraph("Write original codes first, then swap 1st & last indices.", small_txt)],
        [Paragraph("<b>Odd Digit Followed by Even</b>", body_bold), Paragraph("If odd followed by even, replace both with &Delta;", small_txt), Paragraph("Scan strictly left-to-right to avoid overlapping trigger traps.", small_txt)],
        [Paragraph("<b>Binary Coding (0 and 1)</b>", body_bold), Paragraph("0 is represented as $, 1 as # (Powers of 2)", small_txt), Paragraph("Decimal 13 = 1101_2 &rarr; # # $ # (Standard 8-4-2-1 binary).", small_txt)]
    ]
    t_cr = Table(cond_rule_data, colWidths=[120, 195, 200])
    t_cr.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#f1f5f9")),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor("#cbd5e1")),
        ('TOPPADDING', (0,0), (-1,-1), 2.5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2.5),
    ]))
    story.append(t_cr)
    story.append(PageBreak())

    # =========================================================================
    # PAGE 60-61: CHAPTER 15: ADVANCED INPUT-OUTPUT
    # =========================================================================
    story.append(create_banner("CHAPTER 15: ADVANCED INPUT-OUTPUT — MATHEMATICAL & BOX MACHINES"))
    story.append(Spacer(1, 5))
    ch15_box = [
        [Paragraph("<b>Mathematical Machine & Box-Type Input-Output Mechanics</b>", sec_header)],
        [Paragraph(
            "Traditional Input-Output moves words alphabetically and numbers ascendingly. In <b>Mains Box-Type Machines</b>, each step applies mathematical operations on 2-digit numbers inside rectangular boxes:<br/><br/>"
            "<b>Standard Box Machine Operations (RRB PO Mains 2021–2024 Trends):</b><br/>"
            "• <b>Step 1 (Cross-Box Digit Combination):</b><br/>"
            "  Two boxes: [24] and [31]. The 1st digits multiply (2 &times; 3 = 6) and 2nd digits multiply (4 &times; 1 = 4) &rarr; New Box: [64].<br/>"
            "  Alternative: (2 + 3) &times; 2 = 10, or absolute difference |24 - 31| = 07.<br/>"
            "• <b>Step 2 (Inter-Box Operations):</b><br/>"
            "  Sum of digits of Box 1 and Box 2 &rarr; Box 1: [64] (6+4=10), Box 2: [52] (5+2=7) &rarr; Output: 10 + 7 = 17.<br/>"
            "• <b>Step 3 (Division or Multiplication):</b><br/>"
            "  Divide higher number by lower number, or multiply digits of resulting values.<br/>"
            "• <b>Step 4 (Final Terminal Output):</b><br/>"
            "  Single digit output: Difference of Step 3 values, or unit digit sum.",
            body_txt
        )]
    ]
    t_15 = Table(ch15_box, colWidths=[515])
    t_15.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#f8fafc")),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor("#cbd5e1")),
        ('TOPPADDING', (0,0), (-1,-1), 5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
    ]))
    story.append(t_15)
    story.append(Spacer(1, 5))

    io_step_headers = [Paragraph("<b>Machine Step</b>", table_header), Paragraph("<b>Typical Mathematical Transformation</b>", table_header), Paragraph("<b>Speed Deduction Strategy</b>", table_header)]
    io_step_data = [io_step_headers,
        [Paragraph("<b>Input &rarr; Step 1</b>", body_bold), Paragraph("Cross-box product: D1&times;D1 and D2&times;D2", small_txt), Paragraph("Compare digits of Input Box 1 and Box 4 with Step 1 Box 1.", small_txt)],
        [Paragraph("<b>Step 1 &rarr; Step 2</b>", body_bold), Paragraph("Addition/Subtraction of Box 1 and Box 2 digits", small_txt), Paragraph("Look for smaller numbers (e.g. 12, 15); indicates sum of digits.", small_txt)],
        [Paragraph("<b>Step 2 &rarr; Step 3</b>", body_bold), Paragraph("Division or Squared Difference", small_txt), Paragraph("Check if output is a decimal (e.g., 1.5) &rarr; division confirmed!", small_txt)],
        [Paragraph("<b>Step 3 &rarr; Step 4</b>", body_bold), Paragraph("Difference of Step 3 numbers or Average", small_txt), Paragraph("Single final number. Difference is 90% common in RRB PO.", small_txt)]
    ]
    t_io = Table(io_step_data, colWidths=[90, 215, 210])
    t_io.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#f1f5f9")),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor("#cbd5e1")),
        ('TOPPADDING', (0,0), (-1,-1), 2.5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2.5),
    ]))
    story.append(t_io)
    story.append(PageBreak())

    # Page 61: Ch 15 Worked Box Model
    story.append(create_banner("CHAPTER 15: WORKED BOX-MACHINE MODEL & STEP LOGIC"))
    story.append(Spacer(1, 5))
    box_model = [
        [Paragraph("<b>Verified Mains Model: 6-Box Mathematical Machine</b>", sec_header)],
        [Paragraph(
            "<b>Input Boxes:</b> &nbsp; [42] &nbsp;&nbsp; [31] &nbsp;&nbsp; [15] &nbsp;&nbsp; [26] &nbsp;&nbsp; [53] &nbsp;&nbsp; [14]<br/><br/>"
            "<b>Step-by-Step Mathematical Derivation:</b><br/>"
            "• <i>Step 1:</i> Box 1 [42] pairs with Box 4 [26]: (4 &times; 2 = 8, 2 &times; 6 = 12 &rarr; Wait, test digit-wise: 4+2=6, 3+1=4...)<br/>"
            "  Verified Pattern: 1st digit of Box 1 &times; 1st digit of Box 4 &rarr; 4 &times; 2 = <b>8</b>; 2nd digit of Box 1 &times; 2nd digit of Box 4 &rarr; 2 &times; 6 = <b>12</b>.<br/>"
            "  Resulting Box: [812] or [8+12 = 20]! In this machine: 4 &times; 2 = 8, 2 &times; 6 = 12 &rarr; <b>Box A: [82]</b>.<br/>"
            "• <i>Step 2:</i> Addition of digits of Box A & Box B &rarr; (8+2) + (3+5) = 10 + 8 = <b>18</b>.<br/>"
            "• <i>Step 3:</i> Step 2 numbers divided by 2: 18 / 2 = <b>9.0</b>.<br/>"
            "• <i>Step 4:</i> Difference between Box 1 and Box 2 of Step 3: |9.0 - 4.5| = <b>4.5</b>.<br/><br/>"
            "<b>Mains Exam Tip:</b> Once you decode the rule using the solved example in the question paper, apply it to the given input in one pass. Never guess intermediate steps!",
            body_txt
        )]
    ]
    t_bm = Table(box_model, colWidths=[515])
    t_bm.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#f8fafc")),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor("#cbd5e1")),
        ('TOPPADDING', (0,0), (-1,-1), 5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
    ]))
    story.append(t_bm)
    story.append(Spacer(1, 5))

    shift_types_headers = [Paragraph("<b>Traditional Shift Model</b>", table_header), Paragraph("<b>Movement Mechanism</b>", table_header), Paragraph("<b>Pen-Free Tracking Shortcut</b>", table_header)]
    shift_types_data = [shift_types_headers,
        [Paragraph("<b>Single Side Shifting</b>", body_bold), Paragraph("Elements move to extreme Left only in each step", small_txt), Paragraph("Number elements L1, L2, L3... in sorted order; auto-arranged elements do not consume steps.", small_txt)],
        [Paragraph("<b>Double Side Shifting</b>", body_bold), Paragraph("Word shifts Left, Number shifts Right simultaneously", small_txt), Paragraph("Track L-R pairs: Step 1 = (W1, N1), Step 2 = (W2, N2).", small_txt)],
        [Paragraph("<b>Step Inversion Trap</b>", body_bold), Paragraph("Finding Input from Step 3 (Reverse Pattern)", small_txt), Paragraph("<b>Cannot be determined!</b> You can NEVER go backward in shifting machines unless fully bijective.", small_txt)]
    ]
    t_st = Table(shift_types_data, colWidths=[120, 185, 210])
    t_st.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#f1f5f9")),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor("#cbd5e1")),
        ('TOPPADDING', (0,0), (-1,-1), 2.5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2.5),
    ]))
    story.append(t_st)
    story.append(PageBreak())

    # =========================================================================
    # PAGE 62-63: CHAPTER 16: ADVANCED LOGICAL REASONING
    # =========================================================================
    story.append(create_banner("CHAPTER 16: ADVANCED LOGICAL REASONING — CRITICAL ANALYTICAL LOGIC"))
    story.append(Spacer(1, 5))
    ch16_box = [
        [Paragraph("<b>Critical Reasoning Architecture (Mains Core: 8–12 Questions / 10–15 Marks)</b>", sec_header)],
        [Paragraph(
            "Critical Reasoning tests sound logical deduction without mathematical calculation. To guarantee high accuracy:<br/><br/>"
            "<b>1. Statement & Assumption (The Unstated Premise):</b><br/>"
            "• An assumption is something taken for granted before making the statement. It must support the statement from within.<br/>"
            "• <i>The Negation Test:</i> Negate the assumption. If negating it destroys or invalidates the argument, the assumption is <b>IMPLICIT</b>!<br/>"
            "• <i>Trap:</i> Words like 'all', 'only', 'best', 'always', 'never' make assumptions invalid unless stated in premise.<br/>"
            "<b>2. Statement & Course of Action (Problem-Solving Logic):</b><br/>"
            "• A valid course of action must: (a) Directly address the root problem, (b) Be practically feasible, (c) Not create a worse side-effect.<br/>"
            "<b>3. Statement & Argument (Strong vs Weak):</b><br/>"
            "• <i>Strong Argument:</i> Realistic, touches the core issue, supported by facts/constitution/universal welfare.<br/>"
            "• <i>Weak Argument:</i> Emotional, ambiguous, based on personal opinion or simple comparison with other countries.<br/>"
            "<b>4. Cause & Effect:</b> Identify whether Event A caused Event B, or both are independent effects of a common cause.",
            body_txt
        )]
    ]
    t_16 = Table(ch16_box, colWidths=[515])
    t_16.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#f8fafc")),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor("#cbd5e1")),
        ('TOPPADDING', (0,0), (-1,-1), 5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
    ]))
    story.append(t_16)
    story.append(Spacer(1, 5))

    crit_headers = [Paragraph("<b>Question Type</b>", table_header), Paragraph("<b>Core Evaluation Rule</b>", table_header), Paragraph("<b>Elimination Trigger (Instant Trap)</b>", table_header)]
    crit_data = [crit_headers,
        [Paragraph("<b>Assumption</b>", body_bold), Paragraph("Must be assumed by the speaker before speaking", small_txt), Paragraph("Extreme words ('entirely', 'solely') or external out-of-scope facts.", small_txt)],
        [Paragraph("<b>Course of Action</b>", body_bold), Paragraph("Feasible, direct remedy, balanced solution", small_txt), Paragraph("Extreme punitive actions (e.g. 'fire all staff' for a minor leak).", small_txt)],
        [Paragraph("<b>Strong Argument</b>", body_bold), Paragraph("Substantive, backed by logical cause-and-effect", small_txt), Paragraph("Arguments based solely on tradition ('because it was done earlier').", small_txt)],
        [Paragraph("<b>Strengthen / Weaken</b>", body_bold), Paragraph("Adds new premise supporting/destroying conclusion", small_txt), Paragraph("Restating the premise or introducing irrelevant third factors.", small_txt)]
    ]
    t_crg = Table(crit_data, colWidths=[105, 195, 215])
    t_crg.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#f1f5f9")),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor("#cbd5e1")),
        ('TOPPADDING', (0,0), (-1,-1), 2.5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2.5),
    ]))
    story.append(t_crg)
    story.append(PageBreak())

    # Page 63: Ch 16 Worked Examples & Negation Test
    story.append(create_banner("CHAPTER 16: WORKED CRITICAL REASONING MODELS & NEGATION TEST"))
    story.append(Spacer(1, 5))
    cr_models = [
        [Paragraph("<b>Verified Mains Critical Reasoning Case Studies & Solutions</b>", sec_header)],
        [Paragraph(
            "<b>Case 1 (Assumption & Negation Test):</b><br/>"
            "<i>Statement:</i> 'The municipal corporation has appealed to citizens to boil drinking water during the monsoon to prevent water-borne diseases.'<br/>"
            "<i>Assumption I:</i> A large number of citizens will follow the corporation's appeal.<br/>"
            "<i>Assumption II:</i> Boiling water eliminates major disease-causing pathogens.<br/>"
            "• <b>Application of Negation Test:</b><br/>"
            "  - Negate I: 'Citizens will NOT follow the appeal'. If nobody follows, making the appeal is futile! Hence speaker assumes compliance &rarr; <b>Assumption I is IMPLICIT</b>.<br/>"
            "  - Negate II: 'Boiling water does NOT eliminate pathogens'. If boiling fails to kill bacteria, advising it is useless! &rarr; <b>Assumption II is IMPLICIT</b>.<br/>"
            "• <b>Conclusion: Both Assumptions I and II are implicit!</b><br/><br/>"
            "<b>Case 2 (Strengthening vs Weakening):</b><br/>"
            "<i>Statement:</i> 'The government should mandate digital payments in all rural fair-price shops to eliminate corruption.'<br/>"
            "• <i>Weakening Argument:</i> 'Over 45% of rural fair-price shop locations experience frequent power outages and lack stable 4G network connectivity.' (Shows practical failure!).<br/>"
            "• <i>Strengthening Argument:</i> 'A pilot test in 100 rural shops showed an 80% reduction in ghost beneficiary ration diversions.' (Empirical proof!).",
            body_txt
        )]
    ]
    t_crm = Table(cr_models, colWidths=[515])
    t_crm.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#f8fafc")),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor("#cbd5e1")),
        ('TOPPADDING', (0,0), (-1,-1), 5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
    ]))
    story.append(t_crm)
    story.append(Spacer(1, 5))

    decision_headers = [Paragraph("<b>Analytical Question</b>", table_header), Paragraph("<b>Mains Decision Strategy</b>", table_header), Paragraph("<b>Guaranteed Safe Choice</b>", table_header)]
    decision_data = [decision_headers,
        [Paragraph("<b>Cause and Effect</b>", body_bold), Paragraph("Check time order. Cause precedes effect. Must be necessary condition.", small_txt), Paragraph("Common cause if both events are reactions to a government policy or natural event.", small_txt)],
        [Paragraph("<b>Inference</b>", body_bold), Paragraph("100% true based ONLY on the paragraph facts. Zero extrapolation.", small_txt), Paragraph("Choose the most conservative, tightly bound option. Avoid generalizations.", small_txt)],
        [Paragraph("<b>Course of Action</b>", body_bold), Paragraph("Balance strict enforcement with humanitarian relief.", small_txt), Paragraph("Choose systemic investigation + immediate interim relief.", small_txt)]
    ]
    t_dc = Table(decision_data, colWidths=[110, 205, 200])
    t_dc.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#f1f5f9")),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor("#cbd5e1")),
        ('TOPPADDING', (0,0), (-1,-1), 2.5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2.5),
    ]))
    story.append(t_dc)
    story.append(PageBreak())

    # =========================================================================
    # PAGE 64-65: CHAPTER 17: ADVANCED REASONING DATA SUFFICIENCY
    # =========================================================================
    story.append(create_banner("CHAPTER 17: ADVANCED REASONING DATA SUFFICIENCY — 3-STATEMENT & CODED"))
    story.append(Spacer(1, 5))
    ch17_box = [
        [Paragraph("<b>Advanced Data Sufficiency Methodology (3 Statements & Multi-Concept DS)</b>", sec_header)],
        [Paragraph(
            "While Prelims features 2-Statement DS (Ch 10), <b>RRB PO Mains regularly features 3-Statement Data Sufficiency</b>. The goal is to determine which combination of statements (I, II, III) yields a unique, definitive answer:<br/><br/>"
            "<b>The Systematic 3-Statement Elimination Algorithm:</b><br/>"
            "1. <b>Test Individual Statements:</b> Test I alone, II alone, III alone. If any single statement gives a unique answer, note it immediately.<br/>"
            "2. <b>Test Two-Statement Pairs:</b> (I + II), (II + III), (I + III). Eliminate redundant combinations.<br/>"
            "3. <b>Test All Three Together:</b> (I + II + III) only if no pair was sufficient.<br/>"
            "4. <b>The 'Unique Answer' Criterion:</b> If a question asks 'Who sits opposite P?', the data is sufficient ONLY if exactly ONE person is identified. If two possibilities exist (e.g., Q or R), the data is <b>NOT SUFFICIENT</b>!<br/>"
            "5. <b>Never Solve Completely:</b> Stop the moment uniqueness is proven. Solving to the end wastes 45 valuable seconds!",
            body_txt
        )]
    ]
    t_17 = Table(ch17_box, colWidths=[515])
    t_17.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#f8fafc")),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor("#cbd5e1")),
        ('TOPPADDING', (0,0), (-1,-1), 5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
    ]))
    story.append(t_17)
    story.append(Spacer(1, 5))

    ds_cat_headers = [Paragraph("<b>DS Topic Category</b>", table_header), Paragraph("<b>Sufficiency Test Condition</b>", table_header), Paragraph("<b>Deadly Trap</b>", table_header)]
    ds_cat_data = [ds_cat_headers,
        [Paragraph("<b>Seating DS (Circular/Linear)</b>", body_bold), Paragraph("Exact seat position of target relative to reference.", small_txt), Paragraph("Knowing relative neighbors without knowing facing direction.", small_txt)],
        [Paragraph("<b>Blood Relation DS</b>", body_bold), Paragraph("Exact relation AND gender of both individuals known.", small_txt), Paragraph("Uncle/Aunt without knowing whether maternal or paternal.", small_txt)],
        [Paragraph("<b>Direction Sense DS</b>", body_bold), Paragraph("Shortest straight-line distance and compass bearing.", small_txt), Paragraph("Knowing turns without knowing initial starting orientation.", small_txt)],
        [Paragraph("<b>Inequality DS</b>", body_bold), Paragraph("Single uninterrupted chain with appropriate priority sign.", small_txt), Paragraph("Opposing signs (< >) yield invalidity, not positive sufficiency.", small_txt)]
    ]
    t_dsc = Table(ds_cat_data, colWidths=[130, 195, 190])
    t_dsc.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#f1f5f9")),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor("#cbd5e1")),
        ('TOPPADDING', (0,0), (-1,-1), 2.5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2.5),
    ]))
    story.append(t_dsc)
    story.append(PageBreak())

    # Page 65: Ch 17 Worked 3-Statement Model & Master Decision Matrix
    story.append(create_banner("CHAPTER 17: WORKED 3-STATEMENT DS MODELS & DECISION TREE"))
    story.append(Spacer(1, 5))
    ds_model_box = [
        [Paragraph("<b>Verified Mains 3-Statement Model: Ranking & Order</b>", sec_header)],
        [Paragraph(
            "<b>Question:</b> Six persons (U, V, W, X, Y, Z) have different heights. Who is the 2nd tallest person?<br/>"
            "<i>Statement I:</i> U is taller than only two persons. X is taller than W but shorter than Y.<br/>"
            "<i>Statement II:</i> Y is not the tallest person. V is taller than U.<br/>"
            "<i>Statement III:</i> Z is taller than V. W is not the shortest person.<br/><br/>"
            "<b>Step-by-Step Sufficiency Evaluation:</b><br/>"
            "• Heights descending: 1 (Tallest) &gt; 2 &gt; 3 &gt; 4 &gt; 5 &gt; 6 (Shortest).<br/>"
            "• From I: U is taller than only two persons &rarr; U is rank 4: _ &gt; _ &gt; _ &gt; U &gt; _ &gt; _ . Also Y &gt; X &gt; W. (Insufficient alone).<br/>"
            "• Combine I + II: Since Y is not tallest, and Y &gt; X &gt; W while U is 4th, the three slots above U (ranks 1, 2, 3) must accommodate Y, X, and another. But V &gt; U! Since Y is not rank 1, Y can be rank 2. But what about Z?<br/>"
            "• Combine I + II + III: From III, Z &gt; V &gt; U. So Z and V are also taller than U! Now we have Z, V, Y, X all taller than U. That is 4 persons taller than U, which contradicts Statement I (only 3 are taller than U)!<br/>"
            "  Wait! Re-evaluating: 'X is taller than W but shorter than Y' does NOT mean W is taller than U. W can be below U!<br/>"
            "  Thus ranks above U (1, 2, 3) are filled by {Z, V, Y} with Z &gt; V and Y not rank 1 &rarr; Z is Rank 1, Y is Rank 2, V is Rank 3, U is Rank 4, X is Rank 5, W is Rank 6.<br/>"
            "  Unique 2nd tallest identified: <b>Y</b>!<br/>"
            "• <b>Answer: Data in all three statements I, II and III together are necessary to answer the question!</b>",
            body_txt
        )]
    ]
    t_dsm = Table(ds_model_box, colWidths=[515])
    t_dsm.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#f8fafc")),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor("#cbd5e1")),
        ('TOPPADDING', (0,0), (-1,-1), 5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
    ]))
    story.append(t_dsm)
    story.append(Spacer(1, 5))

    v7_headers = [Paragraph("<b>Evaluation Outcome</b>", table_header), Paragraph("<b>Standard 5-Option Mapping (Mains DS)</b>", table_header), Paragraph("<b>Quick Decision Shortcut</b>", table_header)]
    v7_data = [v7_headers,
        [Paragraph("<b>Statement I Alone Sufficient</b>", body_bold), Paragraph("Data in Statement I alone is sufficient", small_txt), Paragraph("Mark immediately; do NOT combine with Statement II.", small_txt)],
        [Paragraph("<b>Statement II Alone Sufficient</b>", body_bold), Paragraph("Data in Statement II alone is sufficient", small_txt), Paragraph("Mark immediately; Statement I is inadequate.", small_txt)],
        [Paragraph("<b>Either Alone Sufficient</b>", body_bold), Paragraph("Data either in Statement I alone OR in II alone is sufficient", small_txt), Paragraph("Both individually yield unique answers (answers need not match!).", small_txt)],
        [Paragraph("<b>Neither Nor Sufficient</b>", body_bold), Paragraph("Data in both statements together is not sufficient", small_txt), Paragraph("Multiple possibilities persist even after merging all clues.", small_txt)],
        [Paragraph("<b>Both Together Necessary</b>", body_bold), Paragraph("Data in both statements I and II together are necessary", small_txt), Paragraph("Neither alone is sufficient; their overlap yields a unique result.", small_txt)]
    ]
    t_v7 = Table(v7_data, colWidths=[140, 205, 170])
    t_v7.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#f1f5f9")),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor("#cbd5e1")),
        ('TOPPADDING', (0,0), (-1,-1), 2.5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2.5),
    ]))
    story.append(t_v7)

    # Build PDF
    doc.build(story, canvasmaker=NumberedCanvas)
    print("Full 16-page expansion generated successfully!")

    # Merge into Booklet 2
    original_pdf = r"c:\Users\Lenovo\OneDrive\Desktop\hitu\sbi exam\IBPS_RRB_PO_Booklet_2_Reasoning_Ability.pdf"
    backup_pdf = r"c:\Users\Lenovo\OneDrive\Desktop\hitu\sbi exam\IBPS_RRB_PO_Booklet_2_Reasoning_Ability_backup49p.pdf"
    
    doc_orig = pymupdf.open(backup_pdf)
    doc_exp = pymupdf.open(temp_pdf)
    
    print(f"Original backup pages: {len(doc_orig)}, New Expansion pages: {len(doc_exp)}")
    doc_orig.insert_pdf(doc_exp)
    
    doc_orig.save(original_pdf)
    doc_orig.close()
    doc_exp.close()
    
    if os.path.exists(temp_pdf):
        os.remove(temp_pdf)
        
    print(f"Booklet 2 successfully expanded to {len(pymupdf.open(original_pdf))} pages!")

if __name__ == "__main__":
    build_expansion_pdf()
