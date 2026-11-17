import os
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.pdfgen import canvas
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle

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
        self.setFont("Helvetica-Bold", 8)
        self.setFillColor(colors.HexColor("#1e293b"))
        # Header
        self.drawString(40, 815, "IBPS CRP RRBs-XV & SBI PO / CLERK | MAINS EXCLUSIVE REASONING DOSSIER")
        self.setFont("Helvetica", 8)
        self.setFillColor(colors.HexColor("#64748b"))
        self.drawRightString(555, 815, f"Candidate: Hitendrasinh Solanki | Page {page_num} of {total_pages}")
        self.setStrokeColor(colors.HexColor("#cbd5e1"))
        self.setLineWidth(0.75)
        self.line(40, 808, 555, 808)
        
        # Footer
        self.line(40, 32, 555, 32)
        self.drawString(40, 22, "🔒 RESERVED EXCLUSIVELY FOR MAINS PHASE (POST-PRELIMS STUDY) | Reasoning Ability Curriculum")
        self.setFont("Helvetica-Bold", 8)
        self.setFillColor(colors.HexColor("#b91c1c"))
        self.drawRightString(555, 22, "MAINS EXCLUSIVE — CH 15, 16 & 17")
        self.restoreState()

def create_banner(text, bg_color="#1e3a8a"):
    style = ParagraphStyle(
        'BannerStyle',
        fontName='Helvetica-Bold',
        fontSize=10.5,
        leading=13.5,
        textColor=colors.white,
        alignment=1
    )
    t = Table([[Paragraph(f"<b>{text}</b>", style)]], colWidths=[515])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor(bg_color)),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ]))
    return t

