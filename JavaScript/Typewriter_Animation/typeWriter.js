const text = "Hello, World..!!";
let index = 0;
const textElement = document.getElementById("text");

function typeWriter() {
  textElement.textContent = text.substring(0, index);

  if (index < text.length) {
    index++;
  } else {
    index = 0; // Reset index to 0 once it reaches the end of the text
  }

  setTimeout(typeWriter, 300);
}

typeWriter();
