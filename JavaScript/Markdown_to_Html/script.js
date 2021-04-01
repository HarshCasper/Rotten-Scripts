let output = '';

document.getElementById('buttonPreview').addEventListener('click', function () {
  const converter = new showdown.Converter();

  showdown.setFlavor('github');

  if (
    document.getElementById('preview') &&
    document.getElementById('inputTextarea').value
  ) {
    output = converter.makeHtml(document.getElementById('inputTextarea').value);
    document.getElementById('outputTextarea').value = output;
    document.getElementById('preview').innerHTML = output;
  } else {
    document.getElementById('preview').innerHTML = 'Markdown Text is Empty!';
  }
});
document.getElementById('buttonClear').addEventListener('click', function () {
  document.getElementById('inputTextarea').value = '';
  document.getElementById('inputTextarea').select();
  document.getElementById('outputTextarea').value = '';
  document.getElementById('preview').innerHTML = 'Markdown Text is Empty!';
});

document
  .getElementById('buttonCopyHTML')
  .addEventListener('click', function () {
    document.getElementById('outputTextarea').select();
    document.execCommand('Copy');
  });
document
  .getElementById('buttonCopyMarkdown')
  .addEventListener('click', function () {
    document.getElementById('inputTextarea').select();
    document.execCommand('Copy');
  });
document.getElementById('buttonPreview').click();
