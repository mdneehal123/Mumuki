# Guide pages for www.mumuki.in. Built into /guides/<slug>/ by tools/build_pages.py.
# Rules: cosmetic wording only (firmer-looking, plumper-looking, more hydrated). Never promise medical results,
# never claim MUMUKI's banana PDRN works like injected salmon PDRN, never invent studies, reviews or numbers.
# Brand claims are always labelled as the brand's own ("MUMUKI says", "in the brand's tests").

REFS = {
    'galeano': ('Galeano M, et al. Polydeoxyribonucleotide: a promising biological platform to accelerate impaired skin wound healing. Pharmaceuticals (Basel). 2021;14(11):1103.',
                'https://pubmed.ncbi.nlm.nih.gov/34832885/'),
    'naik': ('Naik V, et al. The impact of polydeoxyribonucleotide on wound healing: a systematic review. International Surgery Journal. 2025;12(4):568-574.',
             'https://doi.org/10.18203/2349-2902.isj20250816'),
    'park': ('Park GY, Jang BC. Polydeoxyribonucleotide as a regenerative agent in dermatology and wound healing: mechanisms, clinical applications, and safety. Keimyung Med J. 2025;44(1). doi:10.46308/kmj.2025.00115',
             'https://kumel.medlib.dsmc.or.kr/handle/2015.oak/46110'),
}

