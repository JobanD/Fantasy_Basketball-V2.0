window.onload = function () {
  const getCellValue = (tr, idx) =>
    tr.children[idx].innerText || tr.children[idx].textContent;

  const comparer = (idx, asc) => (a, b) =>
    ((v1, v2) =>
      v1 !== "" && v2 !== "" && !isNaN(v1) && !isNaN(v2)
        ? v1 - v2
        : v1.toString().localeCompare(v2))(
      getCellValue(asc ? a : b, idx),
      getCellValue(asc ? b : a, idx)
    );

  document.querySelectorAll("th").forEach((th) =>
    th.addEventListener("click", () => {
      const table = th.closest("table");
      const tbody = table.querySelector("tbody");
      Array.from(tbody.querySelectorAll("tr"))
        .sort(
          comparer(
            Array.from(th.parentNode.children).indexOf(th),
            (this.asc = !this.asc)
          )
        )
        .forEach((tr) => tbody.appendChild(tr));
    })
  );

  // For saving state of checkboxes
  $("input[name='categories']").change(function () {
    var name = $(this).attr("name"),
      values = [];
    // because we have multiple elements with the same name
    // we also remove * after = because the name exactly is 'categories'
    var items = $("input[name='categories']");
    $.each(items, function (index, item) {
      if ($(item).prop("checked")) {
        values.push($(item).val());
      }
    });

    localStorage.setItem("categories", values.join(","));

    // or
    // use JSON.parse in this case when getting data from localStorage
    // you must convert it back to JS array using JSON.parse();
    // localStorage.setItem('favorite',JSON.stringify(values));

    console.log(localStorage.getItem("categories"));
  });
};
