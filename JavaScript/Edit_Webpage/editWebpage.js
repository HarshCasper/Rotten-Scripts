/* Get all the Elements using DOM and store it onto the variable 'a' */

a = document.getElementsByTagName("*");

/* With each variable, add the HTML attribute that contenteditable is true */

for (i = 0; i < a.length; i++){
    a[i].setAttribute("contenteditable", "true");
};

/* Now the attributes related to href are removed from the <a> tags */


href = document.getElementsByTagName("a");

for (i = 0; i < href.length; i++) {
    href[i].removeAttribute("href");
}