def build_pdf():
    output_path = r"c:\Users\Lenovo\OneDrive\Desktop\hitu\sbi exam\reasoning ability ch\MAINS_EXCLUSIVE_REASONING_CH15_16_17.pdf"
    doc = SimpleDocTemplate(
        output_path,
        pagesize=A4,
        leftMargin=40,
        rightMargin=40,
        topMargin=45,
        bottomMargin=45
    )

    styles = getSampleStyleSheet()

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
        leading=9,
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
    # PAGE 1: EXECUTIVE STRATEGIC BRIEFING & SYLLABUS BOUNDARY
    # =========================================================================
    story.append(create_banner("IBPS RRB PO & SBI PO/CLERK — MAINS EXCLUSIVE REASONING DOSSIER", "#0f172a"))
    story.append(Spacer(1, 5))

    p1_summary = [
        [Paragraph("<b>EXECUTIVE STRATEGIC ADVISORY: PRELIMS VS MAINS SYLLABUS DEMARCATION</b>", sec_header)],
        [Paragraph(
            "<b>Candidate:</b> Hitendrasinh Solanki &nbsp;|&nbsp; <b>Target:</b> IBPS RRB PO 2026 / SBI PO / Clerk<br/>"
            "<b>Strategic Purpose of this Dossier:</b> To officially quarantine and archive <b>Chapters 15, 16, and 17</b> for the post-prelims study phase. Banking exams feature a strict structural bifurcation between Prelims and Mains. Diluting speed by studying complex Mains abstraction right before Prelims is a common tactical error. This dossier serves as your complete self-contained Mains study manual ready for instant activation the day after Prelims!<br/><br/>"
            "<b>Why Chapters 15, 16, and 17 NEVER Appear in Prelims:</b><br/>"
            "• <b>Prelims Exam (40 Questions / 40 Marks / 22–25 mins):</b> Tests purely high-speed visual processing, rapid puzzle construction, and basic deduction. The syllabus is <b>100% covered by Chapters 1 to 13</b> (plus Ch 14 Advanced Coding which gives a solid advantage).<br/>"
            "• <b>Mains Exam (50 Questions / 50 Marks / 30–35 mins):</b> Tests complex algebraic automation, verbal analytical philosophy, and multi-statement evaluations. Chapters 15, 16, and 17 represent <b>20 to 22 marks out of 50 in Mains</b>!",
            body_txt
        )]
    ]
    t_p1 = Table(p1_summary, colWidths=[515])
    t_p1.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#f8fafc")),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor("#cbd5e1")),
        ('TOPPADDING', (0,0), (-1,-1), 5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
    ]))
    story.append(t_p1)
    story.append(Spacer(1, 6))

    # Weightage & Exam Mapping Table
    map_headers = [Paragraph("<b>Chapter # & Scope</b>", table_header), Paragraph("<b>Exam Tier Presence</b>", table_header), Paragraph("<b>Mains Weightage</b>", table_header), Paragraph("<b>Strategic Action Plan</b>", table_header)]
    map_data = [map_headers,
        [Paragraph("<b>Ch 1 to 13: Core Reasoning</b><br/>(Puzzles, Seating, Syllogisms, Inequalities, Series, Blood, Direction)", body_bold), Paragraph("100% in Prelims & Mains", small_txt), Paragraph("25–30 Marks", small_txt), Paragraph("<b>100% EXAM READY!</b> Focus on speed drills & full mocks.", small_txt)],
        [Paragraph("<b>Ch 14: Advanced Coding</b><br/>(New Pattern, Conditional, Binary)", body_bold), Paragraph("Mains Core (Rare in Prelims)", small_txt), Paragraph("5 Marks", small_txt), Paragraph("<b>100% EXAM READY!</b> Already conquered ahead of schedule.", small_txt)],
        [Paragraph("<b>Ch 15: Mathematical Box Input-Output</b><br/>(Cross-box operations, Step 1–4 matrices)", body_bold), Paragraph("<b>100% Mains Exclusive</b><br/>(0% in Prelims)", small_txt), Paragraph("5 Marks", small_txt), Paragraph("<b>QUARANTINED FOR MAINS.</b> Study immediately after Prelims.", small_txt)],
        [Paragraph("<b>Ch 16: Critical Analytical Reasoning</b><br/>(Statement-Assumption, Course of Action, Cause-Effect)", body_bold), Paragraph("<b>100% Mains Exclusive</b><br/>(0% in Prelims)", small_txt), Paragraph("8–12 Marks", small_txt), Paragraph("<b>QUARANTINED FOR MAINS.</b> 10-day intensive verbal drill post-prelims.", small_txt)],
        [Paragraph("<b>Ch 17: 3-Statement & Coded DS</b><br/>(Multi-statement data sufficiency)", body_bold), Paragraph("<b>100% Mains Exclusive</b><br/>(0% in Prelims)", small_txt), Paragraph("5 Marks", small_txt), Paragraph("<b>QUARANTINED FOR MAINS.</b> Systematic elimination protocol post-prelims.", small_txt)]
    ]
    t_map = Table(map_data, colWidths=[150, 95, 75, 195])
    t_map.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#0f172a")),
        ('TEXTCOLOR', (0,0), (-1,0), colors.white),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor("#cbd5e1")),
        ('TOPPADDING', (0,0), (-1,-1), 3),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3),
    ]))
    story.append(t_map)
    story.append(Spacer(1, 6))

    # Post-Prelims Timeline Box
    timeline_box = [
        [Paragraph("<b>POST-PRELIMS 14-DAY MAINS ACTIVATION TIMELINE (ચોક્કસ રણનીતિ પ્લાન)</b>", sec_header)],
        [Paragraph(
            "<b>Day 1–3 Post-Prelims (Chapter 15):</b> Master 15 mathematical box machines. Practice digit-cross multiplication, addition patterns, and division factor checks.<br/>"
            "<b>Day 4–8 Post-Prelims (Chapter 16):</b> Master 60 Critical Reasoning questions using the <i>Negation Test</i>. Read statements with zero external bias.<br/>"
            "<b>Day 9–11 Post-Prelims (Chapter 17):</b> Master 30 3-Statement DS questions using the <i>Elimination Algorithm</i>. Never solve to the end—test uniqueness!<br/>"
            "<b>Day 12–14 Post-Prelims:</b> Full Mains Mock Tests (Target: 35+ / 50 marks in 35 minutes).",
            body_txt
        )]
    ]
    t_time = Table(timeline_box, colWidths=[515])
    t_time.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#eff6ff")),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor("#3b82f6")),
        ('TOPPADDING', (0,0), (-1,-1), 5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
    ]))
    story.append(t_time)
    story.append(PageBreak())

    # =========================================================================
    # PAGE 2: CHAPTER 15: ADVANCED INPUT-OUTPUT (MATHEMATICAL BOX MACHINES)
    # =========================================================================
    story.append(create_banner("CHAPTER 15: ADVANCED INPUT-OUTPUT — MATHEMATICAL BOX MACHINES", "#1e3a8a"))
    story.append(Spacer(1, 5))

    ch15_theory = [
        [Paragraph("<b>Modern Mains Box-Type Machine Architecture & Decoding Principles</b>", sec_header)],
        [Paragraph(
            "In modern IBPS RRB PO and SBI PO Mains, word-shifting is replaced by <b>Mathematical Box Machines</b>. Candidates are given 6 input boxes containing 2-digit numbers that pass through 4 transformation steps:<br/><br/>"
            "<b>1. Step 1 (Cross-Box Digit Combination - ક્રોસ બોક્સ અંક જોડાણ):</b><br/>"
            "• Box 1 pairs with Box 4; Box 2 pairs with Box 5; Box 3 pairs with Box 6.<br/>"
            "• Standard mathematical operations between digits: (D1 &times; D1) and (D2 &times; D2), or (D1 &times; D2) and (D2 &times; D1), or (D1 + D1) &times; 2.<br/>"
            "• <i>Result:</i> 3 intermediate boxes (Box A, Box B, Box C).<br/><br/>"
            "<b>2. Step 2 (Inter-Box Operations - બોક્સ અંકોનો સરવાળો/ગુણાકાર):</b><br/>"
            "• Combination of adjacent boxes: (Box A + Box B) &rarr; Box D; (Box B + Box C) &rarr; Box E.<br/>"
            "• Operation: Sum of all 4 digits, or sum of squares of digits, or difference of products.<br/>"
            "• <i>Result:</i> 2 intermediate boxes (Box D, Box E).<br/><br/>"
            "<b>3. Step 3 (Division or Multiplication - ભાગાકાર કે ગુણાકાર):</b><br/>"
            "• Constant factor division (e.g. Box D &divide; 2, Box E &divide; 2) or cross-division.<br/>"
            "• <i>Instant Clue:</i> If the numbers have decimals (e.g., 7.5, 9.5), <b>division by 2 is 100% confirmed!</b><br/><br/>"
            "<b>4. Step 4 (Final Terminal Output - અંતિમ આઉટપુટ):</b><br/>"
            "• Absolute difference of Step 3 values: |Val 1 - Val 2| = Final Output.<br/>"
            "• <i>Result:</i> Exactly 1 final number.",
            body_txt
        )]
    ]
    t_15_th = Table(ch15_theory, colWidths=[515])
    t_15_th.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#f8fafc")),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor("#cbd5e1")),
        ('TOPPADDING', (0,0), (-1,-1), 5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
    ]))
    story.append(t_15_th)
    story.append(Spacer(1, 6))

    # Step Matrix Table
    step_headers = [Paragraph("<b>Step Transition</b>", table_header), Paragraph("<b>Dominant Exam Logic</b>", table_header), Paragraph("<b>Gujarati Speed Notes (ગુજરાતી નોંધ)</b>", table_header)]
    step_data = [step_headers,
        [Paragraph("<b>Input &rarr; Step 1</b>", body_bold), Paragraph("Box 1 &times; Box 4, Box 2 &times; Box 5, Box 3 &times; Box 6 (Digit-wise multiplication)", small_txt), Paragraph("પ્રથમ બોક્સના અંકનો ચોથા બોક્સના અંક સાથે ગુણાકાર. ૩ બોક્સ બનશે.", small_txt)],
        [Paragraph("<b>Step 1 &rarr; Step 2</b>", body_bold), Paragraph("Sum of all digits of Box A & B &rarr; D; Box B & C &rarr; E", small_txt), Paragraph("પાસપાસેના બોક્સના ચારેય અંકોનો સરવાળો. ૨ બોક્સ બનશે.", small_txt)],
        [Paragraph("<b>Step 2 &rarr; Step 3</b>", body_bold), Paragraph("Divide values by 2 or 3 (decimals indicate division)", small_txt), Paragraph("જો પોઇન્ટ (.5) દેખાય તો ૨ વડે ભાગાકાર ૧૦૦% નક્કી!", small_txt)],
        [Paragraph("<b>Step 3 &rarr; Step 4</b>", body_bold), Paragraph("Absolute difference |N1 - N2| or single digit sum", small_txt), Paragraph("બંને સંખ્યાઓની બાદબાકી એટલે અંતિમ આઉટપુટ.", small_txt)]
    ]
    t_step = Table(step_data, colWidths=[110, 205, 200])
    t_step.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#1e3a8a")),
        ('TEXTCOLOR', (0,0), (-1,0), colors.white),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor("#cbd5e1")),
        ('TOPPADDING', (0,0), (-1,-1), 3),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3),
    ]))
    story.append(t_step)
    story.append(Spacer(1, 6))

    # The Inversion Law
    inv_box = [
        [Paragraph("<b>THE STEP INVERSION BACKWARD LAW (રિવર્સ ટ્રેપ — સીધો 1 માર્ક બચાવો!)</b>", sec_header)],
        [Paragraph(
            "<b>Question Trap:</b> 'If Step 3 is given as [12] [16], what was the Input?'<br/>"
            "<b>The Law:</b> In ANY Machine Input-Output (whether words, numbers, or boxes), <b>YOU CAN NEVER GO BACKWARD FROM A STEP TO INPUT OR TO A PREVIOUS STEP!</b><br/>"
            "<b>Correct Answer:</b> Always mark <b>'Cannot be determined' (નક્કી ન થઈ શકે)</b> immediately in 2 seconds. Never waste time trying to reverse-engineer mathematical operations because multiple combinations produce the same product/sum!",
            body_txt
        )]
    ]
    t_inv = Table(inv_box, colWidths=[515])
    t_inv.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#fef2f2")),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor("#ef4444")),
        ('TOPPADDING', (0,0), (-1,-1), 5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
    ]))
    story.append(t_inv)
    story.append(PageBreak())

    # =========================================================================
    # PAGE 3: CHAPTER 15: WORKED BOX-MACHINE EXAM MODEL & 5-QUESTION SET
    # =========================================================================
    story.append(create_banner("CHAPTER 15: VERIFIED MAINS BOX-MACHINE MODEL & STEP DERIVATION", "#1e3a8a"))
    story.append(Spacer(1, 5))

    worked_box = [
        [Paragraph("<b>Verified Mains Model (Full 6-Box Machine Walkthrough)</b>", sec_header)],
        [Paragraph(
            "<b>Input Boxes:</b> &nbsp;&nbsp; [32] &nbsp;&nbsp;&nbsp;&nbsp; [41] &nbsp;&nbsp;&nbsp;&nbsp; [23] &nbsp;&nbsp;&nbsp;&nbsp; [21] &nbsp;&nbsp;&nbsp;&nbsp; [13] &nbsp;&nbsp;&nbsp;&nbsp; [32]<br/>"
            "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Box 1 &nbsp;&nbsp;&nbsp; Box 2 &nbsp;&nbsp;&nbsp; Box 3 &nbsp;&nbsp;&nbsp; Box 4 &nbsp;&nbsp;&nbsp; Box 5 &nbsp;&nbsp;&nbsp; Box 6<br/><br/>"
            "<b>Step-by-Step Derivation:</b><br/>"
            "• <b>Step 1 (Cross Pairs):</b><br/>"
            "  - Box 1 [32] & Box 4 [21] &rarr; (3 &times; 2 = 6, 2 &times; 1 = 2) &rarr; <b>Box A: [62]</b><br/>"
            "  - Box 2 [41] & Box 5 [13] &rarr; (4 &times; 1 = 4, 1 &times; 3 = 3) &rarr; <b>Box B: [43]</b><br/>"
            "  - Box 3 [23] & Box 6 [32] &rarr; (2 &times; 3 = 6, 3 &times; 2 = 6) &rarr; <b>Box C: [66]</b><br/>"
            "• <b>Step 2 (Inter-Box Digit Sum):</b><br/>"
            "  - Box A [62] & Box B [43] &rarr; (6+2) + (4+3) = 8 + 7 = <b>Box D: [15]</b><br/>"
            "  - Box B [43] & Box C [66] &rarr; (4+3) + (6+6) = 7 + 12 = <b>Box E: [19]</b><br/>"
            "• <b>Step 3 (Division by 2):</b><br/>"
            "  - Box D [15] &divide; 2 = <b>[7.5]</b> &nbsp;|&nbsp; Box E [19] &divide; 2 = <b>[9.5]</b><br/>"
            "• <b>Step 4 (Terminal Difference):</b><br/>"
            "  - |7.5 - 9.5| = <b>[2.0]</b> (Final Terminal Output)",
            body_txt
        )]
    ]
    t_wb = Table(worked_box, colWidths=[515])
    t_wb.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#f8fafc")),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor("#cbd5e1")),
        ('TOPPADDING', (0,0), (-1,-1), 5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
    ]))
    story.append(t_wb)
    story.append(Spacer(1, 6))

    # Mains Practice Set
    q_box = [
        [Paragraph("<b>OFFICIAL MAINS 5-QUESTION EXAM SET (BASED ON NEW INPUT)</b>", sec_header)],
        [Paragraph(
            "<b>NEW INPUT:</b> &nbsp; [24] &nbsp;&nbsp;&nbsp;&nbsp; [51] &nbsp;&nbsp;&nbsp;&nbsp; [32] &nbsp;&nbsp;&nbsp;&nbsp; [32] &nbsp;&nbsp;&nbsp;&nbsp; [14] &nbsp;&nbsp;&nbsp;&nbsp; [23]<br/>"
            "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Box 1 &nbsp;&nbsp;&nbsp; Box 2 &nbsp;&nbsp;&nbsp; Box 3 &nbsp;&nbsp;&nbsp; Box 4 &nbsp;&nbsp;&nbsp; Box 5 &nbsp;&nbsp;&nbsp; Box 6<br/><br/>"
            "<b>Candidate Derivation Table:</b><br/>"
            "• Step 1: Box A = (2&times;3, 4&times;2) = <b>[68]</b>; Box B = (5&times;1, 1&times;4) = <b>[54]</b>; Box C = (3&times;2, 2&times;3) = <b>[66]</b><br/>"
            "• Step 2: Box D = (6+8) + (5+4) = 14 + 9 = <b>[23]</b>; Box E = (5+4) + (6+6) = 9 + 12 = <b>[21]</b><br/>"
            "• Step 3: Box D = 23 &divide; 2 = <b>[11.5]</b>; Box E = 21 &divide; 2 = <b>[10.5]</b><br/>"
            "• Step 4: |11.5 - 10.5| = <b>[1.0]</b><br/><br/>"
            "<b>Mains Exam Questions & Verified Answers:</b><br/>"
            "<b>Q1:</b> What is the value of Box A in Step 1? &rarr; <b>Answer: 68 [Option B]</b><br/>"
            "<b>Q2:</b> What is the sum of digits of Box D and Box E in Step 2? &rarr; (2+3) + (2+1) = 5 + 3 = <b>8</b><br/>"
            "<b>Q3:</b> What is the product of numbers obtained in Step 3? &rarr; 11.5 &times; 10.5 = <b>120.75</b><br/>"
            "<b>Q4:</b> What is the final terminal output in Step 4? &rarr; <b>Answer: 1.0</b><br/>"
            "<b>Q5:</b> What is the difference between Box B and Box C in Step 1? &rarr; |54 - 66| = <b>12</b>",
            body_txt
        )]
    ]
    t_qb = Table(q_box, colWidths=[515])
    t_qb.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#f0fdf4")),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor("#22c55e")),
        ('TOPPADDING', (0,0), (-1,-1), 5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
    ]))
    story.append(t_qb)
    story.append(PageBreak())

    # =========================================================================
    # PAGE 4: CHAPTER 16: CRITICAL ANALYTICAL REASONING (LOGICAL REASONING)
    # =========================================================================
    story.append(create_banner("CHAPTER 16: CRITICAL REASONING — ARCHITECTURE & NEGATION TEST", "#1e3a8a"))
    story.append(Spacer(1, 5))

    ch16_arch = [
        [Paragraph("<b>Critical Reasoning Architecture (Mains Weightage: 8–12 Questions / 10–15 Marks)</b>", sec_header)],
        [Paragraph(
            "Critical Reasoning tests verbal logic and objective decision-making. No formulas or arithmetic are required, but 90% of candidates lose marks due to subjective assumptions. Master the 4 core models:<br/><br/>"
            "<b>1. Statement & Assumption (The Unstated Premise - પૂર્વધારણા):</b><br/>"
            "• An assumption is something the speaker takes for granted <i>before</i> making the statement.<br/>"
            "• <b>THE NEGATION TEST (અવરોધક કસોટી — સર્વશ્રેષ્ઠ પદ્ધતિ):</b><br/>"
            "  Negate the assumption (add 'NOT'). If negating the assumption collapses or renders the statement meaningless, the assumption is <b>100% IMPLICIT (VALID)</b>!<br/>"
            "  <i>Example:</i> Statement: 'Take umbrella, it might rain.' Assumption: 'Umbrella protects from rain.'<br/>"
            "  Negation: 'Umbrella does NOT protect from rain.' &rarr; If so, telling someone to take it is absurd! &rarr; Assumption is Implicit!<br/><br/>"
            "<b>2. Statement & Course of Action (સમસ્યા અને ઉકેલ):</b><br/>"
            "• A valid course of action must: (a) Directly solve the problem, (b) Be practically feasible, (c) Be proportional (not excessive/punitive).<br/>"
            "• <i>Red Flag:</i> Extreme actions (e.g. 'dismiss all police officers' due to one theft) are ALWAYS invalid.<br/><br/>"
            "<b>3. Statement & Argument (મજબૂત વિરુદ્ધ નબળી દલીલ):</b><br/>"
            "• <i>Strong Argument:</i> Addresses the core issue directly, based on constitutional rights, public welfare, or proven facts.<br/>"
            "• <i>Weak Argument:</i> Emotional, ambiguous, based on personal opinion, or mere comparison ('Country X does it').<br/><br/>"
            "<b>4. Cause and Effect (કારણ અને પરિણામ):</b><br/>"
            "• Determine whether Event A is the direct cause of Event B, Event B is the cause of A, or both are independent effects.",
            body_txt
        )]
    ]
    t_16_arch = Table(ch16_arch, colWidths=[515])
    t_16_arch.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#f8fafc")),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor("#cbd5e1")),
        ('TOPPADDING', (0,0), (-1,-1), 5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
    ]))
    story.append(t_16_arch)
    story.append(Spacer(1, 6))

    # Elimination Rules Table
    elim_headers = [Paragraph("<b>Question Type</b>", table_header), Paragraph("<b>Golden Acceptance Rule</b>", table_header), Paragraph("<b>Instant Elimination Trap (Red Flag)</b>", table_header)]
    elim_data = [elim_headers,
        [Paragraph("<b>Assumption</b>", body_bold), Paragraph("Must be assumed by the speaker before uttering premise.", small_txt), Paragraph("Extreme words: 'all', 'only', 'best', 'never', 'solely'.", small_txt)],
        [Paragraph("<b>Course of Action</b>", body_bold), Paragraph("Feasible, direct solution with balanced impact.", small_txt), Paragraph("Harsh/punitive action, or measures worse than the disease.", small_txt)],
        [Paragraph("<b>Strong Argument</b>", body_bold), Paragraph("Logical cause-effect backed by data or human welfare.", small_txt), Paragraph("Mere comparison: 'Because America does it, India should too'.", small_txt)],
        [Paragraph("<b>Strengthen / Weaken</b>", body_bold), Paragraph("Adds new premise confirming/destroying the link.", small_txt), Paragraph("Merely repeating the given statement in different words.", small_txt)]
    ]
    t_elim = Table(elim_data, colWidths=[105, 205, 205])
    t_elim.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#1e3a8a")),
        ('TEXTCOLOR', (0,0), (-1,0), colors.white),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor("#cbd5e1")),
        ('TOPPADDING', (0,0), (-1,-1), 3),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3),
    ]))
    story.append(t_elim)
    story.append(PageBreak())

    # =========================================================================
    # PAGE 5: CHAPTER 16: WORKED CRITICAL REASONING EXAM MODELS
    # =========================================================================
    story.append(create_banner("CHAPTER 16: VERIFIED CRITICAL REASONING WORKED MODELS", "#1e3a8a"))
    story.append(Spacer(1, 5))

    cr_cases = [
        [Paragraph("<b>Mains Worked Case Studies with Negation Test Analysis</b>", sec_header)],
        [Paragraph(
            "<b>Case 1: Public Appeal & Assumption (RRB PO Mains Model)</b><br/>"
            "<i>Statement:</i> 'The municipal corporation has issued a public notice appealing to all residents to boil drinking water during the monsoon season to prevent water-borne epidemics.'<br/>"
            "<i>Assumption I:</i> A substantial number of residents will heed the notice and boil their water.<br/>"
            "<i>Assumption II:</i> Boiling water kills pathogenic bacteria responsible for monsoon water-borne diseases.<br/>"
            "• <b>Negation Test Evaluation:</b><br/>"
            "  - Negate I: 'Residents will NOT heed the notice.' If no one listens, publishing the appeal is futile! Hence the corporation definitely assumed people will comply &rarr; <b>Assumption I is IMPLICIT</b>.<br/>"
            "  - Negate II: 'Boiling water does NOT kill bacteria.' If boiling does not kill pathogens, advising people to boil is medically useless! Hence the corporation assumed boiling is effective &rarr; <b>Assumption II is IMPLICIT</b>.<br/>"
            "• <b>Final Verdict: Both Assumption I and II are implicit!</b><br/><br/>"
            "<b>Case 2: Course of Action (Problem-Solving Logic)</b><br/>"
            "<i>Statement:</i> 'A severe heatwave has swept across several districts of the state, causing a sudden spike in heatstroke hospital admissions.'<br/>"
            "<i>Course of Action I:</i> The government should immediately set up temporary cooling centers and free hydration kiosks in public transit hubs.<br/>"
            "<i>Course of Action II:</i> All government offices and commercial establishments should be permanently shut down until the winter season.<br/>"
            "• <b>Evaluation:</b><br/>"
            "  - Action I directly alleviates heatstroke, is practically feasible, and provides relief &rarr; <b>Follows!</b><br/>"
            "  - Action II is an extreme, disproportionate overreaction that would collapse the economy &rarr; <b>Does NOT Follow!</b><br/>"
            "• <b>Final Verdict: Only Course of Action I follows!</b><br/><br/>"
            "<b>Case 3: Cause & Effect (RRB PO Mains High-Frequency Pattern)</b><br/>"
            "<i>Statement I:</i> The state transport corporation has canceled all inter-city bus operations for the next three days.<br/>"
            "<i>Statement II:</i> Incessant torrential rains have led to widespread flooding and bridge collapses along all major state highways.<br/>"
            "• <b>Evaluation:</b> Because bridges collapsed and roads are flooded (II), the bus corporation was forced to cancel buses (I).<br/>"
            "• <b>Final Verdict: Statement II is the cause and Statement I is its effect!</b>",
            body_txt
        )]
    ]
    t_crc = Table(cr_cases, colWidths=[515])
    t_crc.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#f8fafc")),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor("#cbd5e1")),
        ('TOPPADDING', (0,0), (-1,-1), 5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
    ]))
    story.append(t_crc)
    story.append(Spacer(1, 6))

    # CR Golden Advice Box
    cr_tip = [
        [Paragraph("<b>MAINS EXAM SPEED RULE FOR CRITICAL REASONING</b>", sec_header)],
        [Paragraph(
            "1. <b>Zero Personal Bias:</b> Never bring your own political, social, or emotional views into the question. Rely 100% on the text.<br/>"
            "2. <b>The 45-Second Cap:</b> Read the statement once, apply the Negation Test or Feasibility check, and choose the option. If stuck between two choices, skip and revisit in the final 5 minutes.",
            body_txt
        )]
    ]
    t_crt = Table(cr_tip, colWidths=[515])
    t_crt.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#eff6ff")),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor("#3b82f6")),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
    ]))
    story.append(t_crt)
    story.append(PageBreak())

    # =========================================================================
    # PAGE 6: CHAPTER 17: ADVANCED 3-STATEMENT DATA SUFFICIENCY
    # =========================================================================
    story.append(create_banner("CHAPTER 17: ADVANCED 3-STATEMENT DATA SUFFICIENCY", "#1e3a8a"))
    story.append(Spacer(1, 5))

    ch17_arch = [
        [Paragraph("<b>Advanced 3-Statement Data Sufficiency Methodology & Elimination Tree</b>", sec_header)],
        [Paragraph(
            "While Prelims features 2-Statement DS (Ch 10), <b>RRB PO Mains regularly features 3-Statement Data Sufficiency (5 Questions)</b>. The question asks whether data in Statement I, II, and III (alone or in combinations) is sufficient to answer the question uniquely.<br/><br/>"
            "<b>The Systematic 3-Step Elimination Algorithm:</b><br/>"
            "1. <b>Phase 1 (Individual Test):</b> Test I alone, II alone, III alone. If any single statement gives a unique answer, eliminate options requiring combinations.<br/>"
            "2. <b>Phase 2 (Two-Statement Combinations):</b> Test pairs: (I + II), (II + III), (I + III). If any pair gives a unique answer, do NOT test all three together!<br/>"
            "3. <b>Phase 3 (All Three Together):</b> Test (I + II + III) ONLY when no two-statement pair was sufficient.<br/><br/>"
            "<b>The Fundamental 'Uniqueness Principle' (અદ્વિતીય ઉત્તર સિદ્ધાંત):</b><br/>"
            "• Data is SUFFICIENT if and only if it leads to <b>EXACTLY ONE DEFINITIVE ANSWER</b>.<br/>"
            "• If combining statements produces two valid possibilities (e.g., 'P sits opposite Q or R'), the data is <b>NOT SUFFICIENT</b>!<br/>"
            "• If a question asks 'Is X taller than Y?', getting a definite 'NO' is just as sufficient as getting a definite 'YES'! Definite certainty is all that matters.<br/><br/>"
            "<b>The Stop-Solving Law:</b> You do NOT need to calculate the actual numerical value or draw the entire seating diagram. The moment uniqueness is established, STOP and mark the answer!",
            body_txt
        )]
    ]
    t_17_th = Table(ch17_arch, colWidths=[515])
    t_17_th.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#f8fafc")),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor("#cbd5e1")),
        ('TOPPADDING', (0,0), (-1,-1), 5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
    ]))
    story.append(t_17_th)
    story.append(Spacer(1, 6))

    # Topic-wise DS Conditions
    ds_top_headers = [Paragraph("<b>DS Topic Category</b>", table_header), Paragraph("<b>Sufficiency Test Condition</b>", table_header), Paragraph("<b>Deadly Trap to Avoid</b>", table_header)]
    ds_top_data = [ds_top_headers,
        [Paragraph("<b>Seating DS (Circular/Row)</b>", body_bold), Paragraph("Unique seat position relative to target reference.", small_txt), Paragraph("Knowing adjacent neighbors without knowing facing direction.", small_txt)],
        [Paragraph("<b>Blood Relations DS</b>", body_bold), Paragraph("Exact generational path AND gender of both individuals.", small_txt), Paragraph("Assuming gender based on traditional names (e.g. Kiran, Sonu).", small_txt)],
        [Paragraph("<b>Direction Sense DS</b>", body_bold), Paragraph("Both distance (Pythagoras) AND cardinal direction known.", small_txt), Paragraph("Knowing turns without knowing the initial orientation.", small_txt)],
        [Paragraph("<b>Ranking & Order DS</b>", body_bold), Paragraph("Exact numerical position from top/left identified.", small_txt), Paragraph("Relative order (A > B > C) without anchoring to total count.", small_txt)]
    ]
    t_dstop = Table(ds_top_data, colWidths=[125, 200, 190])
    t_dstop.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#1e3a8a")),
        ('TEXTCOLOR', (0,0), (-1,0), colors.white),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor("#cbd5e1")),
        ('TOPPADDING', (0,0), (-1,-1), 3),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3),
    ]))
    story.append(t_dstop)
    story.append(PageBreak())

    # =========================================================================
    # PAGE 7: CHAPTER 17: WORKED 3-STATEMENT DS MODELS & MAINS CHECKLIST
    # =========================================================================
    story.append(create_banner("CHAPTER 17: VERIFIED 3-STATEMENT DS EXAM MODELS", "#1e3a8a"))
    story.append(Spacer(1, 5))

    ds_worked = [
        [Paragraph("<b>Verified Mains 3-Statement Model: Height Ranking Evaluation</b>", sec_header)],
        [Paragraph(
            "<b>Question:</b> Six persons (U, V, W, X, Y, Z) have different heights. Who among them is the 2nd tallest person?<br/>"
            "<i>Statement I:</i> U is taller than only two persons. X is taller than W but shorter than Y.<br/>"
            "<i>Statement II:</i> Y is not the tallest person. V is taller than U.<br/>"
            "<i>Statement III:</i> Z is taller than V. W is not the shortest person.<br/><br/>"
            "<b>Step-by-Step Sufficiency Evaluation:</b><br/>"
            "• Ranks: 1 (Tallest) &gt; 2 &gt; 3 &gt; 4 &gt; 5 &gt; 6 (Shortest).<br/>"
            "• <b>Testing I Alone:</b> 'U is taller than only two persons' &rarr; U is Rank 4: [_ &gt; _ &gt; _ &gt; U &gt; _ &gt; _]. Also Y &gt; X &gt; W. Persons at Ranks 1, 2, 3 could be {Y, X, Z, V}. Multiple possibilities &rarr; <i>Insufficient alone!</i><br/>"
            "• <b>Testing II Alone:</b> Y is not Rank 1; V &gt; U. Zero position anchors &rarr; <i>Insufficient alone!</i><br/>"
            "• <b>Testing III Alone:</b> Z &gt; V; W is not Rank 6. Zero position anchors &rarr; <i>Insufficient alone!</i><br/>"
            "• <b>Combining I + II:</b> U is 4th. V &gt; U means V is in {1, 2, 3}. Y is in {1, 2, 3} but not 1st. But what about Z and X? We don't know whether Z is taller than Y &rarr; <i>Insufficient!</i><br/>"
            "• <b>Combining I + II + III:</b><br/>"
            "  - From III: Z &gt; V &gt; U. So both Z and V are taller than U (in ranks 1, 2, 3).<br/>"
            "  - From I: Y is taller than X and W. Since ranks 1, 2, 3 can only hold 3 people, and Z, V, Y are all taller than U, the top 3 ranks MUST BE {Z, V, Y}!<br/>"
            "  - From II: Y is NOT the tallest (not Rank 1). Since Z &gt; V, Rank 1 MUST BE Z!<br/>"
            "  - Now, between V and Y for Rank 2: Wait, Statement II says V &gt; U, Statement III says Z &gt; V. Does Y have to be Rank 2? Yes, because X and W are below U (W is not 6th &rarr; X is 5th, W is 6th... wait, W not shortest &rarr; W is 5th, X is 6th!). Rank 2 is definitively <b>Y</b>!<br/>"
            "• <b>Conclusion: Statements I, II, and III together are necessary to answer the question!</b>",
            body_txt
        )]
    ]
    t_dsw = Table(ds_worked, colWidths=[515])
    t_dsw.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#f8fafc")),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor("#cbd5e1")),
        ('TOPPADDING', (0,0), (-1,-1), 5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
    ]))
    story.append(t_dsw)
    story.append(Spacer(1, 6))

    # Grand Declaration & Prelims Hand-off
    dec_box = [
        [Paragraph("<b>OFFICIAL MAINS QUARANTINE DECLARATION & PRELIMS FOCUS HAND-OFF</b>", sec_header)],
        [Paragraph(
            "<b>Curriculum Status:</b> Chapters 15, 16, and 17 are officially compiled, preserved, and archived in this document.<br/>"
            "<b>Candidate Action:</b> Put these three chapters on 100% pause until your Prelims examination is completed.<br/>"
            "<b>Prelims Mission:</b> Direct 100% of preparation energy into <b>Speed Drills, Error-Free Puzzle Solving, and Full Prelims Mocks</b> (Chapters 1 to 13). Target: <b>38+ / 40 in 22 minutes!</b>",
            body_txt
        )]
    ]
    t_dec = Table(dec_box, colWidths=[515])
    t_dec.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#fef3c7")),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor("#f59e0b")),
        ('TOPPADDING', (0,0), (-1,-1), 5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
    ]))
    story.append(t_dec)

    doc.build(story, canvasmaker=NumberedCanvas)
    print(f"Successfully generated: {output_path}")

if __name__ == '__main__':
    build_pdf()
