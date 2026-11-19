(function () {
  "use strict";

  // ---------- Mobile navigation ----------
  const toggle = document.querySelector("[data-nav-toggle]");
  const nav = document.querySelector("[data-nav]");

  if (toggle && nav) {
    const setOpen = (open) => {
      nav.classList.toggle("is-open", open);
      toggle.setAttribute("aria-expanded", open ? "true" : "false");
      toggle.setAttribute("aria-label", open ? "Close menu" : "Open menu");
    };

    toggle.addEventListener("click", () => {
      setOpen(!nav.classList.contains("is-open"));
    });

    nav.addEventListener("click", (event) => {
      if (event.target instanceof HTMLAnchorElement) {
        setOpen(false);
      }
    });

    document.addEventListener("keydown", (event) => {
      if (event.key === "Escape") setOpen(false);
    });
  }

  // ---------- Scroll reveal ----------
  const revealItems = document.querySelectorAll(".reveal");

  if (revealItems.length) {
    if ("IntersectionObserver" in window) {
      const observer = new IntersectionObserver(
        (entries) => {
          entries.forEach((entry) => {
            if (entry.isIntersecting) {
              entry.target.classList.add("is-visible");
              observer.unobserve(entry.target);
            }
          });
        },
        { threshold: 0.12, rootMargin: "0px 0px -40px 0px" }
      );

      revealItems.forEach((item) => observer.observe(item));
    } else {
      revealItems.forEach((item) => item.classList.add("is-visible"));
    }
  }

  // ---------- Project filtering ----------
  const filterBar = document.querySelector("[data-filter-bar]");
  const projectGrid = document.querySelector("[data-project-grid]");

  if (filterBar && projectGrid) {
    const buttons = filterBar.querySelectorAll("[data-filter]");
    const cards = projectGrid.querySelectorAll("[data-year]");

    buttons.forEach((button) => {
      button.addEventListener("click", () => {
        const filter = button.getAttribute("data-filter");

        buttons.forEach((b) => b.classList.toggle("is-active", b === button));

        cards.forEach((card) => {
          const show = filter === "all" || card.getAttribute("data-year") === filter;
          card.classList.toggle("is-hidden", !show);
        });
      });
    });
  }

  // ---------- Contact form (progressive enhancement) ----------
  const form = document.querySelector("[data-contact-form]");

  if (form) {
    const status = form.querySelector("[data-form-status]");

    const setStatus = (message, isError) => {
      if (!status) return;
      status.textContent = message;
      status.classList.toggle("is-error", Boolean(isError));
    };

    form.addEventListener("submit", async (event) => {
      event.preventDefault();

      const name = form.querySelector("#name");
      const email = form.querySelector("#email");
      const message = form.querySelector("#message");

      if (!name || !name.value.trim()) {
        setStatus("Please enter your full name.", true);
        name && name.focus();
        return;
      }

      const emailValue = email ? email.value.trim() : "";
      if (!emailValue || !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(emailValue)) {
        setStatus("Please enter a valid email address.", true);
        email && email.focus();
        return;
      }

      if (!message || !message.value.trim()) {
        setStatus("Please tell us a little about your project.", true);
        message && message.focus();
        return;
      }

      const submitButton = form.querySelector("button[type='submit']");
      if (submitButton) {
        submitButton.disabled = true;
        submitButton.textContent = "Sending...";
      }

      try {
        const response = await fetch(form.action, {
          method: "POST",
          body: new FormData(form),
          headers: { "Accept": "application/json", "X-Requested-With": "fetch" }
        });
        const data = await response.json();

        if (!response.ok || !data.ok) {
          setStatus((data.errors && data.errors.join(" ")) || "We couldn’t send your request. Please try again.", true);
          return;
        }

        setStatus(data.message || "Thank you — your request has been received.", false);
        form.reset();
      } catch (error) {
        setStatus("We couldn’t send your request. Please try again or email info@fcceconsultingmw.com.", true);
      } finally {
        if (submitButton) {
          submitButton.disabled = false;
          submitButton.textContent = "Send request";
        }
      }
    });
  }
})();