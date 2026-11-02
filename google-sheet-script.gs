/**
 * MUMUKI India – launch-list sign-ups → Google Sheet
 * 1. Create a Google Sheet named "mumiki.in sign-ups".
 * 2. Extensions → Apps Script. Delete everything, paste this file, Save.
 * 3. Deploy → New deployment → type "Web app".
 *    Execute as: Me.  Who has access: Anyone.  → Deploy → Authorise.
 * 4. Copy the Web app URL and paste it into index.html:  const SIGNUP_ENDPOINT = "PASTE_URL_HERE";
 */
function doPost(e) {
  var sheet = SpreadsheetApp.getActiveSpreadsheet().getSheets()[0];
  if (sheet.getLastRow() === 0) sheet.appendRow(["Time", "Email", "Source", "Page"]);
  var d = {};
  try { d = JSON.parse(e.postData.contents); } catch (err) {}
  var email = String(d.email || "").trim();
  if (email && /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)) {
    sheet.appendRow([new Date(), email, d.source || "", d.page || ""]);
  }
  return ContentService.createTextOutput("ok");
}
