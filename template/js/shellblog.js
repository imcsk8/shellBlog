/*
	requests a post 
*/
function setContent(content_path) {
	//we use extensions to identify the posts
	if( !content_path.contains(".inc") )
		url = content_path + ".inc";
	$.ajax({
		type: "GET",
		url: url,
		dataType: "html"
	})
	.done(function(data) {  
		$('#content').html(data); 
		window.history.pushState(null, content_path, "/?" + content_path);
	})
	.fail(function() { alert("Missing Document: " + content_path); setContent("/content/default");  })
}

/*
 * returns the current path if we are not on the main page
 */

function getPath() {
	path = document.location.search.split('?');
	if( ( document.location.pathname != '/' ) || ( document.location.search != '' ) ){
		return(path[1]);
	}
	return(false);
}


/*
 * Loads the default content
 * and initializes the environment
 */

$(document).ready(function() {
	defaultContent = "/content/default";
	urlContent = getPath();
	if(!urlContent)
		urlContent = defaultContent;
	setContent(urlContent);
	// Revert to a previously saved state
	window.addEventListener('popstate', function(event) {
		url = getPath();
		setContent(url);
	});

});



