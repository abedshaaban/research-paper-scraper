const search_input = document.getElementById("q_text");
const search_btn = document.getElementById("q_button");

search_btn.addEventListener("click", () => {
  const q = search_input.value;

  if (q.length === 0) {
    return;
  }

  console.log(q);

  fetch("/get_q_results", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(q),
  })
    .then((response) => response.json())
    .then((data) => {
      console.log(data);
    })
    .catch((error) => {
      console.error("Error:", error);
    });
});
