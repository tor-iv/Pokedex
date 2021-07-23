document.addEventListener("DOMContentLoaded", function(event) {
    console.log("DOM fully loaded and parsed");
    //Your code to bind event handler
    console.log('page load - entered main.js for js-other api');

    var deleteButton = document.getElementById('deletePokemonButton');
    deleteButton.onmouseup = deletePokemonInfo;

   	var deleteAllButton = document.getElementById('deleteAllPokemonButton');
    deleteAllButton.onmouseup = makeNetworkCallToPokemonAll;
    }
);


// functions for get a pokemon
function deletePokemonInfo(){
    console.log('entered get pokemon info');
    var pokemonName = document.getElementById("typeInputDelete").value;
  	if (pokemonName != "") {
    	makeGetNetworkCallToPokemonApi(pokemonName);
    }
} // end of getFormInfo

function makeGetNetworkCallToPokemonApi(pokemonName){
    console.log('entered makeGetNetworkCallToPokemonApi');
    var url = "http://localhost:51055/pokemon/" + pokemonName;
    var xhr = new XMLHttpRequest(); // 1. creating req
    xhr.open("DELETE", url, true); // 2. configure request attributes

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
   var output = document.getElementById('outputDelete')
   output.innerHTML= pokemonName + ' ' +  response_json['result']

} // end of updateAgeWithResponse

function makeNetworkCallToPokemonAll(){
    console.log('entered makeGetNetworkCallToPokemonApi');
    var url = "http://localhost:51055/pokemon/";
    var xhr = new XMLHttpRequest(); // 1. creating req
    xhr.open("DELETE", url, true); // 2. configure request attributes

    // set up onload - triggered when nw response is received
    // must be defined before making the network call
    xhr.onload = function(e){
        console.log('network response received' + xhr.responseText);
        // do something
        updatePokemonWithResponseAll(xhr.responseText);
    } // end of onload

    // set up onerror - triggered if n response is error response
    xhr.onerror = function(e){
        console.error(xhr.statusText);
    } // end of onerror

    xhr.send(null); // actually send req with no message body
} // end of makeNetworkCallToAgeApi

function updatePokemonWithResponseAll(response_text){
    // extract json info from response
    var response_json = JSON.parse(response_text);
    // update label with it
   var output2 = document.getElementById('outputDelete')
   output2.innerHTML= response_json['result']


} // end of updateTriviaWithResponse
