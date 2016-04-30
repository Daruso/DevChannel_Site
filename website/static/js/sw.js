this.addEventListener('install', function(event) {
	console.log('install!');
	// (2.)
	event.waitUntil(
	    caches.open('my-cache')
	      .then(function(cache) {
	        console.log('cache opened');
		// (3.)
	        return cache.addAll([
	        	'/',
	        	'/js/jquery.js',
	        	'/js/jquery.js',
	        	'/js/sw-register.js',
	        	'/css/bootstrap.css'
	        ]);
	      })
  	);
	
});

this.addEventListener('fetch', function(event) {
  // (4.)
  event.respondWith(
    caches.match(event.request).then(function(response) {
    	if (response) {
		// (5.)
    		console.log('found response in cache for:', event.request.url);
    		return response;
    	}

    	// (6.)
    	return fetch(event.request);
    })
  );
});