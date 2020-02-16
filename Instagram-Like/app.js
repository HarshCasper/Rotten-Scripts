/* 

A Javascript Code that automatically likes all the Posts on a Profile/Hashtag. Just fire up your Developer Console and insert the
code and push it. Let the Magic Redeem itself. 

*/

var count = 0;
setInterval(function() {
	var heart = document.querySelector('.wpO6b');
	var arrow = document.querySelector('a.coreSpriteRightPaginationArrow');

	if (heart)  {
		heart.click();
		count++;
		console.log(`You have liked ${count} photos`);
	}
	arrow.click();
}, 10000);
