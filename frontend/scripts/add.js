document.addEventListener("DOMContentLoaded", function(event) {
    console.log("DOM fully loaded and parsed");
    //Your code to bind event handler
    console.log('page load - entered main.js for js-other api');

    var addPokemonButton = document.getElementById('addPokemonButton');
    addPokemonButton.onmouseup = addPokemonInfo;
    }
);


// functions for get a pokemon
function addPokemonInfo(){
    console.log('entered get pokemon info');
    var pokemonName = document.getElementById("nameInputAdd").value;
  	if (pokemonName != "") {
    	makeGetNetworkCallToPokemonApi(pokemonName);
    }
} // end of getFormInfo

function makeGetNetworkCallToPokemonApi(pokemonName){
    console.log('entered makeGetNetworkCallToPokemonApi');
    var url = "http://localhost:51055/pokemon/";
    var xhr = new XMLHttpRequest(); // 1. creating req
    xhr.open("POST", url, true); // 2. configure request attributes

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
    var types = document.getElementById('typeInputAdd');
    var stats = document.getElementById('statsInputAdd');
    var url = document.getElementById('imageInputAdd')
    var data = {
        "name" : pokemonName,
        "type" : types.value,
        "stats" : stats.value,
        "image" : url.value,
    }
    xhr.send(String(data)); // actually send req with no message body
} // end of makeNetworkCallToAgeApi

function updatePokemonWithResponse(pokemonName, response_text){
    // extract json info from response
    var response_json = JSON.parse(response_text);
    // update label with it
    var output = document.getElementById('outputAdd')
    output.innerHTML = response_json['result'] + ' this is the ' + response_json['id'] + ' pokemon in the pokedex'

} // end of updateAgeWithResponse
