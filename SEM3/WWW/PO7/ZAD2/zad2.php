<!--aby uruchomić:        php -S localhost:8080 -->

<?php
    if($_SERVER['REQUEST_METHOD'] == 'POST') {
        $nr_karty=$_POST["nr_karty"];
        $nr_karty_okay=preg_match("/^[0-9]{4}-[0-9]{4}-[0-9]{4}-[0-9]{4}\$/", $nr_karty); //zwróci 0 lub 1
        $nr_karty_okay=$nr_karty_okay==1;

        $data_waznosci=$_POST["data_waznosci"];
        $data_waznosci_okay=preg_match("/^(1[0-2]|0[1-9])\/[0-2][0-9][0-9][0-9]\$/", $data_waznosci); 
        $data_waznosci_okay=$data_waznosci_okay==1;

        $nr_CVC=$_POST["nr_CVC"];
        $nr_CVC_okay=preg_match("/^[0-9]{3}\$/", $nr_CVC);
        $nr_CVC_okay=$nr_CVC_okay==1;

        $imie=$_POST["imie"];
        $imie_okay=preg_match("/^.+\$/", $imie);
        $imie_okay=$imie_okay==1;

        $nazwisko=$_POST["nazwisko"];
        $nazwisko_okay=preg_match("/^.+\$/", $nazwisko);
        $nazwisko_okay=$nazwisko_okay==1;

        $mail=$_POST["mail"];
        $mail_okay=filter_var($mail, FILTER_VALIDATE_EMAIL);

        $telefon=$_POST["telefon"];
        $telefon_okay=preg_match("/^[0-9]{9}\$/", $telefon);
        $telefon_okay=$telefon_okay==1;
    }
    else
    {
        $nr_karty="";
        $nr_karty_okay=true;
        $data_waznosci="";
        $data_waznosci_okay=true;
        $nr_CVC="";
        $nr_CVC_okay=true;
        $imie="";
        $imie_okay=true;
        $nazwisko="";
        $nazwisko_okay=true;
        $mail="";
        $mail_okay=true;
        $telefon="";
        $telefon_okay=true;
    }
?>

<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
        body{
            family-font: arial;
        }
        p{
            color:red;
        }
        button{
            padding: 5px 10px;
            background-color: grey;
            font-size: 20px;
        }
        button:hover{
            transform: scale(1.1);
            background-color: lightgreen;
        }
    </style>
</head>
<body>
    <form method="POST">
        <h3>WPROWADŹ:</h3>
        <label for="nr_karty">Numer karty</label>
        <input type="text" value="<?php echo $nr_karty; ?>" name="nr_karty" placeholder="XXXX-XXXX-XXXX-XXXX">
        <?php if(!$nr_karty_okay){?>
        <p>Źle wprowadzony numer karty. Wprowadź go w postaci: XXXX-XXXX-XXXX-XXXX</p>
        <?php } ?><br><br>

        <label for="data_waznosci">Data ważnosći karty</label>
        <input type="text" value="<?php echo $data_waznosci; ?>" name="data_waznosci" placeholder="MM/RRRR">
        <?php if(!$data_waznosci_okay){?>
        <p>Źle wprowadzona data ważności karty. Wprowadź ją w postaci: MM/RRRR</p>
        <?php } ?><br><br>

        <label for="nr_CVC">Numer CVC</label>
        <input type="text" value="<?php echo $nr_CVC; ?>" name="nr_CVC" placeholder="XXX">
        <?php if(!$nr_CVC_okay){?>
        <p>Źle wprowadzony numer CVC. Wprowadź go w postaci: XXX</p>
        <?php } ?><br><br>

        <label for="imie">Imię</label>
        <input type="text" value="<?php echo $imie; ?>" name="imie" placeholder=>
        <?php if(!$imie_okay){?>
        <p>Podaj imie</p>
        <?php } ?><br><br>

        <label for="nazwisko">Nazwisko</label>
        <input type="text" value="<?php echo $nazwisko; ?>" name="nazwisko">
        <?php if(!$nazwisko_okay){?>
        <p>Podaj nazwisko</p>
        <?php } ?><br><br>

        <label for="mail">Email</label>
        <input type="text" value="<?php echo $mail; ?>" name="mail" placeholder="xxxxxx@xxx.xxx">
        <?php if(!$mail_okay){?>
        <p>Podaj mail</p>
        <?php } ?><br><br>

        <label for="telefon">Numer telefonu</label>
        <input type="text" value="<?php echo $telefon; ?>" name="telefon" placeholder="XXXXXXXXX">
        <?php if(!$telefon_okay){?>
        <p>Źle wprowadzony numer telefonu. Wprowadź go w postaci: XXXXXXXXX</p>
        <?php } ?><br><br>

        <button>WYŚLIJ</button>
    </form>
</body>

</html>