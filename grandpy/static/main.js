
var xhttp = new XMLHttpRequest();
var mapId = 0


// display loader
function loader(divId, state) {
    var loaderDiv = document.getElementById(divId)
    if (state == true) {        
        loaderDiv.classList.add("loader")
    } else {
        loaderDiv.classList.remove("loader")
    };
};

// Display Map
function displayMap(geocodes) {
    mapName = "map" + mapId
    var newDiv = document.createElement("div")
    newDiv.className = "map"
    newDiv.id = mapName
    var node = document.createTextNode(this.responseText)
    newDiv.appendChild(node)

    var end = document.getElementById("end")
    messages.insertBefore(newDiv, end)

    var map = new google.maps.Map(document.getElementById(mapName), {
        center: geocodes,
        zoom: 15,
        streetViewControl: false,
        mapTypeControl: false
      });
    var marker = new google.maps.Marker({position: geocodes, map: map});
    mapId ++

};

// display wiki summary
function displayWiki(summary) {
    wikiName = "wiki" + mapId
    var newDiv = document.createElement("div")
    newDiv.className = "wiki"
    newDiv.id = wikiName
    var node = document.createTextNode(summary)
    newDiv.appendChild(node)

    var end = document.getElementById("end")
    messages.insertBefore(newDiv, end)
}

// Display user message
function message(response, className) {
    var newDiv = document.createElement("div")
    newDiv.className = className
    var node = document.createTextNode(response)
    newDiv.appendChild(node)

    var end = document.getElementById("end")
    messages.insertBefore(newDiv, end)
};


// Controller
window.onload = function () {
    var form = document.querySelector("form")
    var questionElt = document.getElementById("question");
    var messages = document.getElementById("messages");

    // clear input value onClick
    questionElt.addEventListener("click", function (e) {
        questionElt.value = null;        
    }    
    );
    
    // Ajax query
    form.addEventListener("submit", function (e) {
        var question = JSON.stringify({"question": questionElt.value});
        
        xhttp.onreadystatechange = function () {
            if (this.readyState >= 1 && this.readyState < 4) {
                loader("end", true)                
            }
            if (this.readyState == 4 && this.status == 200) {
                res = JSON.parse(this.response)
                if (res.is_valid == false) {
                    message(res.message, "grandpy");
                    loader("end", false);                    
                } else {
                    message(res.adress, "grandpy");
                    displayMap(res.geocodes);
                    message(res.transition, "grandpy");
                    setTimeout(function() {
                    displayWiki(res.summary)
                    loader("end", false)
                    } , 2000);     
                }                     
              }
        }

        xhttp.open('POST', '/')
        xhttp.setRequestHeader("Content-type", "application/json")
        xhttp.send(question)
        message(questionElt.value, "user")
        form.reset()
        e.preventDefault();
    });

    
};