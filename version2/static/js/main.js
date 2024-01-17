document.addEventListener("DOMContentLoaded", function() {
    var categorySelect = document.getElementById("category-select");
    var updateBtn = document.getElementById("category-update-btn");
    var deleteBtn = document.getElementById("category-delete-btn");
    var searchToggle = document.getElementById("search-toggle");
    var searchForm = document.getElementById("search-form");
    var selectedCategoryId = categorySelect.value;

    categorySelect.addEventListener("change", function() {
        if (categorySelect.value) {
            updateBtn.disabled = false;
            deleteBtn.disabled = false;
        } else {
            updateBtn.disabled = true;
            deleteBtn.disabled = true;
        }
    });

    updateBtn.addEventListener("click", function() {
        if (selectedCategoryId) {
            window.location.href = `/financial/tracker/category/${selectedCategoryId}/update/`;
        }
    });

    deleteBtn.addEventListener("click", function() {
        if (selectedCategoryId) {
            window.location.href = `/financial/tracker/category/${selectedCategoryId}/delete/`;
        }
    });

    searchToggle.addEventListener("click", function() {
        if (searchForm.style.display === "none") {
            searchForm.style.display = "block";
        } else {
            searchForm.style.display = "none";
        }
    });

    function changeDepositsPerPage(value) {
        window.location.href = `?page=1&deposits-per-page=${value}`;
    }

    function changeExpensesPerPage(value) {
        window.location.href = `?page=1&expenses-per-page=${value}`;
    }

    function changeTransactionsPerPage(value) {
        window.location.href = `?page=1&transactions-per-page=${value}`;
    }
});
