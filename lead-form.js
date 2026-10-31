/* ==========================================================================
   LEAD FORM DELIVERY
   Sends form submissions to email via FormSubmit (no backend required).
   If delivery fails, the visitor is handed off to WhatsApp with the
   inquiry pre-filled so no lead is ever silently lost.
   NOTE: The first live submission triggers a one-time activation email
   to LEAD_EMAIL from FormSubmit - click "Activate" in that email.
   ========================================================================== */
(function () {
  var LEAD_EMAIL = 'seowithibrar@gmail.com';
  var WHATSAPP_NUMBER = '923174835008';
  var ENDPOINT = 'https://formsubmit.co/ajax/' + LEAD_EMAIL;

  function toWhatsAppText(fields) {
    var lines = ['Hi Ibrar, I would like a free SEO consultation.'];
    Object.keys(fields).forEach(function (key) {
      if (key.charAt(0) === '_' || !fields[key]) return;
      lines.push(key + ': ' + fields[key]);
    });
    return lines.join('\n');
  }

  window.whatsAppLeadUrl = function (fields) {
    return 'https://wa.me/' + WHATSAPP_NUMBER + '?text=' + encodeURIComponent(toWhatsAppText(fields));
  };

  /**
   * Deliver a lead. Resolves true when the email service accepted it,
   * false otherwise (caller should offer the WhatsApp fallback).
   */
  window.submitLead = function (fields) {
    var payload = Object.assign({
      _subject: 'New website lead: ' + (fields.Name || 'Visitor') + ' (' + location.pathname + ')',
      _template: 'table',
      _captcha: 'false',
      'Page': location.href
    }, fields);

    return fetch(ENDPOINT, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json', 'Accept': 'application/json' },
      body: JSON.stringify(payload)
    })
      .then(function (res) { return res.ok ? res.json() : { success: false }; })
      .then(function (data) { return !!(data && (data.success === true || data.success === 'true')); })
      .catch(function () { return false; });
  };
})();
