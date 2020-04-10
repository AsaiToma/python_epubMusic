<html>
<head>
<title> make_group</title> <meta charset="UTF-8">
    <link rel="stylesheet" href="css.css"> 
</head>
<body>
<?php
session_start();
?>
    <h1>グループを作成する</h1>
<form action=member_list.php method=get>
    <div2 class=kinyu>
<input type=text size=20 name=group placeholder="グループ名">
<br>
<input type=text size=20 name=name placeholder="名前">
    <br>
<input type=text size=20 name=tell placeholder="TEL">
    <br><br>
        <i class="fa fa-user fa-lg fa-fw" aria-hidden="true"></i>
    </div2>

    <div1><input type=submit border=0 value="グループ作成" id="button"></div1>
</form>

    <h1>グループに参加する</h1>
<form action=member_list.php method=get>
    <div2 class=kinyu>
<input type=text size=20 name=group placeholder="参加するグループ名">
<br>
<input type=text size=20 name=name placeholder="名前">
    <br>
<input type=text size=20 name=tell placeholder="TEL">
    <br><br>
<i class="fa fa-user fa-lg fa-fw" aria-hidden="true"></i>
    </div2>
    <div1><input type=submit border=0 value="グループに参加" id="button"></div1>
</form>
<?php
/*
$pdo = new PDO("sqlite:members.sqlite");
$pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
$pdo->setAttribute(PDO::ATTR_DEFAULT_FETCH_MODE, PDO::FETCH_ASSOC);

if(isset($_GET["name_login"])) {
    $name_add=$_GET["name_login"];
    $_SESSION["name"]=$name_add;
}
if(isset($_GET["tell_login"])) {
    $tell_add=$_GET["tell_login"];
    $_SESSION["tell"]=$tell_add;
}
if(isset($_GET["group_login"])) {
    $group_join=$_GET["group_login"];
    $_SESSION["groupname"]=$group_join;

    //$group_joinと一致するグループがDBにあれば個人のデータを取り出す
    $st = $pdo->prepare('SELECT*FROM "'.$group_join.'" WHERE name=(?)');
    $st->execute(array($name_add));
    $add_user = $st->fetch();
}

try{


//追加
if(isset($add_user)){
    $stmt = $pdo->prepare('INSERT OR IGNORE INTO "'.$group_join.'"(name, tell,flag) VALUES (?,?,?)');
    $stmt->execute(array($name_add,$tell_add,"就寝中"));
    
    //member_list.phpに飛ばす
    http_response_code( 301 ) ;
	header( "Location: member_list.php" ) ;
	exit ;
}
} catch (Exception $e) {
	
    echo $e->getMessage() . PHP_EOL;

}
*/
?>
</body>
</html>


