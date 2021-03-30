var output = '';
inputTextarea = document.querySelector('#inputTextarea');
outputTextarea = document.querySelector('#outputTextarea');
buttonClear = document.querySelector('#buttonClear');
buttonCopyHTML = document.querySelector('#buttonCopyHTML');
buttonCopyMarkdown = document.querySelector('#buttonCopyMarkdown');
buttonPreview = document.querySelector('#buttonPreview');

buttonPreview.addEventListener('click', function () {
  const converter = new showdown.Converter(),
    preview = document.getElementById('preview');

  showdown.setFlavor('github');

  if (preview && inputTextarea.value) {
    output = converter.makeHtml(inputTextarea.value);
    outputTextarea.value = output;
    preview.innerHTML = output;
  } else {
    preview.innerHTML = 'Markdown Text is Empty!';
  }
});
buttonClear.addEventListener('click', function () {
  inputTextarea.value = '';
  inputTextarea.select();
  outputTextarea.value = '';
  preview.innerHTML = 'Markdown Text is Empty!';
});

buttonCopyHTML.addEventListener('click', function () {
  outputTextarea.select();
  document.execCommand('Copy');
});
buttonCopyMarkdown.addEventListener('click', function () {
  inputTextarea.select();
  document.execCommand('Copy');
});
buttonPreview.click();
