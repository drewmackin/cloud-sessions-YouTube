// Render report.html to a Letter-size PDF with page numbers, using the preinstalled Chromium.
const { chromium } = require('playwright');

(async () => {
  const [input, output] = process.argv.slice(2);
  const browser = await chromium.launch();
  const page = await browser.newPage();
  await page.goto('file://' + input, { waitUntil: 'load' });
  await page.pdf({
    path: output,
    format: 'Letter',
    printBackground: true,
    margin: { top: '0.7in', bottom: '0.75in', left: '0.75in', right: '0.75in' },
    displayHeaderFooter: true,
    headerTemplate: '<div></div>',
    footerTemplate:
      '<div style="width:100%;font-family:Inter,sans-serif;font-size:7.5px;color:#8a8f98;padding:0 0.75in;display:flex;justify-content:space-between">' +
      '<span>Kevin Martins &amp; FSC · AI video workflow · every quote cut from its source</span>' +
      '<span><span class="pageNumber"></span> / <span class="totalPages"></span></span></div>',
  });
  await browser.close();
})();
