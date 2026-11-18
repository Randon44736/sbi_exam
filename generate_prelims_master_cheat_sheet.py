import os
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.pdfgen import canvas
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, KeepTogether
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase.pdfmetrics import registerFontFamily

# Register Nirmala fonts for perfect English + Gujarati rendering
pdfmetrics.registerFont(TTFont('Nirmala', 'C:/Windows/Fonts/Nirmala.ttc', subfontIndex=0))
pdfmetrics.registerFont(TTFont('Nirmala-Bold', 'C:/Windows/Fonts/Nirmala.ttc', subfontIndex=1))
registerFontFamily('Nirmala', normal='Nirmala', bold='Nirmala-Bold', italic='Nirmala', boldItalic='Nirmala-Bold')

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
        self.setFont("Nirmala-Bold", 8)
        self.setFillColor(colors.HexColor("#0f172a"))
        # Header
        self.drawString(36, 815, "IBPS RRB PO & SBI PRELIMS 2026 | REASONING ABILITY MASTER CHEAT SHEET (સંપૂર્ણ રિવિઝન ચાર્ટ)")
        self.setFont("Nirmala", 8)
        self.setFillColor(colors.HexColor("#64748b"))
        self.drawRightString(559, 815, f"Candidate: Hitendrasinh Solanki | Page {page_num} of {total_pages}")
        self.setStrokeColor(colors.HexColor("#cbd5e1"))
        self.setLineWidth(0.75)
        self.line(36, 808, 559, 808)
        
        # Footer
        self.line(36, 30, 559, 30)
        self.drawString(36, 20, "🎯 TARGET: 38+/40 IN 22 MINUTES | All Tips, Shortcuts, Formulas & 1-Example Identification")
        self.setFont("Nirmala-Bold", 8)
        self.setFillColor(colors.HexColor("#1e3a8a"))
        self.drawRightString(559, 20, "CONFIDENTIAL EXAM PREPARATION")
        self.restoreState()

def create_banner(title_text, bg_hex="#0f172a"):
    p_style = ParagraphStyle(
        'BannerStyle',
        fontName='Nirmala-Bold',
        fontSize=10,
        leading=13,
        textColor=colors.white,
        alignment=1
    )
    t = Table([[Paragraph(f"<b>{title_text}</b>", p_style)]], colWidths=[523])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor(bg_hex)),
        ('TOPPADDING', (0,0), (-1,-1), 3.5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3.5),
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ]))
    return t

def make_rule_box(rule_title, formula_text, trap_text, eg_text, sec_color="#1e3a8a"):
    title_style = ParagraphStyle('RTitle', fontName='Nirmala-Bold', fontSize=8.5, leading=11, textColor=colors.HexColor(sec_color))
    body_style = ParagraphStyle('RBody', fontName='Nirmala', fontSize=7.4, leading=10, textColor=colors.HexColor("#1e293b"))
    trap_style = ParagraphStyle('RTrap', fontName='Nirmala', fontSize=7.2, leading=9.5, textColor=colors.HexColor("#b91c1c"))
    eg_style = ParagraphStyle('REg', fontName='Nirmala', fontSize=7.3, leading=10, textColor=colors.HexColor("#0369a1"))

    content = [
        Paragraph(f"<b>{rule_title}</b>", title_style),
        Spacer(1, 2),
        Paragraph(f"<b>• નિયમ & શોર્ટકટ (Rule/Formula):</b> {formula_text}", body_style),
        Spacer(1, 2),
        Paragraph(f"<b>⚠️ સામાન્ય પરીક્ષા ટ્રેપ (Exam Trap):</b> {trap_text}", trap_style),
        Spacer(1, 2),
        Paragraph(f"<b>💡 ઓળખ & ઉદાહરણ (1 Example Identification):</b> {eg_text}", eg_style),
    ]

    t = Table([[content]], colWidths=[523])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#f8fafc")),
        ('BOX', (0,0), (-1,-1), 0.75, colors.HexColor("#cbd5e1")),
        ('LINELEFT', (0,0), (0,0), 3, colors.HexColor(sec_color)),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
        ('LEFTPADDING', (0,0), (-1,-1), 6),
        ('RIGHTPADDING', (0,0), (-1,-1), 6),
    ]))
    return t

