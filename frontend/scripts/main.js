document.addEventListener("DOMContentLoaded", function(event) {
    console.log("DOM fully loaded and parsed");
    //Your code to bind event handler
    console.log('page load - entered main.js for js-other api');

    var searchButton = document.getElementById('searchButton');
    searchButton.onmouseup = getPokemonInfo;
    }
);



function getPokemonInfo(){
    console.log('entered get pokemon info');
    var pokemonName = document.getElementById("searchNameInput").value;
  	if (pokemonName != "") {
    	makeGetNetworkCallToPokemonApi(pokemonName);
    }
} // end of getFormInfo

function makeGetNetworkCallToPokemonApi(pokemonName){
    console.log('entered makeGetNetworkCallToPokemonApi');
    var url = "http://localhost:51055/pokemon/" + pokemonName;
    var xhr = new XMLHttpRequest(); // 1. creating req
    xhr.open("GET", url, true); // 2. configure request attributes

    // set up onload - triggered when nw response is received
    // must be defined before making the network call
    xhr.onload = function(e){
        console.log('network response received' + xhr.responseText);
        // do something
        updatePokemonWithResponse(pokemonName, xhr.responseText);
    } // end of onload

    // set up onerror - triggered if n response is error response
    xhr.onerror = function(e){
        console.error(xhr.statusText);
    } // end of onerror

    xhr.send(null); // actually send req with no message body
} // end of makeNetworkCallToAgeApi

function updatePokemonWithResponse(pokemonName, response_text){
    // extract json info from response
    var response_json = JSON.parse(response_text);
    // update label with it
    var name = document.getElementById('displayName');
  	var types = document.getElementById('displayType');
    var stats = document.getElementById('displayStats');
	var imageURL = document.getElementById('displayImage');

    if((response_json['name'] == null) || (response_json['types'] == null) || (response_json['stats'] == null) || (response_json['image'] == null)){
        displayName.innerHTML = 'Apologies, we could not find your pokemon info.';
    } else{
        displayName.innerHTML = 'Name : ' + response_json['name'];
      	displayType.innerHTML = 'Types : '  + response_json['types'][0] + ' ' + response_json['types'][1];
            var stats1 = 'Stats'
            var stats2 = 'HP ' + response_json['stats']['HP'];
            var stats3 = 'Attack ' + response_json['stats']['Attack'];
            var stats4 = 'Defense ' + response_json['stats']['Defense']; 
            var stats5 = 'Sp. Attack ' + response_json['stats']['Sp. Attack'];
            var stats5 = 'Sp. Defense ' + response_json['stats']['Sp. Defense'];
            var stats6 = 'Speed ' + response_json['stats']['Speed'];
            displayStats.innerHTML = stats1 + "<br />" + stats2 + "<br />" + stats3 + "<br />" + stats4 + "<br />" + stats5 + "<br />" + stats6
      	imageURL = response_json['image'];
        
      	displayImage.src = imageURL;
    }

} // end of updateAgeWithResponse

function makeNetworkCallToWeatherApi(long, lat){
    console.log('enetered makeNetworkCallToWeatherApi');
    var url = "http://www.7timer.info/bin/astro.php?lon="+long+"&lat="+lat+"&ac=0&lang=en&unit=metric&output=internal&tzshift=0";
    var xhr = new XMLHttpRequest();
    xhr.open("GET", url, true);

    xhr.onload = function(e) {
        console.log('got nw response from weatherapi');
        updateTriviaWithResponse(url);
    }

    xhr.onerror = function(e){
        console.error(xhr.statusText);
    }

    xhr.send(null); // send request without bosy
} // end of makeNetworkCallToNumbersApi

function updateTriviaWithResponse(url){
    console.log('enetered updateTriviaWithResponse');
    var label2 = document.getElementById("response-line2");
//    label2.innerHTML = response_text;

    // dynamically adding a label

  	var img = document.createElement('img');
    img.src = url;
    var container = document.getElementById('response').appendChild(img);


} // end of updateTriviaWithResponse
