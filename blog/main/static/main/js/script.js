function buttonClick() {
    document.getElementById("blockbut").setAttribute("style", "");

    document.getElementById("buttonD1").setAttribute("class", "buttonOn");
    document.getElementById("description").setAttribute("style", "");

    document.getElementById("buttonD2").setAttribute("class", "buttonOff");
    document.getElementById("persons").setAttribute("style", "display: none; height: 0px;");
    
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

function buttonOnOff(i) {
    if (i == 1){
        document.getElementById("buttonD1").setAttribute("class", "buttonOn");
        document.getElementById("description").setAttribute("style", "");

        document.getElementById("buttonD2").setAttribute("class", "buttonOff");
        document.getElementById("persons").setAttribute("style", "display: none; height: 0px;");
    }
    if (i == 2){
        document.getElementById("buttonD1").setAttribute("class", "buttonOff");
        document.getElementById("description").setAttribute("style", "display: none; height: 0px;");

        document.getElementById("buttonD2").setAttribute("class", "buttonOn");
        document.getElementById("persons").setAttribute("style", "");
    }
    if (i == 3){
        document.getElementById("blockbut").setAttribute("style", "");
    }
}


function openCity(evt, cityName) {
    // Declare all variables
    var i, tabcontent, tablinks;

    // Get all elements with class="tabcontent" and hide them
    tabcontent = document.getElementsByClassName("tabcontent");
    for (i = 0; i < tabcontent.length; i++) {
        tabcontent[i].style.display = "none";
    }

    // Get all elements with class="tablinks" and remove the class "active"
    tablinks = document.getElementsByClassName("tablinks");
    for (i = 0; i < tablinks.length; i++) {
        tablinks[i].className = tablinks[i].className.replace(" active", "");
    }

    // Show the current tab, and add an "active" class to the button that opened the tab
    document.getElementById(cityName).style.display = "block";
    evt.currentTarget.className += " active";
}