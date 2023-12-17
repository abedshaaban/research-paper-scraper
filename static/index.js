console.log("i am console");

const search_input = document.getElementById("q_text");
const search_btn = document.getElementById("q_button");

search_btn.addEventListener("click", () => {
  const q = search_input.value;

  if (q.length === 0) {
    return;
  }

  console.log(q);
});