def generate_pdf():
    output_path = r"c:\Users\Lenovo\OneDrive\Desktop\hitu\sbi exam\reasoning ability ch\PRELIMS_REASONING_MASTER_CHEAT_SHEET.pdf"
    doc = SimpleDocTemplate(
        output_path,
        pagesize=A4,
        leftMargin=36,
        rightMargin=36,
        topMargin=40,
        bottomMargin=38
    )

    story = []

    # =========================================================================
    # PAGE 1: CHAPTER 1: INEQUALITIES (અસમાનતાઓ) & PRELIMS SPEED BLUEPRINT
    # =========================================================================
    story.append(create_banner("IBPS RRB PO 2026 | REASONING MASTER CHEAT SHEET (પ્રિલિમ્સ રિવિઝન ચાર્ટ)", "#0f172a"))
    story.append(Spacer(1, 4))

    # Blueprint Intro Box
    bp_style = ParagraphStyle('BP', fontName='Nirmala', fontSize=7.4, leading=10, textColor=colors.HexColor("#0f172a"))
    intro_p = Paragraph(
        "<b>ઉમેદવાર:</b> હિતેન્દ્રસિંહ સોલંકી &nbsp;|&nbsp; <b>લક્ષ્યાંક:</b> IBPS RRB PO પ્રિલિમ્સમાં ૨૨ મિનિટમાં ૩૮+ માર્ક્સ!<br/>"
        "<b>આ ચીટ શીટનો ઉપયોગ કેવી રીતે કરવો:</b> પરીક્ષા આપતા પહેલાં આ PDF ના દરેક નિયમ અને તેની સામે આપેલ ૧ ઉદાહરણ જોઈ લો. પ્રશ્ન જોતાં જ કઈ ટ્રીક વાપરવી તે તરત મગજમાં ક્લિક થશે!",
        bp_style
    )
    t_intro = Table([[intro_p]], colWidths=[523])
    t_intro.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#eff6ff")),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor("#3b82f6")),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
        ('LEFTPADDING', (0,0), (-1,-1), 6),
    ]))
    story.append(t_intro)
    story.append(Spacer(1, 5))

    story.append(create_banner("પ્રકરણ ૧: અસમાનતાઓ (CHAPTER 1: INEQUALITIES — OPEN GATE & SYMBOLS)", "#1e3a8a"))
    story.append(Spacer(1, 4))

    # Rule 1.1: Open Gate Law
    story.append(make_rule_box(
        "૧. ઓપન-ગેટ નિયમ & પ્રતીકોની પ્રાથમિકતા (The Open-Gate Law: King, Soldier, Peon)",
        "દરવાજો હંમેશાં પહોળા મોં તરફથી ખુલે છે: <b>A &gt; B</b> એટલે A થી B જવાય; B થી A બંધ. <br/>"
        "• <b>રાજા (King: &gt;, &lt;):</b> તારણ A &gt; B સાચું કરવા રસ્તામાં ઓછામાં ઓછો એક રાજા હોવો જ જોઈએ!<br/>"
        "• <b>સૈનિક (Soldier: &ge;, &le;):</b> તારણ A &ge; B સાચું કરવા રસ્તાના <i>દરેક</i> દરવાજે સૈનિક કે પટાવાળો હોવો જોઈએ. એક પણ રાજા આવે તો A &ge; B ખોટું પડે!<br/>"
        "• <b>પટાવાળો (Peon: =):</b> બંને બાજુ દરવાજો હંમેશાં ખુલ્લો રાખે છે.",
        "જો રસ્તામાં સામા-સામા દરવાજા (&gt; અને &lt;) આવી જાય તો રસ્તો બ્લોક થાય છે, જેથી કોઈ ચોક્કસ સંબંધ સાચો પડતો નથી.",
        "<b>વિધાન:</b> P &gt; Q &ge; R = S &lt; T. <b>તારણ I:</b> P &gt; S (સાચું: P &rarr; Q &rarr; R &rarr; S ખુલ્લું છે અને રાજા &gt; છે). <b>તારણ II:</b> P &ge; S (ખોટું: રાજા છે એટલે &ge; ન ચાલે). <b>તારણ III:</b> Q &gt; T (ખોટું: R અને S વચ્ચે રસ્તો બ્લોક છે).",
        "#1e3a8a"
    ))
    story.append(Spacer(1, 4))

    # Rule 1.2: Reverse Path Walking
    story.append(make_rule_box(
        "૨. રિવર્સ પાથ વોકિંગ (Reverse Path Chaining — જમણેથી ડાબે મુસાફરી)",
        "જો તારણ ચકાસવા જમણેથી ડાબી બાજુ ચાલવું પડે, તો ચિહ્ન ઊલટું જોવું: ખુલ્લું મોં તમારી સામે હોવું જોઈએ. (દા.ત. M &le; N એટલે N તરફથી M તરફ જવાય).",
        "ચિહ્નને સામાન્ય રીતે ડાબેથી જમણે વાંચવાની ટેવ હોવાથી ઊલટા રસ્તે ગેટ બંધ માની લેવો.",
        "<b>વિધાન:</b> Z &lt; Y &le; X = W. <b>તારણ:</b> W &ge; Y. &rarr; W થી Y ચાલો: W = X &ge; Y. રસ્તો સંપૂર્ણ ખુલ્લો છે અને બધા દરવાજે &ge; છે &rarr; <b>તારણ ૧૦૦% સાચું!</b>",
        "#1e3a8a"
    ))
    story.append(Spacer(1, 4))

    # Rule 1.3: Either-Or Splitting Rule
    story.append(make_rule_box(
        "૩. Either-Or સ્પ્લિટિંગ નિયમ (The Either-Or Splitting Law — વિકલ્પ C)",
        "જો વિધાન પરથી બંને તત્વો વચ્ચે સંબંધ <b>A &ge; B</b> સાબિત થતો હોય, અને તારણોમાં આપેલ હોય: (૧) A &gt; B, (૨) A = B &rarr; બંને એકલા ખોટા છે પરંતુ ભેગા મળીને <b>Either-Or [C]</b> બનાવે છે!",
        "A &ge; B સાચું હોય ત્યારે ઉતાવળમાં A &gt; B ને એકલું સાચું માની લેવું.",
        "<b>વિધાન:</b> K &ge; L = M &ge; N. <b>તારણ I:</b> K &gt; N, <b>તારણ II:</b> K = N. &rarr; સંબંધ K &ge; N બને છે, જે વિભાજીત થઈને {&gt;} અથવા {=} બને છે &rarr; <b>જવાબ: Either I or II follows [C]!</b>",
        "#1e3a8a"
    ))
    story.append(Spacer(1, 4))

    # Rule 1.4: Blocked Path 3-Signs
    story.append(make_rule_box(
        "૪. બ્લોક રસ્તા પર ૩-ચિહ્નો વાળો Either-Or (3 Signs for Blocked Path)",
        "જો બે તત્વો વચ્ચે રસ્તો સામા-સામા ચિહ્નોથી બ્લોક હોય, તો Either-Or બનવા માટે ત્રણેય ચિહ્નો (&gt;, &lt;, =) હાજર હોવા ફરજિયાત છે.",
        "જો માત્ર ૨ ચિહ્નો હાજર હોય (&gt; અને =), તો Neither-Nor [D] આવે, Either-Or નહીં!",
        "<b>વિધાન:</b> A &gt; B &lt; C. <b>તારણ I:</b> A &ge; C, <b>તારણ II:</b> A &lt; C. &rarr; A અને C વચ્ચે રસ્તો બ્લોક છે. તારણ ૧ માં &gt; અને =, તારણ ૨ માં &lt; &rarr; ત્રણેય ચિહ્નો મળી ગયા &rarr; <b>Either I or II follows [C]!</b>",
        "#1e3a8a"
    ))
    story.append(PageBreak())

    # =========================================================================
    # PAGE 2: CHAPTER 2: SYLLOGISMS (સિલોગિઝમ્સ)
    # =========================================================================
    story.append(create_banner("પ્રકરણ ૨: સિલોગિઝમ્સ (CHAPTER 2: SYLLOGISMS — ONLY A FEW, TRAPPED OVERLAP & POSSIBILITIES)", "#065f46"))
    story.append(Spacer(1, 4))

    # Rule 2.1: Only a Few
    story.append(make_rule_box(
        "૧. 'Only a Few' નો બેવડો નિયમ & સંભાવના ટ્રેપ (Only a Few Dual Meaning & Possibility Inversion)",
        "<b>'Only a few A are B' (માત્ર અમુક જ A એ B છે)</b> નો અર્થ એકસાથે બે વસ્તુ થાય છે:<br/>"
        "૧. <b>Some A are B (સાચું)</b> અને ૨. <b>Some A are NOT B (સાચું)</b>.<br/>"
        "• <b>સંભાવના (Possibility):</b> 'All A can be B' &rarr; <b>૧૦૦% અશક્ય (ખોટું)</b>!<br/>"
        "• પરંતુ ઊલટું: 'All B can be A is a possibility' &rarr; <b>૧૦૦% સાચું (શક્ય છે)</b>!",
        "'Only a few' ને સાદું 'Some' સમજીને All A being B ને સાચું માની લેવું.",
        "<b>વિધાન:</b> Only a few Books are Pens. <b>તારણ I:</b> All Books being Pens is a possibility (ખોટું: 0% શક્ય). <b>તારણ II:</b> All Pens being Books is a possibility (સાચું: ૧૦૦% શક્ય). <b>તારણ III:</b> Some Books are not Pens (ચોક્કસ સાચું).",
        "#065f46"
    ))
    story.append(Spacer(1, 4))

    # Rule 2.2: Can Never Be
    story.append(make_rule_box(
        "૨. 'Can Never Be' એટલે Definitely Not (Can Never Be = Definite Negative)",
        "'Can never be' એ સંભાવના નથી, પણ ચોક્કસ નકારાત્મક સત્ય છે. જો કોઈ ભાગ ક્યારેય બીજામાં ન જઈ શકતો હોય તો જ તે સાચું પડે.<br/>"
        "• જો વિધાનો <b>બધા હકારાત્મક (All Positive)</b> હોય, તો 'Can never be' હંમેશાં <b>ખોટું</b> જ પડે!",
        "હકારાત્મક વિધાનોમાં 'Can never be' ને સાચું માની લેવું.",
        "<b>વિધાન:</b> All Men are Strong. Some Strong are Brave. <b>તારણ:</b> Some Men can never be Brave. &rarr; વિધાનો પોઝિટિવ છે, કોઈ દિવાલ નથી, સંભાવના બની શકે &rarr; <b>તારણ ૧૦૦% ખોટું!</b>",
        "#065f46"
    ))
    story.append(Spacer(1, 4))

    # Rule 2.3: Trapped Overlap
    story.append(make_rule_box(
        "૩. ટ્રેપ્ડ ઓવરલેપ નિયમ (The Trapped Overlap Rule — ફસાયેલો ભાગ)",
        "જો Some A are B હોય, All B are C હોય, અને No C is D હોય &rarr; B ની અંદર ફસાયેલો A નો ભાગ ક્યારેય D ને અડી શકતો નથી &rarr; <b>'Some A are not D' ૧૦૦% સાચું બને!</b>",
        "A અને D વચ્ચે સીધી લીટી (No) ન દેખાવાથી તેને ખોટું માની લેવું.",
        "<b>વિધાન:</b> Some Cars are Bikes. All Bikes are Trucks. No Truck is Bus. <b>તારણ:</b> Some Cars are not Buses. &rarr; Bikes વાળી Cars ટ્રકમાં કેદ છે, જે બસ ન હોઈ શકે &rarr; <b>તારણ ૧૦૦% ચોક્કસ સાચું!</b>",
        "#065f46"
    ))
    story.append(Spacer(1, 4))

    # Rule 2.4: Concentric Negative
    story.append(make_rule_box(
        "૪. મકાન અને રૂમનો નિયમ (House & Room Rule — Concentric Negative Inheritance)",
        "જો આખું મકાન (C) કોઈ બીજા સાથે દુશ્મની ધરાવતું હોય (No C is D), તો મકાનની અંદર રહેલા રૂમ (A અને B) પણ D સાથે ક્યારેય સંબંધ રાખી શકે નહીં. (All A in B, All B in C, No C is D &rarr; No A is D સાચું).",
        "અંદરના નાના વર્તુળ માટે નકારાત્મક સંબંધ ભૂલી જવો.",
        "<b>વિધાન:</b> All Stars are Moons. All Moons are Planets. No Planet is Sun. <b>તારણ:</b> No Star is Sun. &rarr; આખું પ્લેનેટ સૂર્ય નથી, તો તેની અંદરનો સ્ટાર પણ સૂર્ય ન જ હોય &rarr; <b>તારણ ૧૦૦% સાચું!</b>",
        "#065f46"
    ))
    story.append(Spacer(1, 4))

    # Rule 2.5: Either-Or in Syllogisms
    story.append(make_rule_box(
        "૫. સિલોગિઝમ્સમાં Either-Or ની '0 અથવા &gt;0' શરત (The 0 or >0 Law: Some + No)",
        "બંને તારણો એકલા ખોટા હોય, વિષય-વિધેય (Elements) એકસરખા હોય, અને જોડી <b>SOME + NO</b> હોય &rarr; ઓવરલેપ કાં તો ૦ (No) હશે અથવા શૂન્યથી વધુ (Some) &rarr; <b>Either-Or [C]</b>!",
        "⚠️ <b>ચેતવણી:</b> `ALL + NO` ક્યારેય Either-Or બનતું નથી (Neither-Nor [D] આવે).",
        "<b>વિધાન:</b> Some Chairs are Desks. No Desk is Bench. <b>તારણ I:</b> Some Chairs are Benches. <b>તારણ II:</b> No Chair is Bench. &rarr; બંને એકલા શંકાસ્પદ ખોટા છે, જોડી Some + No છે &rarr; <b>જવાબ: Either I or II follows [C]!</b>",
        "#065f46"
    ))
    story.append(PageBreak())

    # =========================================================================
    # PAGE 3: CHAPTER 3 & 4: ALPHANUMERIC & CODING-DECODING
    # =========================================================================
    story.append(create_banner("પ્રકરણ ૩ & ૪: આલ્ફાન્યૂમેરિક શ્રેણી અને કોડિંગ-ડીકોડિંગ (SERIES & CODING)", "#475569"))
    story.append(Spacer(1, 4))

    # Rule 3.1: Direction Shifting
    story.append(make_rule_box(
        "૧. સરખી દિશા બાદબાકી, વિરુદ્ધ દિશા સરવાળો (Direction Rules in Series)",
        "• સરખી દિશા (Left to Left અથવા Right to Right) &rarr; <b>બાદબાકી કરો (L - L અથવા R - R)</b>.<br/>"
        "• વિરુદ્ધ દિશા (Left to Right અથવા Right to Left) &rarr; <b>સરવાળો કરો (L + R અથવા R + L)</b>.<br/>"
        "હંમેશાં પ્રશ્નમાં છેલ્લે પૂછાયેલ છેડેથી ગણતરી કરવી (દા.ત. 'from the left end').",
        "ડાબે-જમણે ગૂંચવાઈને બંને વખતે અલગ-અલગ ગણતરી કરીને સમય બગાડવો.",
        "<b>શ્રેણી:</b> A 4 & B 9 @ C 2 D 5 E... &rarr; <b>પ્રશ્ન:</b> 'Which element is 4th to the right of 9th from the left?' &rarr; વિરુદ્ધ દિશા (Right of Left) = 9 + 4 = <b>13th from Left</b>. સીધું ૧૩મું તત્વ ગણી લો!",
        "#475569"
    ))
    story.append(Spacer(1, 4))

    # Rule 3.2: Preceded by vs Followed by
    story.append(make_rule_box(
        "૨. 'આગળ' અને 'પાછળ' માળખું (Preceded By vs Followed By Framework)",
        "• <b>Preceded by X (X આગળ / પહેલાં):</b> `[ X ] &rarr; [ મુખ્ય તત્વ / TARGET ]`<br/>"
        "• <b>Followed by Y (Y પાછળ / પછી):</b> `[ મુખ્ય તત્વ / TARGET ] &rarr; [ Y ]`<br/>"
        "સંપૂર્ણ સમીકરણ: `[ X ] &rarr; [ TARGET ] &rarr; [ Y ]` (પહેલાં X, વચ્ચે Target, પછી Y).",
        "'Preceded' અને 'Followed' ના અર્થ ઊલટા સમજીને આગળ-પાછળ ખોટું ચેક કરવું.",
        "<b>પ્રશ્ન:</b> 'How many consonants are immediately preceded by a number and followed by a symbol?' &rarr; માળખું: <b>[Number] &rarr; [Consonant] &rarr; [Symbol]</b>. શ્રેણીમાં '7 B @' મળે તો ૧ જોડી બની!",
        "#475569"
    ))
    story.append(Spacer(1, 4))

    # Rule 4.1: Chinese Coding Elimination
    story.append(make_rule_box(
        "૩. ચાઇનીઝ સબસ્ટીટ્યુશન કોડિંગ (Chinese Coding 2-Line Elimination)",
        "આખી લાઈનો ડીકોડ કરવાની જરૂર નથી! જે શબ્દ પૂછાયો હોય તે કઈ બે લાઈનમાં કોમન છે તે જુઓ. જમણી બાજુ જે કોડ બંને લાઈનમાં કોમન હોય તે જ સીધો જવાબ!",
        "બધા શબ્દો રફ શીટમાં લખીને ૧.૫ મિનિટ બગાડવી. માત્ર સામાન્ય શબ્દ સ્ક્રીન પર જોઈને ઉડાડો.",
        "Line 1: 'bank exam score high' = 'la ka ta pa'<br/>Line 2: 'bank rank easy clear' = 'ka ma da za'<br/>&rarr; બંને લાઈનમાં માત્ર 'bank' સામાન્ય છે, સામે કોડમાં માત્ર 'ka' સામાન્ય છે &rarr; <b>'bank' = 'ka'! (૩ સેકન્ડ)</b>",
        "#475569"
    ))
    story.append(Spacer(1, 4))

    # Rule 4.2: Means vs Is Called
    story.append(make_rule_box(
        "૪. 'MEANS' વિરુદ્ધ 'IS CALLED' ની ખાલી જગ્યા પદ્ધતિ (The Means vs Is Called Rule)",
        "• <b>'IS CALLED' (કહેવાય છે):</b> જવાબ <b>જમણી બાજુનો આગળનો શબ્દ</b> આવે. (દા.ત. 'Red is called Blue' &rarr; લોહીનો રંગ Blue કહેવાય).<br/>"
        "• <b>'MEANS' (નો અર્થ થાય છે):</b> જવાબ <b>ડાબી બાજુનો શબ્દ</b> આવે! ફોર્મ્યુલા: `[ ? ] means [ સાચો જવાબ ]`.",
        "'Means' માં 'Is called' ની જેમ આગળનો શબ્દ ટીક કરી દેવો.",
        "<b>પ્રશ્ન:</b> 'Sky is called Sea, Sea is called Water, Water is called Air.' Where do fish live? &rarr; માછલી Water માં રહે, 'Water is called Air' &rarr; <b>Air [સાચો જવાબ]</b>.<br/>જો 'means' હોય: 'Sea means Water' &rarr; માછલી Water માં રહે, એટલે <b>Sea [સાચો જવાબ]</b>!",
        "#475569"
    ))
    story.append(PageBreak())

    # =========================================================================
    # PAGE 4: CHAPTER 5: BLOOD RELATIONS & DIRECTION SENSE
    # =========================================================================
    story.append(create_banner("પ્રકરણ ૫: લોહીના સંબંધો અને દિશા-અંતર (BLOOD RELATIONS & DIRECTIONS)", "#b45309"))
    story.append(Spacer(1, 4))

    # Rule 5.1: Generation Stacking
    story.append(make_rule_box(
        "૧. પેઢી સ્તર પદ્ધતિ (Generation Level Stacking Framework)",
        "• <b>સમાન આડી લાઈન (Level 0):</b> ભાઈ-બહેન (`A — B`), પરિણીત યુગલ (`A = B`).<br/>"
        "• <b>ઊભો ઘટાડો (Level -1):</b> સંતાનો હંમેશાં નીચે આવે (`↓`).<br/>"
        "• <b>ઊભો વધારો (Level +1):</b> માતા-પિતા હંમેશાં ઉપર આવે (`↑`).<br/>"
        "લેવલ ગણતરી: ૦ તફાવત = ભાઈ/બહેન/પતિ/પત્ની/કઝિન; ૧ તફાવત = પિતા/માતા/કાકા/મામા/સસરા; ૨ તફાવત = દાદા/દાદી/નાના/નાની.",
        "પતિ-પત્ની કે ભાઈ-બહેનને ઊભા ગોઠવીને પેઢીઓની ગણતરીમાં સસરાને દાદા બનાવી દેવા.",
        "M is father of N, N is sister of O, O is mother of P. &rarr; લેવલ: M (+1) &rarr; N, O (0) &rarr; P (-1). M અને P વચ્ચે ૨ પેઢીનો તફાવત છે &rarr; <b>M એ P ના નાના (Maternal Grandfather) થાય!</b>",
        "#b45309"
    ))
    story.append(Spacer(1, 4))

    # Rule 5.2: In-Law vs Grand & Gender Trap
    story.append(make_rule_box(
        "૨. 'In-Law' વિરુદ્ધ 'Grand-' શબ્દાવલી & નામ પરથી જાતિ નક્કી ન કરવાનો નિયમ",
        "• <b>'-IN-LAW' (સાસરિયાં):</b> માત્ર અને માત્ર <b>લગ્ન (Marriage)</b> દ્વારા જ અસ્તિત્વમાં આવે! (દા.ત. પત્નીના પિતા = Father-in-law).<br/>"
        "• <b>'GRAND-' (દાદા/નાના):</b> સીધો ૨ પેઢીનો લોહીનો સંબંધ છે. માતાના પિતા એટલે 'નાના', સસરા નહીં!<br/>"
        "• ⚠️ <b>જાતિ (Gender):</b> નામ પરથી ક્યારેય પુરુષ/સ્ત્રી નક્કી ન થાય ('કિરણ', 'સોનુ'). માત્ર 'he/she' કે 'brother/sister' થી જ નક્કી થાય.",
        "નામ પરથી પુરુષ માની લેવું અને છેલ્લે વિકલ્પ 'Cannot be determined' આવતો હોય છતાં ભૂલ કરવી.",
        "P is child of Q. Q is husband of R. &rarr; P ની જાતિ (મેલ કે ફીમેલ) આપેલી નથી! જો પૂછાય 'How is P related to R?' &rarr; જવાબ: <b>Son or Daughter (અથવા Cannot be determined)!</b>",
        "#b45309"
    ))
    story.append(Spacer(1, 4))

    # Rule 5.3: Pythagoras Triplets
    story.append(make_rule_box(
        "૩. પાયથાગોરસ લઘુત્તમ અંતર ત્રિપુટીઓ (Pythagoras Shortest Distance Shortcuts)",
        "પ્રારંભિક બિંદુથી લઘુત્તમ અંતર = $D = \\sqrt{(\\Delta X)^2 + (\\Delta Y)^2}$.<br/>"
        "પરીક્ષાની સૌથી વધુ પૂછાતી ત્રિપુટીઓ મોઢે યાદ રાખો: <b>(3, 4 &rarr; 5)</b>, <b>(6, 8 &rarr; 10)</b>, <b>(5, 12 &rarr; 13)</b>, <b>(8, 15 &rarr; 17)</b>.",
        "કાટકોણ ત્રિકોણમાં સીધો સરવાળો (૬ + ૮ = ૧૪) કરી દેવો.",
        "એક વ્યક્તિ ઉત્તરમાં 12m ચાલે છે, પછી જમણે વળી પૂર્વમાં 5m ચાલે છે. પ્રારંભિક બિંદુથી અંતર: $\\sqrt{12^2 + 5^2} = \\sqrt{144 + 25} = \\sqrt{169} = \\mathbf{13m}$ (દિશા: North-East).",
        "#b45309"
    ))
    story.append(Spacer(1, 4))

    # Rule 5.4: Shadow Rules
    story.append(make_rule_box(
        "૪. સૂર્ય અને પડછાયાનો નિયમ & સામસામે ચહેરાની અદલાબદલી (Shadow Inversion Rule)",
        "• <b>સવારે (Sunrise - પૂર્વમાં):</b> પડછાયો હંમેશાં <b>પશ્ચિમ (West)</b> માં પડે.<br/>"
        "  - જો પડછાયો ડાબી બાજુ પડે &rarr; મુખ <b>ઉત્તર (North)</b> તરફ.<br/>"
        "  - જો પડછાયો જમણી બાજુ પડે &rarr; મુખ <b>દક્ષિણ (South)</b> તરફ.<br/>"
        "• ⚠️ <b>સામસામે ઉભેલા મિત્રો:</b> આપેલ વ્યક્તિની દિશા શોધો, અને સામે ઉભેલા મિત્ર માટે દિશા <b>ઊંધી (Opposite)</b> કરો! (ઉત્તરનું ઊંધું દક્ષિણ).",
        "મોહિતની દિશા (North) ગણીને સુમિતના પ્રશ્નમાં પણ North ટીક કરી દેવું.",
        "એક સવારે અમિત અને સુમિત સામસામે વાત કરે છે. જો અમિતનો પડછાયો અમિતની ડાબી બાજુ પડતો હોય, તો સુમિતનું મુખ કઈ દિશામાં હશે? &rarr; સવારે ડાબી બાજુ પડછાયો એટલે અમિત = <b>North</b>. સુમિત તેની સામે છે એટલે સુમિત = <b>South [સાચો જવાબ]!</b>",
        "#b45309"
    ))
    story.append(PageBreak())

    # =========================================================================
    # PAGE 5: CHAPTER 6 & 9: ORDER & RANKING / INPUT-OUTPUT
    # =========================================================================
    story.append(create_banner("પ્રકરણ ૬ & ૯: ક્રમ-સરખામણી અને મશીન ઇનપુટ-આઉટપુટ (RANKING & MACHINE I/O)", "#1e3a8a"))
    story.append(Spacer(1, 4))

    # Rule 6.1: Single Person Total
    story.append(make_rule_box(
        "૧. એક જ વ્યક્તિના બંને બાજુના ક્રમ પરથી કુલ સંખ્યા (Single Person Total & Position)",
        "• <b>કુલ સંખ્યા (Total):</b> $T = L + R - 1$ (ડાબેથી ક્રમ + જમણેથી ક્રમ - ૧).<br/>"
        "• <b>બીજી બાજુનો ક્રમ:</b> $R = T - L + 1$ અથવા $L = T - R + 1$.<br/>"
        "(૧ શા માટે બાદ થાય છે? કારણ કે તે એક જ વ્યક્તિ બે વાર ગણાઈ જાય છે).",
        "કુલ સંખ્યા શોધવામાં -1 કરવાનું ભૂલી જવું, અથવા ક્રમ શોધવામાં +1 કરવાનું ભૂલી જવું.",
        "૪૦ વિદ્યાર્થીઓની લાઈનમાં રોહન ડાબેથી ૧૫મો છે. જમણેથી તેનો ક્રમ કેટલો? &rarr; $R = 40 - 15 + 1 = 25 + 1 = \\mathbf{26}$ <b>મો ક્રમ!</b>",
        "#1e3a8a"
    ))
    story.append(Spacer(1, 4))

    # Rule 6.2: Overlapping vs Non-overlapping
    story.append(make_rule_box(
        "૨. વચ્ચે બેઠેલી વ્યક્તિઓ: ઓવરલેપિંગ વિરુદ્ધ નોન-ઓવરલેપિંગ (Between Persons & Overlapping)",
        "• <b>નોન-ઓવરલેપિંગ (જો $T > L + R$ હોય):</b> વચ્ચેની સંખ્યા $M = T - (L + R)$.<br/>"
        "• <b>ઓવરલેપિંગ કેસ (જો $L + R > T$ હોય):</b> વચ્ચેની સંખ્યા $M = (L + R) - T - 2$!<br/>"
        "(ઓવરલેપમાં ૨ શા માટે બાદ થાય? કારણ કે બંને વ્યક્તિઓ એકબીજાને ક્રોસ કરતી વખતે વધારાની ગણાઈ જાય છે).",
        "ઓવરલેપિંગ કેસમાં સાદી બાદબાકી કરી દેવી અને -2 કરવાનું ભૂલી જવું.",
        "૫૦ વ્યક્તિઓની હરોળમાં A ડાબેથી ૩૦મો અને B જમણેથી ૨૫મો છે. વચ્ચે કેટલા? &rarr; $30 + 25 = 55 > 50$ (ઓવરલેપ!). વચ્ચેની સંખ્યા = $55 - 50 - 2 = 5 - 2 = \\mathbf{3}$ <b>વ્યક્તિઓ!</b>",
        "#1e3a8a"
    ))
    story.append(Spacer(1, 4))

    # Rule 9.1: Pen-Free Numbering in Machine I/O
    story.append(make_rule_box(
        "૩. મશીન ઇનપુટ-આઉટપુટ: પેન-ફ્રી નંબરિંગ પદ્ધતિ (Pen-Free Element Labeling Shortcut)",
        "આખી શ્રેણી વારંવાર નીચે લખવાને બદલે મૂળ ઇનપુટમાં જ તત્વો પર સ્ટેપ નંબર લખો:<br/>"
        "• ડાબે ગોઠવાતા તત્વો: $L_1, L_2, L_3 \\dots$ &nbsp;|&nbsp; જમણે ગોઠવાતા તત્વો: $R_1, R_2, R_3 \\dots$<br/>"
        "• <b>ઓટો-અરેન્જ નિયમ:</b> જો કોઈ તત્વ તેના ક્રમ વખતે પહેલેથી જ યોગ્ય જગ્યાએ બેઠેલું હોય, તો તે <b>૦ સ્ટેપ</b> વાપરે છે (નવું સ્ટેપ ગણવું નહીં!).",
        "ઓટો-અરેન્જ થયેલા તત્વ માટે અલગ સ્ટેપ ગણીને કુલ સ્ટેપ્સ વધારે બતાવી દેવા.",
        "શબ્દો ડાબે A-Z અને સંખ્યાઓ જમણે ઉતરતા ક્રમમાં ગોઠવાય છે. જો સૌથી મોટો નંબર પહેલાથી જ છેલ્લે બેઠો હોય, તો તે $R_1$ તરીકે ૦ સ્ટેપ લેશે!",
        "#1e3a8a"
    ))
    story.append(Spacer(1, 4))

    # Rule 9.2: Backward Inversion Trap
    story.append(make_rule_box(
        "૪. ધ રિવર્સ ઇન્વર્ઝન લો (The Step Inversion Backward Law — સીધો ૧ માર્ક બચાવો!)",
        "જો પ્રશ્નમાં પૂછાય: <i>'સ્ટેપ ૩ આપેલ છે, તો ઇનપુટ શું હતું?'</i> અથવા <i>'સ્ટેપ ૪ પરથી સ્ટેપ ૨ શોધો'</i> &rarr; કોઈપણ મશીન ઇનપુટ-આઉટપુટમાં પાછળ (પાછલા સ્ટેપ કે ઇનપુટ તરફ) ક્યારેય જઈ શકાતું નથી!<br/>"
        "• <b>સાચો જવાબ હંમેશાં: 'Cannot be determined' (નક્કી ન થઈ શકે)</b> આંખો બંધ કરીને ૨ સેકન્ડમાં ટીક કરો!",
        "પાછળ જવાની ગણતરીમાં રફ પેપર ભરીને ૨ મિનિટ બગાડવી.",
        "<b>પ્રશ્ન:</b> 'If Step IV of an input is: apple 92 cat 85 dog 41, what will be Step II?' &rarr; સીધો જવાબ: <b>Cannot be determined [ઓપ્શન D/E]!</b>",
        "#1e3a8a"
    ))
    story.append(PageBreak())

    # =========================================================================
    # PAGE 6: CHAPTER 7 & 8: SEATING & PUZZLES CORE
    # =========================================================================
    story.append(create_banner("પ્રકરણ ૭ & ૮: બેઠક વ્યવસ્થા અને પઝલ્સ મૂળભૂત (SEATING & PUZZLES CORE)", "#065f46"))
    story.append(Spacer(1, 4))

    # Rule 7.1: Circular/Square Compass
    story.append(make_rule_box(
        "૧. ગોળાકાર ટેબલ: અંદર વિરુદ્ધ બહાર મુખની હોકાયંત્ર દિશા (Circular/Square Facing Compass)",
        "• <b>અંદર મુખ (Facing Center):</b> Right = ઘડિયાળની વિરુદ્ધ દિશા (Counter-Clockwise); Left = ઘડિયાળની દિશા (Clockwise).<br/>"
        "• <b>બહાર મુખ (Facing Outside):</b> <b>Right = ઘડિયાળની દિશા (Clockwise); Left = ઘડિયાળની વિરુદ્ધ દિશા (Counter-Clockwise).</b><br/>"
        "(બહાર જોતી વ્યક્તિ માટે તમારો જે જમણો હાથ છે તે જ તેનો જમણો હાથ બને છે!).",
        "બહાર જોતી વ્યક્તિ માટે અંદરવાળો નિયમ વાપરીને જમણે અને ડાબે ઊંધા બેસાડી દેવા.",
        "૮ વ્યક્તિઓ વર્તુળમાં બહાર મુખ રાખીને બેઠા છે. P ના જમણે બીજો Q છે. &rarr; P થી <b>ઘડિયાળની દિશામાં (Clockwise)</b> ૨ સ્ટેપ ચાલો &rarr; Q નું સ્થાન ફિક્સ!",
        "#065f46"
    ))
    story.append(Spacer(1, 4))

    # Rule 7.2: Two Parallel Cases
    story.append(make_rule_box(
        "૨. બે સમાંતર કેસનો સુવર્ણ નિયમ (The Two Parallel Cases Golden Rule)",
        "પઝલ કે સીટિંગમાં જ્યારે પહેલી શરતમાં ૨ શક્યતાઓ દેખાય (દા.ત. P ડાબે છેડે અથવા જમણે છેડે), ત્યારે મગજમાં વિચારવાને બદલે તાત્કાલિક રફ પેપર પર <b>Case 1</b> અને <b>Case 2</b> સમાંતર દોરી નાખો.<br/>"
        "આગળ જતાં ૧ શરત એક કેસને આપોઆપ ઉડાડી દેશે અને સાચો કેસ ૧૦૦% સાચો ઉકેલાઈ જશે!",
        "એક જ ડાયાગ્રામમાં છેકછાક કરીને ગૂંચવાઈ જવું અને આખી પઝલ ફરી શરૂ કરવી.",
        "P sits at one of the extreme ends. &rarr; રફ પેપરમાં તરત જ: Case 1 માં P ને ડાબે છેડે (૧) બેસાડો, Case 2 માં P ને જમણે છેડે (૮) બેસાડો. ૨ મિનિટમાં પઝલ સોલ્વ!",
        "#065f46"
    ))
    story.append(Spacer(1, 4))

    # Rule 8.1: Floor Puzzles Setup
    story.append(make_rule_box(
        "૩. ફ્લોર પઝલ: ગ્રાઉન્ડ ફ્લોર ૧ થી ટોપ ફ્લોર સુધીનું ફિક્સ માળખું (Floor Puzzle Setup)",
        "હંમેશાં રફ શીટમાં ઊભા નંબરો લખો: સૌથી ઉપર ટોપ ફ્લોર (દા.ત. ૭, ૬, ૫, ૪, ૩, ૨, ૧).<br/>"
        "• 'Three persons live between A and B' &rarr; $|\\text{Floor}_A - \\text{Floor}_B| = 4$ (વચ્ચે ૩ ફ્લોર એટલે તફાવત ૪ થાય!).<br/>"
        "• 'A lives immediately above B' &rarr; $\\text{Floor}_A = \\text{Floor}_B + 1$.",
        "વચ્ચે ૩ વ્યક્તિઓ કીધી હોય ત્યારે તફાવત ૩ ગણી લેવો (૪ ગણવો જોઈએ).",
        "A lives on floor 6. Three floors between A and B. B lives below A. &rarr; Floor of B = $6 - (3 + 1) = 6 - 4 = \\mathbf{2}$ (Floor 2)! વચ્ચે 3, 4, 5 ત્રણ માળ આવ્યા.",
        "#065f46"
    ))
    story.append(Spacer(1, 4))

    # Rule 8.2: Month-Date Puzzles
    story.append(make_rule_box(
        "૪. મહિના-તારીખ પઝલ: ૩૦ વિરુદ્ધ ૩૧ દિવસની એન્કરિંગ પદ્ધતિ (Month-Date 30/31 Day Anchoring)",
        "પરીક્ષામાં સામાન્ય રીતે ૪ મહિના અને ૨ તારીખો (દા.ત. ૭ અને ૨૦) આપેલા હોય છે.<br/>"
        "• સૌથી પહેલાં દરેક મહિનાના દિવસો લખી લો: <b>April (30), May (31), June (30), July (31)</b>.<br/>"
        "• ક્લૂ: 'P was born in a month having 30 days on an odd date' &rarr; સીધું April 7 અથવા June 7 જ આવે! (માત્ર ૨ શક્યતાઓ).",
        "મહિનાના દિવસો (૩૦ કે ૩૧) લખ્યા વગર સીધા વ્યક્તિઓ બેસાડવા જવું.",
        "P is born in a 30-day month on 7th. &rarr; માત્ર ૨ કેસ: Case 1 (April 7), Case 2 (June 7). બાકીના વ્યક્તિઓ આ એન્કરની આસપાસ તરત ગોઠવાઈ જશે!",
        "#065f46"
    ))
    story.append(PageBreak())

    # =========================================================================
    # PAGE 7: CHAPTER 10 & 11: DATA SUFFICIENCY & MISCELLANEOUS
    # =========================================================================
    story.append(create_banner("પ્રકરણ ૧૦ & ૧૧: ડેટા સફિશિયન્સી અને પરચૂરણ રીઝનિંગ (DATA SUFFICIENCY & MISC)", "#475569"))
    story.append(Spacer(1, 4))

    # Rule 10.1: DS Elimination
    story.append(make_rule_box(
        "૧. ડેટા સફિશિયન્સી: ૨-વિધાનોનો સિસ્ટમેટિક એલિમિનેશન ટ્રી (Data Sufficiency 2-Statement Tree)",
        "૧. પહેલાં Statement I એકલું ચકાસો &rarr; જો અનન્ય (Unique) જવાબ આપે તો [A] અથવા [D] ની શક્યતા.<br/>"
        "૨. Statement II એકલું ચકાસો &rarr; જો અનન્ય જવાબ આપે અને I પણ આપતું હોય તો <b>[D] (Either I alone or II alone)</b>!<br/>"
        "૩. જો બંને એકલા નિષ્ફળ જાય તો જ <b>(I + II) ભેગા કરો</b> &rarr; જો ભેગા મળીને ૧ ચોક્કસ જવાબ આપે તો <b>[E] (Both together necessary)</b>, ન આપે તો <b>[C] (Neither sufficient)</b>.",
        "પ્રશ્નનો વાસ્તવિક ગણતરી કરીને છેલ્લો જવાબ કાઢવામાં ૪૫ સેકન્ડ બગાડવી. માત્ર એટલું જ નક્કી કરવાનું છે કે ચોક્કસ જવાબ મળે છે કે નહીં!",
        "<b>પ્રશ્ન:</b> Who is tallest among A, B, C? St I: A is taller than B and C. &rarr; I એકલું પર્યાપ્ત છે (A tallest). St II: B is shortest. &rarr; II એકલું પર્યાપ્ત નથી (A કે C નક્કી નથી). &rarr; <b>જવાબ: Statement I alone is sufficient!</b>",
        "#475569"
    ))
    story.append(Spacer(1, 4))

    # Rule 10.2: Definite NO is Sufficient
    story.append(make_rule_box(
        "૨. ડેટા સફિશિયન્સીમાં ચોક્કસ 'ના' પણ ૧૦૦% પર્યાપ્ત છે (Definite NO is 100% Sufficient)",
        "જો પ્રશ્ન પૂછે: <i>'શું P ઉત્તર તરફ મુખ રાખીને બેઠો છે?'</i> અને વિધાન પરથી સાબિત થાય કે <b>'ના, P દક્ષિણ તરફ બેઠો છે'</b> &rarr; આ ડેટા ૧૦૦% પર્યાપ્ત (Sufficient) છે!<br/>"
        "કારણ કે તમને પ્રશ્નનો ચોક્કસ નિશ્ચિત જવાબ મળી ગયો છે. પર્યાપ્તતા એટલે માત્ર 'હા' નહીં, પણ ચોક્કસ 'ના' પણ પર્યાપ્ત છે!",
        "'ના' જવાબ આવતો હોવાથી ડેટા અધૂરો માનીને Not Sufficient ટીક કરી દેવું.",
        "Is P facing North? Statement says: P faces South. &rarr; Definite answer is NO &rarr; <b>Data is SUFFICIENT!</b>",
        "#475569"
    ))
    story.append(Spacer(1, 4))

    # Rule 11.1: Alphabet Numerical Translation
    story.append(make_rule_box(
        "૩. અક્ષર જોડી ગણતરી: આલ્ફાબેટને નંબરમાં ફેરવવાની સુપર-ટ્રીક (Letter Pairs Numerical Translation)",
        "મનમાં 'A, B, C, D...' ગણવાને બદલે અક્ષરોની ઉપર તેના ક્રમાંક લખી દો: <b>A=1, B=2, ..., Z=26</b>.<br/>"
        "હવે કોઈપણ અંકથી આગળ અને પાછળ ક્રમિક એકડા બોલો (દા.ત. ૧૬ થી શરૂ કરો તો ૧૭, ૧૮, ૧૯...). જે બોલો તે જ અંક સ્ક્રીન પર દેખાય એટલે ૧ જોડી રોકડી!",
        "રિવર્સ ગણતરીમાં મગજ ગૂંચવાઈ જવું અને Z થી ઊંધી ABCD બોલવામાં ભૂલ કરવી.",
        "શબ્દ: <b>POST</b> &rarr; નંબરો: <b>16, 15, 19, 20</b>. ૧૯ પછી બોલો '૨૦' અને સામે ૨૦ જ છે &rarr; (19, 20 એટલે S, T) એક જોડી! પાછળ: ૧૫ પછી '૧૬' બોલો અને સામે ૧૬ જ છે &rarr; (15, 16 એટલે O, P) બીજી જોડી!",
        "#475569"
    ))
    story.append(Spacer(1, 4))

    # Rule 11.2: Meaningful Word 1-X-Y Rule
    story.append(make_rule_box(
        "૪. અર્થપૂર્ણ શબ્દ બનાવવાનો ૧-X-Y સ્કીપ નિયમ (Meaningful Word 1-X-Y Skip Strategy)",
        "પરીક્ષામાં જો આપેલ અક્ષરો પરથી ૧ શબ્દ બને તો તેનો પહેલો અક્ષર, ૧ થી વધુ બને તો 'X', અને એક પણ ન બને તો 'Y' પૂછાય છે.<br/>"
        "• <b>ટોપર સ્ટ્રેટેજી:</b> અંગ્રેજી શબ્દભંડોળ અસીમિત છે. જો ૧૫ સેકન્ડમાં સામાન્ય શબ્દ ન દેખાય, તો આ પ્રશ્ન <b>તરત છોડી દો (Skip)</b> અને ૨૪મી મિનિટે રિવ્યૂ કરો. નેગેટિવ માર્કિંગથી બચવાનો આ બેસ્ટ રસ્તો છે!",
        "અજાણ્યા શબ્દોના તુક્કા લગાવીને રોકડા ૦.૨૫ માર્ક્સ ગુમાવવા.",
        "અક્ષરો: E, A, T, M &rarr; TEAM, MEAT, MATE, TAME (૪ શબ્દો બને છે!). એકાદ શબ્દ ચૂકી જવાનો ભય રહે છે, તેથી જો ૧૦૦% ખાતરી ન હોય તો સ્કીપ કરવો.",
        "#475569"
    ))
    story.append(PageBreak())

    # =========================================================================
    # PAGE 8: CHAPTER 12 & 13: ADVANCED PUZZLES & ADVANCED SEATING
    # =========================================================================
    story.append(create_banner("પ્રકરણ ૧૨ & ૧૩: અદ્યતન પઝલ્સ અને બેઠક વ્યવસ્થા (ADVANCED PUZZLES & SEATING)", "#b45309"))
    story.append(Spacer(1, 4))

    # Rule 12.1: Floor + Flat
    story.append(make_rule_box(
        "૧. ફ્લોર + ફ્લેટ પઝલ (૪ માળ × ૨ ફ્લેટ: Flat A & Flat B Matrix)",
        "• રફ પેપરમાં ગ્રીડ: ઊભા માળ ૪, ૩, ૨, ૧ &rarr; ડાબી કોલમ Flat A (West), જમણી કોલમ Flat B (East).<br/>"
        "• 'P lives immediately above Q in the same flat' &rarr; P અને Q એક જ કોલમમાં ક્રમિક માળ પર.<br/>"
        "• 'P lives North-East of Q' &rarr; Q નીચલા માળે Flat A માં હશે, અને P ઉપલા માળે Flat B માં હશે!",
        "'Immediately above' માં ફ્લેટ અલગ હોઈ શકે તે ભૂલી જવું.",
        "B lives on an even floor in Flat A. C lives East of B. &rarr; Floor 4 અથવા 2. Flat A = B, Flat B = C. જો Floor 4 લઈએ તો Flat A(4)=B, Flat B(4)=C!",
        "#b45309"
    ))
    story.append(Spacer(1, 4))

    # Rule 12.2: Designation Hierarchy
    story.append(make_rule_box(
        "૨. હોદ્દાની પઝલ: સિનિયરથી જુનિયર ફિક્સ કરોડરજ્જુ (Designation Hierarchy Fixed Backbone)",
        "હંમેશાં સિનિયરથી જુનિયર ઊભો ક્રમ અગાઉથી લખી લો: `Chairman > GM > DGM > AGM > Manager > Officer > Clerk`.<br/>"
        "• 'R is senior to only two persons' &rarr; R સીધો <b>Manager (Rank 5)</b> પર જ આવે!<br/>"
        "• આ ફિક્સ કરોડરજ્જુ પર બાકીના વ્યક્તિઓના કેસ ઝડપથી બેસી જશે.",
        "વ્યક્તિઓના નામ પરથી પઝલ બનાવવી અને હોદ્દા ગૂંચવી નાખવા.",
        "૭ હોદ્દામાં 'P is senior to only three persons' &rarr; Clerk(7), Officer(6), Manager(5) થી સિનિયર &rarr; P = <b>AGM (Rank 4)</b>!",
        "#b45309"
    ))
    story.append(Spacer(1, 4))

    # Rule 13.1: Top-Edge Outside Inversion Trap
    story.append(make_rule_box(
        "૩. ચોરસ ટેબલ: બહાર જોતી ટોપ-એજ વ્યક્તિનો નિયમ (Top-Edge Facing Outside Compass Fix)",
        "ટેબલની ઉપરની ધાર (Top Middle) પર બેઠેલી વ્યક્તિ જો <b>બહાર (Outside &uarr;)</b> જોતી હોય, તો તે ઉત્તર તરફ જોઈ રહી છે.<br/>"
        "• <b>નિયમ:</b> ઉત્તર તરફ જોતી વખતે <b>તમારો જમણો હાથ તે જ તેનો જમણો હાથ (East / Clockwise)</b> બને છે! અહીં દિશા ઊલટી કરવી નહીં!",
        "ટોપ પર બેઠેલી વ્યક્તિ બહાર જોતી હોવા છતાં તેને અંદર જોતી માનીને જમણે બદલે ડાબે ગણી લેવું (Ch 13 માં આ ભૂલ થઈ હતી).",
        "U ચોરસ ટેબલની ટોપ એજ પર બહાર (&uarr;) જોવે છે. U ના જમણે બીજો કોણ? &rarr; ઉત્તર મુખ હોવાથી Right = Clockwise (જમણી બાજુ &rarr; East) &rarr; ટોપ-રાઈટ કોર્નર અને પછી રાઈટ એજ પર પહોંચશો!",
        "#b45309"
    ))
    story.append(Spacer(1, 4))

    # Rule 13.2: Step-Zero Law & Triangular Parity
    story.append(make_rule_box(
        "૪. સ્ટેપ-ઝીરો નિયમ & ત્રિકોણાકાર ટેબલ એકાંતર નિયમ (Step-Zero Law & Triangular Parity)",
        "• <b>સ્ટેપ-ઝીરો નિયમ:</b> મૂળ સંદર્ભ વ્યક્તિ હંમેશાં <b>Step 0</b> છે. ૧ સ્ટેપ = Immediate (તાત્કાલિક પાડોશી); ૨ સ્ટેપ = Second (વચ્ચે ૧ વ્યક્તિ); ૩ સ્ટેપ = Third (વચ્ચે ૨ વ્યક્તિ).<br/>"
        "• <b>ત્રિકોણાકાર ટેબલ એકાંતર નિયમ (Triangular Alternate Parity):</b> ૬ વ્યક્તિઓના ત્રિકોણમાં ખૂણા (Corners) અને બાજુઓ (Sides) એકાંતરે આવે છે. <b>ખૂણાથી ૨ સ્ટેપ હંમેશાં બીજો ખૂણો જ હોય!</b> (ક્યારેય સાઈડ ન બને).",
        "પાડોશીને 'Second' ગણી લેવો, અથવા ત્રિકોણમાં ખૂણાથી ૨ સ્ટેપ સાઈડ પર બેસાડી દેવા.",
        "In a triangle, P is at a Corner. Q sits 2nd to the right of P. &rarr; ૧ સ્ટેપ = Side Middle, ૨ સ્ટેપ = <b>Another Corner!</b> Q ફરજિયાત ખૂણા પર જ બેસશે!",
        "#b45309"
    ))
    story.append(PageBreak())

    # =========================================================================
    # PAGE 9: CHAPTER 14: ADVANCED CODING & 22-MINUTE EXAM ROADMAP
    # =========================================================================
    story.append(create_banner("પ્રકરણ ૧૪: અદ્યતન કોડિંગ & ૨૨-મિનિટ સ્પીડ બ્લુપ્રિન્ટ (ADVANCED CODING & ROADMAP)", "#0f172a"))
    story.append(Spacer(1, 4))

    # Rule 14.1: Sum-27 Opposite Letters
    story.append(make_rule_box(
        "૧. સરવાળો-૨૭ સામસામેના અક્ષરોની ફોર્મ્યુલા (Sum-27 Opposite Letter Inversion Formula)",
        "નવા પેટર્નના કોડિંગમાં કોડ લેટર હંમેશાં શબ્દના છેલ્લા અક્ષરનો <b>સામેનો અક્ષર (Opposite Letter: Sum 27)</b> હોય છે:<br/>"
        "• ફોર્મ્યુલા: $\\text{Opposite Rank} = 27 - \\text{Word's Letter Rank}$.<br/>"
        "યાદ રાખવાની શોર્ટકટ જોડીઓ: <b>AZ (1+26), BY (2+25), CX (3+24), DW (4+23), EV (5+22), FU (6+21), GT (7+20), HS (8+19), IR (9+18), JQ (10+17), KP (11+16), LO (12+15), MN (13+14)</b>.",
        "શબ્દના છેલ્લા અક્ષરનો સીધો અક્ષર અથવા +1 અક્ષર કોપી કરી લેવો.",
        "શબ્દ 'MOUSE' નો છેલ્લો અક્ષર E(5) છે &rarr; સામેનો અક્ષર = $27 - 5 = 22$ (V). કોડમાં લેટર <b>V</b> આવશે (દા.ત. #5V). જો કોડ લેટર V હોય તો શબ્દ E થી પૂરો થતો હોવો જોઈએ!",
        "#0f172a"
    ))
    story.append(Spacer(1, 4))

    # Rule 14.2: 2-Step Conditional Protocol
    story.append(make_rule_box(
        "૨. શરતી કોડિંગનો ૨-સ્ટેપ પ્રોટોકોલ (2-Step Conditional Matrix Protocol: Draft -> Oven)",
        "૧. <b>Step 1 (કાચો કોડ - Raw Draft):</b> આપેલા ટેબલ પરથી દરેક અક્ષરનો સીધો કોડ શોધો.<br/>"
        "૨. <b>Step 2 (શરતોનું ઓવન - Condition Oven):</b> આપેલ શબ્દના પહેલા અને છેલ્લા અક્ષરને ૧, ૨, ૩ શરતો સાથે સરખાવો. જો શરત લાગુ પડે તો જ કાચા કોડમાં ફેરફાર કરો!",
        "શરત લાગુ પડતી હોવા છતાં ટેબલનો સીધો કાચો કોડ ઓપ્શનમાંથી ટીક કરી દેવો.",
        "શબ્દ: 'K...O'. શરત: 'જો પહેલો વ્યંજન અને છેલ્લો સ્વર હોય તો બંનેના કોડ % થશે'. કાચો કોડ ગમે તે હોય, બંને છેડે <b>% ... %</b> આવશે!",
        "#0f172a"
    ))
    story.append(Spacer(1, 4))

    # Exam Hall 22-Min Strategy
    plan_style = ParagraphStyle('PlanH', fontName='Nirmala-Bold', fontSize=8.5, leading=11, textColor=colors.HexColor("#0f172a"))
    plan_body = ParagraphStyle('PlanB', fontName='Nirmala', fontSize=7.2, leading=9.8, textColor=colors.HexColor("#1e293b"))

    plan_rows = [
        [Paragraph("<b>પરીક્ષા હોલ ૨૨-મિનિટ ટાઈમ મેનેજમેન્ટ બ્લુપ્રિન્ટ (38+/40 Speed Blueprint)</b>", plan_style)],
        [Paragraph(
            "<b>૧. મિનિટ ૦:૦૦ થી ૪:૩૦ (Speed Core):</b> Inequalities (Ch 1) + Syllogisms (Ch 2) &rarr; ૮ થી ૧૦ પ્રશ્નો રોકડા સાચા!<br/>"
            "<b>૨. મિનિટ ૪:૩૦ થી ૯:૩૦ (Positional Scoring):</b> Alphanumeric (Ch 3), Coding (Ch 4), Blood & Direction (Ch 5), Order (Ch 6), Misc (Ch 11) &rarr; ૧૦ મી મિનિટે ૨૦+ માર્ક્સ બેંક થઈ જશે!<br/>"
            "<b>૩. મિનિટ ૯:૩૦ થી ૧૭:૦૦ (Standard Puzzles & Seating):</b> Circular/Square (Ch 7), Floor/Box (Ch 8) &rarr; બે સમાંતર કેસ બનાવીને ૩૦+ માર્ક્સ પર પહોંચો!<br/>"
            "<b>૪. મિનિટ ૧૭:૦૦ થી ૨૨:૦૦ (Advanced Spatial Puzzles):</b> Floor+Flat (Ch 12), Mixed Facing Seating (Ch 13) &rarr; <b>૩૮+ માર્ક્સ વિજયી!</b><br/>"
            "<b>૫. મિનિટ ૨૨:૦૦ થી ૨૪:૦૦:</b> બફર સમય & રિવ્યૂ.",
            plan_body
        )]
    ]
    t_plan = Table(plan_rows, colWidths=[523])
    t_plan.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#fef3c7")),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor("#f59e0b")),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
        ('LEFTPADDING', (0,0), (-1,-1), 6),
    ]))
    story.append(t_plan)

    doc.build(story, canvasmaker=NumberedCanvas)
    print(f"Successfully generated: {output_path}")

if __name__ == '__main__':
    generate_pdf()
