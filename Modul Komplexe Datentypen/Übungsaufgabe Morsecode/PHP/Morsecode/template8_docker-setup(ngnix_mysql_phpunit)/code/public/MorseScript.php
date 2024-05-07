<?php
$morseArr = array(

    'a'=> '.-',
    'b'=> '-...',
    'c'=> '-.-.',
    'd'=> '-..',
    'e'=> '.',
    'f'=> '..-.',
    'g'=> '--.',
    'h'=> '....',
    'i'=> '..',
    'j'=> '.---',
    'k'=> '-.-',
    'l'=> '.-..',
    'm'=> '--',
    'n'=> '-.',
    'o'=> '---',
    'p'=> '.--.',
    'q'=> '--.-',
    'r'=> '.-.',
    's'=> '...',
    't'=> '-',
    'u'=> '..-',
    'v'=> '...-',
    'w'=> '.--',
    'x'=> '-..-',
    'y'=> '-.--',
    '1'=> '.----',
    '2'=> '..---',
    '3'=> '...--',
    '4'=> '....-',
    '5'=> '.....',
    '6'=> '-....',
    '7'=> '--...',
    '8'=> '---..',
    '9'=> '----.',
    '0'=> '-----'


);

$userstring = trim(fgets(STDIN));

function replaceWithMorse($string,$morseArr)
{
    $len = strlen($string);
    $result='';

    for ($i = 0; $i < $len; $i++) {

        $char = strtolower($string[$i]);

        if ($char == ' ') {
            $result .= ' ';
        } else $char = $morseArr[$char];


        $result .= $char;

    }
    return $result ;

};

echo replaceWithMorse($userstring,$morseArr);
