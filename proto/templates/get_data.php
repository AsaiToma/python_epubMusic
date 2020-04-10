
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<script src="https://ajax.googleapis.com/ajax/libs/jquery/2.1.4/jquery.min.js"></script>
<title>サンプル</title>
</head>
<body>
<script>
let now_page = 1;
function back_page(){
  now_page = now_page -1;
  location.reload();
}

function next_page(){
  now_page = now_page +1;
  location.reload();
}
document.write(now_page);


</script>



<p> {{ text_list[3] }} </p>
<p> {{ text_type[3] }} </p>
<p>{{pages}}</p>


<form action = "#">
<input type="button"  value="前へ" onclick = "back_page()">
<input type="button"  value="次へ" onclick = "next_page()">
</form>




</body>
</html>