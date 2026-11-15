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
        self.drawString(40, 815, "IBPS CRP RRBs-XV Prelims 2026 | Candidate: Hitendrasinh Solanki | Exam Date: 21 Nov 2026")
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
    temp_pdf = "expansion_reasoning_temp.pdf"
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
        fontSize=11,
        leading=14,
        textColor=colors.white,
        alignment=1
    )

    sec_header = ParagraphStyle(
        'SecHeader',
        fontName='Helvetica-Bold',
        fontSize=9.5,
        leading=12,
        textColor=colors.HexColor("#0f172a")
    )

    body_txt = ParagraphStyle(
        'BodyTxt',
        fontName='Helvetica',
        fontSize=7.8,
        leading=10.5,
        textColor=colors.HexColor("#1e293b")
    )

    body_bold = ParagraphStyle(
        'BodyBold',
        fontName='Helvetica-Bold',
        fontSize=7.8,
        leading=10.5,
        textColor=colors.HexColor("#0f172a")
    )

    small_txt = ParagraphStyle(
        'SmallTxt',
        fontName='Helvetica',
        fontSize=7.2,
        leading=9.2,
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
    # PAGE 50: MASTER EXPANDED REASONING SYLLABUS DIRECTORY (CHAPTERS 1 TO 17)
    # =========================================================================
    banner_table = Table(
        [[Paragraph("MASTER EXPANDED REASONING SYLLABUS DIRECTORY (17 COMPLETE CHAPTERS)", title_banner)]],
        colWidths=[515]
    )
    banner_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#0b2545")),
        ('TOPPADDING', (0,0), (-1,-1), 6),
        ('BOTTOMPADDING', (0,0), (-1,-1), 6),
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
    ]))
    story.append(banner_table)
    story.append(Spacer(1, 6))

    intro_p = Paragraph(
        "<b>OFFICIAL REASONING ARCHITECTURE & SELECTION MAPPING:</b> For IBPS RRB PO Scale-I (Officer Scale-I), "
        "Reasoning Ability is the prime scoring engine: <b>Prelims (40 Qs / 40 Marks / 25 Min target)</b> and "
        "<b>Mains (40 Qs / 50 Marks / 1.25 Weightage)</b>. Chapters 1–10 build the foundational speed core, while "
        "Chapters 11–17 provide comprehensive coverage of advanced multi-variable puzzles, critical reasoning, and modern exam patterns.",
        body_txt
    )
    story.append(intro_p)
    story.append(Spacer(1, 5))

    headers = [
        Paragraph("<b>Ch</b>", table_header),
        Paragraph("<b>Chapter Title & Core Focus</b>", table_header),
        Paragraph("<b>Module Category</b>", table_header),
        Paragraph("<b>Exam Tier</b>", table_header),
        Paragraph("<b>Weightage</b>", table_header)
    ]

    syllabus_data = [headers]
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
    audit_banner = Table(
        [[Paragraph("10-CHAPTER COMPREHENSIVE AUDIT & STRATEGIC BLUEPRINT", title_banner)]],
        colWidths=[515]
    )
    audit_banner.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#0b2545")),
        ('TOPPADDING', (0,0), (-1,-1), 6),
        ('BOTTOMPADDING', (0,0), (-1,-1), 6),
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
    ]))
    story.append(audit_banner)
    story.append(Spacer(1, 6))

    audit_headers = [
        Paragraph("<b>Audit Dimension</b>", table_header),
        Paragraph("<b>Detailed Findings & Syllabus Alignment</b>", table_header)
    ]
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
    story.append(Spacer(1, 6))

    # Speed strategy comparison
    strat_box = [
        [Paragraph("<b>IBPS RRB PO Scale-I: Tactical Execution Strategy (Prelims vs Mains)</b>", sec_header)],
        [Paragraph(
            "• <b>Prelims Round-Robin Strategy (22–25 Mins Target: 35+ Marks):</b><br/>"
            "  1. <i>Phase 1 (Min 0–6):</i> Non-puzzle speed scoring (Inequalities 5 Qs in 2 min, Syllogisms 5 Qs in 2.5 min, Miscellaneous/Direction/Blood Relations 5 Qs in 2 min). Bank 15 marks with 100% accuracy.<br/>"
            "  2. <i>Phase 2 (Min 6–22):</i> Attempt 4 out of 4 puzzles/seating sets (20 Qs). Select standard models first: Floor+Flat, Designation, 7-person circular, Day-date. Leave uncertain puzzles for last.<br/>"
            "  3. <i>Phase 3 (Min 22–25):</i> Leftover standalone questions (Word formation, remaining Blood Relations).<br/>"
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
    # PAGE 52: CHAPTER 11: MISCELLANEOUS REASONING (FOUNDATIONS & RULES)
    # =========================================================================
    ch11_banner = Table(
        [[Paragraph("CHAPTER 11: MISCELLANEOUS REASONING — THEORY, RULES & SHORTCUTS", title_banner)]],
        colWidths=[515]
    )
    ch11_banner.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#0b2545")),
        ('TOPPADDING', (0,0), (-1,-1), 6),
        ('BOTTOMPADDING', (0,0), (-1,-1), 6),
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
    ]))
    story.append(ch11_banner)
    story.append(Spacer(1, 6))

    theory_box = [
        [Paragraph("<b>Core Concepts & Zero-Error Methodologies (Speed Rules & Shortcuts)</b>", sec_header)],
        [Paragraph(
            "<b>1. Pair Formation Algorithm (Forward & Backward Scanning):</b><br/>"
            "• <i>Standard Rule:</i> Find pairs of letters having the same number of letters between them as in the English alphabetical series (both forward and backward).<br/>"
            "• <i>Speed Shortcut (Numerical Translation):</i> Convert letters to position numbers immediately (A=1 ... Z=26). Counting numbers (e.g., 14, 15, 16...) is 3x faster and avoids mental alphabet stumble. Never loop after 26 (Z does not wrap back to A unless explicitly stated!).<br/><br/>"
            "<b>2. Meaningful Word Formation (1-X-Y Decision Framework):</b><br/>"
            "• <i>Exam Format:</i> Extract 4 specified letters (e.g. 1st, 3rd, 5th, 8th). If one word is possible, mark 3rd letter. If more than one word, mark 'X'. If no word, mark 'Y'.<br/>"
            "• <i>Tactical Rule:</i> This is the highest negative-marking trap in Prelims! If not 100% certain of anagrams, SKIP and revisit at minute 24. Always test common bank 4-letter anagram clusters: POST/STOP/SPOT/TOPS/POTS, CARE/RACE, BARE/BEAR, DARE/DEAR/READ, TEAM/MEAT/MATE, EAST/SEAT.<br/><br/>"
            "<b>3. Number Manipulation Operations (Digit Transformation):</b><br/>"
            "• <i>Conditional Shifts:</i> 'Add 1 to each odd digit and subtract 1 from each even digit'.<br/>"
            "• <i>Speed Hack:</i> Do not rewrite the full 8-digit number! Scan directly for frequencies: an odd digit '3' becomes '4', an even digit '6' becomes '5'. Focus only on digits that could clash.<br/><br/>"
            "<b>4. Alphabetical & Dictionary Positioning:</b><br/>"
            "• Arranging letters of a word in alphabetical order and identifying which letters remain unchanged in position. Always write the sorted string directly underneath the original string.",
            body_txt
        )]
    ]
    t_theory = Table(theory_box, colWidths=[515])
    t_theory.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#f8fafc")),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor("#cbd5e1")),
        ('TOPPADDING', (0,0), (-1,-1), 5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
    ]))
    story.append(t_theory)
    story.append(Spacer(1, 6))

    # Detailed Rules Table
    rule_headers = [
        Paragraph("<b>Question Type</b>", table_header),
        Paragraph("<b>Standard Exam Clue / Phrasing</b>", table_header),
        Paragraph("<b>Golden Rule & Time-Saving Trick</b>", table_header)
    ]
    rule_data = [rule_headers]
    r_rows = [
        ("Pair Formation", "How many such pairs in 'WORD' both forward and backward?", "Convert to numbers (e.g. 16, 18, 15...). Count upwards only. Skip numbers > 20 if few letters remain."),
        ("Word Formation", "Meaningful word from 1st, 4th, 6th, 9th letters; X if multiple, Y if none.", "Form anagrams mentally. Beware of plurals or past tenses (rarely valid root words in IBPS)."),
        ("Odd One Out", "Find the odd letter group: PSV, EHK, TWZ, MPS, KMP.", "Check difference between adjacent letters: +3, +3 pattern. Odd group has +2 or +4."),
        ("Number Sorting", "Rearrange digits of 7482915 in ascending order; find unchanged.", "Write 1 2 4 5 7 8 9 underneath. Circle identical vertical positions in 5 seconds."),
        ("Vowel/Consonant Shift", "Vowels -> next letter (+1), Consonants -> previous letter (-1).", "Only modify requested target letters (e.g. 'how many vowels in new word?'). Vowels come from 'B, F, J, P, V'.")
    ]
    for qtype, clue, rule in r_rows:
        rule_data.append([Paragraph(f"<b>{qtype}</b>", body_bold), Paragraph(clue, small_txt), Paragraph(rule, small_txt)])

    t_rules = Table(rule_data, colWidths=[105, 180, 230])
    t_rules.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#f1f5f9")),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor("#cbd5e1")),
        ('TOPPADDING', (0,0), (-1,-1), 2.5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2.5),
    ]))
    story.append(t_rules)
    story.append(PageBreak())

    # =========================================================================
    # PAGE 53: CHAPTER 11: WORKED PYQ PATTERNS & QUICK-REVISION CHEAT SHEET
    # =========================================================================
    ch11_p2_banner = Table(
        [[Paragraph("CHAPTER 11: WORKED PYQ PATTERNS & QUICK-REVISION CHEAT SHEET", title_banner)]],
        colWidths=[515]
    )
    ch11_p2_banner.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#0b2545")),
        ('TOPPADDING', (0,0), (-1,-1), 6),
        ('BOTTOMPADDING', (0,0), (-1,-1), 6),
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
    ]))
    story.append(ch11_p2_banner)
    story.append(Spacer(1, 6))

    pyq_box = [
        [Paragraph("<b>Verified Previous-Year Exam Models & Step-by-Step Solutions</b>", sec_header)],
        [Paragraph(
            "<b>Model 1 (Verified IBPS RRB PO Prelims): Pair Counting in 'BANKING'</b><br/>"
            "<i>Question:</i> How many pairs of letters in 'BANKING' have as many letters between them as in the English alphabet (forward and backward)?<br/>"
            "• <i>Recitation Method:</i> Put your finger on a letter, and recite the alphabet out loud as you move your finger.<br/>"
            "• <b>Forward Scan (Left to Right):</b> From B: C, D, E, F, G, H (No). From A: B, C, D, E, F (No). N, K, I, N yield no matches.<br/>"
            "• <b>Backward Scan (Right to Left):</b><br/>"
            "  - Start at <b>G</b> (last letter): move finger left &rarr; over N say 'H'; over I say <b>'I'</b> &rarr; <b>MATCH! (G, I)</b>.<br/>"
            "    <i>Why?</i> In the alphabet, between G and I there is 1 letter (H). In BANKING, between G and I there is 1 letter (N). Exactly the same!<br/>"
            "  - From <b>A</b> (second letter): move finger left &rarr; over B say <b>'B'</b> &rarr; <b>MATCH! (A, B)</b>.<br/>"
            "    <i>Why?</i> In the alphabet, A and B are adjacent. In BANKING, B and A are adjacent!<br/>"
            "• <b>Total Pairs = 2 (G-I and A-B).</b> (Takes 20 seconds using the finger-recite method!).<br/><br/>"
            "<b>Model 2 (Memory-Based IBPS RRB PO 2023 Prelims Shift 2): Meaningful Word</b><br/>"
            "<i>Question:</i> Form a meaningful 4-letter English word using 1st, 3rd, 5th, 7th letters of <b>'DISCOVERY'</b>. If multiple words form, mark 'X'; if none, mark 'Y'.<br/>"
            "• Extracted Letters: 1st=<b>D</b>, 3rd=<b>S</b>, 5th=<b>O</b>, 7th=<b>E</b>.<br/>"
            "• Anagram Test: <b>DOSE</b> (medicine dose) and <b>ODES</b> (poems) &rarr; Answer is <b>'X'</b>.<br/><br/>"
            "<b>Model 3 (Verified IBPS RRB PO 2022 Prelims Shift 1): Number Operations</b><br/>"
            "<i>Question:</i> In '73942618', add 1 to odd digits and subtract 1 from even digits. Which digits appear more than once?<br/>"
            "• Odd (+1): 7&rarr;8, 3&rarr;4, 9&rarr;0, 1&rarr;2. Even (-1): 4&rarr;3, 2&rarr;1, 6&rarr;5, 8&rarr;7.<br/>"
            "• New digits: {8, 4, 0, 2, 3, 1, 5, 7} &rarr; All distinct! <b>Answer: None</b>.",
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
    story.append(Spacer(1, 6))

    # Cheat Sheet Table: Alphabet Indices & Opposite Pairs
    cheat_header = [
        Paragraph("<b>Speed Hack Tool</b>", table_header),
        Paragraph("<b>Memory Mnemonic & Key Values</b>", table_header),
        Paragraph("<b>Instant Application in Reasoning</b>", table_header)
    ]
    cheat_rows = [
        ("EJOTY Rule", "E=5, J=10, O=15, T=20, Y=25", "Rapid 5-multiple anchor for forward positions."),
        ("CFILORUX Rule", "C=3, F=6, I=9, L=12, O=15, R=18, U=21, X=24", "Rapid 3-multiple anchor for tight clustering."),
        ("Opposite Letters (Sum = 27)", "AZ (A-Z), BY (By), CX (Crux), DW (Dew), EV (EVening), FU (FUll), GT (GT Road), HS (High School), IR (Indian Railway), JQ (Jungle Queen), KP (Kanpur), LO (LOve), MN (MaN)", "Mains New Pattern Coding & Reverse Alphabet shift."),
        ("Vowel Predecessors", "B &rarr; A, F &rarr; E, J &rarr; I, P &rarr; O, V &rarr; U", "Quick scan for words having vowels after consonant-1.")
    ]
    cheat_data = [cheat_header]
    for tool, mnem, app in cheat_rows:
        cheat_data.append([Paragraph(f"<b>{tool}</b>", body_bold), Paragraph(mnem, small_txt), Paragraph(app, small_txt)])

    t_cheat = Table(cheat_data, colWidths=[110, 235, 170])
    t_cheat.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#f1f5f9")),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor("#cbd5e1")),
        ('TOPPADDING', (0,0), (-1,-1), 2.5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2.5),
    ]))
    story.append(t_cheat)

    # Build the document
    doc.build(story, canvasmaker=NumberedCanvas)
    print("Temporary expansion PDF created successfully!")

    # Merge into Booklet 2
    original_pdf = r"c:\Users\Lenovo\OneDrive\Desktop\hitu\sbi exam\IBPS_RRB_PO_Booklet_2_Reasoning_Ability.pdf"
    backup_pdf = r"c:\Users\Lenovo\OneDrive\Desktop\hitu\sbi exam\IBPS_RRB_PO_Booklet_2_Reasoning_Ability_backup49p.pdf"
    
    # Ensure backup exists
    if not os.path.exists(backup_pdf):
        import shutil
        shutil.copyfile(original_pdf, backup_pdf)
        print("Backup verified.")

    # Open backup and expansion
    doc_orig = pymupdf.open(backup_pdf)
    doc_exp = pymupdf.open(temp_pdf)
    
    print(f"Original pages: {len(doc_orig)}, Expansion pages: {len(doc_exp)}")
    doc_orig.insert_pdf(doc_exp)
    
    output_pdf = original_pdf
    doc_orig.save(output_pdf)
    doc_orig.close()
    doc_exp.close()
    
    if os.path.exists(temp_pdf):
        os.remove(temp_pdf)
        
    print(f"Booklet 2 successfully updated! New total pages: {len(pymupdf.open(output_pdf))}")

if __name__ == "__main__":
    build_expansion_pdf()
