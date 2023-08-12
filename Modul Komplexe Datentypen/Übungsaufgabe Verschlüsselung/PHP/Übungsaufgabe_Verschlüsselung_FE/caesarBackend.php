<?php
require_once "CaesarDeEnCrypter.php";

$code = $_POST["inputCode"];
$toDo = $_POST["inputCheckbox"];
$key = $_POST["inputKey"];

$crypter = new caesarDeEnCrypter();

if($toDo == "encrypt"){     //if it was chosen to encrypt the code
    echo "Your code: " . $code . "<br>";
    echo "Encrypted code: " . $crypter->encrypt($code, $key);

}else{      //if it was chosen to decrypt the code
    echo "Your code: " . $code;
    echo "Decrypted code with wished key: " . $crypter->decryptWithKey($code, $key);
    //echo "Decrypted code with auto-decrypt: " . $crypter->decrypt($code);
}
