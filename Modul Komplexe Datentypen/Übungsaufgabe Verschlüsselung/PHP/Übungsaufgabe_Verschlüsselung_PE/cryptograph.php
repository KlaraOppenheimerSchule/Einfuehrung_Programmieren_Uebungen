<?php

define("MINASCII", 32);
define("MAXASCII", 126);

class cryptograph {
	public function encrypt (string $as_text, int $ai_key): string {

		$la_text = str_split($as_text);
		$la_encryptedText = [];

		foreach ($la_text as $key => $value) {
			//Using native "ord()" to get ASCII values check@"https://www.php.net/manual/de/function.ord.php"
			$li_original = ord($value);
			$li_encrypted = $li_original + $ai_key;

			//if its not in the selected char range, don't touch it
			if ($li_original >= MINASCII && $li_original <= MAXASCII) {
				if ($li_encrypted > MAXASCII) {
					$li_encrypted = MINASCII + ($li_encrypted - MAXASCII) -1 ;
					$la_encryptedText[ $key ] = $li_encrypted;
				}

				//Using native "chr()" to char for ASCII value  check@"https://www.php.net/manual/de/function.chr.php"
				$la_encryptedText [ $key ] = chr($li_encrypted);
			}
		}

		//we need a string to return
		return implode('', $la_encryptedText);
	}


	public function decrypt (string $as_text, int $ai_key): string {

		$la_text = str_split($as_text);
		$la_decryptedText = [];

		foreach ($la_text as $key => $value) {

			//Using native "ord()" to get ASCII values check@"https://www.php.net/manual/de/function.ord.php"
			$li_original = ord($value);
			$li_decrypted = $li_original - $ai_key;

			//if its not in the selected char range, don't touch it
			if ($li_original >= MINASCII && $li_original <= MAXASCII) {
				if ($li_decrypted < MINASCII) {
					//adding a negative value
					$li_decrypted = $li_decrypted + (MAXASCII - MINASCII) + 1;
				}

				//Using native "chr()" to char for ASCII value  check@"https://www.php.net/manual/de/function.chr.php"
				$la_decryptedText[ $key ] = chr($li_decrypted);
			}
		}

		//We need a string to return
		return $entschluesselterText = implode("", $la_decryptedText);
	}
}