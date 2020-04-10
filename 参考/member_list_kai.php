<html>
<head>
<title> member_list</title> <meta charset="UTF-8">
<link rel="stylesheet" href="css.css">
</head>
<body>
		<div id='main-container'>
				<h2 id='clock'></h2>
			</div>
	
			<div id='alarm-container'>
				<h3>Set Alarm Time</h3>
					<label>
						<div>
						<select id='alarmhrs' ></select>
						</div>
					</label>
					<label>
						<div>
						<select id='alarmmins' ></select>
						</div>
					</label>
					<label>
						<div>
						<select id='alarmsecs' ></select>
						</div>
					</label>
					
					</div>
			</div>
	
			<div id='buttonHolder'>
				<div>
					<button  id='setButton' onClick='alarmSet()'>Set Alarm</button>
				</div>
	
				<div>
					<button  id='clearButton' onClick='alarmClear()'>Clear Alarm</button>
				</div>
			</div>
	
			<script type='text/javascript' src='main2.js'></script>
	
	


    <table border=0 cellpadding=0 cellspacing=0>
<tr bgcolor=#b0c4de>
<th width=50><br>No</th>
<th width=80><br><b>名前 </b></th>
<th width=150><br><b>TEL</b></th>
<th width=50><br><b>状況</b></th>
<?php
session_start();

//make_group.phpからのデータ
if(isset($_GET['id'])) 	      $id=$_GET['id']; 
if(isset($_GET['name'])) {
	$name=$_GET['name']; 
	$_SESSION["name"]=$name;
}
if(isset($_GET['tell']))  {
	$tell=$_GET['tell']; 
	$_SESSION["tell"]=$tell;
}
if(isset($_GET['group'])){
	$group=$_GET['group'];
	$_SESSION["groupname"]=$group;
	
}
 




try{

	$pdo = new PDO("sqlite:members.sqlite");
	$pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
	$pdo->setAttribute(PDO::ATTR_DEFAULT_FETCH_MODE, PDO::FETCH_ASSOC);
	

	//「グループ作成」の場合
		// テーブル作成
		$pdo->exec('CREATE TABLE IF NOT EXISTS "'.$_SESSION["groupname"].'"(
			id INTEGER PRIMARY KEY AUTOINCREMENT,
			name text,
			tell text,
			flag text,
			UNIQUE(name)
		)');
		

		// 挿入
		$stmt = $pdo->prepare('INSERT OR IGNORE INTO "'.$_SESSION["groupname"].'"(name, tell,flag) VALUES (?,?,?)');
		$stmt->execute(array($_SESSION["name"],$_SESSION["tell"],"就寝中"));
		



		//起きた時の入力データ
		//入力された名前がDBにあればその人のデータを変数へ
		if(isset($_GET['name_check'])) {
    	$name_check = $_GET['name_check'];
    
   		$st = $pdo->prepare('SELECT*FROM "'.$_SESSION["groupname"].'" WHERE name=(?)');
    	$st->execute(array($name_check));
    	$kisyou_user = $st->fetch();
    
		}
		if(isset($_GET['tell_check'])) $tell_check = $_GET['tell_check'];







		//flagを起床に変更
		if(isset($kisyou_user)){
    	$pdo->query('UPDATE "'.$_SESSION["groupname"].'" SET flag="起床" WHERE name="'.$name_check.'"');
  		}
	
		// 選択
		$result=$pdo->query('SELECT * FROM "'.$_SESSION["groupname"].'"');
	for($i = 0; $row=$result->fetch(); ++$i ){
		echo "<tr valign=center>";
		echo "<td >". $row['id']. "</td>";
		echo "<td >". $row['name']. "</td>";
		echo "<td >". $row['tell']. "</td>";
		echo "<td >". $row['flag']. "</td>";
		echo "</tr>";
	}

	//何人起床しているか調べる
    $ninnzuu=0;//何人起きてるか
    $max_id = intval($pdo->query('SELECT count(name) FROM "'.$_SESSION["groupname"].'"')->fetchColumn());//idの最大値を取得
    $st2 = $pdo->query('SELECT*FROM "'.$_SESSION["groupname"].'"');
    for($i=0;$users = $st2->fetch();++$i){
        if($users["flag"]=="起床"){
            $ninnzuu+=1;
        }
        if($ninnzuu==$max_id){
            $joukyou="全員起きた！！！";
        }else{
            $joukyou="まだ誰か寝てるね";
        }
    }
echo "<h1>" .$joukyou . "</h1>";

	
	} catch (Exception $e) {
	
		echo $e->getMessage() . PHP_EOL;
	
	}





?>

</table>
<br>
        <h2>起きたら入力!</h2>
<form action=member_list.php method=get>
    <div2 class=kinyu>
<input type=text size=20 name=name_check placeholder="名前">
    <br>
<input type=text size=20 name=tell_check placeholder="TEL">
    <br><br>
    <i class="fa fa-user fa-lg fa-fw" aria-hidden="true"></i>
    </div2>
    <div1><input type=submit border=0 value="起床" id="button"></div1>
</form>


</body>
</html>


