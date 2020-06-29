<html>
   <head>
    <title>Activate MC</title>
    <style type="text/css">
      .form-style-6{
        font: 95% Arial, Helvetica, sans-serif;
        max-width: 400px;
        margin: 10px auto;
        padding: 16px;
        background: #F7F7F7;
      }
      .form-style-6 h1{
        background: #43D1AF;
        padding: 20px 0;
        font-size: 140%;
        font-weight: 300;
        text-align: center;
        color: #fff;
        margin: -16px -16px 16px -16px;
      }
      .form-style-6 input[type="text"],
      .form-style-6 input[type="date"],
      .form-style-6 input[type="datetime"],
      .form-style-6 input[type="password"],
      .form-style-6 input[type="number"],
      .form-style-6 input[type="search"],
      .form-style-6 input[type="time"],
      .form-style-6 input[type="url"],
      .form-style-6 textarea,
      .form-style-6 select{
        -webkit-transition: all 0.30s ease-in-out;
        -moz-transition: all 0.30s ease-in-out;
        -ms-transition: all 0.30s ease-in-out;
        -o-transition: all 0.30s ease-in-out;
        outline: none;
        box-sizing: border-box;
        -webkit-box-sizing: border-box;
        -moz-box-sizing: border-box;
        width: 100%;
        background: #fff;
        margin-bottom: 4%;
        border: 1px solid #ccc;
        padding: 3%;
        color: #555;
        font: 95% Arial, Helvetica, sans-serif;
      }
      .form-style-6 input[type="text"]:focus,
      .form-style-6 input[type="date"]:focus,
      .form-style-6 input[type="datetime"]:focus,
      .form-style-6 input[type="password"]:focus,
      .form-style-6 input[type="number"]:focus,
      .form-style-6 input[type="search"]:focus,
      .form-style-6 input[type="time"]:focus,
      .form-style-6 input[type="url"]:focus,
      .form-style-6 textarea:focus,
      .form-style-6 select:focus{
        box-shadow: 0 0 5px #43D1AF;
        padding: 3%;
        border: 1px solid #43D1AF;
      }

      .form-style-6 input[type="submit"],
      .form-style-6 input[type="button"]{
        box-sizing: border-box;
        -webkit-box-sizing: border-box;
        -moz-box-sizing: border-box;
        width: 100%;
        padding: 3%;
        background: #43D1AF;
        border-bottom: 2px solid #30C29E;
        border-top-style: none;
        border-right-style: none;
        border-left-style: none;
        color: #fff;
      }
      .form-style-6 input[type="submit"]:hover,
      .form-style-6 input[type="button"]:hover{
        background: #2EBC99;
      }
    </style>
   </head>

   <body>
     <?php
      $web_status = '&#8987; Nothing happened';
      $hash = '$2y$10$mUb8UTMi8izRGT3SKRolqu/jaY.y8NVkWxMeTMoohrw6qMiph5Z1y';

      $server_file = fopen("server_status.txt", "r") or die("Unable to open file!");
      if (fread($server_file,filesize("server_status.txt"))=="ACTIVE"){
        $server_status = "&#9989; ACTIVE!";
      } else {
        $server_status = "&#10060; Not booted yet!";
      }

      fclose($server_file);


      if (isset($_POST['submit'])){
        $pw = $_POST['password'];
        if (password_verify($pw, $hash)) {
          $web_status = "&#9989; Success!";
          $t = shell_exec("wakeonlan 40:61:86:c3:f1:18");
      } else {
         $web_status = "&#10060; Error, probably wrong password, try again.";
      }
    }
      ?>


      <div class="form-style-6">
        <h1>Let the games begin!</h1>
        <br/><b>Current server status:</b> <?php echo $server_status; ?>
        
        <form method="post" action="">
          <input type="password" name="password" placeholder="Password" />
          <input type="submit" value="submit" name="submit"/>
        </form>
        <br/><b>Result:</b> <?php echo $web_status; ?>
        <br/><b>Reminder:</b> ip adress is: <a href="mc.remy-moll.selfhost.eu">mc.remy-moll.selfhost.eu</a>.
        <p>If the Result is positive, wait a minute and reload the page to check that the PC has indeed booted.
        <br/>The actual Minecraft-server takes longer to load, have a little patience!</p>
      </div>
   </body>
</html>
