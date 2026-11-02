# mumuki.in — setup guide

Upload **everything in this folder** to the root of mumuki.in (index.html, the policy pages, `images/`, favicon.svg, apple-touch-icon.png, sitemap.xml, robots.txt).

All settings live near the top of `index.html`. Search for the names below and paste your values.

## 1. Save launch-list sign-ups to a Google Sheet (5 minutes)
1. Create a Google Sheet called **mumuki.in sign-ups**.
2. Open **Extensions → Apps Script**, delete the sample code, paste the contents of `google-sheet-script.gs`, then click **Save**.
3. Click **Deploy → New deployment → Web app**. Set *Execute as*: **Me** and *Who has access*: **Anyone**. Click **Deploy** and allow access.
4. Copy the **Web app URL** and paste it in index.html:
   `const SIGNUP_ENDPOINT = "https://script.google.com/macros/s/....../exec";`

Until you do this, each sign-up opens WhatsApp with the customer's email so you don't lose anyone.

## 2. Google Analytics 4
1. Go to analytics.google.com → Admin → Create property → Web stream for `https://mumuki.in`.
2. Copy the Measurement ID (starts with `G-`) and paste it: `window.GA4_ID = "G-XXXXXXXXXX";`

Tracked automatically: page views, product views (`view_item`), Notify clicks (`notify_me`) and sign-ups (`generate_lead`).

## 3. Meta (Facebook / Instagram) Pixel
1. In Meta Events Manager → Connect data → Web → Meta Pixel. Name it *mumuki.in*.
2. Copy the Pixel ID (numbers only) and paste it: `window.META_PIXEL_ID = "123456789012345";`

Tracked automatically: PageView, ViewContent (product opened), Contact (Notify clicked) and Lead (sign-up).

## 4. Google Search Console
1. Go to search.google.com/search-console and add the domain `mumuki.in` (verify with the DNS record they give you).
2. Under **Sitemaps**, submit `https://mumuki.in/sitemap.xml`.

## 5. Still to fill in
- **Grievance officer name**: search for `[Grievance officer name]` in privacy.html, terms.html and returns.html, and `[Name]` in the index.html footer.
- **GSTIN**: add to the footer line in index.html once available.
- **hello@mumuki.in**: make sure this inbox exists (set it up with your domain/email provider).
- **WhatsApp**: currently `919980881230`. Change `const WHATSAPP` if needed.

## 6. Before taking orders
- Have the policy pages reviewed by your CA or lawyer.
- Confirm your CDSCO import registration and Indian labelling on every product.
- Keep MUMUKI's written approval and their test reports for any results claims (for example the % figures in product images).
