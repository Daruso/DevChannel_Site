if ('serviceWorker' in navigator){
	navigator.serviceWorker.register('/js/sw.js').then(function(registration)
	{
		console.log('Success!', registration.scope);
	}).catch(function(err){
		console.log('Rip dreams', err);
	})
}
