document.addEventListener("DOMContentLoaded", function() {
    console.log("JavaScript loaded successfully!");

    document.querySelectorAll("a").forEach(anchor => {
        anchor.addEventListener("click", function(event) {
            if (this.getAttribute("href").startsWith("#")) {
                event.preventDefault();
                document.querySelector(this.getAttribute("href")).scrollIntoView({
                    behavior: "smooth"
                });
            }
        });
    });
});
