<?php

class CaesarDeEnCrypter{
    //ATTRIBUTES
    // private $code;
    // private $toDo;
    // private $key;

    //CONSTRUCTORS
    public function __construct(){
        //empty cause standard constr
    }

    // function __constructor (String $code, String $toDo, int $key){      //constructor with parameters already handed over
    //     $this->code = $code;
    //     $this->toDo = $toDo;
    //     $this->key = $key;
    // }

    //METHODS    
    public function encrypt(String $code, int $key):String{
        $codeArray = str_split($code);      //turn code string into character array
        
        foreach($codeArray as $i => $char){       //turn each letter first into ascii (dec), adds the key value and then converts it back to the letter/symbol represented by that ascii dec value
            $x = ord($char) + $key;
            while($x < 32 || $x > 126){         //only printable characters allowed
                if($x < 32){        //if smaller than 33 ascii (dez) then start from the end (126)
                    $x = 127 - (32 - $x);
                }else{
                    $x = 32 + ($x - 127);
                }
            }
            
            $codeArray[$i] = chr($x);
        }        
        $code = implode($codeArray);        //turns character array back into string
        return $code;
    }

    // public function decrypt(String $code): String{          //if wished to auto decrypt
    //     //todo
    // }

    public function decryptWithKey(String $code, int $key): String{          //if wished to "decrypt" with a key
        $codeArray = str_split($code);      //turn code string into character array

        foreach($codeArray as $i => $char){       //turn each letter first into ascii (dec), adds the key value and then converts it back to the letter/symbol represented by that ascii dec value
            $x = ord($char) - $key;
            while($x < 32 || $x > 126){         //only printable characters allowed
                if($x < 32){        //if smaller than 33 ascii (dez) then start from the end (126)
                    $x = 127 - (32 - $x);
                }else{
                    $x = 32 + ($x - 127);
                }
            }
            
            $codeArray[$i] = chr($x);
        }        
        $code = implode($codeArray);        //turns character array back into string
        return $code;
    }
}