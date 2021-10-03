<h1><strong>Introduction</strong></h1>

<p>Here&#39;s what Adobe has to say about PDFs :&nbsp;</p>

<blockquote>
<p>PDFs run your world. You know you use PDFs to make your most important work happen. That&#39;s why we invented the Portable Document Format (better known by the abbreviation PDF), to present and exchange documents reliably &mdash; independent of software, hardware or operating system.<br />
The PDF is now an open standard, maintained by the International Organisation for Standardisation (ISO). PDF documents can contain links and buttons, form fields, audio, video, and business logic.</p>
</blockquote>

<p>You use PDFs almost every day. If you are a student, you have scanned copies of&nbsp;assignments to submit, or your resume can be in PDF format. Various other important documents come in PDF format. We share it with others. But as we share it, there are high chances of its data being leaked or stolen. Thus, it becomes necessary to encrypt its data or make it password-protected so that only genuine and authorized people can access it.&nbsp;</p>

<p>Some examples of password-protected PDFs that we encounter in daily life are:</p>

<ul>
	<li>Account statements from banks</li>
	<li>Important governmental documents</li>
	<li>Documents sent from companies</li>
</ul>

<p>here, we&#39;ll learn&nbsp;how can we set a password to protect a PDF file. We&rsquo;ll be using the&nbsp;<a href="https://pypi.org/project/PyPDF2/"><strong>PyPDF2</strong></a><strong>&nbsp;</strong>module to encrypt and decrypt our PDF files.</p>

<p>PyPDF2 is an external library and needs to be installed using the command:</p>

<pre>
<code class="language-bash">pip install PyPDF2</code></pre>

<p>Once installed, we are ready to work with it. For demo purposes, you can download this <a href="https://drive.google.com/file/d/1AYmcEsGADQi4RDOM5GoQ7C1O69GqBbqN/view?usp=sharing">PDF file</a>.<br />
&nbsp;</p>

<h1><strong>Encrypt PDF File</strong></h1>

<p>First of all, let&#39;s create a function that checks whether a file is already encrypted.</p>

<pre>
<code class="language-python">from PyPDF2 import PdfFileReader

def is_encrypted(filename: str) -&gt; bool:
    with open(filename, 'rb') as f:
        pdf_reader = PdfFileReader(f, strict=False)
        return pdf_reader.isEncrypted</code></pre>

<p>Now that we have a function ready to check whether the file is already encrypted or not, we can create our function that encrypts the file if it&#39;s not.</p>

<pre>
<code class="language-python">def encrypt_file(filename: str, password: str) -&gt; str:
    pdf_writer = PdfFileWriter()
    pdf_reader = PdfFileReader(open(filename, 'rb'), strict=False)
    if is_encrypted(filename):
        return "PDF File is already encrypted."

    try:
        for page_number in range(pdf_reader.numPages):
            pdf_writer.addPage(pdf_reader.getPage(page_number))
    except utils.PdfReadError:
        return "Error while reading PDF file"

    pdf_writer.encrypt(user_pwd=password, use_128bit=True)
    with open("encypted_demo.pdf", "wb") as f:
        pdf_writer.write(f)
        
    return "PDF file encrypted successfully"</code></pre>

<p>In the above code, we are creating a function&nbsp; <code>encrypt_file</code>. Inside that, we are first checking if the file is already encrypted or not. If it is already encrypted, we simply return a message from there. Else, we iterate over each page of the PDF file and add it to the <code>pdf_writer</code> object created. We are using exception handling so that we can return an error message if any error is encountered while reading the file. After that, we are creating a new file and encrypting it with the given password. We have created a new file just to avoid any damage to the original file. Once it&#39;s done, we are returning a success message at the end.</p>

<p>You can download the encrypted file from <a href="https://drive.google.com/file/d/1pe0aIWVe13eYXwTCTBz7VdIeAWnmjZp2/view?usp=sharing">here</a>.<br />
&nbsp;</p>

<h1><strong>Decrypt PDF File</strong></h1>

<p>Now that we have an encrypted file ready, let&#39;s try decrypting the same file. We can do that using the same library.&nbsp;</p>

<pre>
<code class="language-python">def decrypt_file(filename: str, password: str) -&gt; str:
    pdf_writer = PdfFileWriter()
    pdf_reader = PdfFileReader(open(filename, 'rb'), strict=False)
    if not is_encrypted(filename):
        return "PDF File is not encrypted."

    pdf_reader.decrypt(password=password)
    try:
        for page_number in range(pdf_reader.numPages):
            pdf_writer.addPage(pdf_reader.getPage(page_number))
    except utils.PdfReadError:
        return "Error while reading PDF file"

    with open("decypted_demo.pdf", "wb") as f:
        pdf_writer.write(f)

    return "PDF file decrypted successfully"</code></pre>

<p>In the above code, we are creating a function&nbsp; <code>decrypt_file</code>. Inside that, we are first checking if the file is already encrypted or not. If it is not encrypted, we simply return an error message from there. Else, we first decrypt it using the password and&nbsp;iterate over each page of the PDF file and add it to the <code>pdf_writer</code> object created. We are using exception handling so that we can return an error message if any error is encountered while reading the file. After that, we are creating a new file and writing everything to it. We have created a new file just to avoid any damage to the original file. Once it&#39;s done, we are returning a success message at the end.</p>

<p>You can download the encrypted file from <a href="https://drive.google.com/file/d/1RiyS9Vs1cglfXXWvx1SdW-NILbJpJkNd/view?usp=sharing">here</a>.<br />
&nbsp;</p>

<h1><strong>Conclusion</strong></h1>

<p>Read more about the same in <a href="https://iread.ga/posts/52/encrypt-and-decrypt-pdf-files-using-python">my blog post</a> on <a href="https://iread.ga">iRead</a>.</p>