GUIDES = [
dict(slug='what-is-pdrn', short='What is PDRN?',
     title='What is <em>PDRN</em>? The "salmon DNA" skincare ingredient, explained',
     seo='What Is PDRN? Salmon DNA Skincare Explained (India)',
     desc='What is PDRN in skincare? How the "salmon DNA" ingredient works, what research shows, plant and banana PDRN, and what to expect from a PDRN serum.',
     dek='PDRN is the ingredient behind one of the biggest K-beauty trends of 2026. Here is what it actually is, where it comes from and what it can realistically do for your skin.',
     answer='PDRN (polydeoxyribonucleotide) is a mix of small DNA fragments, traditionally purified from salmon or trout. In clinics it is injected to support skin repair. In serums and creams it is used for hydrated, plumper-looking, calmer skin. Topical results are gentler than injections.',
     refs=['galeano', 'park'],
     products=[1, 2, 14],
     related=['plant-pdrn-vs-salmon-pdrn', 'pdrn-benefits-for-skin', 'pdrn-serum-vs-pdrn-injection'],
     body='''<h2>PDRN in one paragraph</h2>
<p><b>PDRN stands for polydeoxyribonucleotide.</b> It is a purified mix of DNA fragments, most often taken from salmon or trout. The fragments do not carry genetic instructions into your skin. They act more like a signal: in lab and clinical research, PDRN works mainly by activating a receptor on skin cells called the <b>adenosine A2A receptor</b>, which is linked to calmer inflammation and cell repair (<a href="https://pubmed.ncbi.nlm.nih.gov/34832885/" rel="noopener">Galeano et al., 2021</a>).</p>

<h2>Where PDRN comes from</h2>
<div class="tbl"><table><thead><tr><th>Source</th><th>What it is</th><th>How much research</th></tr></thead><tbody>
<tr><td>Salmon or trout</td><td>The original PDRN, purified from fish DNA</td><td>The most research, mainly on injections and wound healing</td></tr>
<tr><td>Plants (rose, ginseng, banana and others)</td><td>DNA-based ingredients made from plant cells</td><td>Early, mostly lab studies</td></tr>
<tr><td>Fermentation (microbes)</td><td>DNA ingredients grown with biotechnology</td><td>Early, mostly lab studies</td></tr>
</tbody></table></div>
<p>MUMUKI uses a plant version it calls <b>BDRN</b>, made from Jeju bananas. Read the honest comparison in <a href="/guides/plant-pdrn-vs-salmon-pdrn/">plant PDRN vs salmon PDRN</a>.</p>

<h2>How PDRN is used</h2>
<ul><li><b>Injections in clinics</b> ("skin boosters", "salmon DNA" treatments). This is where most of the evidence comes from. Reviews describe faster wound healing and a good safety record in medical use (<a href="https://kumel.medlib.dsmc.or.kr/handle/2015.oak/46110" rel="noopener">Park &amp; Jang, 2025</a>).</li>
<li><b>Serums, ampoules, creams and masks.</b> These are applied on the skin. PDRN fragments are fairly large, so how much reaches deeper skin depends on the formula. Expect hydration, comfort and a plumper look rather than injection-level change. See <a href="/guides/pdrn-serum-vs-pdrn-injection/">PDRN serum vs injection</a>.</li></ul>

<h2>What a PDRN product can realistically do</h2>
<ul><li>Make skin feel more hydrated and look plumper, especially with hyaluronic acid and ceramides in the same formula.</li>
<li>Help skin feel calmer and more comfortable, including after sun or a harsh product.</li>
<li>Support a smoother, glowier, "glass skin" look over a few weeks of regular use.</li></ul>
<p>What it cannot do: replace sunscreen, remove deep wrinkles or pigmentation in days, or work like a clinic treatment. If a product promises that, be careful.</p>

<h2>Why PDRN became so popular in India</h2>
<p>PDRN started in Korean dermatology clinics, then moved into K-beauty serums and masks. In India it is now found in clinic treatments and in a fast-growing number of serums. People like that it is gentle compared with strong actives such as retinol or acids, and that it suits dry, dehydrated and sensitive skin. See <a href="/guides/pdrn-for-indian-skin/">PDRN for Indian skin</a>.</p>

<h2>Who should be careful</h2>
<ul><li>Anyone with a <b>fish allergy</b> should avoid salmon-derived PDRN or ask a doctor first.</li>
<li>There is little safety data on PDRN in <b>pregnancy and breastfeeding</b>; ask your doctor.</li>
<li>Everyone should patch test a new product. See <a href="/guides/is-pdrn-safe/">is PDRN safe?</a></li></ul>''',
     faq=[('Is PDRN really made from salmon sperm?', 'Traditional PDRN is purified from the DNA of salmon or trout sperm cells. Plant-based versions, such as MUMUKI\'s banana BDRN, are made from plant sources instead.'),
          ('Does PDRN change your DNA?', 'No. PDRN fragments are used as a signal for skin cells; they do not insert genetic information into your skin.'),
          ('How long does a PDRN serum take to work?', 'Hydration and comfort can feel better within days to two weeks. If you see a plumper, smoother look, it usually takes 4 to 8 weeks of regular use.'),
          ('Is PDRN good for oily skin?', 'Yes, in light textures such as serums, ampoules and mists. Pair it with a gel moisturiser in humid weather.')]),

dict(slug='plant-pdrn-vs-salmon-pdrn', short='Plant PDRN vs salmon PDRN',
     title='Plant PDRN vs salmon PDRN: <em>what is the difference?</em>',
     seo='Plant PDRN vs Salmon PDRN: Vegan, Banana BDRN Explained',
     desc='Plant (vegan) PDRN vs salmon PDRN: where each comes from, what research shows for each, and what MUMUKI\'s banana BDRN is, explained honestly.',
     dek='Banana, rose, ginseng: plant "PDRN" is everywhere. Here is how it differs from the original salmon PDRN, and what that means for your skin.',
     answer='Salmon PDRN is the original, with the most research behind it, mainly from injections. Plant PDRN is made from plant sources and suits people who prefer vegetarian or fish-free skincare, but its research is still early. In a well-made formula both can support hydrated, plumper-looking skin.',
     refs=['galeano'],
     products=[1, 2, 10],
     related=['what-is-pdrn', 'is-pdrn-safe', 'pdrn-benefits-for-skin'],
     body='''<h2>The short comparison</h2>
<div class="tbl"><table><thead><tr><th></th><th>Salmon PDRN</th><th>Plant PDRN (e.g. banana BDRN)</th></tr></thead><tbody>
<tr><td>Source</td><td>Purified DNA from salmon or trout</td><td>DNA-based ingredients from plant cells</td></tr>
<tr><td>Research</td><td>Larger body of work, mostly injections and wound healing</td><td>Early, mostly lab and brand studies</td></tr>
<tr><td>Fish allergy</td><td>Avoid or ask a doctor</td><td>The PDRN itself has no fish source, but check the full formula</td></tr>
<tr><td>Vegetarian preference</td><td>No</td><td>The PDRN is plant-sourced; other ingredients may not be</td></tr>
<tr><td>Typical use</td><td>Clinic injections, serums, creams</td><td>Serums, creams, masks</td></tr>
</tbody></table></div>

<h2>Why salmon PDRN has more evidence</h2>
<p>PDRN was first developed from fish DNA for medical use, so most published studies, including the reviews on wound healing and skin repair, are about salmon or trout PDRN, usually injected (<a href="https://pubmed.ncbi.nlm.nih.gov/34832885/" rel="noopener">Galeano et al., 2021</a>). Plant versions are newer. In cell studies, some plant PDRN, such as one made from ginseng, acted on the same skin-cell receptor (<a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC10649580/" rel="noopener">Molecules, 2023</a>), but there is little or no research on people, and none we know of on banana PDRN.</p>

<h2>Why many people still choose plant PDRN</h2>
<ul><li><b>Vegetarian preference:</b> the PDRN itself comes from plants, which matters to many Indian families. Other ingredients in the same product may still be animal-derived.</li>
<li><b>Fish allergy:</b> no fish source in the PDRN itself; always check the full ingredient list.</li>
<li><b>Texture and formula:</b> the overall formula (hyaluronic acid, ceramides, collagen, panthenol) matters as much as the PDRN source for hydration and comfort.</li></ul>

<h2>What MUMUKI's BDRN is</h2>
<p>MUMUKI calls its ingredient <b>BDRN</b>: a PDRN-type ingredient from Jeju bananas. The brand describes it as 99% banana-derived and says that in its own tests it absorbed faster and deeper than its salmon-PDRN ampoule. That is the brand's own test, not an independent study, so we present it as such.</p>
<p>In MUMUKI products, BDRN is paired with Manuka honey, hydrolysed collagen, multi-layer hyaluronic acid, panthenol and ceramide capsules. That combination is built for hydration, a plumper look and glow, which is what most people want from a PDRN product. Some MUMUKI products also contain hydrolysed collagen, whose source the brand does not state, so if you have a fish allergy or are vegetarian, check the ingredient list and message us before buying.</p>

<h2>How to choose</h2>
<ul><li>Want the ingredient with the longest research history and have no fish allergy? Salmon PDRN.</li>
<li>Prefer vegetarian or fish-free skincare, or have a fish allergy? Plant PDRN, but check every ingredient, not just the PDRN.</li>
<li>Either way: check the full ingredient list, patch test, and judge results after 4 to 8 weeks, not 4 days.</li></ul>''',
     faq=[('Is plant PDRN real PDRN?', 'Some dermatologists use "PDRN" only for purified fish DNA and call plant versions PDRN-inspired ingredients. Brands use the name for both. What matters for you is the full formula and how your skin tolerates it.'),
          ('Is banana PDRN vegan?', 'MUMUKI says its BDRN is banana-derived. Some MUMUKI products also contain honey and hydrolysed collagen, whose source is not stated, so they are not suitable for a strict vegan routine. Message us if you need to check a product.'),
          ('Is plant PDRN better for sensitive skin?', 'Not automatically. Sensitive skin reacts to the whole formula. Fragrance-free products and a patch test matter more than the PDRN source.')]),

dict(slug='pdrn-benefits-for-skin', short='PDRN benefits for skin',
     title='PDRN benefits for skin: <em>what to expect, honestly</em>',
     seo='PDRN Benefits for Skin: What a PDRN Serum Can Do',
     desc='PDRN benefits for skin explained: hydration, a plumper look, calmer skin and glow. What research supports, what is hype, and how long results take.',
     dek='PDRN is sold as a "repair" ingredient. Here is what it can realistically do in a serum or cream, and where the evidence ends.',
     answer='In serums and creams, PDRN is used for more hydrated, plumper-looking, calmer and glowier skin. Research on injected PDRN shows support for skin repair; topical results are gentler. Any visible change usually takes 4 to 8 weeks of regular use, alongside sunscreen.',
     refs=['galeano', 'naik', 'park'],
     products=[1, 2, 3],
     related=['how-to-use-pdrn-serum', 'pdrn-serum-vs-pdrn-injection', 'what-is-pdrn'],
     body='''<h2>The benefits, one by one</h2>
<div class="tbl"><table><thead><tr><th>Benefit</th><th>What you may notice</th><th>When</th></tr></thead><tbody>
<tr><td>Hydration</td><td>Skin feels less tight, looks dewier</td><td>Days to 2 weeks</td></tr>
<tr><td>Calmer skin</td><td>Less redness and stinging from dryness or harsh products</td><td>1 to 3 weeks</td></tr>
<tr><td>Plumper look</td><td>Fine dryness lines look softer</td><td>4 to 8 weeks</td></tr>
<tr><td>Glow and smoother texture</td><td>The "glass skin" look</td><td>2 to 6 weeks</td></tr>
<tr><td>Firmer-looking skin</td><td>Skin looks bouncier</td><td>8 weeks or more, modest</td></tr>
</tbody></table></div>
<p>These timings are typical for hydrating skincare in general, not figures from PDRN studies. Results vary by skin, product and routine. Sunscreen every morning matters more than any single ingredient.</p>

<h2>What the research actually says</h2>
<p>Reviews of PDRN describe it activating the adenosine A2A receptor on skin cells, supporting new blood vessel growth, collagen-making cells and calmer inflammation, mostly in wound-healing studies, many of them in the lab or in animals (<a href="https://pubmed.ncbi.nlm.nih.gov/34832885/" rel="noopener">Galeano et al., 2021</a>; <a href="https://doi.org/10.18203/2349-2902.isj20250816" rel="noopener">Naik et al., 2025</a>). A 2025 review reports few side effects in medical studies of salmon PDRN (<a href="https://kumel.medlib.dsmc.or.kr/handle/2015.oak/46110" rel="noopener">Park &amp; Jang, 2025</a>).</p>
<p>Most of that research uses <b>injected</b> PDRN. On the skin surface, large DNA fragments do not travel as deep, so serums and creams give gentler results. That is why a good PDRN product also contains proven hydrators such as hyaluronic acid, panthenol and ceramides.</p>

<h2>Who benefits most</h2>
<ul><li><b>Dry, dehydrated or tight skin</b>, especially in AC offices and winter.</li>
<li><b>Sensitive or easily irritated skin</b> that cannot handle strong acids or retinol every night.</li>
<li><b>Dull, tired-looking skin</b> that needs bounce and glow.</li>
<li><b>Skin recovering</b> from sun, a harsh product or a facial (wait until any broken skin has healed).</li></ul>

<h2>What PDRN will not do</h2>
<ul><li>It will not lighten your natural skin colour or remove melasma.</li>
<li>It will not replace sunscreen, retinoids or a dermatologist's treatment for acne or pigmentation.</li>
<li>It will not give injection-level results from a bottle.</li></ul>

<h2>Getting the most from it</h2>
<ol><li>Use it on clean skin, before your moisturiser.</li>
<li>Use it every day, morning or night, for at least 4 to 8 weeks.</li>
<li>Pair it with hydrators (hyaluronic acid, ceramides) and daily sunscreen.</li>
<li>Take photos in the same light every two weeks.</li></ol>
<p>Step-by-step routines are in <a href="/guides/how-to-use-pdrn-serum/">how to use a PDRN serum</a>.</p>''',
     faq=[('Does PDRN reduce wrinkles?', 'It can make fine dryness lines look softer by plumping and hydrating skin. Deeper wrinkles need a dermatologist; topical PDRN gives modest changes at best.'),
          ('Does PDRN help acne scars?', 'Research on PDRN for scars mostly uses injections or clinic procedures. A serum may help skin look smoother and calmer, but see a dermatologist for scars.'),
          ('Is PDRN good for pigmentation?', 'PDRN is not a pigment-fading ingredient on its own. Sunscreen and ingredients like niacinamide or vitamin C do more for dark spots.')]),

dict(slug='how-to-use-pdrn-serum', short='How to use a PDRN serum',
     title='How to use a PDRN serum or ampoule: <em>a simple routine</em>',
     seo='How to Use PDRN Serum: Morning and Night Routine',
     desc='How to use a PDRN serum or ampoule: where it goes in your routine, morning and night steps, what to mix it with, and mistakes to avoid in Indian weather.',
     dek='PDRN is one of the easiest actives to add to a routine. Here is exactly where it goes, what to pair it with, and how to use it in Indian heat and humidity.',
     answer='Apply a PDRN serum or ampoule after cleansing (and toner, if you use one), then follow with moisturiser, and sunscreen in the morning. It can be used morning and night. Start with once a day if your skin is sensitive, and give it 4 to 8 weeks.',
     refs=[],
     products=[14, 1, 2],
     related=['korean-glass-skin-routine-india', 'pdrn-for-indian-skin', 'is-pdrn-safe'],
     body='''<h2>Where PDRN goes in your routine</h2>
<ol><li><b>Cleanse</b> with a gentle face wash and lukewarm water.</li>
<li><b>Toner or a prep step</b> (optional). MUMUKI's <a href="/products/honey-banana-pdrn-bubble-mask/">Bubble Mask</a> is a leave-on prep step that melts in within seconds.</li>
<li><b>PDRN serum or ampoule.</b> Massage a small amount into face and neck until absorbed.</li>
<li><b>Moisturiser</b> to seal it in, such as a ceramide cream.</li>
<li><b>Morning only: sunscreen</b>, SPF 30 or higher.</li></ol>

<h2>A simple morning and night routine</h2>
<div class="tbl"><table><thead><tr><th></th><th>Morning</th><th>Night</th></tr></thead><tbody>
<tr><td>1</td><td>Gentle cleanse</td><td>Cleanse (double cleanse if you wore sunscreen or makeup)</td></tr>
<tr><td>2</td><td>PDRN serum or ampoule</td><td>PDRN serum or ampoule</td></tr>
<tr><td>3</td><td>Light moisturiser</td><td>Richer moisturiser</td></tr>
<tr><td>4</td><td>Sunscreen</td><td>Sheet or hydrogel mask 2 to 3 times a week (optional)</td></tr>
</tbody></table></div>

<h2>What to mix PDRN with</h2>
<div class="tbl"><table><thead><tr><th>Ingredient</th><th>With PDRN?</th><th>How</th></tr></thead><tbody>
<tr><td>Hyaluronic acid, ceramides, panthenol</td><td>Yes, ideal</td><td>Same routine; many PDRN products already contain them</td></tr>
<tr><td>Niacinamide</td><td>Yes</td><td>Same routine, serum first then PDRN, or alternate mornings</td></tr>
<tr><td>Vitamin C</td><td>Yes</td><td>Vitamin C in the morning, PDRN at night if your skin is sensitive</td></tr>
<tr><td>Retinol or retinoids</td><td>Yes, carefully</td><td>Retinol at night, PDRN in the morning or on rest nights</td></tr>
<tr><td>AHA/BHA exfoliants, peels</td><td>Yes, on different nights</td><td>Do not stack strong acids with a new product while your skin adjusts</td></tr>
</tbody></table></div>

<h2>How much to use</h2>
<p>For an ampoule, 2 to 3 drops cover the face and neck. Thick, stretchy ampoules, like MUMUKI's <a href="/products/honey-banana-pdrn-capsule-ampoule/">Capsule Ampoule</a>, spread further than they look. More product does not work faster.</p>

<h2>Using it in Indian weather</h2>
<ul><li><b>Humid summer and monsoon:</b> serum plus a light gel moisturiser, or a mist, is often enough.</li>
<li><b>Dry winter and AC rooms:</b> add a richer cream at night; a cream mist helps during the day.</li>
<li><b>After sun:</b> PDRN products are soothing, but sunscreen is what prevents more tan.</li></ul>
<p>More in <a href="/guides/pdrn-for-indian-skin/">PDRN for Indian skin</a>.</p>

<h2>Mistakes to avoid</h2>
<ul><li>Skipping sunscreen in the morning.</li>
<li>Starting several new actives in the same week; add one at a time.</li>
<li>Judging after a few days. Give it 4 to 8 weeks.</li>
<li>Using it on broken or infected skin.</li></ul>''',
     faq=[('Can I use PDRN serum every day?', 'Yes. Most PDRN serums are gentle enough for daily use, morning and night. Start once a day if your skin is sensitive.'),
          ('Should PDRN go before or after vitamin C?', 'If you use both in one routine, apply the thinner, watery product first. Many people keep vitamin C for the morning and PDRN for the night.'),
          ('Can I use PDRN with retinol?', 'Yes. Use retinol at night and PDRN in the morning, or use PDRN on nights you skip retinol, to help skin feel more comfortable.'),
          ('Do I still need sunscreen?', 'Yes, every morning. Sunscreen protects the results of any routine.')]),

dict(slug='pdrn-serum-vs-pdrn-injection', short='PDRN serum vs injection',
     title='PDRN serum vs PDRN injection: <em>which do you need?</em>',
     seo='PDRN Serum vs PDRN Injection: Differences, Cost, Results',
     desc='PDRN serum vs PDRN injection (skin booster) in India: how each works, results, side effects, cost and who each suits, explained simply.',
     dek='"Salmon DNA" injections and PDRN serums share an ingredient, not results. Here is how they really compare.',
     answer='PDRN injections are clinic treatments that place PDRN inside the skin, with the strongest evidence and the biggest changes, plus needle side effects and higher cost. PDRN serums are daily skincare: gentler, cheaper and needle-free, best for hydration, comfort and glow. Many people use a serum, and some add injections with a dermatologist.',
     refs=['galeano', 'park'],
     products=[1, 2, 10],
     related=['what-is-pdrn', 'pdrn-benefits-for-skin', 'is-pdrn-safe'],
     body='''<h2>Side by side</h2>
<div class="tbl"><table><thead><tr><th></th><th>PDRN serum, ampoule or cream</th><th>PDRN injection (skin booster)</th></tr></thead><tbody>
<tr><td>Where it goes</td><td>On the skin surface</td><td>Injected into the skin by a doctor</td></tr>
<tr><td>Evidence</td><td>Limited; gentle effects</td><td>Stronger; most PDRN research is on injections</td></tr>
<tr><td>Typical results</td><td>Hydration, comfort, glow, a plumper look</td><td>Bigger changes in skin quality over several sessions</td></tr>
<tr><td>Side effects</td><td>Rare; occasional irritation</td><td>Redness, swelling, bruising for a few days</td></tr>
<tr><td>Who gives it</td><td>You, at home, daily</td><td>Only a qualified doctor or dermatologist</td></tr>
<tr><td>Cost in India</td><td>Hundreds to a couple of thousand rupees a bottle</td><td>Usually much more, per session</td></tr>
</tbody></table></div>

<h2>Why injections show bigger effects</h2>
<p>PDRN is made of fairly large DNA fragments. Injected, they reach the deeper skin where repair happens. That is the setting for most of the research on wound healing and skin repair (<a href="https://pubmed.ncbi.nlm.nih.gov/34832885/" rel="noopener">Galeano et al., 2021</a>). Large fragments are unlikely to reach that deep from the skin surface, and topical studies are limited, so serums are better thought of as excellent hydrating and soothing skincare, not a bottled injection.</p>

<h2>Safety</h2>
<p>A 2025 review reports very few side effects with PDRN in medical use (<a href="https://kumel.medlib.dsmc.or.kr/handle/2015.oak/46110" rel="noopener">Park &amp; Jang, 2025</a>). Injections still carry the usual needle risks, and must only be done by a qualified doctor in a proper clinic, never at a salon. People with a fish allergy, who are pregnant or breastfeeding, or who have an active skin infection should not have salmon PDRN injections without a doctor's advice.</p>

<h2>Which one is right for you?</h2>
<ul><li><b>Choose a serum</b> if you want daily hydration, glow and comfort, have sensitive skin, or are new to PDRN.</li>
<li><b>Consider injections</b>, with a dermatologist, if you want bigger changes in skin texture or quality and accept the cost and downtime.</li>
<li><b>Both:</b> many people use a PDRN serum at home between clinic sessions, as their doctor advises.</li></ul>''',
     faq=[('Can a PDRN serum replace PDRN injections?', 'No. A serum is gentle daily skincare. It will not give the same results as injections.'),
          ('Is a PDRN injection painful?', 'Clinics usually use numbing cream. Expect some redness, small bumps or bruising for a few days.'),
          ('Can I use a PDRN serum after a PDRN injection?', 'Usually yes, once your doctor says the skin has settled. Follow your clinic\'s aftercare instructions first.')]),

dict(slug='is-pdrn-safe', short='Is PDRN safe?',
     title='Is PDRN safe? <em>Side effects and who should avoid it</em>',
     seo='Is PDRN Safe? Side Effects, Fish Allergy and Pregnancy',
     desc='Is PDRN safe for skin? Side effects of PDRN serums and injections, fish allergy, pregnancy, sensitive skin, and how to patch test, explained simply.',
     dek='PDRN is generally well tolerated in medical studies. Here is who should still be careful, and how to start safely.',
     answer='PDRN is generally well tolerated. In serums and creams, reactions, when they happen, often come from other ingredients such as fragrance or retinol. Avoid salmon PDRN if you have a fish allergy, ask a doctor in pregnancy or breastfeeding, and patch test any new product for 24 to 48 hours.',
     refs=['park', 'galeano'],
     products=[2, 3, 1],
     related=['what-is-pdrn', 'plant-pdrn-vs-salmon-pdrn', 'how-to-use-pdrn-serum'],
     body='''<h2>How safe is PDRN?</h2>
<p>Reviews of PDRN in medical use report very few adverse events across trials and real-world use (<a href="https://kumel.medlib.dsmc.or.kr/handle/2015.oak/46110" rel="noopener">Park &amp; Jang, 2025</a>; <a href="https://pubmed.ncbi.nlm.nih.gov/34832885/" rel="noopener">Galeano et al., 2021</a>).</p>

<h2>Possible side effects</h2>
<div class="tbl"><table><thead><tr><th>Reaction</th><th>Often linked to</th><th>What to do</th></tr></thead><tbody>
<tr><td>Mild stinging or warmth</td><td>Applying on damp skin, or retinol and acids in the formula</td><td>Apply on fully dry skin; use less often</td></tr>
<tr><td>Small bumps or breakouts</td><td>A texture too rich for your skin</td><td>Use a lighter texture; check the moisturiser too</td></tr>
<tr><td>Redness, itching, rash</td><td>Irritation or allergy to an ingredient</td><td>Stop and rinse; see a doctor if it does not settle</td></tr>
<tr><td>Swelling of face, lips or eyes</td><td>Allergic reaction</td><td>Stop and get medical help at once</td></tr>
<tr><td>Injection only: redness, swelling, bruising</td><td>The injection itself; usually lasts a few days</td><td>Follow your clinic's aftercare</td></tr>
</tbody></table></div>

<h2>Who should be careful</h2>
<ul><li><b>Fish allergy:</b> avoid salmon-derived PDRN, or ask a doctor. With plant PDRN, still check the full ingredient list for fish-derived ingredients such as collagen.</li>
<li><b>Pregnancy and breastfeeding:</b> there is little safety data on PDRN, and some MUMUKI products list retinol. Ask your doctor before starting.</li>
<li><b>Active skin infection, open wounds or eczema flares:</b> wait until the skin has healed.</li>
<li><b>Very sensitive skin:</b> choose fragrance-free products and patch test first.</li>
<li><b>Injections:</b> only from a qualified doctor, never a salon.</li></ul>

<h2>How to patch test</h2>
<ol><li>Apply a small amount behind your ear or on your inner arm.</li>
<li>Leave it for 24 to 48 hours.</li>
<li>No redness, itching or swelling? Start on the face once a day.</li></ol>

<h2>Reading the label</h2>
<p>Check the full ingredient list, the importer or maker's name and address, batch number and expiry. Many reactions come from fragrance or other actives, not PDRN. MUMUKI's Honey Banana skincare is fragrance-free. Several MUMUKI products, including the masks, list retinol among their ingredients, so check the pack and start slowly if your skin is sensitive. See <a href="/genuine-mumuki-india/">how to buy genuine MUMUKI in India</a>.</p>''',
     faq=[('Is PDRN safe for sensitive skin?', 'Usually, yes. Choose fragrance-free formulas, patch test, and add one new product at a time.'),
          ('Can I use PDRN during pregnancy?', 'There is little safety data on PDRN in pregnancy. Ask your doctor before using it.'),
          ('Is PDRN vegetarian?', 'Salmon PDRN comes from fish. Plant PDRN, such as MUMUKI\'s banana BDRN, is plant-sourced, but other ingredients in the same product, such as collagen, may be animal-derived. Check the full ingredient list.')]),

dict(slug='pdrn-for-indian-skin', short='PDRN for Indian skin',
     title='PDRN for Indian skin: <em>heat, humidity and oily skin</em>',
     seo='PDRN for Indian Skin: Oily Skin, Humidity and Summer',
     desc='Does PDRN suit Indian skin? How to use PDRN in humid summers, monsoon and dry winters, for oily, dry and sensitive skin, with simple routines.',
     dek='Korean routines are built for a different climate. Here is how to make PDRN work in Indian heat, humidity, dust and AC rooms.',
     answer='PDRN suits most Indian skin types because it hydrates without heaviness. Oily skin does best with a serum or mist and a gel moisturiser; dry skin can add a ceramide cream. In every season, daily sunscreen does more for tan and dark spots than PDRN.',
     refs=[],
     products=[3, 1, 4],
     related=['how-to-use-pdrn-serum', 'korean-glass-skin-routine-india', 'pdrn-benefits-for-skin'],
     body='''<h2>Does PDRN suit Indian skin?</h2>
<p>Yes. PDRN is a hydrating, soothing ingredient, not a strong exfoliant, so it suits brown skin that can darken after irritation. The bigger question is <b>texture</b>: the right serum, cream or mist for your weather and skin type.</p>

<h2>By skin type</h2>
<div class="tbl"><table><thead><tr><th>Skin type</th><th>Best PDRN format</th><th>Tip</th></tr></thead><tbody>
<tr><td>Oily or acne-prone</td><td>Ampoule or serum; a mist over sunscreen if skin feels dry</td><td>Finish with a light gel moisturiser; skip heavy creams in summer</td></tr>
<tr><td>Combination</td><td>Ampoule all over, cream only on dry areas</td><td>Use less product on the T-zone</td></tr>
<tr><td>Dry</td><td>Ampoule plus a ceramide cream</td><td>Add a mask 2 to 3 times a week in winter</td></tr>
<tr><td>Sensitive</td><td>Fragrance-free cream or mist</td><td>Patch test; add one product at a time</td></tr>
</tbody></table></div>

<h2>By season</h2>
<ul><li><b>Summer (March to June):</b> light layers. PDRN ampoule, gel moisturiser, sunscreen. A mist on the go cools and refreshes.</li>
<li><b>Monsoon:</b> humidity can make rich creams feel greasy, so use less. Keep skin clean and dry before applying.</li>
<li><b>Winter and AC rooms:</b> skin loses water faster. Add a ceramide cream at night and a mist during the day.</li></ul>

<h2>Tan, pigmentation and PDRN</h2>
<p>PDRN is not a pigment-fading ingredient. Hydrated, calmer skin looks brighter, but to prevent new tan you need sunscreen every morning, reapplied outdoors. For dark spots, ingredients such as niacinamide or vitamin C, or a dermatologist, do more.</p>

<h2>A simple Indian-summer routine</h2>
<ol><li>Gentle cleanser.</li>
<li>2 to 3 drops of PDRN ampoule.</li>
<li>Light gel moisturiser.</li>
<li>Sunscreen SPF 30 or higher.</li>
<li>Midday: a few sprays of a cream mist over makeup or sunscreen if skin feels dry in the AC.</li></ol>
<p>For the full Korean-style version, see <a href="/guides/korean-glass-skin-routine-india/">a glass-skin routine for India</a>.</p>''',
     faq=[('Will PDRN make oily skin greasier?', 'Not if you choose light textures. Ampoules and serums absorb quickly; pair them with a gel moisturiser.'),
          ('Can PDRN help with tan?', 'It can help sun-stressed skin feel calmer and look fresher, but it does not remove tan. Sunscreen prevents new tan.'),
          ('Is PDRN good for monsoon skin?', 'Yes, in light layers. Keep skin clean and use less of rich creams when humidity is high.')]),

dict(slug='pdrn-serum-price-in-india', short='PDRN serum price in India',
     title='PDRN serum price in India: <em>what you should pay</em>',
     seo='PDRN Serum Price in India (2026): What Is Worth Paying',
     desc='PDRN serum price in India in 2026: typical ranges for Indian and imported Korean PDRN serums, why prices differ, and how to avoid fakes and overpaying.',
     dek='PDRN serums in India range from a few hundred rupees to several thousand. Here is what drives the price, and how to know what you are paying for.',
     answer='In India, PDRN serums from Indian brands mostly cost around ₹550 to ₹1,000 for 30 ml. Imported Korean PDRN serums, ampoules and creams usually cost about ₹1,200 to ₹3,000. The price reflects the full formula, the import, and the seller, not just the PDRN.',
     refs=[],
     products=[1, 2, 9],
     related=['genuine-mumuki', 'what-is-pdrn', 'plant-pdrn-vs-salmon-pdrn'],
     body='''<h2>Typical PDRN prices in India (2026)</h2>
<div class="tbl"><table><thead><tr><th>Type</th><th>Typical price</th><th>Notes</th></tr></thead><tbody>
<tr><td>Indian-brand PDRN serum, 30 ml</td><td>About ₹550 to ₹1,000</td><td>Often PDRN plus niacinamide, peptides or collagen</td></tr>
<tr><td>Imported Korean PDRN serum or ampoule</td><td>About ₹1,200 to ₹3,000</td><td>Import, duties and Korean formulations add cost</td></tr>
<tr><td>Korean PDRN creams and sets</td><td>About ₹1,500 to ₹4,500+</td><td>Sets bundle 2 to 3 steps</td></tr>
<tr><td>PDRN injections at a clinic</td><td>Much higher, per session</td><td>A medical treatment, not skincare</td></tr>
</tbody></table></div>
<p>Prices change often with offers; use these as a guide, not a quote.</p>

<h2>Why prices differ so much</h2>
<ul><li><b>The whole formula:</b> hyaluronic acid, ceramides, collagen and capsules cost more than a simple serum base.</li>
<li><b>Import:</b> imported cosmetics carry shipping, duties, compliance and importer costs.</li>
<li><b>Seller:</b> authorised importers price differently from resellers and grey-market sellers.</li>
<li><b>PDRN source and amount:</b> brands state amounts differently (ppm, %), so compare carefully.</li></ul>

<h2>How to avoid overpaying or buying fakes</h2>
<ul><li>Check for an <b>Indian importer label</b> with name, address, batch number, MRP and expiry.</li>
<li>Be wary of prices far below the usual range on marketplaces.</li>
<li>Buy from a seller who imports officially into India and gives a GST invoice.</li>
<li>Avoid "ship from abroad" offers that cannot handle returns in India.</li></ul>
<p>More in <a href="/genuine-mumuki-india/">how to buy genuine MUMUKI in India</a>.</p>

<h2>MUMUKI prices in India</h2>
<p>MUMUKI Honey Banana PDRN skincare is imported from Korea and sold in India by Beauty Mart Pvt Ltd. For current prices and availability, message us on WhatsApp from any <a href="/#shop">product page</a>. People on the launch list get 10% off their first order.</p>

<h2>Is a more expensive PDRN serum better?</h2>
<p>Not automatically. Choose by your skin type, the full ingredient list, a texture you will use every day, and an honest seller. A serum you use daily for two months will do more than an expensive one you use once a week.</p>''',
     faq=[('Why is Korean PDRN serum costly in India?', 'Imported cosmetics carry international shipping, import duties, compliance and importer costs, on top of the formula itself.'),
          ('Is a cheap PDRN serum fake?', 'Not necessarily; many Indian-brand PDRN serums are affordable. But a famous imported product sold far below its usual price is a warning sign.'),
          ('What is the price of MUMUKI PDRN in India?', 'Message MUMUKI India on WhatsApp for current prices and availability; launch-list members get 10% off their first order.')]),

dict(slug='korean-glass-skin-routine-india', short='Glass-skin routine for India',
     title='A Korean <em>glass-skin</em> routine for India',
     seo='Korean Glass Skin Routine for India: Simple Steps',
     desc='A Korean glass-skin routine adapted for India: simple morning and night steps, masks, what to skip in humidity, and realistic expectations for brown skin.',
     dek='You do not need ten steps. Here is a short, Korean-style routine that works in Indian weather and fits a real budget.',
     answer='Glass skin means hydrated, smooth, even-looking skin with a soft glow. In India, a simple routine works best: gentle cleanser, a hydrating PDRN or hyaluronic serum, a moisturiser suited to your weather, and sunscreen every morning, with a sheet or hydrogel mask a few times a week.',
     refs=[],
     products=[10, 14, 1, 2, 3, 13],
     related=['how-to-use-pdrn-serum', 'how-to-use-korean-face-masks', 'pdrn-for-indian-skin'],
     body='''<h2>What "glass skin" really means</h2>
<p>Glass skin is the Korean idea of skin so well hydrated and smooth that it reflects light. It is about <b>hydration, a healthy barrier and gentle care</b>, not about changing your skin colour. Brown skin can glow beautifully with the same principles.</p>

<h2>The routine</h2>
<div class="tbl"><table><thead><tr><th>Step</th><th>Morning</th><th>Night</th><th>MUMUKI option</th></tr></thead><tbody>
<tr><td>1. Cleanse</td><td>Gentle wash</td><td>Double cleanse if you wore sunscreen</td><td>Your usual gentle cleanser</td></tr>
<tr><td>2. Prep</td><td>Optional</td><td>Leave-on prep</td><td><a href="/products/honey-banana-pdrn-bubble-mask/">Bubble Mask</a></td></tr>
<tr><td>3. Treat</td><td>PDRN ampoule</td><td>PDRN ampoule</td><td><a href="/products/honey-banana-pdrn-capsule-ampoule/">Capsule Ampoule</a></td></tr>
<tr><td>4. Seal</td><td>Light moisturiser</td><td>Richer cream</td><td><a href="/products/honey-banana-pdrn-capsule-cream/">Capsule Cream</a></td></tr>
<tr><td>5. Protect</td><td>Sunscreen SPF 30+</td><td>None</td><td>Any sunscreen you will wear daily</td></tr>
<tr><td>Extra</td><td>Mist over makeup</td><td>Mask 2 to 3 times a week</td><td><a href="/products/honey-banana-pdrn-cream-mist/">Cream Mist</a>, <a href="/products/honey-banana-bdrn-hydrogel-mask/">Hydrogel Mask</a></td></tr>
</tbody></table></div>
<p>MUMUKI's <a href="/products/honey-banana-pdrn-3-step-skincare-set/">3-Step Skincare Set</a> bundles steps 2 to 4.</p>

<h2>Adapting it to Indian weather</h2>
<ul><li><b>Humid months:</b> skip the rich cream in the morning; ampoule plus gel moisturiser and sunscreen is enough.</li>
<li><b>Dry months and AC:</b> use the cream morning and night, and a mist during the day.</li>
<li><b>Dust and pollution:</b> cleanse properly at night; a gentle double cleanse removes sunscreen.</li></ul>

<h2>What to skip</h2>
<ul><li>Ten-step routines you will not keep up.</li>
<li>Harsh scrubs and daily peels: they cause irritation and can darken brown skin.</li>
<li>Lemon, baking soda or toothpaste "hacks".</li>
<li>Layering many strong actives at once.</li></ul>

<h2>What to expect</h2>
<p>Hydration and glow often improve within 2 weeks. Smoother texture takes 4 to 8 weeks. Dark spots and acne marks need sunscreen and targeted treatment, and time.</p>''',
     faq=[('Can Indian skin get glass skin?', 'Yes. Glass skin is about hydration, smoothness and glow, which any skin tone can achieve with gentle, consistent care and sunscreen.'),
          ('How many steps do I need?', 'Four is plenty for most people: cleanse, serum, moisturiser and sunscreen, with a mask a few times a week.'),
          ('Is glass skin the same as skin whitening?', 'No. Glass skin is about healthy, hydrated, glowing skin. It does not change your natural skin colour.')]),

dict(slug='how-to-use-korean-face-masks', short='How to use Korean face masks',
     title='How to use sheet, hydrogel and bubble masks: <em>a simple guide</em>',
     seo='How to Use Sheet, Hydrogel and Bubble Masks Correctly',
     desc='How to use Korean sheet masks, hydrogel masks and bubble masks: how long to leave them on, how often, what to do after, and common mistakes.',
     dek='Masks are the easiest way to give skin a quick hydration boost. Here is how to use each type properly, and how often.',
     answer='Use a sheet mask for 10 to 20 minutes on clean, toned skin, then pat in the leftover essence and seal with a moisturiser. Hydrogel masks are worn as the pack directs; some, like MUMUKI\'s, are made for longer or overnight wear. Leave-on bubble masks go on after cleansing and absorb in seconds. Most people mask 2 to 3 times a week.',
     refs=[],
     products=[4, 13, 14],
     related=['korean-glass-skin-routine-india', 'how-to-use-pdrn-serum', 'pdrn-for-indian-skin'],
     body='''<h2>The three mask types</h2>
<div class="tbl"><table><thead><tr><th>Type</th><th>What it is</th><th>How long</th><th>How often</th></tr></thead><tbody>
<tr><td>Sheet mask</td><td>Fabric soaked in essence</td><td>10 to 20 minutes</td><td>2 to 3 times a week</td></tr>
<tr><td>Hydrogel mask</td><td>Gel sheet that hugs the face</td><td>As directed on the pack (often 20 to 30 minutes; some, like MUMUKI's, are made for longer or overnight wear)</td><td>2 to 3 times a week</td></tr>
<tr><td>Bubble mask (leave-on)</td><td>A foam that melts into skin</td><td>About 30 seconds to absorb</td><td>As a daily prep step</td></tr>
</tbody></table></div>

<h2>How to use a sheet mask</h2>
<ol><li>Cleanse and, if you use one, apply toner.</li>
<li>Unfold the mask and fit it to your eyes, nose and mouth.</li>
<li>Leave it on for 10 to 20 minutes. Do not let it dry out on the face.</li>
<li>Remove it and pat the leftover essence into face and neck.</li>
<li>Seal with a moisturiser.</li></ol>
<p>MUMUKI's <a href="/products/honey-banana-pdrn-ampoule-mask/">Ampoule Mask</a> has a visible hyaluronic layer that fades as the formula absorbs.</p>

<h2>How to use a hydrogel mask</h2>
<ol><li>Cleanse and tone.</li>
<li>Apply the two pieces (top and bottom) smoothly.</li>
<li>Leave it on for the time on the pack. MUMUKI's is made to be worn until it turns transparent, or overnight as the last step.</li>
<li>Remove and pat in any remaining essence.</li></ol>
<p>The brand says MUMUKI's <a href="/products/honey-banana-bdrn-hydrogel-mask/">Hydrogel Mask</a> starts turning transparent after about 40 to 50 minutes and recommends around 3 hours of wear.</p>

<h2>How to use a bubble mask</h2>
<ol><li>After cleansing, pump 2 to 3 times into your palm.</li>
<li>Spread evenly over the face; the bubbles melt in quickly.</li>
<li>Let it absorb for about 30 seconds. Do not rinse.</li>
<li>Follow with your serum and moisturiser.</li></ol>
<p>See MUMUKI's <a href="/products/honey-banana-pdrn-bubble-mask/">Bubble Mask</a>.</p>

<h2>Mistakes to avoid</h2>
<ul><li>Leaving a sheet mask on until it dries; it can pull moisture back out.</li>
<li>Rinsing off the essence afterwards.</li>
<li>Reusing a mask or keeping an opened pouch.</li>
<li>Masking on broken, sunburnt or freshly waxed skin.</li>
<li>Skipping moisturiser after a sheet mask.</li></ul>

<h2>Best times to mask in India</h2>
<ul><li>The night before a wedding, party or photoshoot.</li>
<li>After a long day in the sun (once skin has cooled), or in dry AC rooms.</li>
<li>Store sheet masks in a cool place; a few minutes in the fridge feels refreshing in summer.</li></ul>''',
     faq=[('Can I sleep with a sheet mask on?', 'No. Sheet masks should come off after 10 to 20 minutes. Hydrogel masks made for overnight use are different.'),
          ('Should I wash my face after a sheet mask?', 'No. Pat the leftover essence in, then apply moisturiser.'),
          ('Can I use a face mask every day?', 'Gentle hydrating masks can be used often, but 2 to 3 times a week is enough for most people. Leave-on bubble masks are made for daily use.')]),
]

