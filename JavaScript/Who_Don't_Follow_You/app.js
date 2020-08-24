/* 

A Javascript Code which allows you to check who is not following you back on Instagram. 

*/


var loop_followers = parseInt($$('ul li span')[2].textContent, 10);
var loop_following = parseInt($$('ul li span')[3].textContent, 10);
var btn_followers = $$('ul li a')[0]; //click on followers attribute
var btn_following = $$('ul li a')[1]; //click on followers attribute
var scroll_followers, scroll_following, div_followers, div_following;
var list_followers = [], list_nonfollowers = [];
var int_isFollowersDivReady = setInterval(isFollowersDivReady, 1000);
var int_scrollToEndFollowers;

btn_followers.click();
function isFollowersDivReady() {
	//div of list of followers
	div_followers = document.querySelector('body').children;
	div_followers = div_followers[div_followers.length-1].querySelector('ul').parentElement;
   	if ( typeof(div_followers) !== "undefined" && div_followers !== null ) {
		int_scrollToEndFollowers = setInterval(scrollToEndFollowers, 100);
		clearInterval(int_isFollowersDivReady);
	}
}
function scrollToEndFollowers() {
	div_followers.scrollTop = div_followers.scrollHeight;
	scroll_followers = document.querySelector('div ul div');
	if(scroll_followers.childElementCount === loop_followers){
		clearInterval(int_scrollToEndFollowers);
		loadFollowers();
	}
}
function loadFollowers() {
	var arr_followers = Array.apply(null, scroll_followers.querySelectorAll('li')); //nodelist to array conversion
	arr_followers.forEach(function(li) {
		list_followers.push(li.querySelector('a').href);
	});
	div_followers.parentElement.querySelector('button').click(); //close the followers screen
	setTimeout(function(){
		btn_following = document.querySelectorAll('ul li a');
		btn_following[1].click();
		following();
	}, 2000);
}

function following() {
	var int_isFollowingDivReady = setInterval(isFollowingDivReady, 1000);
	var int_scrollToEndFollowing;
	function isFollowingDivReady() {
		//div of list of following
		div_following = document.querySelector('body').children;
		div_following = div_following[div_following.length-1].querySelector('ul').parentElement;
		if ( typeof(div_following) !== "undefined" && div_following !== null ) {
			int_scrollToEndFollowing = setInterval(scrollToEndFollowing, 100);
			clearInterval(int_isFollowingDivReady);
		}
	}
	function scrollToEndFollowing() {
		div_following.scrollTop = div_following.scrollHeight;
		scroll_following = document.querySelector('div ul div');
		if(scroll_following.childElementCount === loop_following){
			clearInterval(int_scrollToEndFollowing);
			loadFollowing();
		}
	}
	function loadFollowing() {
		var arr_following = Array.apply(null, scroll_following.querySelectorAll('li')); //nodelist to array conversion
		arr_following.forEach(function(li) {
			if( !list_followers.includes(li.querySelector('a').href)){
				list_nonfollowers.push(li.querySelector('a').href);
			}
		});
		div_following.parentElement.querySelector('button').click(); //close the followers screen
		console.log(list_nonfollowers.length + " traitors are found!");
		list_nonfollowers.forEach(function(traitor) {
			console.log(traitor);
		});
	}
	
}
