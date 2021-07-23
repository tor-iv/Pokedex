document.addEventListener("DOMContentLoaded", function(event) {
    console.log("DOM fully loaded and parsed");
    //Your code to bind event handler
    console.log('page load - entered main.js for js-other api');

    var resetButton = document.getElementById('resetButton');
    resetButton.onmouseup = resetPokemonInfo;

   	var resetAllButton = document.getElementById('resetButtonAll');
    resetAllButton.onmouseup = makeNetworkCallToPokemonAll;
    }
);


// functions for get a pokemon
function resetPokemonInfo(){
    console.log('entered get pokemon info');
    var pokemonName = document.getElementById("resetName").value;
  	if (pokemonName != "") {
    	makeGetNetworkCallToPokemonApi(pokemonName);
    }
} // end of getFormInfo

function makeGetNetworkCallToPokemonApi(pokemonName){
    console.log('entered makeGetNetworkCallToPokemonApi');
    var url = "http://localhost:51055/reset/" + pokemonName;
    var xhr = new XMLHttpRequest(); // 1. creating req
    xhr.open("PUT", url, true); // 2. configure request attributes

    // set up onload - triggered when nw response is received
    // must be defined before making the network call
    xhr.onload = function(e){
        console.log('network response received' + xhr.responseText);
        // do something
        updatePokemonWithResponse(pokemonName, xhr.responseText);
    } // end of onload

    // set up onerror - triggered if n response is error response
    var data = {
        "stuff": 'stuff'
    }
    // data = String(data)

    xhr.send(data); // actually send req with no message body
} // end of makeNetworkCallToAgeApi

function updatePokemonWithResponse(pokemonName, response_text){
    // extract json info from response
    var response_json = JSON.parse(response_text);
    // update label with it
   var output = document.getElementById('output')
   output.innerHTML = pokemonName + response_json['response']

} // end of updateAgeWithResponse

function makeNetworkCallToPokemonAll(){
    console.log('entered makeGetNetworkCallToPokemonApi');
    var url = "http://localhost:51055/reset/";
    var xhr = new XMLHttpRequest(); // 1. creating req
    xhr.open("PUT", url, true); // 2. configure request attributes

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
    var data = {
        "stuff": 'stuff'
    }
    // data = String(data)
    xhr.send(data); // actually send req with no message body
} // end of makeNetworkCallToAgeApi

function updatePokemonWithResponseAll(response_text){
     // extract json info from response
     var response_json = JSON.parse(response_text);
     // update label with it
    var output2 = document.getElementById('output')
    output2.innerHTML = response_json['response']


} // end of updateTriviaWithResponse