GENUINE = dict(slug='genuine-mumuki-india', short='Genuine MUMUKI in India',
     title='How to buy <em>genuine MUMUKI</em> in India',
     seo='Genuine MUMUKI in India: How to Spot Original Products',
     desc='How to buy genuine MUMUKI Honey Banana PDRN skincare in India: the importer label, batch and expiry checks, warning signs of fakes, and who sells MUMUKI here.',
     dek='Popular K-beauty products are often copied or sold past their best. Here is how to know your MUMUKI is the real thing.',
     answer='Genuine MUMUKI sold in India carries an Indian importer label with the importer\'s name and address, batch number, MRP and expiry date. MUMUKI products in India are imported and marketed by Beauty Mart Pvt Ltd, Bhatkal, Karnataka. Buy directly from MUMUKI India and ask for a GST invoice.',
     body='''<h2>Who sells MUMUKI in India</h2>
<p>MUMUKI India (www.mumuki.in) is run by <b>Beauty Mart Pvt Ltd</b>, Azad Nagar 4th Cross, Bhatkal, Uttara Kannada, Karnataka 581320. We import MUMUKI Honey Banana PDRN skincare from Korea and ship it from within India, so there are no surprise customs charges at your door.</p>

<h2>Check these on every pack</h2>
<div class="tbl"><table><thead><tr><th>Check</th><th>What to look for</th></tr></thead><tbody>
<tr><td>Indian importer label</td><td>Importer name and full address in India, and the import registration details where printed</td></tr>
<tr><td>Batch number</td><td>Printed clearly, matching the box and the bottle or pouch</td></tr>
<tr><td>Manufacturing and expiry dates</td><td>Clearly printed and not expired</td></tr>
<tr><td>MRP</td><td>Printed on the label, inclusive of taxes</td></tr>
<tr><td>Ingredient list</td><td>Full list, readable</td></tr>
<tr><td>Seal and packaging</td><td>Intact seal, clean print, no smudged or misspelt text</td></tr>
<tr><td>Invoice</td><td>A proper GST invoice from the seller</td></tr>
</tbody></table></div>

<h2>Warning signs</h2>
<ul><li>A price far below what authorised sellers charge.</li>
<li>No Indian importer label, or a sticker covering the original details.</li>
<li>Expiry date missing, scratched off or very close.</li>
<li>Sellers who cannot give an invoice or accept returns for damaged items.</li>
<li>"Shipped from abroad" listings with long, untracked delivery times.</li></ul>

<h2>If you are unsure</h2>
<p>Send us a clear photo of the box, the label and the batch number on WhatsApp at +91 99808 81230, and we will check the label and batch details against our stock. If a product you bought from us arrives damaged or wrong, share an unboxing video or clear photos within 48 hours and we will replace it or refund you, as described in our <a href="/returns.html">returns policy</a>.</p>

<h2>Reviews</h2>
<p>MUMUKI's Honey Banana line has customer reviews on the brand's official store. Reviews from our customers in India will appear on our product pages after launch. We do not post made-up reviews.</p>''',
     faq=[('Is MUMUKI a Korean brand?', 'Yes. MUMUKI is a Korean skincare brand. MUMUKI India imports it from Korea and sells it in India.'),
          ('Is MUMUKI available on Amazon or Flipkart?', 'Message us on WhatsApp to confirm current authorised sellers before you buy elsewhere.'),
          ('Do I pay customs duty when ordering from mumuki.in?', 'No. We ship from within India, so there is no customs charge at delivery.')])
