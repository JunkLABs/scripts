// ==UserScript==
// @id              FoolzFilterModified
// @description     Hides filtered users posts on Foolz.
// @warning         Like any script, this will slow down your browser. Also my JS is rusty so this might fuck your shit up.
// @license         WTFPLv2
// @version         1.1
// @namespace       Foolz
// @author          Wohlfe
// @downloadURL     https://github.com/Wohlfe/scripts/blob/master/FoolzFilterModified.js
// @run-at          document-end
// @match           *://*.foolz.us*
// ==/UserScript==

//Fair warning: Like any script, this will slow down your browser. Also my JS is rusty so this might fuck your shit up.

(function() {
    //These are arrays, so you can add multiple users/trips, separated by commas and enclosed with quotes.
	var filterName = ['Wohlfe'];
	var filterTrip = [];

	function isFiltered(filter, data)
	{
		if (data !== undefined)
		{
			switch (filter)
			{
				case 'trip':
					return (filterTrip.indexOf(data) == 0);
				default:
					return (filterName.indexOf(data) == 0);
			}
		}

		return false;
	}

	function filterPosts()
	{
		// Get the <aside class="posts"> for every thread opened
		var threads = document.getElementsByClassName('posts');

		// Process all <aside class="posts">
		for (t = 0; t < threads.length; t++)
		{
			var replies = threads[t].getElementsByTagName('article');

			// process all replies
			for (p = replies.length - 1; p >= 0; p--)
			{
			    var post = replies[p];
				var name = post.getElementsByClassName('post_author');
				var trip = post.getElementsByClassName('post_tripcode');
				//This uses case-insensitive global regex to identify the username anywhere in the post_author field, this is extreme so it's commented out, only use it if necessary.
				//var regex = new RegExp('\\{'name'\\}', 'gi');

				// Checks name, regex of name, or trip
				if ((name && isFiltered('name', name[0].textContent)) || (regex == true && isFiltered('name', name[0].textContent)) || (typeof trip[0] !== 'undefined' && isFiltered('trip', trip[0].textContent)))
				{
					// If true, hides the post
					post.style.display = 'none';
				}
		}
	}

	// filter upon loading dom content
	window.addEventListener("DOMContentLoaded", filterPosts, false);

	// filter ajax requests on dom node inserts
	window.addEventListener("DOMNodeInserted", filterPosts, false);
})();

// jQuery Alternative
// jQuery('aside.posts span.post_author').filter(function() { return $(this).text() == '??'; }).closest('article').remove();
// jQuery('aside.posts span.post_tripcode').filter(function() { return $(this).text() == '??'; }).closest('article').remove();
