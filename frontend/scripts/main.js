document.addEventListener("DOMContentLoaded", function(event) {
    console.log("DOM fully loaded and parsed");
    //Your code to bind event handler
    console.log('page load - entered main.js for js-other api');

    var searchButton = document.getElementById('searchButton');
    searchButton.onmouseup = getPokemonInfo;

   	var getAllButton = document.getElementById('getAll');
    getAllButton.onmouseup = makeNetworkCallToPokemonAll;
    }
);


// functions for get a pokemon
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
        displayType.innerHTML = ' ';
      	displayStats.innerHTML = ' ';
    } else if (response_json['message'] == 'pokemon not found') {
		displayName.innerHTML = 'Apologies, we could not find your pokemon info. 2';
      	displayType.innerHTML = ' ';
      	displayStats.innerHTML = ' ';
    }
               
  	else{
        displayName.innerHTML = 'Name : ' + response_json['name'];
      	displayType.innerHTML = 'Types : '  + response_json['types'];
        //   [0] + ' ' + response_json['types'][1];
        if (response_json['stats']['HP']) {
            var stats1 = 'Stats'
            var stats2 = 'HP ' + response_json['stats']['HP'];
            var stats3 = 'Attack ' + response_json['stats']['Attack'];
            var stats4 = 'Defense ' + response_json['stats']['Defense']; 
            var stats5 = 'Sp. Attack ' + response_json['stats']['Sp. Attack'];
            var stats5 = 'Sp. Defense ' + response_json['stats']['Sp. Defense'];
            var stats6 = 'Speed ' + response_json['stats']['Speed'];
            displayStats.innerHTML = stats1 + "<br />" + stats2 + "<br />" + stats3 + "<br />" + stats4 + "<br />" + stats5 + "<br />" + stats6
        }
        else {
            displayStats.innerHTML = "stats" + response_json['stats'];
        }
      	imageURL = response_json['image'];
        // var names = document.getElementsByClassName('name-list');
        // while(names[0]) {
        //     names[0].parentNode.removeChild(names[0]);
        // }​
        document.querySelectorAll('.name-list').forEach(e => e.remove());
        
      	displayImage.src = imageURL;
    }

} // end of updateAgeWithResponse

function makeNetworkCallToPokemonAll(){
    console.log('entered makeGetNetworkCallToPokemonApi');
    var url = "http://localhost:51055/pokemon/";
    var xhr = new XMLHttpRequest(); // 1. creating req
    xhr.open("GET", url, true); // 2. configure request attributes

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
    console.log('enetered updateTriviaWithResponse');
    var response_json = JSON.parse(response_text);
    var pokemon_list = response_json['pokemon'][0]
    console.log(pokemon_list);
    displayName.innerHTML = ' ';
    displayType.innerHTML = ' ';
    displayStats.innerHTML = ' ';
    displayImage.src = '../images/group.png';
    var pokemonInfo = document.getElementById('pokemonInfo')
    for(var i=0; i < pokemon_list.length; i++){
   		var newDiv = document.createElement('pokemon_info');
      	var temp_name = pokemon_list[i]['name']['english']
   		newDiv.id = 'r'+i;
   		newDiv.className = 'name-list';
   		pokemonInfo.appendChild(newDiv);
      	newDiv.innerHTML = temp_name + "<br />";
    }


} // end of updateTriviaWithResponse
