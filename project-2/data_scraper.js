const puppeteer = require("puppeteer");

(async () => {
  const browser = await puppeteer.launch();
  const page = await browser.newPage();
  const url =
    "https://track.authorhub.elsevier.com/?uuid=bb51235c-66b1-48df-9c9d-45d5ef4efbb4";
  await page.goto(url, {
    waitUntil: "domcontentloaded",
  });

  await page.waitForSelector(".review-comments li");
  await page.waitForSelector(".lastdate");

  const reviewNumbers = await page.evaluate(() => {
    const listItems = document.querySelectorAll(".review-comments li");
    const content = [];

    listItems.forEach((item) => {
      content.push(item.textContent);
    });

    return content;
  });

  const date = await page.evaluate(() => {
    const divElement = document.querySelector(".lastdate");
    const dateRegex = /(\d{1,2}(st|nd|rd|th) [a-zA-Z]+ \d{4})/;
    const match = divElement ? divElement.textContent.match(dateRegex) : null;
    return match ? match[0] : null;
  });
  console.log("Review Numbers:", reviewNumbers);
  console.log("Last review activity:", date);
  await browser.close();
})();
