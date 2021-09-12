<?php

class TestClass
{
    public $variable;
    public function __destruct()
    {
        print_r(shell_exec("ping ".$this->variable));    
    }

}
unserialize($_GET['data']);
?>
