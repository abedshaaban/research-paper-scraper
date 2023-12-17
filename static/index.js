function ArticleLayout(
  title,
  abstract,
  authors,
  citations_number,
  year,
  link,
  pdf_link
) {
  const writers = authors?.map((user) => {
    return `&nbsp;${user}`;
  });

  return `
    <div class="article">
        <div class="flex-row article-header">
          <a href=${link} target="_blank" class="article-header-a">
            <h2>${title}</h2>
          </a>

          ${
            pdf_link !== ""
              ? `
              <a href=${pdf_link} target="_blank" class="article-header-btn">
                PDF
              </a>
            `
              : ""
          }
        </div>

        <div class="flex-row article-info">
          <i>Authors:</i> &nbsp; ${writers} &nbsp;| &nbsp;<i>Citations:</i> &nbsp; ${citations_number}
        </div>

        <div class="article-abstract"> ${abstract} </div>
    </div>
    `;
}

const search_input = document.getElementById("q_text");
const search_btn = document.getElementById("q_button");
const results_form = document.getElementById("results");

search_btn.addEventListener("click", async () => {
  let articles = [];
  const q = search_input.value;

  if (q.length === 0) {
    return;
  }

  console.log(q);

  await fetch("/get_q_results", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(q),
  })
    .then((response) => response.json())
    .then((data) => {
      console.log(data);
      articles = data;
    })
    .catch((error) => {
      console.error("Error:", error);
    });

  articles.map((art) => {
    results_form.innerHTML += ArticleLayout(
      art.title,
      art.abstract,
      art.authors,
      art.citations_number,
      // art.year,
      2004,
      art.link,
      art.pdf
    );
  });
});
