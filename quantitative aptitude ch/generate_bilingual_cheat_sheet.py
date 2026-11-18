import os
import subprocess

def generate_html_and_pdf():
    html_path = os.path.abspath("quantitative aptitude ch/cheat_sheet_bilingual.html")
    pdf_path = os.path.abspath("quantitative aptitude ch/IBPS_RRB_PO_Quant_Ultimate_Cheat_Sheet.pdf")
    chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

    html_content = """<!DOCTYPE html>
<html lang="gu">
<head>
<meta charset="utf-8">
<title>IBPS RRB PO Quant Ultimate Speed Cheat Sheet</title>
<style>
  @page {
    size: A4;
    margin: 12mm 12mm 12mm 12mm;
    @bottom-right {
      content: counter(page);
    }
  }
  body {
    font-family: 'Nirmala UI', 'Segoe UI', Arial, sans-serif;
    color: #2D3748;
    background: #FFFFFF;
    margin: 0;
    padding: 0;
    font-size: 11.5px;
    line-height: 1.5;
  }
  .banner {
    background: linear-gradient(135deg, #EBF8FF 0%, #EDF2F7 100%);
    border: 2px solid #2B6CB0;
    border-radius: 8px;
    padding: 12px 16px;
    margin-bottom: 14px;
    text-align: center;
  }
  .banner h1 {
    margin: 0 0 4px 0;
    color: #1A365D;
    font-size: 19px;
    letter-spacing: 0.5px;
  }
  .banner h2 {
    margin: 0 0 6px 0;
    color: #2B6CB0;
    font-size: 12px;
    font-weight: 700;
  }
  .banner .meta {
    font-size: 10.5px;
    color: #4A5568;
    margin: 0;
  }
  .module-header {
    background: #1A365D;
    color: #FFFFFF;
    font-size: 12.5px;
    font-weight: 700;
    padding: 6px 12px;
    border-radius: 6px;
    margin-top: 14px;
    margin-bottom: 10px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    page-break-after: avoid;
  }
  .module-header span {
    font-size: 11px;
    background: #2B6CB0;
    padding: 2px 8px;
    border-radius: 4px;
  }
  .trick-card {
    border: 1px solid #CBD5E0;
    border-radius: 6px;
    margin-bottom: 10px;
    background: #FFFFFF;
    page-break-inside: avoid;
    box-shadow: 0 1px 3px rgba(0,0,0,0.04);
  }
  .trick-card-header {
    background: #EDF2F7;
    border-bottom: 1px solid #CBD5E0;
    padding: 5px 10px;
    font-weight: 700;
    color: #1A365D;
    font-size: 11.5px;
    display: flex;
    justify-content: space-between;
  }
  .trick-card-body {
    padding: 8px 10px;
  }
  .line {
    margin-bottom: 5px;
  }
  .line-label {
    font-weight: 700;
    color: #1A365D;
  }
  .rule-box {
    background: #EBF8FF;
    border-left: 3px solid #2B6CB0;
    padding: 4px 8px;
    margin: 4px 0 6px 0;
    font-weight: 600;
    color: #1A365D;
  }
  .example-box {
    background: #F7FAFC;
    border: 1px solid #E2E8F0;
    border-radius: 4px;
    padding: 6px 8px;
    margin-top: 4px;
    font-size: 11px;
  }
  .trap-box {
    background: #FFF5F5;
    border-left: 3px solid #E53E3E;
    padding: 4px 8px;
    margin-top: 5px;
    color: #9B2C2C;
    font-size: 10.5px;
  }
  .gold-box {
    background: #FEFCBF;
    border: 2px solid #D69E2E;
    border-radius: 6px;
    padding: 10px 14px;
    margin-top: 14px;
    page-break-inside: avoid;
  }
  .gold-box h3 {
    margin: 0 0 6px 0;
    color: #744210;
    font-size: 13px;
    text-align: center;
  }
  .gold-box ol {
    margin: 0;
    padding-left: 20px;
  }
  .gold-box li {
    margin-bottom: 4px;
    color: #744210;
    font-size: 11px;
  }
  .page-break {
    page-break-before: always;
  }
  .highlight {
    color: #2B6CB0;
    font-weight: 700;
  }
  .tag {
    display: inline-block;
    padding: 1px 6px;
    font-size: 9.5px;
    font-weight: 700;
    border-radius: 3px;
    background: #E2E8F0;
    color: #2D3748;
    margin-right: 4px;
  }
</style>
</head>
<body>

  <!-- TITLE BANNER -->
  <div class="banner">
    <h1>⚡ IBPS RRB PO PRELIMS QUANTITATIVE APTITUDE</h1>
    <h2>ULTIMATE SPEED CHEAT SHEET &amp; FORMULAE DOSSIER (સંપૂર્ણ રિવિઝન માર્ગદર્શિકા)</h2>
    <p class="meta">
      <b>ઉમેદવાર:</b> હિતેન્દ્રસિંહ સોલંકી &nbsp;|&nbsp; 
      <b>પરીક્ષા ટાર્ગેટ:</b> ૨૧ નવેમ્બર ૨૦૨૬ (૩૫+/૪૦ માર્ક્સ) &nbsp;|&nbsp; 
      <b>વિષયવસ્તુ:</b> પ્રકરણ ૧ થી ૧૨ અને પ્રકરણ ૨૦ (All Prelims Speed Core)
    </p>
  </div>

  <!-- MODULE 1 -->
  <div class="module-header">
    MODULE 1: SPEED MATH &amp; RAPID APPROXIMATION (પ્રકરણ ૧ અને ૨)
    <span>૫ માર્ક્સ | ટાર્ગેટ: ૧.૫ મિનિટ</span>
  </div>

  <!-- Trick 1.1 -->
  <div class="trick-card">
    <div class="trick-card-header">
      <span>TRICK 1.1: VBODMAS LEFT-TO-RIGHT LAW (ડાબેથી જમણી બાજુનો નિયમ)</span>
      <span class="tag">BODMAS Priority</span>
    </div>
    <div class="trick-card-body">
      <div class="line">
        <span class="line-label">🎯 પરીક્ષામાં કઈ રીતે ઓળખવો:</span> જ્યારે દાખલામાં કૌંસ વગર સળંગ ભાગાકાર (÷) અને ગુણાકાર (×) આપેલા હોય.
      </div>
      <div class="rule-box">
        ભાગાકાર અને ગુણાકારની સમાન પ્રાથમિકતા છે. ગણતરી હંમેશા <u>ડાબેથી જમણી બાજુ (Strictly Left-to-Right)</u> જ કરવી! પહેલા ગુણાકાર કરવાની ઉતાવળ ક્યારેય ન કરવી.
      </div>
      <div class="example-box">
        <b>📝 Real Exam Example:</b> ૨ સેકન્ડમાં કિંમત શોધો: <b>256 ÷ 16 × 4 = ?</b><br/>
        <b>[Speed Solution]:</b> સ્ટેપ ૧: (256 ÷ 16) = 16. સ્ટેપ ૨: 16 × 4 = <b>64</b>!
      </div>
      <div class="trap-box">
        <b>⚠️ ટ્રેપથી બચો:</b> જો તમે પહેલા 16 × 4 = 64 કરશો, તો 256 ÷ 64 = 4 આવશે, જે ખોટો જવાબ છે અને સીધા -0.25 માર્ક્સ કપાશે!
      </div>
    </div>
  </div>

  <!-- Trick 1.2 -->
  <div class="trick-card">
    <div class="trick-card-header">
      <span>TRICK 1.2: WHOLE MINUS MIXED FRACTION 3-SEC HACK (પૂર્ણાંક - અપૂર્ણાંક હેક)</span>
      <span class="tag">Zero-Pen Hack</span>
    </div>
    <div class="trick-card-body">
      <div class="line">
        <span class="line-label">🎯 પરીક્ષામાં કઈ રીતે ઓળખવો:</span> જ્યારે કોઈ આખા પૂર્ણાંક N માંથી મિશ્ર અપૂર્ણાંક A (b/c) બાદ કરવાનો હોય (દા.ત. 25 - 6 3/8).
      </div>
      <div class="rule-box">
        <b>N - A (b/c) = (N - A - 1) &nbsp;[ (c - b) / c ]</b><br/>
        (નિયમ: પૂર્ણાંક ભાગમાં ૧ ઉમેરીને N માંથી બાદ કરો, અને અંશમાં છેદમાંથી અંશ બાદ કરીને મૂકો).
      </div>
      <div class="example-box">
        <b>📝 Real Exam Example:</b> પેન ઉપાડ્યા વગર ઉકેલો: <b>25 - 6 3/8 = ?</b><br/>
        <b>[Speed Solution]:</b> ૨૫ માંથી (૬ + ૧ = ૭) બાદ કરો: 25 - 7 = <b>18</b>. અપૂર્ણાંક: (8 - 3)/8 = <b>5/8</b>. જવાબ: <b>18 5/8</b>!
      </div>
      <div class="trap-box">
        <b>⚠️ ટ્રેપથી બચો:</b> 6 3/8 ને 51/8 માં ફેરવીને 25 સાથે લ.સા.અ. લેવા બેસશો તો ૪૫ સેકન્ડનો બગાડ થશે.
      </div>
    </div>
  </div>

  <!-- Trick 1.3 -->
  <div class="trick-card">
    <div class="trick-card-header">
      <span>TRICK 1.3: BENCHMARK PERCENTAGE-FRACTION SWAP (ટકાવારી સ્વેપ નિયમ)</span>
      <span class="tag">% Swapping</span>
    </div>
    <div class="trick-card-body">
      <div class="line">
        <span class="line-label">🎯 પરીક્ષામાં કઈ રીતે ઓળખવો:</span> જ્યારે 37.5%, 62.5%, 87.5%, 16.66%, 83.33%, 14.28%, 12.5% જેવા પોઇન્ટ વાળા ટકા દેખાય.
      </div>
      <div class="rule-box">
        <b>A% of B = B% of A</b> (ટકાની અદલાબદલી કરી શકાય છે). નીચેના ફ્રેક્શન સીધા યાદ રાખો:<br/>
        • 12.5% = 1/8 &nbsp;|&nbsp; 37.5% = 3/8 &nbsp;|&nbsp; 62.5% = 5/8 &nbsp;|&nbsp; 87.5% = 7/8<br/>
        • 16.66% = 1/6 &nbsp;|&nbsp; 33.33% = 1/3 &nbsp;|&nbsp; 66.66% = 2/3 &nbsp;|&nbsp; 83.33% = 5/6<br/>
        • 14.28% = 1/7 &nbsp;|&nbsp; 28.57% = 2/7 &nbsp;|&nbsp; 9.09% = 1/11
      </div>
      <div class="example-box">
        <b>📝 Real Exam Example:</b> કિંમત શોધો: <b>64% of 875 = ?</b><br/>
        <b>[Speed Solution]:</b> સ્વેપ કરો: 87.5% of 640 = <b>(7/8) × 640 = 7 × 80 = 560</b>!
      </div>
      <div class="trap-box">
        <b>⚠️ ટ્રેપથી બચો:</b> 64 × 875 નો ગુણાકાર કરવા જશો તો થાકી જશો અને ખોટો જવાબ આવવાની શક્યતા વધી જશે.
      </div>
    </div>
  </div>

  <!-- Trick 1.4 -->
  <div class="trick-card">
    <div class="trick-card-header">
      <span>TRICK 1.4: 5-SECOND SQUARE ROOT HACK (દશક બેન્ચમાર્ક + એકમનો અંક)</span>
      <span class="tag">5-Sec Roots</span>
    </div>
    <div class="trick-card-body">
      <div class="line">
        <span class="line-label">🎯 પરીક્ષામાં કઈ રીતે ઓળખવો:</span> Approximation માં ચાર આંકડાનું વર્ગમૂળ શોધવાનું હોય (દા.ત. √1024, √3136).
      </div>
      <div class="rule-box">
        ૧. દશકના વર્ગ વચ્ચે મૂકો: 30² = 900, 40² = 1600, 50² = 2500, 60² = 3600.<br/>
        ૨. છેલ્લો અંક મેળવો: 1 → 1/9, 4 → 2/8, 5 → 5, 6 → 4/6, 9 → 3/7.<br/>
        ૩. જે દશકના વર્ગની વધુ નજીક હોય તે વિકલ્પ પસંદ કરો.
      </div>
      <div class="example-box">
        <b>📝 Real Exam Example:</b> આશરે કિંમત શોધો: <b>√1024 = ?</b><br/>
        <b>[Speed Solution]:</b> 900 (30²) અને 1600 (40²) ની વચ્ચે છે. છેલ્લે 4 છે → એકમ 2 કે 8 હોય (32 કે 38). 1024 એ 900 ની ખૂબ નજીક છે → સીધો જવાબ <b>32</b>!
      </div>
    </div>
  </div>

  <!-- Trick 1.5 -->
  <div class="trick-card">
    <div class="trick-card-header">
      <span>TRICK 1.5: DIFFERENCE OF SQUARES SHORTCUT (વર્ગોના તફાવતનું સૂત્ર)</span>
      <span class="tag">Algebraic Hack</span>
    </div>
    <div class="trick-card-body">
      <div class="line">
        <span class="line-label">🎯 પરીક્ષામાં કઈ રીતે ઓળખવો:</span> જ્યારે (A.98)² - (B.95)² પ્રકારના બે વર્ગોની બાદબાકી દેખાય.
      </div>
      <div class="rule-box">
        બંનેના અલગ વર્ગ કરવાને બદલે: <b>a² - b² = (a - b)(a + b)</b> વાપરો.
      </div>
      <div class="example-box">
        <b>📝 Real Exam Example:</b> સાદુરૂપ આપો: <b>(17.98)² - (13.95)² = ?</b><br/>
        <b>[Speed Solution]:</b> 18² - 14² લો: (18 - 14)(18 + 14) = <b>4 × 32 = 128</b>!
      </div>
    </div>
  </div>

  <!-- MODULE 2 -->
  <div class="module-header page-break">
    MODULE 2: QUADRATIC EQUATIONS &amp; INEQUALITIES (પ્રકરણ ૪)
    <span>૫ માર્ક્સ | ટાર્ગેટ: ૨ મિનિટ</span>
  </div>

  <!-- Trick 2.1 -->
  <div class="trick-card">
    <div class="trick-card-header">
      <span>TRICK 2.1: THE 2-SECOND INSTANT CND HACK (રોકડા માર્ક્સ આપતી ટ્રીક)</span>
      <span class="tag">2-Second CND</span>
    </div>
    <div class="trick-card-body">
      <div class="line">
        <span class="line-label">🎯 પરીક્ષામાં કઈ રીતે ઓળખવો:</span> બંને સમીકરણોમાં છેલ્લું અચળ પદ (Constant c) ની આગળ <b>ઋણ ચિહ્ન (-)</b> હોય.
      </div>
      <div class="rule-box">
        જો બંને સમીકરણોમાં છેલ્લે ઋણ (-) નિશાની હોય, તો કોઈ પણ ગણતરી કે અવયવ પાડ્યા વગર જવાબ <b>હંમેશા [E] x = y or Relationship Cannot Be Established (CND)</b> જ આવે!
      </div>
      <div class="example-box">
        <b>📝 Real Exam Example:</b> સંબંધ નક્કી કરો: <b>I.</b> x² + 2x - 35 = 0 &nbsp;|&nbsp; <b>II.</b> y² - 4y - 45 = 0<br/>
        <b>[Speed Solution]:</b> બંને સમીકરણોમાં છેલ્લે minus (-35 અને -45) છે. પેન વગર ૨ સેકન્ડમાં ટીક કરો: <b>[E] CND</b>!
      </div>
      <div class="trap-box">
        <b>⚠️ ટ્રેપથી બચો:</b> આ પ્રકારના દાખલામાં અવયવ પાડીને સમય બગાડવો એ સૌથી મોટી ભૂલ છે.
      </div>
    </div>
  </div>

  <!-- Trick 2.2 -->
  <div class="trick-card">
    <div class="trick-card-header">
      <span>TRICK 2.2: UNIVERSAL ROOT SIGN TABLE &amp; SIGN JUMP (સાઈન ટેબલ મેજિક)</span>
      <span class="tag">Sign Jump</span>
    </div>
    <div class="trick-card-body">
      <div class="line">
        <span class="line-label">🎯 પરીક્ષામાં કઈ રીતે ઓળખવો:</span> ax² + bx + c = 0 ના ચિહ્નો જોઈને સીધા બીજના ચિહ્નો નક્કી કરવા.
      </div>
      <div class="rule-box">
        સમીકરણના ચિહ્નો પરથી બીજના ચિહ્નો સીધા યાદ રાખો:<br/>
        • સમીકરણ <b>(-, +)</b> હોય → બંને બીજ <b>ધન (+, +)</b> આવે.<br/>
        • સમીકરણ <b>(+, +)</b> હોય → બંને બીજ <b>ઋણ (-, -)</b> આવે.<br/>
        • સમીકરણ <b>(+, -)</b> હોય → મોટો ઋણ, નાનો ધન <b>(-, +)</b> આવે.<br/>
        • સમીકરણ <b>(-, -)</b> હોય → મોટો ધન, નાનો ઋણ <b>(+, -)</b> આવે.<br/>
        <b>ડાયરેક્ટ સાઈન જમ્પ:</b> જો Eq I (-, +) હોય અને Eq II (+, +) હોય → (+, +) > (-, -) → સીધું <b>x > y</b>!
      </div>
      <div class="example-box">
        <b>📝 Real Exam Example:</b> <b>I.</b> x² - 11x + 30 = 0 &nbsp;|&nbsp; <b>II.</b> y² + 15y + 56 = 0<br/>
        <b>[Speed Solution]:</b> Eq I માં (-, +) છે → x ના બીજ (+, +) આવે. Eq II માં (+, +) છે → y ના બીજ (-, -) આવે. ધન હંમેશા ઋણ કરતાં મોટો હોય → <b>x > y</b>!
      </div>
    </div>
  </div>

  <!-- Trick 2.3 -->
  <div class="trick-card">
    <div class="trick-card-header">
      <span>TRICK 2.3: SQUARE VS SQUARE ROOT TRAP (વર્ગ વિરુદ્ધ વર્ગમૂળની ટ્રેપ)</span>
      <span class="tag">Major Exam Trap</span>
    </div>
    <div class="trick-card-body">
      <div class="line">
        <span class="line-label">🎯 પરીક્ષામાં કઈ રીતે ઓળખવો:</span> એક સમીકરણ x² = N હોય અને બીજું y = √N આપેલું હોય.
      </div>
      <div class="rule-box">
        • <b>x² = N</b> ના હંમેશા બે બીજ આવે: <b>+√N અને -√N</b>.<br/>
        • <b>y = √N</b> નું ફક્ત એક જ બીજ આવે: <b>+√N</b> (વર્ગમૂળનું ચિહ્ન ફક્ત ધન મૂલ્ય દર્શાવે છે).<br/>
        • સરખામણી: {+√N, -√N} વિરુદ્ધ {+√N} હંમેશા <b>x ≤ y</b> જ પરિણમે!
      </div>
      <div class="example-box">
        <b>📝 Real Exam Example:</b> <b>I.</b> x² = 196 &nbsp;|&nbsp; <b>II.</b> y = √196<br/>
        <b>[Speed Solution]:</b> x = {+14, -14}. y = {+14}. +14 = +14 અને -14 &lt; +14 → સંબંધ: <b>x ≤ y</b> (Option [D])!
      </div>
      <div class="trap-box">
        <b>⚠️ ટ્રેપથી બચો:</b> મોટાભાગના ઉમેદવારો √196 = ±14 માનીને ભૂલથી [E] CND ટીક કરી દે છે અને માર્ક્સ ગુમાવે છે!
      </div>
    </div>
  </div>

  <!-- Trick 2.4 -->
  <div class="trick-card">
    <div class="trick-card-header">
      <span>TRICK 2.4: COEFFICIENT CROSS-BALANCING (સહગુણક ગુણાકાર શોર્ટકટ)</span>
      <span class="tag">Cross Multiply</span>
    </div>
    <div class="trick-card-body">
      <div class="line">
        <span class="line-label">🎯 પરીક્ષામાં કઈ રીતે ઓળખવો:</span> જ્યારે x² અને y² ની આગળ અલગ સહગુણક હોય (દા.ત. 2x² અને 3y²).
      </div>
      <div class="rule-box">
        અવયવોને સહગુણક વડે ભાગવા નહીં (દશાંશ અપૂર્ણાંક અઘરા બને છે). તેના બદલે: <b>Eq I ના અવયવોને a₂ વડે અને Eq II ના અવયવોને a₁ વડે ગુણી નાખો!</b>
      </div>
      <div class="example-box">
        <b>📝 Real Exam Example:</b> <b>I.</b> 2x² - 7x + 6 = 0 &nbsp;|&nbsp; <b>II.</b> 3y² - 11y + 10 = 0<br/>
        <b>[Speed Solution]:</b> Eq I ના અવયવ: 3, 4. Eq II ના અવયવ: 5, 6.<br/>
        x ના અવયવોને 3 વડે ગુણો: {9, 12}. y ના અવયવોને 2 વડે ગુણો: {10, 12}. સરખામણી: 9 &lt; 10, પણ 12 &gt; 10 → ઓવરલેપ → <b>[E] CND</b>!
      </div>
    </div>
  </div>

  <!-- MODULE 3 -->
  <div class="module-header page-break">
    MODULE 3: NUMBER SERIES &amp; TWO-SERIES PATTERNS (પ્રકરણ ૩ અને ૧૨)
    <span>૫ માર્ક્સ | ટાર્ગેટ: ૨.૫ મિનિટ</span>
  </div>

  <!-- Trick 3.1 -->
  <div class="trick-card">
    <div class="trick-card-header">
      <span>TRICK 3.1: 3-SECOND VISUAL SCAN FLOWCHART (શ્રેણી ઓળખવાનો ફ્લોચાર્ટ)</span>
      <span class="tag">Visual Scan</span>
    </div>
    <div class="trick-card-body">
      <div class="line">
        <span class="line-label">🎯 પરીક્ષામાં કઈ રીતે ઓળખવો:</span> શ્રેણી જોતાં જ પ્રથમ ૩ સેકન્ડમાં પેટર્નનો પ્રકાર નક્કી કરવો.
      </div>
      <div class="rule-box">
        • <b>ધીમી અને નિયમિત વૃદ્ધિ:</b> તફાવત શ્રેણી (Difference Series: +n², +n³, અવિભાજ્ય સંખ્યા, અથવા D₂ પગથિયાં).<br/>
        • <b>અચાનક મોટો ઉછાળો:</b> ગુણાકાર શ્રેણી (Multiplication: ×1+1, ×2+2, ×3+3...).<br/>
        • <b>બીજી સંખ્યા અડધી થાય:</b> ડેસિમલ શ્રેણી (Decimal: ×0.5 + 0.5, ×1 + 1, ×2 + 2...).<br/>
        • <b>ઉપર-નીચે (Zig-Zag):</b> એકાંતરે શ્રેણી (Alternating: એક-એક સંખ્યા છોડીને).
      </div>
      <div class="example-box">
        <b>📝 Real Exam Example:</b> ખૂટતી સંખ્યા શોધો: <b>12, 13, 28, 87, 352, ?</b><br/>
        <b>[Speed Solution]:</b> સંખ્યાઓ ઝડપથી વધી રહી છે → 12×1+1=13, 13×2+2=28, 28×3+3=87, 87×4+4=352. આગળનું પદ: <b>352 × 5 + 5 = 1765</b>!
      </div>
    </div>
  </div>

  <!-- Trick 3.2 -->
  <div class="trick-card">
    <div class="trick-card-header">
      <span>TRICK 3.2: WRONG NUMBER "TWO BAD GAPS" LAW (બે બગડેલા ગેપનો નિયમ)</span>
      <span class="tag">Wrong Number</span>
    </div>
    <div class="trick-card-body">
      <div class="line">
        <span class="line-label">🎯 પરીક્ષામાં કઈ રીતે ઓળખવો:</span> તફાવત વાળી શ્રેણીમાંથી ખોટી સંખ્યા શોધવાની હોય.
      </div>
      <div class="rule-box">
        શ્રેણીમાં રહેલી એક જ ખોટી સંખ્યા પોતાની આજુબાજુના <b>બે ગેપ (Two Adjacent Gaps) બગાડે છે</b>. જે સંખ્યા આ બંને બગડેલા ગેપની બરાબર વચ્ચે (Junction) આવેલી હોય, તે જ <b>હંમેશા ખોટી સંખ્યા (Wrong Number)</b> હોય!
      </div>
      <div class="example-box">
        <b>📝 Real Exam Example:</b> ખોટી સંખ્યા શોધો: <b>6, 12, 20, 30, 41, 56</b><br/>
        <b>[Speed Solution]:</b> તફાવત: +6, +8, +10, +11, +15. ક્રમિક બેકી સંખ્યાની પેટર્નમાં +11 અને +15 બગડેલા ગેપ છે. આ બંનેની વચ્ચે આવેલી સંખ્યા <b>41</b> છે (ત્યાં 30 + 12 = 42 હોવા જોઈએ). માટે <b>41 ખોટી છે</b>!
      </div>
    </div>
  </div>

  <!-- Trick 3.3 -->
  <div class="trick-card">
    <div class="trick-card-header">
      <span>TRICK 3.3: TWO-SERIES PARALLEL SHIFT SHORTCUT (બે-શ્રેણી પેરેલલ શિફ્ટ)</span>
      <span class="tag">Ch 12 Two-Series</span>
    </div>
    <div class="trick-card-body">
      <div class="line">
        <span class="line-label">🎯 પરીક્ષામાં કઈ રીતે ઓળખવો:</span> બે શ્રેણી આપેલી હોય અને બીજી શ્રેણી નવી સંખ્યાથી શરૂ થઈને પહેલી શ્રેણીની જેમ જ ચાલતી હોય.
      </div>
      <div class="rule-box">
        <b>Shift = Series II ની પ્રથમ સંખ્યા - Series I ની પ્રથમ સંખ્યા</b>.<br/>
        <b>Term_n(Series II) = Term_n(Series I) + Shift</b>.<br/>
        (નોંધ: આ શોર્ટકટ તફાવત, વર્ગ, ઘન, અવિભાજ્ય અને એકાંતરે શ્રેણી માટે ૧૦૦% સાચો પડે છે).
      </div>
      <div class="example-box">
        <b>📝 Real Exam Example:</b> Series I: 14, 22, 38, 70, 134, 262.<br/>
        Series II: 25, a, b, c, d, e. તો <b>(b)</b> ની કિંમત શોધો.<br/>
        <b>[Speed Solution]:</b> Shift = 25 - 14 = <b>+11</b>. (b) એ ત્રીજું પદ છે. Series I નું ત્રીજું પદ 38 છે. માટે: <b>b = 38 + 11 = 49</b>! (૨ સેકન્ડમાં સોલ્વ).
      </div>
      <div class="trap-box">
        <b>⚠️ ટ્રેપથી બચો:</b> પ્રશ્નમાં (b) પૂછ્યું હોય અને ઉતાવળમાં (a) શોધીને Option [A] ટીક કરવાની ભૂલ ન કરવી.
      </div>
    </div>
  </div>

  <!-- MODULE 4 -->
  <div class="module-header page-break">
    MODULE 4: DATA INTERPRETATION SPEED HACKS (પ્રકરણ ૯)
    <span>૧૫ માર્ક્સ | ટાર્ગેટ: ૭-૮ મિનિટ</span>
  </div>

  <!-- Trick 4.1 -->
  <div class="trick-card">
    <div class="trick-card-header">
      <span>TRICK 4.1: THE 'THAN' REFERENCE DENOMINATOR LAW ("THAN" પછીનો છેદ)</span>
      <span class="tag">% More/Less</span>
    </div>
    <div class="trick-card-body">
      <div class="line">
        <span class="line-label">🎯 પરીક્ષામાં કઈ રીતે ઓળખવો:</span> "X is what % MORE than Y?" અથવા "X is what % LESS than Y?".
      </div>
      <div class="rule-box">
        <b>ટકાવારી વધારો/ઘટાડો = [ (બંનેનો તફાવત) / (THAN પછી આવતી સંખ્યા) ] × 100</b>.<br/>
        નિયમ: છેદ (Denominator) માં હંમેશા <b>"THAN" શબ્દ પછી આવતી સંખ્યા જ મૂકવી!</b>
      </div>
      <div class="example-box">
        <b>📝 Real Exam Example:</b> સુરતના કુલ ખાતા = 2,400. ગાંધીનગરના કુલ ખાતા = 1,200. સુરતના ખાતા ગાંધીનગર કરતાં કેટલા ટકા વધારે છે?<br/>
        <b>[Speed Solution]:</b> તફાવત = 2400 - 1200 = 1200. 'THAN' પછી ગાંધીનગર (1200) છે. % More = <b>(1200 / 1200) × 100 = 100%</b>!
      </div>
      <div class="trap-box">
        <b>⚠️ ટ્રેપથી બચો:</b> છેદમાં ભૂલથી સુરત (2400) મૂકી દેશો તો 50% આવશે અને નેગેટિવ માર્કિંગ થશે!
      </div>
    </div>
  </div>

  <!-- Trick 4.2 -->
  <div class="trick-card">
    <div class="trick-card-header">
      <span>TRICK 4.2: PIE CHART DIRECT DEGREE RATIO (પાઇ ચાર્ટ સીધો ડિગ્રી ગુણોત્તર)</span>
      <span class="tag">Pie Chart Hack</span>
    </div>
    <div class="trick-card-body">
      <div class="line">
        <span class="line-label">🎯 પરીક્ષામાં કઈ રીતે ઓળખવો:</span> એક જ પાઇ ચાર્ટમાં બે વિષયો કે જૂથો વચ્ચેનો ગુણોત્તર પૂછ્યો હોય.
      </div>
      <div class="rule-box">
        ૧. સંપૂર્ણ વર્તુળ = 360° = 100% → 36° = 10% → 18° = 5%.<br/>
        ૨. <b>ગુણોત્તર શોર્ટકટ:</b> ક્યારેય પણ વાસ્તવિક સંખ્યાઓ શોધવાની જરૂર નથી! <u>ડિગ્રીનો સીધો ગુણોત્તર</u> લો!
      </div>
      <div class="example-box">
        <b>📝 Real Exam Example:</b> ૩,૬૦૦ વિદ્યાર્થીઓના પાઇ ચાર્ટમાં એન્જિનિયરિંગ 54° અને અન્ય 36° છે. બંનેનો ગુણોત્તર શોધો.<br/>
        <b>[Speed Solution]:</b> વાસ્તવિક મૂલ્ય ન શોધો! સીધો ડિગ્રી ગુણોત્તર: <b>54° : 36° = 3 : 2</b>!
      </div>
    </div>
  </div>

  <!-- Trick 4.3 -->
  <div class="trick-card">
    <div class="trick-card-header">
      <span>TRICK 4.3: MONTH-WISE GAP SUMMATION (ગેપનો સીધો સરવાળો)</span>
      <span class="tag">Line/Bar Hack</span>
    </div>
    <div class="trick-card-body">
      <div class="line">
        <span class="line-label">🎯 પરીક્ષામાં કઈ રીતે ઓળખવો:</span> લાઇન ગ્રાફ કે બાર ગ્રાફમાં બે કંપનીઓના કુલ ઉત્પાદનનો તફાવત પૂછ્યો હોય.
      </div>
      <div class="rule-box">
        બે મોટા સરવાળા અલગ-અલગ કરવાને બદલે, <b>દરેક મહિનાના નાના તફાવતો (Gaps) નો સીધો જ સરવાળો કરો!</b>
      </div>
      <div class="example-box">
        <b>📝 Real Exam Example:</b> કંપની P અને Q: જાન્યુ (35 vs 45), ફેબ્રુ (40 vs 50), માર્ચ (55 vs 60), એપ્રિલ (65 vs 70). કુલ તફાવત શોધો.<br/>
        <b>[Speed Solution]:</b> સીધો ગેપ સરવાળો: 10 + 10 + 5 + 5 = <b>30</b>! (૫ સેકન્ડમાં પૂર્ણ).
      </div>
    </div>
  </div>

  <!-- MODULE 5 -->
  <div class="module-header page-break">
    MODULE 5: CORE ARITHMETIC 10-SECOND FORMULAS (પ્રકરણ ૫ થી ૮, ૨૦)
    <span>૧૦ માર્ક્સ | ટાર્ગેટ: ૬ મિનિટ</span>
  </div>

  <!-- Trick 5.1 -->
  <div class="trick-card">
    <div class="trick-card-header">
      <span>TRICK 5.1: AGES RATIO-UNIT INVARIANCE RULE (ઉંમરનો રેશિયો-યુનિટ નિયમ)</span>
      <span class="tag">Ages Hack</span>
    </div>
    <div class="trick-card-body">
      <div class="line">
        <span class="line-label">🎯 પરીક્ષામાં કઈ રીતે ઓળખવો:</span> બે સમયગાળાના ઉંમરના ગુણોત્તર આપેલા હોય (દા.ત. હાલમાં અને ૬ વર્ષ પછી).
      </div>
      <div class="rule-box">
        બે વ્યક્તિઓની ઉંમરનો તફાવત સમય સાથે ક્યારેય બદલાતો નથી. જો ગુણોત્તરમાં વધારો સમાન હોય, તો <b>૧ યુનિટ = વર્ષોનો તફાવત</b>.
      </div>
      <div class="example-box">
        <b>📝 Real Exam Example:</b> A અને B ની હાલની ઉંમરનો ગુણોત્તર 4:5 છે. ૬ વર્ષ પછી 5:6 થશે. A ની હાલની ઉંમર શોધો.<br/>
        <b>[Speed Solution]:</b> યુનિટ વધારો: 5 - 4 = 1 યુનિટ. માટે 1 યુનિટ = 6 વર્ષ. A ની ઉંમર = 4 યુનિટ = <b>4 × 6 = 24 વર્ષ</b>!
      </div>
    </div>
  </div>

  <!-- Trick 5.2 -->
  <div class="trick-card">
    <div class="trick-card-header">
      <span>TRICK 5.2: PRICE-CONSUMPTION FRACTION LADDER (ભાવ-વપરાશ ફ્રેક્શન સીડી)</span>
      <span class="tag">Fraction Ladder</span>
    </div>
    <div class="trick-card-body">
      <div class="line">
        <span class="line-label">🎯 પરીક્ષામાં કઈ રીતે ઓળખવો:</span> કોઈ વસ્તુના ભાવમાં X% ફેરફાર થાય અને ખર્ચ અચળ રાખવા વપરાશમાં કેટલો ઘટાડો કરવો?
      </div>
      <div class="rule-box">
        • જો ભાવ <b>+1/n</b> વધે → વપરાશ <b>-1/(n+1)</b> ઘટાડવો પડે.<br/>
        • જો ભાવ <b>-1/n</b> ઘટે → વપરાશ <b>+1/(n-1)</b> વધારવો પડે.
      </div>
      <div class="example-box">
        <b>📝 Real Exam Example:</b> ખાંડનો ભાવ 25% વધે, તો ખર્ચ અચળ રાખવા વપરાશ કેટલા ટકા ઘટાડવો પડે?<br/>
        <b>[Speed Solution]:</b> ભાવ +25% = +1/4 વધ્યો. વપરાશ ઘટાડો = -1/(4 + 1) = -1/5 = <b>20%</b>!
      </div>
      <div class="trap-box">
        <b>⚠️ ટ્રેપથી બચો:</b> ભાવ 25% વધે તો વપરાશ પણ 25% જ ઘટે એવું ક્યારેય ન માનવું!
      </div>
    </div>
  </div>

  <!-- Trick 5.3 -->
  <div class="trick-card">
    <div class="trick-card-header">
      <span>TRICK 5.3: DYNAMIC AVERAGE GROUP SHIFT (સરેરાશ ડાયનેમિક શિફ્ટ)</span>
      <span class="tag">Average Shift</span>
    </div>
    <div class="trick-card-body">
      <div class="line">
        <span class="line-label">🎯 પરીક્ષામાં કઈ રીતે ઓળખવો:</span> જૂથમાં કોઈ નવી વ્યક્તિ ઉમેરાવાથી કે બદલાવાથી સરેરાશ બદલાય.
      </div>
      <div class="rule-box">
        <b>નવી વ્યક્તિનું મૂલ્ય = જૂની સરેરાશ + (નવી કુલ સંખ્યા × સરેરાશમાં વધારો)</b>.
      </div>
      <div class="example-box">
        <b>📝 Real Exam Example:</b> ૨૪ વિદ્યાર્થીઓનું સરેરાશ વજન 45 kg છે. શિક્ષક ઉમેરાતાં સરેરાશ 1 kg વધે છે. શિક્ષકનું વજન શોધો.<br/>
        <b>[Speed Solution]:</b> શિક્ષકનું વજન = 45 + (25 × 1) = 45 + 25 = <b>70 kg</b>!
      </div>
    </div>
  </div>

  <!-- Trick 5.4 -->
  <div class="trick-card">
    <div class="trick-card-header">
      <span>TRICK 5.4: LOSS-TO-PROFIT JUMP RULE (ખોટથી નફાનો જમ્પ રૂલ)</span>
      <span class="tag">P&amp;L Jump</span>
    </div>
    <div class="trick-card-body">
      <div class="line">
        <span class="line-label">🎯 પરીક્ષામાં કઈ રીતે ઓળખવો:</span> વેચાણ કિંમત ₹K વધારવાથી L% ખોટમાંથી P% નફો થવા લાગે.
      </div>
      <div class="rule-box">
        કુલ ટકાવારી ઉછાળો = <b>(L + P)%</b>. પછી: <b>(L + P)% = ₹K → મૂળ કિંમત (CP 100%) = [ K / (L + P) ] × 100</b>.
      </div>
      <div class="example-box">
        <b>📝 Real Exam Example:</b> વેચાણ કિંમત ₹450 વધારતાં 15% ખોટનું રૂપાંતર 15% નફામાં થાય છે. મૂળ કિંમત શોધો.<br/>
        <b>[Speed Solution]:</b> ઉછાળો = 15% + 15% = 30%. 30% = ₹450 → 1% = 15 → <b>CP (100%) = ₹1,500</b>!
      </div>
    </div>
  </div>

  <!-- Trick 5.5 -->
  <div class="trick-card">
    <div class="trick-card-header">
      <span>TRICK 5.5: CI DOUBLING POWER RULE (ચક્રવૃદ્ધિ વ્યાજ ઘાતાંક નિયમ)</span>
      <span class="tag">CI Power Rule</span>
    </div>
    <div class="trick-card-body">
      <div class="line">
        <span class="line-label">🎯 પરીક્ષામાં કઈ રીતે ઓળખવો:</span> ચક્રવૃદ્ધિ વ્યાજે રકમ T વર્ષમાં બમણી કે ત્રણ ગણી થતી હોય.
      </div>
      <div class="rule-box">
        CI માં રકમ ઘાતાંક (Powers) માં વધે છે: <b>ગણા = (આધાર)^k → સમય = k × T</b>.<br/>
        જો T વર્ષમાં બમણી (2¹) થાય, તો 2T માં ૪ ગણી (2²), અને 3T વર્ષમાં ૮ ગણી (2³) થાય.
      </div>
      <div class="example-box">
        <b>📝 Real Exam Example:</b> CI પર રકમ 4 વર્ષમાં બમણી થાય છે. તે 8 ગણી ક્યારે થશે?<br/>
        <b>[Speed Solution]:</b> 8 = 2³. ઘાત 3 છે. માટે લાગતો સમય = <b>3 × 4 = 12 વર્ષ</b> (Option [C])!
      </div>
      <div class="trap-box">
        <b>⚠️ ટ્રેપથી બચો:</b> સાદા વ્યાજની જેમ 4 + 4 = 8 વર્ષ ન ગણવું. 8 વર્ષમાં રકમ ફક્ત 4 ગણી જ થાય!
      </div>
    </div>
  </div>

  <!-- Trick 5.6 -->
  <div class="trick-card">
    <div class="trick-card-header">
      <span>TRICK 5.6: TIME &amp; WORK LCM CHOCOLATE METHOD (ચોકલેટ LCM પદ્ધતિ)</span>
      <span class="tag">LCM Method</span>
    </div>
    <div class="trick-card-body">
      <div class="line">
        <span class="line-label">🎯 પરીક્ષામાં કઈ રીતે ઓળખવો:</span> અલગ-અલગ દિવસોમાં કામ કરતા માણસો સાથે મળીને કામ કરે કે વચ્ચેથી છોડી દે.
      </div>
      <div class="rule-box">
        ૧. કુલ કાર્ય = દિવસોનો લ.સા.અ. (કુલ ચોકલેટ).<br/>
        ૨. કાર્યક્ષમતા = કુલ કાર્ય / દિવસો.<br/>
        ૩. બાકી દિવસ = બાકી કાર્ય / સક્રિય કાર્યક્ષમતા.
      </div>
      <div class="example-box">
        <b>📝 Real Exam Example:</b> A કામ 12 દિવસમાં અને B 18 દિવસમાં કરે છે. 4 દિવસ સાથે કામ કર્યા પછી A છોડી દે છે. B બાકીનું કામ કેટલા દિવસમાં પૂરું કરશે?<br/>
        <b>[Speed Solution]:</b> કુલ કાર્ય = LCM(12, 18) = 36 ચોકલેટ. A = 3, B = 2 ચોકલેટ/દિવસ. 4 દિવસમાં સાથે કરેલું = 4 × 5 = 20 ચોકલેટ. બાકી = 36 - 20 = 16. B પૂરું કરશે = 16 / 2 = <b>8 દિવસ</b>!
      </div>
    </div>
  </div>

  <!-- Trick 5.7 -->
  <div class="trick-card">
    <div class="trick-card-header">
      <span>TRICK 5.7: SPEED 18-TABLE &amp; TRAIN CROSSING (૧૮ નો ઘડિયો &amp; ટ્રેન)</span>
      <span class="tag">Speed Table</span>
    </div>
    <div class="trick-card-body">
      <div class="line">
        <span class="line-label">🎯 પરીક્ષામાં કઈ રીતે ઓળખવો:</span> ઝડપ km/h માંથી m/s માં ફેરવવાની હોય અથવા ટ્રેન પ્લેટફોર્મ પાર કરતી હોય.
      </div>
      <div class="rule-box">
        • ઝડપ ૧૮-ટેબલ શોર્ટકટ: 18 km/h = 5 m/s &nbsp;|&nbsp; 36 = 10 &nbsp;|&nbsp; 54 = 15 &nbsp;|&nbsp; 72 = 20 &nbsp;|&nbsp; 90 = 25 m/s.<br/>
        • પ્લેટફોર્મ પાર કરતી વખતે: <b>કુલ અંતર = ટ્રેનની લંબાઈ + પ્લેટફોર્મની લંબાઈ</b>.
      </div>
      <div class="example-box">
        <b>📝 Real Exam Example:</b> 180 m લાંબી ટ્રેન 54 km/h ની ઝડપે પ્લેટફોર્મને 24 સેકન્ડમાં પાર કરે છે. પ્લેટફોર્મની લંબાઈ શોધો.<br/>
        <b>[Speed Solution]:</b> ઝડપ = 54 km/h = 15 m/s. 24 સેકન્ડમાં અંતર = 15 × 24 = 360 m. પ્લેટફોર્મ = 360 - 180 = <b>180 m</b>!
      </div>
    </div>
  </div>

  <!-- Trick 5.8 -->
  <div class="trick-card">
    <div class="trick-card-header">
      <span>TRICK 5.8: BOATS &amp; STREAMS SPEED FORMULAS (હોડી અને પ્રવાહના સૂત્રો)</span>
      <span class="tag">Boats &amp; Streams</span>
    </div>
    <div class="trick-card-body">
      <div class="line">
        <span class="line-label">🎯 પરીક્ષામાં કઈ રીતે ઓળખવો:</span> હોડી પ્રવાહની દિશામાં (Downstream D) અને સામી દિશામાં (Upstream U) ગતિ કરતી હોય.
      </div>
      <div class="rule-box">
        • <b>શાંત પાણીમાં હોડીની ઝડપ (u) = (D + U) / 2</b>.<br/>
        • <b>પ્રવાહની ઝડપ (Stream Speed v) = (D - U) / 2</b>.
      </div>
      <div class="example-box">
        <b>📝 Real Exam Example:</b> હોડી 36 km ડાઉનસ્ટ્રીમ 3 કલાકમાં અને 24 km અપસ્ટ્રીમ 4 કલાકમાં કાપે છે. પ્રવાહની ઝડપ શોધો.<br/>
        <b>[Speed Solution]:</b> D = 36/3 = 12 km/h. U = 24/4 = 6 km/h. પ્રવાહની ઝડપ v = (12 - 6) / 2 = 6/2 = <b>3 km/h</b>!
      </div>
    </div>
  </div>

  <!-- Trick 5.9 -->
  <div class="trick-card">
    <div class="trick-card-header">
      <span>TRICK 5.9: 7-44-154 CIRCLE SCALING BENCHMARK (૭-૪૪-૧૫૪ વર્તુળ બેન્ચમાર્ક)</span>
      <span class="tag">Mensuration 2D</span>
    </div>
    <div class="trick-card-body">
      <div class="line">
        <span class="line-label">🎯 પરીક્ષામાં કઈ રીતે ઓળખવો:</span> વર્તુળની ત્રિજ્યા, પરિઘ કે ક્ષેત્રફળની ગણતરી.
      </div>
      <div class="rule-box">
        બેન્ચમાર્ક વર્તુળ (ત્રિજ્યા r = 7 cm): પરિઘ = 44 cm | ક્ષેત્રફળ = 154 cm².<br/>
        જો પરિઘ k ગણો થાય → ક્ષેત્રફળ <b>k² ગણું</b> (154 × k²) થાય!
      </div>
      <div class="example-box">
        <b>📝 Real Exam Example:</b> વર્તુળનો પરિઘ 88 cm છે. તેનું ક્ષેત્રફળ શોધો.<br/>
        <b>[Speed Solution]:</b> પરિઘ 88 = 44 × 2 (k = 2, ત્રિજ્યા r = 14). ક્ષેત્રફળ = 154 × 2² = 154 × 4 = <b>616 cm²</b>!
      </div>
    </div>
  </div>

  <!-- Trick 5.10 -->
  <div class="trick-card">
    <div class="trick-card-header">
      <span>TRICK 5.10: FAST COMBINATIONS (nC₂) &amp; PROBABILITY (સંભાવના શોર્ટકટ)</span>
      <span class="tag">Probability</span>
    </div>
    <div class="trick-card-body">
      <div class="line">
        <span class="line-label">🎯 પરીક્ષામાં કઈ રીતે ઓળખવો:</span> થેલામાંથી ૨ દડા કે પત્તા પસંદ કરવાના હોય અને 'એક પણ અમુક રંગનો ન હોય' તેવી સંભાવના.
      </div>
      <div class="rule-box">
        • <b>nC₂ = n(n - 1) / 2</b> (દા.ત. 12C₂ = 66, 8C₂ = 28, 10C₂ = 45).<br/>
        • 'એક પણ X રંગનો ન હોય' માટે સીધા બાકીના રંગોમાંથી ૨ દડા પસંદ કરો: <b>P = (બાકીના)C₂ / કુલ C₂</b>.
      </div>
      <div class="example-box">
        <b>📝 Real Exam Example:</b> થેલામાં 6 લાલ, 4 બ્લુ, 2 લીલા (કુલ 12) દડા છે. ૨ દડા લેતાં એક પણ બ્લુ ન હોય તેની સંભાવના કેટલી?<br/>
        <b>[Speed Solution]:</b> કુલ પરિણામ = 12C₂ = 66. બ્લુ સિવાયના = 6 લાલ + 2 લીલા = 8 દડા. સાનુકૂળ = 8C₂ = 28. સંભાવના = 28 / 66 = <b>14 / 33</b>!
      </div>
    </div>
  </div>

  <!-- GOLDEN RULES BOX -->
  <div class="gold-box">
    <h3>🏆 હિતેન્દ્રસિંહ માટે પરીક્ષા હોલના ૩ સુવર્ણ નિયમો (21 NOV 2026 EXAM PROTOCOL)</h3>
    <ol>
      <li><b>૨૦-સેકન્ડ ડ્રોપ રૂલ (The 20-Second Drop Law):</b> પ્રશ્ન વાંચ્યા પછી જો ૨૦ સેકન્ડમાં રીત કે પેટર્ન ન સમજાય, તો તરત જ SKIP કરો! ૩ મિનિટ અટવાઈ રહીને પછી સ્કીપ કરવાથી આગળના ૨-૩ સરળ પ્રશ્નો છૂટી જશે.</li>
      <li><b>ઝીરો તુક્કા નિયમ (Zero Tukka Law):</b> ક્યારેય અંદાજ (Guess) ન લગાવો! ૧ અંદાજ પણ -0.25 માર્ક્સ કાપે છે. સ્કીપ કરવાથી તમારા પોઝિટિવ માર્ક્સ સંપૂર્ણ સુરક્ષિત રહે છે.</li>
      <li><b>છેલ્લી સેકન્ડનું વેરિફિકેશન (Final Click Check):</b> માઉસનું બટન દબાવતાં પહેલાં ૧ ઊંડો શ્વાસ લો અને ઓપ્શન કન્ફર્મ કરો (દા.ત. સરવાળામાં 440 છે કે 460? પ્રશ્નમાં A પૂછ્યું છે કે B?).</li>
    </ol>
  </div>

</body>
</html>
"""

    with open(html_path, "w", encoding="utf-8") as f:
        f.write(html_content)

    print(f"HTML generated: {html_path}")

    # Compile to PDF using Chrome Headless
    cmd = [
        chrome_path,
        "--headless=new",
        "--disable-gpu",
        "--no-pdf-header-footer",
        f"--print-to-pdf={pdf_path}",
        f"file:///{html_path}"
    ]
    res = subprocess.run(cmd, capture_output=True, text=True)
    if res.returncode == 0 and os.path.exists(pdf_path):
        print(f"Bilingual PDF successfully generated: {pdf_path}")
        print(f"File size: {os.path.getsize(pdf_path)} bytes")
    else:
        print("Error compiling PDF:", res.stderr)

if __name__ == "__main__":
    generate_html_and_pdf()
