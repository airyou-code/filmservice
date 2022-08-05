function buttonClick() {
    document.getElementById("blockbut").setAttribute("style", "");
    document.getElementById('footer').scrollIntoView(false);
}

window.onload = function () {
    document.body.classList.add('loaded_hiding');
    window.setTimeout(function () {
        document.body.classList.add('loaded');
        document.body.classList.remove('loaded_hiding');
    }, 500);
    // document.querySelector('.buttonWatch').click()
}

function linkFilm(id) {
    return location.href = id + "/";
}