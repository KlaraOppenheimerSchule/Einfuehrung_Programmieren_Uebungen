<?php
require_once "cryptograph.php";

//if no key is given, we assume 3 as default case (maybe use ternery operator)
if (empty($_POST['text'])){
	echo'<p style="color:red;">Achtun! Kein Wort übergeben!</p>';
	echo'<p><a href="index.html">Wer hat noch nicht, wer will noch mal?</a></p>';
	exit;
}
if (empty($_POST['key'])){
	$_POST['key'] = 3;
}

$lo_cryptograph = new cryptograph();
?>
<div>
	<h1>Ver-und Entschlüsselung nach Cäsar</h1>
	<p>Das ergebnis ist:</p>
	<div style="padding 5px; background-color:lightgray;border:1px solid black">
			<?php
			switch ($_POST['method']) {
				case"decrypt":
					echo $lo_cryptograph->decrypt($_POST['text'], $_POST['key']);
					break;
				case "encrypt":
				default:
					echo $lo_cryptograph->encrypt($_POST['text'], $_POST['key']);
			}
			?>
	</div>
</div>
<div>
	<p><a href="index.html">Wer hat noch nicht, wer will noch mal?</a></p>
</div>
